import bs4

webPage = open('HTML/Sample03.html', 'rt', encoding='utf-8').read()
bsObject = bs4.BeautifulSoup(webPage, 'html.parser')

tag = bsObject.find('div', {'id':'myId1'})
print(tag)
print()

tag = bsObject.find('div', {'class':'myClass1'})
print(tag)
print()

tag = bsObject.findAll('div', {'class':'myClass1'})
print(tag)
print()