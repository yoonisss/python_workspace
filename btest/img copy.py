from bs4 import BeautifulSoup as bs
from urllib.request import urlopen

queryUrl = input('검색어 입력: ')
crawl_num = int(input('크롤링할 페이지 수 입력: '))
cafe_name = []
# crawl_num으로 설정한 페이지 수 만큼 크롤링
for i in range(1,crawl_num):
	# 검색어 입력 값과 페이지 값을 입력받아 처리해주기 위한 url
    url = 'http://www.menupan.com/search/restaurant/restaurant_result.asp?sc=basicdata&kw=' + queryUrl + '&page=' + str(i)
    html = urlopen(url)
    # bs4를 이용한 파싱
    soup = bs(html, "html.parser")
    
    # image, name 정보를 수집하기 위한 soup 메서드
    img = soup.find_all(class_='thumb')
    img_text = soup.find_all('dt')
	
    # name 정보 list에 저장
    for i in img_text:
        cafe_name.append(i.text)
    
    # name 정보의 공백 문자열 제거
    word_slice = "\n\n"
    for i, word in enumerate(cafe_name):
        if word_slice in word:
            cafe_name[i] = word.strip(word_slice)
            
    n = 1
    # image를 수집하기 위한 original_url 설정
    originalUrl = 'https://www.menupan.com/'
    for i in img:
    	# 태그의 src 속성 추출
        imgUrl = i['src']
        
        # image 주소
        url = originalUrl + imgUrl
        
        # images 폴더에 .jpg 확장자로 카페 이미지 저장
        with urlopen(url) as f:
            with open('./images/' + cafe_name[n-1] + '.jpg', 'wb') as h:
                 img = f.read()
                 h.write(img)
        
        n += 1
        if n > crawl_num:
            break
    print('크롤링 종료')