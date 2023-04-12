import bs4
import urllib.request

nateUrl = "https://vibe.naver.com/chart"
htmlObject = urllib.request.urlopen(nateUrl)
webPage = htmlObject.read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

tag = bsObject.find('div', {'class':'data-v-e6467c90'})

print('## vibe의 메뉴 목록 ##')
li_list = tag.findAll('a href')
for li in li_list :
    print(li.text, end='  ' )