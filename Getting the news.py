#Puts news in a folder called Raw Data
import requests
import json
import os
os.chdir(os.curdir+"/1.Raw Data")
''' Go to https://newsapi.org/docs/endpoints/everything for parameterisation'''
url = ('https://newsapi.org/v2/everything?q=bitcoin&language=en&apiKey=0e4810893f704b91bbc0c4f557f32072')
response = requests.get(url)
print(response.json())
for page_no in range(int(response.json()["totalResults"]/100)-1):
	url = ('https://newsapi.org/v2/everything?q=bitcoin&pageSize=100&page=' + str(
		page_no+1) + '&language=en&apiKey=0e4810893f704b91bbc0c4f557f32072')
	response2 = requests.get(url)
	array = response2.json()
	print(response2.json())
	articles = array['articles']
	for int in range(100):
		print(int+page_no*100)
		with open("article"+str(int+page_no*100)+'.json', 'w') as outfile:
			json.dump(articles[int]["description"], outfile)