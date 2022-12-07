
#########################
##  Import and Set Up  ##
#########################
import os
# os.environ['KMP_DUPLICATE_LIB_OK']='True'
from flask import Flask, request
import pandas as pd
from sentence_transformers import SentenceTransformer # For embeddings generation
from sklearn.metrics.pairwise import cosine_similarity # For cosine similarity
from PIL import Image # For loading image
import nmslib # For approximate neareast neighbor search
import pickle

# Instantiate the Flask API with name 'ModelEndpoint'
api = Flask('ModelEndpoint')

##################################
##    Load Content-Based Model  ##
##################################
# Read embeddings data
image_data = pd.read_pickle('../datasets/image_embeddings_merged.pkl')

# Load CLIP model for embedding generation
clip_model = SentenceTransformer('clip-ViT-B-32')

##########################################
##  Load Collaborative Filtering Model  ##
##########################################
# 1. Load the model without indexes
implicit_model = pickle.load(open('../streamlit/collaborative_filtering_model', 'rb'))
# 2. Load indexes
recommend_index = nmslib.init(method="hnsw", space="cosinesimil")
recommend_index.loadIndex(filename='../streamlit/search_index', load_data=True)
similar_items_index = nmslib.init(method="hnsw", space="cosinesimil")
similar_items_index.loadIndex(filename='../streamlit/similar_item_index', load_data=True)
# 3. Set indexes
implicit_model.recommend_index = recommend_index
implicit_model.similar_items_index = similar_items_index
print('implicit model success')

#########################
##      Route 1        ##
#########################
# Home Route - Health check. Just return success if the API is running
@api.route('/') 
def home(): 
    return {"message": "Hello!", "success": True}, 200

#########################
##      Route 2        ##
#########################
# Text Query Recommender
@api.route('/text_query_recommender', methods = ['POST'])

def text_query_recommender():
    user_input = request.get_json(force=True)
    df_schema = {"search_words":str}
    user_input_df = pd.read_json(user_input, lines=True, dtype=df_schema) # Read the file as json object per line
    
    # Encode the text using CLIP
    text_emb = clip_model.encode(user_input_df["search_words"])
    
    # Calculate cosine similarities for queried product
    similarities = cosine_similarity(text_emb,image_data['clip_embedding'].values.tolist())[0]
    
    # Sort cosine similarities in descending order, and select the top 6 recommended products
    similarities = pd.DataFrame(similarities,index=image_data['article_id'], columns=['cosine_sim']).sort_values(by='cosine_sim',ascending=False).iloc[:6]
    
    # Get descriptions of top 6 recommended products from image_data
    nearest_articles_id = similarities.index.tolist()
    recommended_products = image_data[image_data['article_id'].isin(nearest_articles_id)]
    recommended_products = pd.merge(recommended_products,similarities,on='article_id').sort_values(by='cosine_sim',ascending=False).reset_index().to_dict()
    return recommended_products

#########################
##      Route 3        ##
#########################
# Image Query Recommender
@api.route('/image_query_recommender', methods = ['POST'])

def image_query_recommender():
    # Read the image - binary
    # https://stackoverflow.com/questions/65266569/how-can-i-open-an-image-of-filestorage-type-in-pillow
    file = request.files['image']
    img = Image.open(file).convert('RGB')
    
    # Encode the image using CLIP
    image_emb = clip_model.encode([img])
    
    # Calculate cosine similarities for queried product
    similarities = cosine_similarity(image_emb,image_data['clip_embedding'].values.tolist())[0]
    
    # Sort cosine similarities in descending order, and select the top 6 recommended products
    similarities = pd.DataFrame(similarities,index=image_data['article_id'], columns=['cosine_sim']).sort_values(by='cosine_sim',ascending=False).iloc[:6]
    
    # Get descriptions of top 6 recommended products from image_data
    nearest_articles_id = similarities.index.tolist()
    recommended_products = image_data[image_data['article_id'].isin(nearest_articles_id)]
    recommended_products = pd.merge(recommended_products,similarities,on='article_id').sort_values(by='cosine_sim',ascending=False).reset_index().to_dict()
    
    return recommended_products

#########################
##      Route 4        ##
#########################
@api.route('/show_sampled_products',methods=['POST'])

def show_random_products():
    sampled_products = image_data.dropna(subset='article').head(14).reset_index().to_dict()
    return sampled_products

#########################
##      Route 5        ##
#########################
# Collaborative Filtering
@api.route('/collaborative_filtering',methods=['POST'])

def item_index_recommender():
    user_input = request.get_json(force=True)
    df_schema = {"item_index":int}
    user_input_df = pd.read_json(user_input, lines=True, dtype=df_schema) # Read the file as json object per line
    user_input_index = user_input_df['item_index'][0]
    
    similar_df = pd.DataFrame(implicit_model.similar_items(user_input_index, 6)).T
    similar_df.columns = ['article','cosine_sim']
    recommended_products = image_data[image_data['article'].isin(similar_df['article'])]
    recommended_products = pd.merge(recommended_products,similar_df,on='article').sort_values(by='cosine_sim',ascending=False).iloc[1:].reset_index().to_dict()
    
    return recommended_products
    
#########################
##     Run the API     ##
#########################
if __name__ == '__main__': 
    api.run(host='0.0.0.0', 
            debug=True,
            port=int(os.environ.get("PORT", 8080)) 
           )
