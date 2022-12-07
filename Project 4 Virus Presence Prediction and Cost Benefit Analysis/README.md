<img src="http://imgur.com/1ZcRyrc.png" style="float: left; margin: 20px; height: 55px">

# Project 4 - West Nile Virus Prediction
Authors: Wan Xian, Qingyi, Ian, Clare

## Executive Summary 
According to the Centers for Disease Control and Prevention (CDC), West Nile virus (WNV) is the leading cause of mosquito-borne diseases in the United States. Cases of WNV usually occurs from the start of summer until the end of autumn. Since 2004, the Chicago Department of Public Health (CDPH) has been running a surveillance and control program on the trends of WNV cases and the population of Culex Mosquito in the city. As part of the mosquito control plan, airborne pesticides are sprayed in areas of the city with a high influx of WNV cases. 

The purpose of this project is to create a machine learning (ML) classification model to predict the probability of the presence of West Nile Virus in different clusters around Chicago. This project report will address two issues. Firstly, we will create a ML classification model that can predict when and where different species of mosquitos will test positive for West Nile virus. Secondly, we will conduct a cost-benefit analysis on spraying of airborne pesticides in Chicago. With a more accurate method of predicting outbreaks of WNV in mosquitos and a cost-benefit analysis on its surveillance and control program, the City of Chicago and CDPH will be able to more efficiently and effectively allocate resources towards preventing transmission of this potentially deadly virus. 

This report has a total of 6 jupyter notebooks. 
- Notebook 1 covers data cleaning and exploratory data analysis (EDA) on train and test datasets
- Notebook 2 covers data cleaning and EDA on weather dataset
- Notebook 3 covers the merger of train and weather dataset & test and weather dataset, EDA on the merged dataset, preprocessing and feature engineering
- Notebook 4 covers data cleaning and EDA on spray dataset
- Notebook 5 covers ML Modeling
- Notebook 6 consists of two parts which cover the cost-benefit anaylsis, conclusion and recommendation

This report shows that Gradient Boosting is the most suitable model to use for predicting the traps with WNV present. Gradient boosting is able to correctly predict traps with WNV, with a recall score of 0.75. This is far greater than leaving the prediction to chance, where the probability of a correct prediction is 0.5.

## Problem Statement 
We are a team of data specialists from the Disease and Treatment Agency, and we have been tasked to look into two issues. Firstly, to develop a machine learning (ML) classification model to predict the probability of the presence of WNV. Secondly, to conduct a cost-benefit analysis on the annual cost projections for various levels of pesticide coverage and the effect of these various levels of pesticide coverage.

## Data Dictionary
Data dictionary for the original datasets (train.csv, test.csv, spray.csv, weather.csv) from Kaggle can be found <a href="https://www.kaggle.com/competitions/predict-west-nile-virus/data" target="_blank">here</a>.
<br><br>
<b>For train_merged.csv and test_merged.csv datasets</b>
|Feature|Type|Description|
|---|---|---|
|date|datetime64[ns]|Date that the WNV test was performed|
|species|object|The species of mosquitos|
|trap|object|ID of trap|
|latitude|float64|Latitude returned from GeoCoder|
|longitude|float64|Longitude returned from GeoCoder|
|tavg|float64|Average temperature in °F|
|heat|float64|Heating|
|precip_total|float64|Rainfall & melted snow in inches|
|result_dir|float64|Resultant direct of wind speed in mph|
|avg_speed|float64|Average wind speed in mph|
|daytime_min|float64|Time difference between sunrise and sunset in minutes|
|temp_diff|float64|Difference between maximum temperature and minimum temperature in °F|
|year|int64|Year|
|month|int64|Month|

## EDA Summary
Most of the traps are located mainly in the metropolitan area of Chicago where the residential houses are situated. There is a higher concentration of traps located in the residential areas of the city, as compared to non-residential areas (i.e. the airport). In total, there are 136 distinct traps recorded in the train dataset.

Mosquitos are usually caught when temperatures are between 71°F to 81°F. They are also usually caught when precipitation is 0, and wind speeds are low (less than 10mph).

WNV presence usually peaks in August, which coincides with that of the mosquitoes population caught by the traps. The species genus `CULEX PIPIENS` and `CULEX RESTUANS` has been found to be major vectors of transmission in Chicago. This can be inferred that these 2 species are the dominant species in the city and thus stands a higher likelihood of being transmission vectors for WNV.

## Model Evaluation
Given that the classes in this train dataset is very imbalanced, we need to access the model's performance based on multiple metrics. In relation to the problem statement, it is important that the model predicts the true positives as accurate as possible. A high false positives will result in the city spending more on pesticides unnecessarily while a high false negatives will result in more cases of WNV going undetected. Thus, F1 score and ROC AUC score will be the key metrics to access the best performing model. A limitation with using only ROC AUC scores solely for imbalanced dataset is that it is prone to misleading results ([source](https://stephenallwright.com/f1-score-vs-auc/)).
<br>
Model|Resampling method|F1 (Train)|F1 (Test/Hold-Out)|ROC AUC|Precision|Recall|Average Precision
---|---|---|---|---|---|---|---
Naive Bayes (Baseline)|Random Over Sampler|0.10|0.11|0.75|0.06|1.00|0.11
Random Forest|SMOTE|0.27|0.24|0.80|0.17|0.40|0.20
Random Forest|Random Under Sampler|0.22|0.20|0.80|0.12|0.71|0.20
kNN|SMOTE|0.22|0.21|0.73|0.14|0.41|0.12
kNN|Random Under Sampler|0.18|0.18|0.74|0.10|0.68|0.11
Gradient Boosting|SMOTE|0.30|0.26|0.81|0.19|0.41|0.21
**Gradient Boosting**|**Random Under Sampler**|**0.22**|**0.21**|**0.80**|0.12|0.75|0.19

