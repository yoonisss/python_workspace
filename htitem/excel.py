import bs4
import urllib.request
import xlsxwriter
import time
import datetime
import random


## 함수 선언부
def getItemInfo(item_tag) :
   #제품명
    titles = item_tag.find("div", {"class": "title"}).text
    #회사명
    companys = item_tag.find("div", {"class": "company"}).text
    # 최종가격
    fPrice = item_tag.find("span", {"class": "final_price"}).text
    #price_origin no_discount = 할인없을시 출력되는 태그값     
    #할인율
    disRate = item_tag.find("span", {"class": "discount_rate"}).text
    #원가격
    oriPrice = item_tag.find("span", {"class": "price_origin"}).text
    #상품 이미지
    itemsImgUrl = item_tag.find("div", {"class": "product_pic"}).img
    return [titles, companys, fPrice, disRate, oriPrice, itemsImgUrl]

## 전역 변수부
url = "https://hottracks.kyobobook.co.kr/ht/evnExh/evnExhDetail/82107?gnbIndex=3"
folderName = 'C:/python_workspace/hottrack/'
wsName = '핫딜 목록'
header = ['제품명', '회사명', '최종가격', '할인율', '원가격', '상품이미지']

## 메인 코드부
while True :
    print()
    print("--------------------")
    now = datetime.datetime.now()
    print('핫트랙스 핫딜 이벤트 크롤링  --> ', now.strftime('%Y-%m-%d %H:%M:%S'), )
    filename = folderName + 'htitem_' + now.strftime('(%Y년%m월%d일%H시%M분%S초)')+'.xlsx'

    workbook = xlsxwriter.Workbook(filename)
    worksheet = workbook.add_worksheet(wsName)
    cell_format1 = workbook.add_format()
    cell_format1.set_bold()
    cell_format1.set_font_color(random.choice(['red','green', 'blue', 'gray', 'magenta', 'cyan']))
    cell_format1.set_font_size(15)
    cell_format1.set_align('center')
    cell_format1.set_align('vcenter')
    cell_format1.set_bg_color('yellow')
    cell_format1.set_border(1)

    worksheet.set_column('A:F', 20)  # 약 0.34
    for i in range(len(header)) :
        worksheet.write(0, i, header[i], cell_format1)

    cell_format2 = workbook.add_format()
    cell_format2.set_border(1)

    pageNumber = 1
    rowNum = 1
    while True :
        try :
            itemUrl = url + str(pageNumber)
            pageNumber += 1

            htmlObject = urllib.request.urlopen(itemUrl)
            webPage = htmlObject.read()
            bsObject = bs4.BeautifulSoup(webPage, 'html.parser')
            tag = bsObject.find('ul', {'class': 'evt_products'})
            all_items = tag.findAll('li', {'class': 'prod_item'})

            for item in all_items:
                info_list = getItemInfo(item)
                worksheet.write(rowNum, 0, rowNum,  cell_format2)
                for i in range(len(info_list)) :
                    worksheet.write(rowNum, i+1, info_list[i], cell_format2)
                rowNum += 1

        except :
            break


    print(filename, '으로 저장됨.')
    print("--------------------")
    time.sleep(60*60*24) # 1일에 해당하는 초(60초*60분*24시)