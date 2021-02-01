import tweepy
import requests
import re
import time
from bs4 import BeautifulSoup

i = 1

while i == 1:
    r = requests.get('https://www.worldometers.info/coronavirus/')
    soup = BeautifulSoup(r.text, 'html.parser')

    test = [0,1,2]
    counter = 0;
    for div in soup.findAll('div',{'class':'maincounter-number'}):
        counter+1
        test.insert(counter, div)

    CVCT = str(test[2])
    CVCT = (re.sub('<[^>]+>','',CVCT)).strip()

    CVCD = str(test[1])
    CVCD = (re.sub('<[^>]+>','',CVCD)).strip()

    CVCR = str(test[0])
    
    CVCR = (re.sub('<[^>]+>','',CVCR)).strip()


    print("Total Coronavirus Cases: " + CVCT,'\n' "Current Deaths: " + CVCD, '\n' "Total Recoveries: " + CVCR)

# personal details 
    consumer_key = "replace with consumer key"
    consumer_secret = "replace with consumer secret"
    access_token = "replace with access token"
    access_token_secret = "replace with acces token secret"

# authentication of consumer key and secret 
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret) 
  
# authentication of access token and secret 
    auth.set_access_token(access_token, access_token_secret) 
    api = tweepy.API(auth) 
  
# update the status 
    api.update_status(status = "Total Coronavirus Cases: " + CVCT + '\n' "Current Deaths: " + CVCD + '\n' "Total Recoveries: "
                  + CVCR + "\n #Coronavirus #Corona #Covid19 #CoronaVirusUpdate")

    time.sleep(3600)
