# Insurance Prediction Project 🏥

- Created a model that predicts the Insurance charges of a person based on different attributes such as number of children, smoker or not, and the like. The best accuracy of the model is about <b>(MAE ~ $ 1600)</b>
- Dataset was obtained on Kaggle [here](https://www.kaggle.com/mirichoi0218/insurance).
- Applied Linear Regression, Lasso Regression, Random Forests, and Gradient Boosted Random Forests and also tuned the hyper-parameters using GridSearchCV to get the best model.
- Productionized the model using Flask and hosted the model on Heroku cloud [here](https://flask-health-insurance.herokuapp.com/)

## Motivation 💪

I wanted to get started with some basic algorithms that are used in Data Science and Machine Learning. I thought that a regression project is the most basic way in which I can kickstart my journey of learning Data Science.

## References 📚

| What | Where | 
| --- | --- |
| <b>Dataset</b> | https://www.kaggle.com/mirichoi0218/insurance | 
| <b>Productionization</b> | https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2 <br> & <br> https://towardsdatascience.com/productionizing-your-machine-learning-model-221468b0726d |
<br>

## Dataset 💾

Although I have a profound interest in collecting my own data, I came across this dataset on [Kaggle](https://www.kaggle.com/mirichoi0218/insurance).
The dataset has various attributes such as age, number of children and such. The primary motive of this dataset is to be able to predict the amount of insurance 💲 money used by the person.

## Exploratory Data Analysis

![Corr Plot]()
![Bar Plot]()
![Box Plot]()
## Model Building

I tried 4 different regression models, Multiple Linear Regression, Lasso Regression, Random Forests and Gradient Boosted Random Forests. The metric I used was Mean Absolute Error. I split the dataset with 75-25 train test split.
The results are this:
<br>
| Model | MAE |
| --- | --- |
| MLR | 4445.74 |
| Lasso | 4445.79 |
| Random Forests | 2632.81 |
| Gradient Boosted Random Forests | 1593.48 |

<br>

I tried tuning the hyper parameters of the Random Forests using <b>GridSearchCV</b>, but it did not have any significant impact on the model.

## Productionization 💻

I used the Gradient Boosted Random Forests as the final model. I used Flask to Productionize the model, and hosted the model on Heroku [here](https://flask-health-insurance.herokuapp.com/). The reference for doing this can be found [here](https://towardsdatascience.com/productionize-a-machine-learning-model-with-flask-and-heroku-8201260503d2) and [here](https://towardsdatascience.com/productionizing-your-machine-learning-model-221468b0726d).

Once again, the model is live [here](https://flask-health-insurance.herokuapp.com/)!
Go ahead, try it!
