import sys
sys.path.insert(0, '/Users/KSC/sbaProject')
from crawler.entity import Entity
from crawler.service import Service

class Controller:
    def __init__(self):
        self.entity = Entity()
        self.service = Service()

    def modeling(self, soup):
        servie = self.service
        this = self.entity
        this.soup = service.naver_cartoon(soup)
        return this 
    
    def creating(self, myfolder, myfile):
        service = self.service
        # this = self.modeling(soup)
        this.myfolder = service.create_folder_weekend(myfolder)
        this.myfile = service.create_saveFile(myfile)
        return this

if __name__ == '__main__':
    api = Controller()
    service = Service()
    service.naver_cartoon('https://comic.naver.com/webtoon/weekday.nhn')
    api.creating('c:\\imsi\\', 'cartoon.csv') 
    