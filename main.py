
from bs4 import BeautifulSoup

import requests

class LP:
    def __init__(self, name, price, avail, href, store):
        self.name = name
        self.price = price
        self.avail = avail
        self.href = href
        self.store = store


store = ["사운드룩", "바이닐 코리아", "서울 바이닐", "레코드스톡", "마이페이보릿시네마스토어",
         "마이페이보릿시네마스토어", "마이페이보릿시네마스토어", "마이페이보릿시네마스토어"]

store_url = ["soundlook/category/e77769162d0441328d8fd5b8bd05aa97?",
             "waxtime/category/9ca4b5886a1347a080cdd81f1da49a14?",
             "seoulvinyl/category/c346b188a53b479d86103c7eb4a9a66e?",
             "recordstock/category/e690f8a7f105476c899bf0a94966d467?",
             "cinemastore/category/e10a19ae19974d81b7653c0833d872e6?",
             "cinemastore/category/0c0ce5f2d62e4378862c72398d84c803?",
             "cinemastore/category/126207230e3a47cdadc5ea51535e9e8d?",
             "cinemastore/category/778ec8837bb74a3e9ce4beb2d63368a1?"]
store_range = [66, 14, 23, 9, 1, 2, 5, 5]




arr = []

for k in range(1):
    for i in range(1, store_range[k]+1):
        url = "https://smartstore.naver.com/" + store_url[k] + "st=POPULAR&free=false&dt=IMAGE&page=" + str(i) + "&size=40"
        parse_url = requests.get(url)

        soup = BeautifulSoup(parse_url.content, "html.parser")
        try:
            item = soup.find_all('li', {'class': '-qHwcFXhj0'})
            for each in item:
                name = each.find('strong', {'class': 'QNNliuiAk3'}).text
                price = each.find('div', {'class': '_23DThs7PLJ'}).text

                try:
                    avail = each.find('div', {'class': '_18kuVNtTNE'}).text
                except:
                    avail = "avail"

                href = "https://smartstore.naver.com/" + each.find('a').attrs['href']

                arr.append(LP(name, price, avail, href, store[k]))

        except:
            print()



for each in arr:
    print("[" + each.store + "]")
    print("이름", each.name)
    print("가격", each.price)
    print("주소", each.href)

    if each.avail != "avail":
        print("품절")

    print()


