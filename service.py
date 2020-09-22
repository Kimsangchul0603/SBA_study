from bs4 import BeautifulSoup
from urllib.request import urlopen
from pandas import DataFrame

class Service:
    def __init__(self):
        pass

    def bugs_music(self):
        pass

    def naver_movie(self):
        pass

    def naver_cartoon(response, soup):
        myparser = 'html.parser'
        myurl = 'https://comic.naver.com/webtoon/weekday.nhn'
        response = urlopen(myurl)
        soup = BeautifulSoup(response, myparser)
        
        return response, soup

        # 요일별 폴더 생성
    def create_folder_weekend(self):
        weekday_dict = {'mon':'월요일', 'tue':'화요일', 'wed':'수요일', 'thu':'목요일', 'fri':'금요일', 'sat':'토요일', 'sun':'일요일'}

        # shutil : shell utility
        import os, shutil
        myfolder = 'c:\\imsi\\'

        # 각 이미지를 저장해주는 함수
    def create_saveFile(self):
        image_file = urlopen(mysrc)
        filename = myfolder + weekday_dict[myweekday] + '\\' + mytitle + '.jpg'
        # print(mysrc)
        # print(filename)

        myfile = open(filename, mode='wb')
        myfile.write(image_file.read()) # 바이트 형태로 저장
        myfile.close()

        try :
            if not os.path.exists(myfolder):
                os.mkdir(myfolder)

            for mydir in weekday_dict.values():
                mypath = myfolder + mydir

            if os.path.exists(mypath):
                # rmtree : remove tree
                shutil.rmtree(mypath)

                os.mkdir(mypath)

        except FileExistsError as err :
            print(err)

        mylist = [] # 데이터를 저장할 리스트

        mytarget = soup.find_all('div', attrs={'class':'thumb'})
        print(len(mytarget))

        for abcd in mytarget:
            myhref = abcd.find('a').attrs['href']
            myhref = myhref.replace('/webtoon/list.nhn?', '')
            result = myhref.split('&')
            # print(myhref)
            # print(result)
            mytitleid = result[0].split('=')[1]
            myweekday = result[1].split('=')[1]
            # print(mytitleid)
            # print(myweekday)

            imgtag = abcd.find('img')
            mytitle = imgtag.attrs['title'].strip()
            mytitle = mytitle.replace('?', '').replace(':', '')
            # print(mytitle)

            mysrc = imgtag.attrs['src']
            # print(mysrc)

            saveFile(mysrc, myweekday, mytitle)
            # break

            sublist = []
            sublist.append(mytitleid)
            sublist.append(myweekday)
            sublist.append(mytitle)
            sublist.append(mysrc)
            mylist.append(sublist)
        
        mycolumns = ['타이틀번호', '요일', '제목', '링크']
        myframe = DataFrame(mylist, columns=mycolumns)

        filename = 'cartoon.csv'

        return myframe.to_csv(filename, encoding='utf-8', index=False)
        print(filename + '파일로 저장됨')
        print('finished')

        

