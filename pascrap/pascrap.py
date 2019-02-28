from urllib.request import urlopen
from bs4 import BeautifulSoup

#globar_variable
url_pa="https://samakal.com/"
filepath= "html/al.html"

class Pascraper:
    __url   =''
    __data  =''
    __palog =None
    __soup  =None

    def __init__(self,url,palog):
        self.__url   =url
        self.__palog = palog

    def retrieve_webpage(self):
        try:
            html= urlopen(self.__url)
        except Exception as e:
            print(e)
            self.__palog.report(e)
        else:
            self.__data= html.read()
            if len(self.__data)>0:
                print("retrieve sucessfully")

    def write_page_as_html(self,file= filepath,data=''):
        try:
            with open(file, 'wb') as fileobject:
                if data:
                    fileobject.write(data)
                else:
                    fileobject.write(self.__data)
        except Exception as e:
            print(e)
            self.__palog.report(e)

    def read_page_from_html(self,file=filepath):
        try:
            with open(file) as fileobjects:
                self.__data=fileobjects.read()
        except Exception as e:
            print(e)
            self.__palog.report(e)

    def change_url(self,url):
        self.__url= url

    def print_data(self):
        print(self.__data)

    def convert_data_to_BS4(self):
        self.__soup=BeautifulSoup(self.__data,"html.parser")

    def perser_soup_to_normal_html(self):
        news_list=self.__soup.find_all(['h3'])
        print(news_list)
