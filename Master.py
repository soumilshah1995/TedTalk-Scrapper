import  requests
import pandas as pd
import ast



title = []
duration= []
talk=[]
url_data=[]


for page_num in range(100):

    print("Page Number", page_num)
    Query_String = {
        'curator':'editorial',
        'per_page':'24',
        'page':str(page_num +1)}

    headers={
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'en-US,en;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'http://www.wikipedia.org/',
        'Connection': 'keep-alive'}

    url = "https://www.ted.com/playlists/browse.json"
    r = requests.get(url=url,params=Query_String, headers=headers)
    data = r.json()

    for index in range(len(data["records"])):

            title.append(data["records"][index]["title"])
            duration.append(data["records"][index]["duration"])
            talk.append(data["records"][index]["talks"])
            url_data.append(data["records"][index]["url"])

            #print("{}\t{}\t{}\t{}".format(title,duration,talk,url))


zipped = zip(title,duration,talk,url_data)
df =pd.DataFrame(data=zipped)
df.to_csv("TED_DataSet.csv")


