import bs4
import urllib.request

## 함수 선언부
def getItemInfo(item_tag) :
    
    #제품명
    titles = item_tag.find("div", {"class": "title"}).text
    #이미지 .. 이미지 파일 형식 변경?
#     thumbs = item_tag.find("img", {"class": "product_pic"}).src

    #회사명
    companys = item_tag.find("div", {"class": "company"}).text
    # 최종가격
    fPrice = item_tag.find("span", {"class": "final_price"}).text
  
    #price_origin no_discount = 할인없을시 출력되는 태그값     
    #할인율
    disRate = item_tag.find("span", {"class": "discount_rate"}).text
     
    #원가격
    oriPrice = item_tag.find("span", {"class": "price_origin"}).text
      
    itemsImgUrl = item_tag.find("src", {"class": "product_pic"}).text
    
    return [titles, companys, fPrice, disRate, oriPrice, itemsImgUrl]
  

   
# thumbs,
# 썸네일 이미지 경로 
 # 이미지 없는 경우 예외처리
            # if news.select_one('.thumb img') is not None : 
            #     thumbnail_url = news.select_one('.thumb img')['src']
            # else :
            #     thumbnail_url = 'none'
# price_origin no_discount
## 전역 변수부
itemUrl = "https://hottracks.kyobobook.co.kr/ht/evnExh/evnExhDetail/82107?gnbIndex=3"




## 메인 코드부
htmlObject = urllib.request.urlopen(itemUrl)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
tag = bsObject.find('ul', {'class': 'evt_products'})
all_items = tag.findAll('li', {'class': 'prod_item'})

for item in all_items :
    print(getItemInfo(item))

