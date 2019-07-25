try:
    import requests
    from bs4 import BeautifulSoup
    import  re
except:
    print("Some Modules are Missing ..... ")


class TedTalk(object):
    def __init__(self):
        self.title = []
        self.url_data = []
        self.time = []
        self.talk = []
        self.data=[]
        self.url="https://www.ted.com/playlists/browse?topics=list"

    def __worker(self):
        r = requests.get(url=self.url)
        soup = BeautifulSoup(r.text, 'html.parser')

        for x in soup.findAll(class_="media__message"):
            for y in x.findAll(class_="h9"):
                base_url = "https://www.ted.com"
                self.url_data.append(base_url +y.find('a')["href"])
                self.title.append(y.text.strip())

        pattern_talk =  re.compile(r'\d{1,3} talks')
        pattern_time =  re.compile(r'\d{1,2}h \d{1,2}[hms]')

        for x in soup.findAll(class_="media__message"):
            for y in x.findAll(class_="meta"):
                text = y.text.strip()

                matches = pattern_talk.finditer(text)
                for match in matches:
                    self.talk.append(match.group(0))

                matches1 = pattern_time.finditer(text)
                for match1 in matches1:
                    self.time.append(match1.group(0))

        for c,x in enumerate(zip(self.title, self.url_data, self.time, self.talk)):
            self.data.append(x)

        return self.data



    @property
    def get(self):
        user_data = self.__worker()
        return user_data

obj = TedTalk()
print(obj.get)