import bs4
import urllib.request
import csv
import ssl

ssl_context = ssl.SSLContext()
ssl_context.verify_mode = ssl.CERT_NONE

## 함수 선언부
def getBookInfo(book_tag) :
   #제품명
    titles = book_tag.find("div", {"class": "title"}).text
    #회사명
    companys = book_tag.find("div", {"class": "company"}).text
    # 최종가격
    fPrice = book_tag.find("span", {"class": "final_price"}).text
    #price_origin no_discount = 할인없을시 출력되는 태그값     
    #할인율
    disRate = book_tag.find("span", {"class": "discount_rate"}).text
    #원가격
    oriPrice = book_tag.find("span", {"class": "price_origin"}).text
    #상품이미지
    itemsImgUrl = book_tag.find("dic", {"class": "product_pic"}).text
    return [titles, companys, fPrice, disRate, oriPrice, itemsImgUrl]

## 전역 변수부
#판매량 순 , 페이지 넘버 
url = "https://hottracks.kyobobook.co.kr/ht/evnExh/evnExhDetail/82107?gnbIndex=3"
# pageNumber = 1
# gnbIndex= 3

## 메인 코드부
csvName =  'CSV/test12.csv'

with open(csvName, 'w', newline='') as csvFp:
    csvWriter = csv.writer(csvFp)
    csvWriter.writerow(['제품명', '회사명', '최종가격', '할인율', '원가격'])


    try :
        itemUrl = url 
         #+ str(gnbIndex)+ str(pageNumber)
        # gnbIndex += 1
        htmlObject = urllib.request.urlopen(itemUrl)
        webPage = htmlObject.read()
        bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
        tag = bsObject.find('ul', {'class': 'evt_products'})
        all_items = tag.findAll('li', {'class': 'prod_item'})

        for item in all_items :
            info_list = getBookInfo(item)
            with open(csvName, 'a', newline='') as csvFp:
                csvWriter = csv.writer(csvFp)
                csvWriter.writerow(info_list)
    finally:
        
        print('Save. OK~')