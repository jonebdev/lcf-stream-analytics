import matplotlib.pyplot as plt
import numpy as np
import requests
import time
import datetime
import json

"""
  script for getting all of the views for streams and putting them into a csv
"""

url: str = "https://lighthousechristianfellowship.sermon.net/restapi/getPostingCollection"
offset = 273
start = offset
limit = 1
playlistId = 4049957
mediaCenterId = 4046784
csvFile = open("LCF_Stream_Analytics.csv", "w")
csvFile.write("id,date,title,playcount\n")

dates = []
views = []
titles = []
ids = []

for i in range(start):
    requestUrl = "{url}?offset={offset}&limit={limit}&playlistId=4049957&mediaCenterId=4046784".format(offset=offset, limit=limit, url=url)
    req = requests.get(requestUrl)
    data = req.json()
    ids.append(data['data'][0]['collection'][0]['id'])
    views.append(data['data'][0]['collection'][0]['playsCount'])
    titles.append(data['data'][0]['collection'][0]['ogTitle'])
    tempDate = datetime.datetime.fromtimestamp(data['data'][0]['collection'][0]['posted'])
    dates.append(tempDate.strftime("%m/%d/%Y, %H:%M:%S"))
    
    
    play = views[i]
    title = titles[i]
    date = dates[i]
    


    line = '{vidId},"{title}","{date}",{plays}\n'.format(vidId=ids[i], title=titles[i], date=dates[i], plays=views[i])
    csvFile.write(line)
    offset -= 1

csvFile.close()

