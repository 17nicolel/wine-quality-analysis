# wine-quality-analysis
Analyze wine features and qualities with Machine Learning

# Goal
To predict wine quality using KNN classification.

# Method 
The x and y varibles are first idendified, with unnecessary x features dropped from the dataframe. Then the x features are first standarized so that the numbers could be better compared with each other. A trainning and testing is split to 0.8 and 0.2, with y stratified.

To find the best K neighbor number for the model, a graph is produced to compare performance for each k number. 

<img src="https://user-images.githubusercontent.com/65926359/101328055-620e1400-3824-11eb-9179-07a7e4af0dc0.png" width="90%"></img> 

(The photo above shows accuracy rates for each number. Because Trainning A set is only for reference, Trainning B is used for deciding which k number to pick. The number of 27 shows the highest accuracy score for Trainning B, thus it is used for the final model)

Confusion Matrix:

<img src="https://user-images.githubusercontent.com/65926359/101328504-ef516880-3824-11eb-81bf-d54bff8f8f4e.png" width="90%"></img> 

The final model exhibits an accuracy score of 0.590625. This might indicate the KNN classification model might not be the best model for this dataset, or that further data cleaning is needed.

# Outcome 
This model could be used on prediction of wine quality with given wine features. 
