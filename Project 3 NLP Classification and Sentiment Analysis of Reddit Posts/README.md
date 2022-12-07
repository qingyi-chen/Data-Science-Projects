# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) NLP - Classification and Sentiment Analysis of Reddit Posts


## Problem Statement

Apple and Google are two of the biggest tech giants today. The two companies compete on several fronts: operating systems, browsers, app store, cloud computing etc ([source](https://www.marketingsociety.com/the-library/apple-v-google-they%E2%80%99re-rivals-many-ways-it%E2%80%99s-not-quite-death-match)). 

The present project aims to levearage on natural language processing to analyze Google and Apple's social media presence, particularly on Reddit. The project attempts to understand the contents of discussion on Google and Apple subreddit. The deliverables are a classification model that is able to predict whether a post comes from Google and Apple subreddit, as well as sentiment analysis of users' posts. The insights would shed light on what service and products offered by either company were most talked about in Reddit, and how well received these products and service are among users, hence drive future businesss decision-making in product and service improvement.


## Data

Text data were collected from Google ([link](https://www.reddit.com/r/google/)) and Apple subreddit ([link](https://www.reddit.com/r/apple/)) using [Pushshift's](https://github.com/pushshift/api)'s API. 20000 posts were collected from each subreddit.

<br>

## Summary of Analysis

1. Text preprocessing using `regex`,`nltk`(for tokenization, lemmatising, stemming) and `sklearn`(for vectorization)

2. Run baseline classification models using logistic regression and random forest, with `MLflow` to keep track of experiment results.

3. Use automated machine learning tool `PyCaret` to scan through 16 different classification models, including probabilistic model, distance-based algorithm, tree based algorithm and ensemble models.

4. Zero-shot text classification using pre-trained model from Hugging Face

5. Sentiment analysis (`Vader`, `spaCy`, `Hugging Face Transformer`) on contents of posts

<br>

## Summary of Results and Insights

|                  Model | Accuracy |    AUC | Recall |  Prec. |     F1 |
|-----------------------:|---------:|-------:|-------:|-------:|-------:|
| Extra Trees Classifier |   0.8564 | 0.9195 | 0.8540 | 0.8709 | 0.8623 |

1. The best performing classification model was extra trees classifier. It was able to classify 86% of the posts correctly. Additionally, extra tree classifier was able to address overfitting issues much better compared to basic tree based algorithm, since it used random split and random subspace method to reduce variance.

2. Zero shot classification using a model trained on other corpus fared poorer compared to models trained on Reddit corpus in this dataset.

3. Discussion in both subreddits are mostly centred around the respective products offered by Google or Apple. For Apple subreddit, users have extensive discussion on hardware products like ipad, airpods, macbook, watch, iphone. For Google subreddit, discussion on products centred around software products like chrome, calendar, photos and google drive.

4. General sentiments were neutral in both subreddit. However, Hugging Face Transformer model captured more negative sentiment in Google subreddit. A more granular emotion analysis revealed that most salient emotions were sadness and suprise, whereby sadness was mostly related to dissatisfaction of certain product or service, while surprise was mostly related to users' enquiry on product and features.


<br>

## Limitation

1. Model was only trained on English text and has no capacity to make predictions for posts in foreign language, which would be pretty common on social media.

2. Model may not necessairly generalise well to texts from social media other than Reddit, which may have very different user profiles and different linguistics. In fact, zero shot classification model trained on other corpus fared much poorer compared to models trained using the Reddit corpus in the dataset. This again highlights the risk of limited generalisability for text classification model.

3. Accuracy of sentiment analysis was not derived due to lack of actual sentiment labels.

<br>

## Future Direction

1. Gather text data from multiple platforms and in different languages to improve the generalisability of the model.

2. Create a subset of data with manually labelled sentiments to assess accuracy in sentiment analysis.