<br>
From the table above, the baseline model performed fairly in general. F1 scores on train data versus that of test/hold-out data have a small difference of 0.01, indicating that there is no signifcant overfitting of the model. It is noted that all of these models show signs of underfitting since their F1 scores are below 0.5. However, these models are still relevant when assessing them through ROC AUC score, where all of them have scores far away from 0.5, towards 1.0. The reason for the poor F1 scores can be attributed to the extreme imbalanced classes in the train dataset.<br>

Gradient Boosting Classifier with Random Under Sampler performed the best out of the 7 models. Even though ROC AUC scores are similar amongst gradient boosting classifier and random forest classifier, the variance between F1 scores (Train) and F1 scores (Test/Hold-out) is the smallest for Gradient Boosting classifier with Random Under Sampler.<br>

Considering all other metrics, the overall metrics for Gradient Boosting Classifier when Random Under Sampler is applied are considerably fine. With a recall score of 0.75, it performs very well in reducing False Negatives. In a sense, we are able to predict more clusters where WNV is present and take action accordingly. In terms of precision, the model had an average performance where False positives are quite high. In a sense, we will end up spraying more clusters with pesticides depite the fact that they do not have any WNV present.

## Cost Benefit Analysis
<b>Overall Effectiveness of Spraying</b>
- Overall, spraying was effective in reducing the number of mosquito across most of the clusters. In some occasions, mosquito counts spiked up again after spraying but subside subsequently.
- Spraying was more effective in 2013 than 2011 because:
    - Increased pesticide coverage from 3 clusters to 11 clusters.
    - Frequency of spraying was also increased to 2 times for some clusters.
    - Spraying was more in time for some of the clusters. It was done around or even before the peak period of mosquito breeding.
- To maximise the benefit, the above factors should be considered.
- To avoid unnecessary expensiture on excessive spraying, insights from the prediction models can be used to do targeted spraying in areas that are predicted to have virus presence.

<b>Quantifying Benefits</b>
- Cost savings for spraying were estimated using the following formula:<br>
Total Cost Savings = Number of reduced positive human cases x Cost-savings of each positive human case
- Each positive human cases will incur $39000 cost on average, including medical costs and indirect costs from lost productivity ([source](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3291438/))
- Number of reduced positive human cases were estimated from number of mosquito reduced, based on official statistics ([source](https://www.nsmad.org/about_mosquitoes_/west_nile_virus.php)), using the following formula:<br>
Number of mosquito reduced * percentage of mosquito with virus * mosquito to human positive cases ratio

|Year|Mosquito Reduced|Mosquito with Virus Reduced|Human Cases Reduced|Cost Savings ($)|
|---|---|---|---|---|
|2011|135.0|17.6|0.35|13689|
|2013|1362.0|286.0|4.27|166489|

## Conclusion 
**Classification Model**
Gradient Boosting is the most suitable model to use for predicting the traps with WNV present out of those without WNV. This model is able to predict the correct traps with WNV (recall score = 0.75) better than leaving the prediction by chance. Leaving the prediction by chance has a probabilty of it being correct at around 0.5.<br>

Reasons are stated as per below:
1. F1 scores between train dataset and test/hold-out dataset do not vary a lot (Difference of 0.01)
2. Recall score is well above 0.5, which is the rough probability of the label tagging being correct, if left to chance. This means that the model is able to predict true positive cases better than pure randomness.
3. ROC AUC metric is relatively close to 1 and far away from 0.5. This implies that the model seems to fit well with the imbalanced dataset on hand.
4. F1 score and Precision scores are signifcantly higher than that of baseline model. This means that the model is better at predicting true positives while keeping false positives low, as compared to baseline model.

## Limitations
A limitation with Gradient Boosting is that they are prone to overfitting. Hence, any new dataset given to this model are more likely to perform badly and return poor predictions. This would result in the agency not being able to predict which traps are more likely to have WNV for future observations.

Our model might not be able to predict well when there are new datasets. This is because the train data used was too imbalanced where observations with WNV present is only 5% of the total observations. It would be good to have more data records of traps with WNV present to balance the classes out. Another point would be the lack of key features that have a strong relationship with the presence of WNV. If the dataset contain information like humidity, carbon dioxide concentration, approximate distance to water bodies or a cleaner recording of number of mosquitoes trapped, it should help with the model training and improve its predicting performance.

## Recommendation
Going back to the problem statement, we recommend that Gradient Boosting Classifier model should be used to predict the presence of WNV in mosquito traps.<br><br>
We also recommend to continue spraying airborne pesticides as part of the mosquito control plan, as our cost-benefit analysis proves that it is effective in reducing the number of mosquitos as well as humans with WNV. Furthermore, to maximize the benefit of pesticide spraying, it is advisable to increase pesticide coverage by increasing the number of clusters covered and increasing the frequency pesticide is sprayed. 
