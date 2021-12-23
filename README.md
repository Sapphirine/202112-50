# Sentiment Analysis between Social Media Personalities Events and Market/Cryptocurrency Trends
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
EECS E6893 Final Project
Group 50


**Project Objective:** \
 This project aims to uncover trends between social media and the stock/cryptocurrency markets. An LSTM model is used to predict market trends for both stocks and cryptocurrencies based on the events occurring on Twitter and Reddit.

### Packages
This project is developed using python Python 3.7.12 and the packages below

 i) 	Python 3.7.12
 ii) 	tensorflow 2.7.0
 iii) 	Numpy
 iv)	Pandas
 v) 	Tweepy
 vi) 	snscrape.modules.twitter
 vii) 	PRAW
 viii)	PSAW
 ix) 	yfinance
 x)  	Sklearn
 xi)	keras_tuner
 xi) 	Airflow

## Code Run Instructions
Install the necessary requirements by running the following command.

~~~python
pip install -r requirements.txt
~~~

next run the main_notebook which contains the keras model defination.
The model can be loaded directly using the 
~~~python
import tensorflow
model = tensorflow.keras.models.load_model('path/to/location')()
~~~
Each model can be run and verified.

**Methodology:**
1. Twitter and Reddit data are used to guage social media sentiment about specific stock/cryptocurrency.
2. Daily data collection is done using Twitter and Reddit API(See Data_Streaming_Scripts)
3. Prediction of Open price for next day is given using LSTM Model trained using historical data.


**Dataset:** \
Our dataset consists of 3 parts:
1. Reddit Data: Historical Reddit Data is collected using RedditPastClient.py. Daily updates to reddit data are done using the RedditClient.py script which is deployed with the help of PRAW package in pyt

2. Yahoo Finance + Airflow
The stock prices are updated by the Airflow scheduler, which runs Yahoo Finance in Python to get the most recent close price of all companies. The data are saved and sent to the backend of our Django system.

