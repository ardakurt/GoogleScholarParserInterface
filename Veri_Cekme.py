from Yazar import *
from bs4 import BeautifulSoup
import Scholar_Lib
#sudo apt-get install python3-bs4 (beautifulsoup kurma)
import requests


class Veri_Cekme(Yazar):

    def schoolar_url_getir(self):
        url = "https://scholar.google.com.tr/" + "scholar?hl=tr&q=" + self.get_yazar_ad() + " " + self.get_yazar_soyad() + "&btnG=&lr="
        r = requests.get(url)

        if r.status_code == 200:
            print("Bağlantı Başarılı")
            soup = BeautifulSoup(r.content,"html.parser")
            soup.prettify()
        else:
            print("Bağlantı Başarısız")

        return r.url




    def get_yazar_sayfasi_href(self):


            url = self.schoolar_url_getir()
            href_link = " "
            r = requests.get(url)
            print(r.url)

            if r.status_code == 200:
                soup = BeautifulSoup(r.content,"html.parser")
                soup.prettify()
                for link in soup.find_all('h4','gs_rt2'):
                    for a in link.find_all('a'):
                       href_link = a.get('href')
                       print(href_link)

            else:
                print("Bağlantı Başarısız")
                return

            return href_link



    def get_yazar_sayfasi_html(self):

        url = "https://scholar.google.com.tr" + self.get_yazar_sayfasi_href()
        r = requests.get(url)
        print(url)

        return r.url













kisi = Veri_Cekme("Ecir Uğur" , "Küçüksille")
#print(kisi.schoolar_url_getir())
#kisi.get_alintilar_href_link()
#print(kisi.get_yazar_sayfasi_href())
kisi.get_yazar_sayfasi_html()