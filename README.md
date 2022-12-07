# Data Science Projects

## Project 5: Computer Vision Based Fashion Product Recommender
**Aim**
- Develop a web application for image-search enabled fashion product recommender to improve online shopping experience

**Methodology**
- Both content-based filtering and collaborative filtering were used to build the recommender
- Contrastive Language-Image Pre-Training (CLIP) model was used to allow image-to-image or text-to-image search
- To reduce computational time for collaborative filtering, Alternating Least Square Matrix Factorisation and Hierarchical Navigable Small Worlds (HNSW) were used.

**Tools**
- Hugging Face Sentence Transformer | implicit | nmslib | flask | streamlit 

## Project 4: Virus Presence Prediction and Cost-Benefit Analysis
**Aim**
- Build a classification model with time-series and geographical data to predict virus presence in mosquitoes
- Run a cost-benefit analysis of mosquito control measures to optimize effectiveness while minimizing costs.

**Methodology**
- Address imbalanced classes using techniques like random under sampling, random over sampling, SMOTE (synthetic minority over-sampling technique)
- Visualize geographical distribution of mosquito breeding sites and locations of mosquito control measures

**Tools**
- scikit-learn | imblearn | matplotlib | seaborn | plotly 

## Project 3: Natural Language Processing - Classification and Sentiment Analysis of Reddit Posts
**Aim**
- Analyze Google and Apple’s user sentiments on social media (Reddit) and build a text classification model to understand contents of discussion

**Methodology**
- Webscraping of Reddit posts using API
- Text preprocessing using regex, nltk(for tokenization, lemmatising, stemming) and sklearn(for vectorization)
- Explore a variety of classification algorithm (probabilistic model, distance-based algorithm, tree based algorithm and ensemble models)
- Sentiment analysis

**Tools**
- scikit-learn | nltk | MLFlow | PyCaret | Vader | spaCy | Hugging Face Transformer

## Project 2: Housing Price Prediction using Regression Model
**Aim**
- Develop a regression model to predict resale values of residential properties in Ames, US and generate insights on features affecting property price.

**Methodology**
- Feature engineering was done to generate additional relevant features.
- Feature selection was done to reduce collinearity and remove unimportant features.
- Linear regression, Ridge, Lasso and Elastic Net were used to predict sale price.

**Tools**
- scikit-learn | pandas | matplotlib | seaborn

## Project 1: SAT Score Analysis for College Admission
**Aim**
- Performed exploratory data analysis of SAT scores by major and by college to provide recommendations for students applying for colleges.
<br>

**Tools**
- Python pandas | matplotlib | seaborn
