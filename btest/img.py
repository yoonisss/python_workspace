import urllib.request
from bs4 import BeautifulSoup
 
print('Beginning file download with urllib2...')
 
url = 'http://image.kyobobook.co.kr/newimages/giftshop_new/resources/images/common/noimg.png'
req = urllib.request.Request(url)
res = urllib.request.urlopen(url).read()
 
soup = BeautifulSoup(res,'html.parser')
soup = soup.find("div",class_="poster")
#img의 경로를 받아온다
imgUrl = soup.find("img")["src"]
 
#urlretrieve는 다운로드 함수
#img.alt는 이미지 대체 텍스트 == 마약왕
urllib.request.urlretrieve(imgUrl, soup.find("img")["alt"]+'.jpg')


# <img src="http://image.kyobobook.co.kr/newimages/giftshop_new/goods/400/1642/hot1673537360360.jpg" 
# lt="핫트랙스 상품" class="bd_img" onerror="this.src='http://image.kyobobook.co.kr/newimages/giftshop_new/resources/images/common/noimg.png';">