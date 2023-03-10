
# Goal , post a random cat clipping to Mastodon as a bot.

import random
import requests

baseserver = "https://digi.kansalliskirjasto.fi"
## local = "http://localhost:9090"

api_url = baseserver + "/rest/article-search/search-by-type?offset=0&count=22"


#from mastodon import Mastodon


#Mastodon.create_app(
#    'oldcatclipbot',
#    api_base_url = 'https://mastodon.social',
#    to_file = 'pytooter_clientcred.secret'
#)


headers = {'Content-type': 'application/json', 'Accept': 'application/json'}

data = {
    "keywords": ['kissa']
}


r = requests.post(url=api_url, json=data, headers=headers)  


print("Status:", r.status_code)

if (r.status_code == 200):

    response = r.json() 

    totalResults = response['totalResults']
    allResults = response['rows']
    randomOne = random.choice(allResults)

    ## print(randomOne)

    # Grab data of the clipping.

    articleTitle = randomOne['title']
    previewImageUrl = baseserver + randomOne['previewImageUrl']
    bindingTitle = randomOne['bindingTitle']
    bindingDate = randomOne['bindingDate']
    fullUrl = baseserver + randomOne['url']


    tootText = articleTitle + "\nFrom:" + bindingTitle  \
        + "\nPublished originally on (DD.MM.YYYY): " + bindingDate

    tootText += "\nSee full image at: "+fullUrl

    print(tootText)



