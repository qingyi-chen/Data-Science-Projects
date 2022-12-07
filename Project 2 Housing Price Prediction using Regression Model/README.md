# Housing Price Prediction using Regression Model

## Problem Statement
This project aims to develop a regression model to predict property sale price, using a dataset of resdiential home features. Important features that help to uplift sale price will be identified. This will help homeowners or property agents in making optimal decisions in property transactions.

## Data Dictionary
The dataset contains 79 features and the sale price of residential homes in Ames, Iowa from 2006 to 2010. Data dictionary of the dataset can be found [here](http://jse.amstat.org/v19n3/decock/DataDocumentation.txt). 


## Summary of Data Analysis
1. Feature engineering was done to generate additional relevant features.
2. Feature selection was done to reduce collinearity and remove unimportant features.
3. Linear regression, Ridge, Lasso and Elastic Net were used to predict sale price. Accuracy score (R^2) and root mean square of error were generated on test set to measure model success.


## Conclusion and Recommendations
**Summary of Findings**
- Most important features for property sale price is living area, overall quality and location.
- Living area is the strongest predictor for sale price.
- Huge difference in sale price was observed among different neighborhood, with most expensive neighborhood more than twice the price of cheapest neighborhood. This highlights the importance of prime location for purchasing and selling property.
- Improving quality of the house by upgrading the finish and materials can bring price uplist for homeowners looking to sell their property.

**Future Steps**
- Sale price prediction model can be tested against other property market outside Ames, Iowa to understand model generalisability and to identify features that are robust in different markets.