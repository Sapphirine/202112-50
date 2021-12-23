# Sentiment Analysis between Social Media Personalities Events and Market/Cryptocurrency Trends
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)
EECS E6893 Final Project
Group 50


**Project Objective:** \
 This project aims to uncover trends between social media and the stock/cryptocurrency markets. An LSTM model is used to predict market trends for both stocks and cryptocurrencies based on the events occurring on Twitter and Reddit.

### Packages
This project is developed using python Python 3.7.12 and the packages below

 *	Python 3.7.12 
 * 	tensorflow 2.7.0
 * 	Numpy
 *	Pandas
 * 	Tweepy
 * 	snscrape.modules.twitter
 * 	PRAW
 *	PSAW
 * 	yfinance
 *  Sklearn
 *	keras_tuner
 * 	Airflow

## Code Run Instructions
Install the necessary requirements by running the following command.

~~~python
pip install -r requirements.txt
~~~

next run the main_notebook which contains calls to all the APIs present in the project. You can choose the stock for which you want to run the prediction model.
A pre-run model for Bitcoin prediction is present in the Example_Notebooks directory.


**Methodology:**
1. Twitter and Reddit data are used to guage social media sentiment about specific stock/cryptocurrency.
2. Daily data collection is done using Twitter and Reddit API(See Data_Streaming_Scripts)
3. Prediction of Open price for next day is given using LSTM Model trained using historical data.


**Dataset:** \
Our dataset consists of 3 parts:
1. Reddit Data: Historical Reddit Data is collected using RedditPastClient.py. Daily updates to reddit data are done using the RedditClient.py script which is deployed with the help of PRAW package in python.
2. Twitter Data: snscrape.modules.twitter is used for collection of historic tweets(500 per day) for every specific stock/crypto. Tweepy is used for live collection of tweets.
3. Yahoo Finance: yfinance api is used for collection of stock data

The historic data for Bitcoin used in the Bitcoin_Prediction_and_Experimentation.ipynb notebook is available at https://drive.google.com/drive/folders/1_Kujv9WRrK-vIHeOU2scmiTb9vbc9u2U?usp=sharing


**Result:** 

| Model      | MSE |
| ----------- | ----------- |
| ARIMA      | 0.239       |
| XGBoost   | 0.008        |
| LSTM-1  | 0.0102       |
| LSTM-2  | 0.008       |
| LSTM-Final   | 0.003        |