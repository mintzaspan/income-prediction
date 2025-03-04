# Model Card

## Model Details
This is an income prediction model, where the aim is to predict if a person earns more or less than $50,000 per annum. For reference, it is a Gradient Boosting classifier with a preprocessing pipeline.

## Intended Use
It is an educational project and the intended use is to demonstrate how such models can be deployed to an online service for inference.

## Training Data
The [Census Income](https://archive.ics.uci.edu/dataset/20/census+income) dataset has been used for training the model. It contains approximately 49,000 records and data is organised in 14 features and a label.

## Evaluation Data
Evaluation is data by splitting the data to train and test sets. The test set is approximately 20% of the total data size. Fairness of predictions is also evaluated by calculating metrics for each distinct value in all categorical variables.

## Metrics
F1 score has been chosen as the evaluation metric, giving a balanced view of precision and recall. 
- The F1-Score on training data is 0.8283
- The F1-Score on test data is 0.7066
Overall, the model's performance is good. However, there are signs of overfitting that can be addressed by tuning hyperparameters or applying cross validation.

Detailed performance results on model slices can be seen in `outputs/slice_output.txt`.

## Ethical Considerations
This model should not be used in the real world, especially as means to decide a persons salary regardless of their qualifications, the job requirements and other important factors that are not covered at all or adequately by the model. It's purpose is educational. The data used to build the model is old (1994), hence now out of touch with modern salaries. Also, it is an extremely small sample of 49,000 people out the hundreds of millions workers in the US. It should not be considered representative.

## Caveats and Recommendations
This tool can be further improved by the addition of a UI, the improvement of the base model, and the use of better data. Use accordingly.
