<img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">

# H&M Fashion Products Recommender
Author: Chen Qingyi

## Executive Summary 
H&M is a multinational fast-fashion clothing company with a wide selection of products. This project aims to build a web-based recommendation application for fashion products from H&M. The purposes are multi-fold.

**For customers**: <br>
Reduce friction in the product search process by optimising the search exprience in the following ways:
1) introducing a computer vision empowered recommendation system that allows image search by uploading or taking photos, a feature that is currently lacking in [H&M website](https://www2.hm.com/en_sg/index.html).
2) generating recommendations based on customers with similar preferences

**For business**: <br>
Boost customer engagement, retention and drive up sales, by delivering more seamless product search experience and more personalized recommendations.

## Datasets and Data Dictionary
**Source of Datasets: kaggle ([link](https://www.kaggle.com/competitions/h-and-m-personalized-fashion-recommendations/data))**
- `Transactions` : tabular data of transaction history
- `Articles` : tabular data of product descriptions
- Product images

| **Dataset**           | **Feature**                   | **Description**                           |
|-----------------------|-------------------------------|-------------------------------------------|
| Transactions          | t_dat                         | Transaction date                          |
| Transactions          | customer_id                   | A unique identifier of every customer     |
| Articles/Transactions | article_id                    | A unique identifier of every item         |
| Articles              | prod_name                     | Product name                              |
| Articles              | product_group_name            | Product groups (e.g. upper body garment)  |
| Articles              | graphical_appearance_name     | Gaphical appearance                       |
| Articles              | perceived_colour_master_name  | Color names                               |
| Articles              | index_group_name              | Product index (e.g. ladieswear, menswear) |
| Articles              | detail_desc                   | Detailed description of the product       |

## Streamlit Model Deployment
![Screenshot 2022-11-16 at 10 56 48 PM](https://media.git.generalassemb.ly/user/44670/files/5be167f5-0b98-408a-b1b8-ac5d234779f1)

**Example: Image Search**
![Screenshot 2022-11-17 at 12 04 23 AM](https://media.git.generalassemb.ly/user/44670/files/21cc1a84-8fd6-4ac4-9b69-17e0877c309f)

**Example: Recommendations Based on Customers with Similar Preferences**
![Screenshot 2022-11-17 at 12 06 04 AM](https://media.git.generalassemb.ly/user/44670/files/f74eacb0-cf9e-43e6-a54a-57e26a9db6f5)

## Methodology
This project incorporates two types of recommenders:
1) **Content-based filtering**: Find features of an item and recommend items with similar features.
2) **Collaborative filtering**: Recommend items based on people with similar preferences.

### Methodology for Content-Based Filtering
- Content-based recommender was built by extracting features from product images.
- It supports both text and image query. When user inputs either text or image, the recommender was able to find similar images in the product dataset.
- This was achieved using **Contrastive Language-Image Pre-Training (CLIP) model**, which is a state-of-the-art computer vision system that maps texts and images into the same shared vector space ([Radford et al., 2021](https://arxiv.org/abs/2103.00020)) to allow for multi-modal similarity search (text-to-image, image-to-image). 

<br>

**Contrastive Language-Image Pre-Training (CLIP) model**
- CLIP uses convolutional neural networks pre-trained with Simple framework for Contrastive Learning of Visual Representations. More simply put, the embeddings are generated in a way that preserves the objects’ similarity — similar objects get closer to each other and dissimilar objects get further apart.
- Text and image pass through separate encoders but are eventually mapped into the same vector space to allow for multi-modal similarity search.
- The generated embeddings are evaluated using contrastive loss function. The objective is to minimise the distance between the text-image pair, and maximise the distance between the source image and dissimilar images.

![Screenshot 2022-11-16 at 11 59 57 PM](https://media.git.generalassemb.ly/user/44670/files/dcdf06cd-7eb9-420d-8bcc-155a341426f6)

**Process Flow of Content-Based Filtering using CLIP model**

![Screenshot 2022-11-17 at 12 01 28 AM](https://media.git.generalassemb.ly/user/44670/files/3ab99f2b-f2c7-419f-b513-ac3cf15b72ff)

### Methodology for Collaborative Filtering
- Collaborative-filtering recommender was built using customers' transaction data. 
- Given the large volumns of transaction data, **Alternating Least Square Matrix Factorisation** was used to reduce dimensionality of user-item matrix. Approximate nearest neighbour search algorithm **Hierarchical Navigable Small Worlds (HNSW)** was used to generate quick and reliable results for similarity search.

**Hierarchical Navigable Small Worlds (HNSW)**
- Data points are organised in a small world network, where not all the points are connected to one another but they are within close proximity (a few links away) to each other.
- Search for approximate nearest neighbour is implemented in a hierarchical fashion from top layer (with least data points) to bottom layer (with most data points).

![hnsw-5](https://media.git.generalassemb.ly/user/44670/files/ea4571d5-0ea8-47d4-94f1-9d1f86c7ebe2)

## Future Work (In Progress)
- Model deployment on cloud for real-time access to the web application
- Test out alternative search algorithm to optimise similarity search, such as Facebook AI Similarity Search (Faiss).

