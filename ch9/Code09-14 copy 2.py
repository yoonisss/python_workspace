import bs4
import urllib.request

## 함수 선언부
def getBookInfo(book_tag) :
    fPrice = 0
    disRate = 0
    oriPrice = 0
    #제품명
    titles = book_tag.find("div", {"class": "title"}).text
    #이미지 .. 이미지 파일 형식 변경?
    # thumbs = book_tag.find("div", {"class": "product_pic"})
    # itemThumb = thumbs.find("img").text
    #회사명
    companys = book_tag.find("div", {"class": "company"}).text
    # 최종가격
    # fPrice = book_tag.find("span", {"class": "final_price"}).text
    if fPrice is not None :
         fPrice = book_tag.find("span", {"class": "final_price"}).text
    else :
         fPrice = book_tag.find("span", {"class": "price_origin no_discount"}).text
    #price_origin no_discount = 할인없을시 출력되는 태그값     
    #할인율
    # disRate = book_tag.find("span", {"class": "discount_rate"}).text
    if disRate is not None :
         disRate = book_tag.find("span", {"class": "discount_rate"}).text
    else :
         disRate = 'none'  
    #원가격
    # oriPrice = book_tag.find("span", {"class": "price_origin"}).text
    if oriPrice is not None :
         oriPrice = book_tag.find("span", {"class": "price_origin"}).text
    else :
         oriPrice = 'none'

    return [titles, companys, fPrice, disRate, oriPrice]
# 썸네일 이미지 경로 
 # 이미지 없는 경우 예외처리
            # if news.select_one('.thumb img') is not None : 
            #     thumbnail_url = news.select_one('.thumb img')['src']
            # else :
            #     thumbnail_url = 'none'
# price_origin no_discount
## 전역 변수부
bookUrl = "https://hottracks.kyobobook.co.kr/ht/gift/category/000020"




## 메인 코드부
htmlObject = urllib.request.urlopen(bookUrl)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
tag = bsObject.find('ul', {'class': 'evt_products'})
all_items = tag.findAll('li', {'class': 'prod_item'})

for item in all_items :
    print(getBookInfo(item))

