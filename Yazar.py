class Yazar:
    journal = " "       #makaleler
    volume = 0          #version
    number = 0          #numara
    pages = 0           #sayfa
    year = 0            #yıllar
    publisher = " "     #yayımcı

    def __init__(self,yazar_ad, yazar_soyad):
        self.yazar_ad = yazar_ad
        self.yazar_soyad = yazar_soyad

    def get_yazar_ad(self):
        return self.yazar_ad

    def get_yazar_soyad(self):
        return self.yazar_soyad

    def get_yazar_journal(self):
        return self.journal

    def get_yazar_volume(self):
        return self.journal

    def get_yazar_number(self):
        return self.number

    def get_yazar_pages(self):
        return self.pages

    def get_yazar_year(self):
        return self.year

    def get_yazar_publisher(self):
        return self.publisher

