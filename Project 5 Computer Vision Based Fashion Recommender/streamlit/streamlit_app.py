import streamlit as st
import requests
import json
from PIL import Image
from io import BytesIO

from streamlit_cropper import st_cropper
from streamlit_image_select import image_select

#########################
##        Setup        ##
#########################

# Title and layout of the webpage
st.set_page_config(layout="wide", initial_sidebar_state='expanded')
st.title("H&M Fashion Products Recommender")
st.sidebar.info("Get started by choosing ONE way to search for products, and we would recommend H&M products that you may interested in.")

# Side Bar - Select Page
page_selection = st.sidebar.radio(
    'Search by:',
    ('📚 Keywords', '🖼️ Uploading a Photo', '📸 Taking a Photo', '👀 Browsing Products'))

# Set api url
api_url = 'http://localhost:8080'

# Function to Format Recommender Output
def render_recommended_products():
    # Get response from server
    recommended_products = response.json()
    st.header('Recommended Products')

    # Display top 4 recommended products in 4 columns
    cols = st.columns(4)
    for index, col in enumerate(cols):
        with col:
            index_str = str(index)
            img = Image.open(recommended_products['img_path'][index_str])
            st.image(img)
            st.caption(f"Similarity Score: {round(recommended_products['cosine_sim'][index_str]*100,0)}/100")

            # An expandable description box
            with st.expander("Description"):
                st.write(f"Article ID: {recommended_products['article_id'][index_str]}")
                st.write(f"{recommended_products['detail_desc'][index_str]}")
                link = f"[Product Link](https://www2.hm.com/en_sg/productpage.0{recommended_products['article_id'][index_str]}.html)"
                st.markdown(link, unsafe_allow_html=True)

#########################
##  Search by Keywords ##
#########################
if page_selection == '📚 Keywords':
    cols = st.columns(3)
    
    # Form for user input
    with cols[0]:
        with st.form(key='text_search'):
            search_words = st.text_input("📚 Enter Keywords", placeholder='floral dress',help='Key in the search words to search relevant items here') 
            submit_text = st.form_submit_button(label='Search by Keywords')
    
    # Output
    if submit_text:
        with st.spinner('✨Searching relevant products for you...✨'):    
            # Route to send request to
            api_route = '/text_query_recommender' 
            
            # Request
            user_input = {"search_words":search_words}
            response = requests.post(f'{api_url}{api_route}', json=json.dumps(user_input))
            render_recommended_products()

#########################
##     Upload Image    ##
#########################
if page_selection == '🖼️ Uploading a Photo':
    
    cols = st.columns(3)
    
    # Form for user input
    with cols[0]:
        st.subheader("🖼️ Upload a Photo")
        with st.form(key='upload_file'):
            uploaded_file = st.file_uploader("Upload a Photo", type=['jpg','png','jpeg'])
            submit_uploaded_file = st.form_submit_button(label='Search by Image')
    
    if submit_uploaded_file:
        with cols[1]:
            st.subheader('Uploaded Photo')
            st.image(Image.open(uploaded_file),width=200)
        with st.spinner('✨Searching relevant products for you...✨'): 
            # Route to send request to
            api_route = '/image_query_recommender' 
            # Request
            image_file = {'image':uploaded_file.getvalue()} # Getvalue: read file as bytes
            response = requests.post(f'{api_url}{api_route}', files=image_file)
            render_recommended_products()
            
#########################
##      Take Photo     ##
#########################        
if page_selection == '📸 Taking a Photo':
    cols = st.columns(4)
    
    # User input
    with cols[0]:
        st.subheader("📸 Take a Photo")
        taken_picture = st.camera_input("Take a Photo Here")
    
    # Crop the image
    if taken_picture:
        with cols[1]:
            st.subheader("Crop the Image ")
            cropped_img = st_cropper(Image.open(taken_picture), realtime_update=True, box_color='#000000', aspect_ratio=None, return_type='image')
            st.caption("Crop out the item you are searching for to reduce background noise and improve search accuracy")
        with cols[2]:
            st.subheader("Preview of Cropped Image")
            _ = cropped_img.thumbnail((150,150))
            st.image(cropped_img)
        submit_cropped_image = st.button('Search by Photo')
        
        # Output using cropped image
        if submit_cropped_image:
            with st.spinner('✨Searching relevant products for you...✨'): 
            
                # Route to send request to
                api_route = '/image_query_recommender' 
                
                # Convert cropped image to byte array - https://stackoverflow.com/questions/33101935/convert-pil-image-to-byte-array
                img_byte = BytesIO()
                cropped_img.save(img_byte,format='PNG')
                image_file = {'image':img_byte.getvalue()} # Getvalue: read file as bytes

                # Request
                response = requests.post(f'{api_url}{api_route}', files=image_file)
                render_recommended_products()

#########################
##   Browse Products   ##
#########################
if page_selection == '👀 Browsing Products':
    # Route to send request to
    api_route = '/show_sampled_products'

    # Request
    response = requests.post(f'{api_url}{api_route}')
    sampled_products = response.json()

    # Display 4 sampled products
    images = []
    for index in range(14):
        index_str = str(index)
        img = Image.open(sampled_products['img_path'][index_str])
        images.append(img)

    st.header('Product Gallery')
    product_gallery = image_select(
        label = "Select a product, and find out what people with similar preference usually buy!",
        images = images)

    submit_selected_product = st.button("Search by Selected Product")

    if submit_selected_product:
        index_str = str(images.index(product_gallery))
        article_index = sampled_products['article'][index_str]

        # Route to send request to
        api_route = '/collaborative_filtering' 

        # Request
        user_input = {"item_index":article_index}
        response = requests.post(f'{api_url}{api_route}', json=json.dumps(user_input))
        render_recommended_products()
