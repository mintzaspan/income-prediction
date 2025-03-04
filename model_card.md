# Model Card

## Model Details
This is an income prediction model, where the aim is to predict if a person earns more or less than $50,000 per annum.

## Intended Use
It is an educational project and the intended use is to demonstrate how such models can be deployed to an online service for inference.

## Training Data
The [Census Income](https://archive.ics.uci.edu/dataset/20/census+income) dataset has been used for training the model. It contains approximately 49,000 records and data is organised in 14 features and a label.

## Evaluation Data
Evaluation is data by splitting the data to train and test sets. The test set is approximately 20% of the total data size. Fairness of predictions is also evaluated by calculating metrics for each distinct value in all categorical variables.

## Metrics
F1 score has been chosen as the evaluation metric, giving a balanced view of precision and recall. 

## Ethical Considerations

## Caveats and Recommendations
