
# coding: utf-8

# In[1]:


import requests


# In[2]:


response = requests.post(
        "https://api.mailgun.net/v3/sandboxf739b30cd9aa47bf9fb818fc4c6883da.mailgun.org/messages",
        auth=("api", mailgun_key),
        data={"from": "Excited User <mailgun@sandbox69f4b1683cf340f1b876b47ae74e0d74.mailgun.org>",
              "to": "Excited User <mailgun@sandbox69f4b1683cf340f1b876b47ae74e0d74.mailgun.org>",
              "subject": "Hello",
              "text": "Testing some Mailgun awesomness!"})

response.text


# In[3]:


response = requests.get('https://api.darksky.net/forecast/dark_sky_key/37.8267,-122.4233?units=si')
data = response.json()
print(data)


# In[4]:


# Right now it is TEMPERATURE degrees out and SUMMARY. 
#Today will be TEMP_FEELING with a high of HIGH_TEMP and a low of LOW_TEMP. RAIN_WARNING.


response = requests.get('https://api.darksky.net/forecast/dark_sky_key/40.7128,-74.0060?units=si')
nyc = response.json()
print(nyc)


# In[5]:


nyc.keys()


# In[6]:


current_temperature = nyc['currently']['temperature']
current_temperature


# In[7]:


summary = nyc['currently']['summary']
summary


# In[8]:


temp_feeling = nyc['currently']['temperature']

if temp_feeling > 25:
    print("hot")
elif temp_feeling < 15:
    print("cold")
else:
    print("warm")


# In[10]:


daily = nyc['daily']['data'][0]
    
print(daily['temperatureMax'])


# In[11]:


daily = nyc['daily']['data'][0]
    
print(daily['temperatureMin'])


# In[12]:


print(daily['precipProbability'])


# In[27]:


rain_warning = daily['precipProbability']

if rain_warning > 0.5:
    sentence = "Right now it is "+str(current_temperature)+" degrees out and "+summary+". Today will be "+str(temp_feeling)+" with a high of "+str(daily['temperatureMax'])+" and a low of "+str(daily['temperatureMin'])+" degrees. It's going to rain. Bring an umbrella!"

else:
    sentence = "Right now it is "+str(current_temperature)+" degrees out and "+summary+". Today will be "+str(temp_feeling)+" with a high of "+str(daily['temperatureMax'])+" and a low of "+str(daily['temperatureMin'])+" degrees. It's not going to rain. You don't need an umbrella!"
    
print(sentence)


# In[28]:


import datetime
right_now = datetime.datetime.now()
right_now

response = requests.post(
        "https://api.mailgun.net/v3/sandboxf739b30cd9aa47bf9fb818fc4c6883da.mailgun.org/messages",
        auth=("api", mailgun_key),
        data={"from": "Excited User <mailgun@sandbox69f4b1683cf340f1b876b47ae74e0d74.mailgun.org>",
              "to": "Excited User <mailgun@sandbox69f4b1683cf340f1b876b47ae74e0d74.mailgun.org>",
              "subject": "8AM Weather forecast: "+ str(right_now.strftime("%Y-%m-%d")),
              "text": sentence})

