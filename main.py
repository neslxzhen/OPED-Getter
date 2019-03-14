import re
import urllib.request
import time
from bs4 import BeautifulSoup

#�Ѽƽվ�---------------------------------------------------------------
from selenium import webdriver

format="mp4" #�U���榡
fileName="test.txt"

urls=[]
vedioTitles=[]
songTitles=[]
myTitles=[]

#�}���ɮ�Ū���ʵe�W�١A�ϥ�wiki�j�M����oOP.ED--------------------------------------------------
print("���oOP.ED...")
browser=webdriver.Chrome()
browser.implicitly_wait(1)

c=0
browser.get("https://zh.wikipedia.org/wiki/Wikipedia:%E9%A6%96%E9%A1%B5") #������
for myTitle in open(fileName,"r",encoding="UTF-8"):
    print(c)
    myTitle=myTitle.strip()
    myTitles.append(myTitle)

    #�j�M
    browser.find_element_by_id("searchInput").send_keys(myTitle+" �ʵe")
    browser.find_element_by_id("searchButton").click() #������
    browser.implicitly_wait(1)

    #��Ĥ@��
    x=BeautifulSoup(browser.page_source,"html.parser").find("div","mw-search-result-heading")
    a="https://zh.wikipedia.org"+x.find("a").get("href")
    code=urllib.request.urlopen(a).read() #���HTML
    browser.get(a) #������
    browser.implicitly_wait(1)

    #�NHTML��r��
    codeStr=str(code,'utf-8') #�ϥ�utf-8�\Ū�r��

    #�M��q�W
    i=""
    j1=0
    j2=0
    i=codeStr[codeStr.find("���Y���u"):]
    line=(i[:i.find("�v")+1])
    while(line.find("<")>0):
        j1=line.find("<")
        j2=line.find(">")
        line=line[:j1]+line[j2+1:]
    print (line)
    if line !="":
        songTitles.append(line)
    else:
        songTitles.append(None)

    i=codeStr[codeStr.find("�������u"):]
    line=(i[:i.find("�v")+1])
    while(line.find("<")>0):
        j1=line.find("<")
        j2=line.find(">")
        line=line[:j1]+line[j2+1:]
    print (line)
    if line !="":
        songTitles.append(line)
    else:
        songTitles.append(None)
    c=c+1
print("�w���oOP.ED")
print(songTitles)

#�N�q�W�t�s--------------------------------------------------------
print("�N�q�W�t�s...")
with open("songTitle.txt","w",encoding="UTF-8") as f:
    i=0
    j=0
    for line in songTitles:
        try:
            f.write(myTitles[j]+','+line+'\n') #line���Oint
        except:
            f.write(myTitles[j]+','+"None\n")
        i=i+1
        if i%2==0:j=j+1
print("�w�N�q�W�t�s")

#�N�q�W�g�J--------------------------------------------------------
print("�N�q�W�g�J...")
songTitles.clear()
for songTitle in open("songTitle.txt","r",encoding="UTF-8"):
    songTitle=songTitle.strip()
    list=songTitle.split(",")
    songTitles.append(list[1])
print("�w�N�q�W�g�J")
print(songTitles)

#�j�MYT------------------------------------------------------------------------
for songTitle in songTitles:
    if songTitle!="None":
        browser.get('https://www.youtube.com/results?search_query='+songTitle+"+OP")
        soup=BeautifulSoup(browser.page_source, "html.parser")
        browser.implicitly_wait(0) # �t��(��������)

        x=soup.find('a','yt-simple-endpoint style-scope ytd-video-renderer') # ��M�Ĥ@�� a �϶��B class="yt-simple-endpoint style-scope ytd-video-renderer"
        vedioTitle=x.get('title')
        href = x.get('href')
        urls.append("https://www.youtube.com"+href)
        vedioTitles.append(vedioTitle)
    else:
        urls.append("None")
        vedioTitles.append("None")
print (urls)
print ('-'*100)

#urls=['https://www.youtube.com/watch?v=PqY8dcRZ06k', 'https://www.youtube.com/watch?v=OYwcXfAYAbg', 'https://www.youtube.com/watch?v=FAOnsPouYGE', 'https://www.youtube.com/watch?v=nrGB04GIePQ', 'https://www.youtube.com/watch?v=xkMdLcB_vNU', 'https://www.youtube.com/watch?v=yi0428jRI9U', 'https://www.youtube.com/watch?v=F9kqColvQhA', 'https://www.youtube.com/watch?v=kLAZja_0cCs', 'https://www.youtube.com/watch?v=8aZ_hMX87eo', 'https://www.youtube.com/watch?v=evwO4B8nxsU', 'https://www.youtube.com/watch?v=CicnGW43Ukw', 'https://www.youtube.com/watch?v=09yPyy9eldI', 'https://www.youtube.com/watch?v=Cp89qis1ddo', 'https://www.youtube.com/watch?v=nHztuf7NRiU', 'https://www.youtube.com/watch?v=0V6mb19viaw', 'https://www.youtube.com/watch?v=BHtgSerQvSI', 'https://www.youtube.com/watch?v=oxxKm_O1xwo', 'https://www.youtube.com/watch?v=gbj_v67IrB4', 'https://www.youtube.com/watch?v=zuoER3g-FTg', 'https://www.youtube.com/watch?v=07XFP6BhGac', 'https://www.youtube.com/watch?v=OC8oadcsPxw', 'https://www.youtube.com/watch?v=_4sEQYAaMhM']

#�Nurl�t�s--------------------------------------------------------------------
with open('urlFile.txt','w',encoding='UTF-8') as f:
    i=0
    j=0
    for line in urls:
        if urls[i]!="None":
            f.write(myTitles[j]+","+line+','+vedioTitles[i]+'\n') #line���Oint
        i=i+1
        if i%2==0:j=j+1

#�Nurl�g�J--------------------------------------------------------
urls=urls.clear()
urls=[]
for url in open("urlFile.txt","r",encoding="UTF-8"):
    url=url.strip()
    list=url.split(",")
    urls.append(list[1])

#�U��----------------------------------------------------------------------------
i2=0
for url in urls:
    browser.get('https://ytmp3.cc/')
    print ('���Jhttps://ytmp3.cc/')

    i=0
    while (i==0):
        print ('�i�J�����ˬd�j��:'+myTitles[i2])
        time.sleep(5)
        try:
            print ('�M������')
            print (browser.find_element_by_id("title"))
            i=1
        except:
            print ('���s��z')
            browser.refresh() #���s��z

    print ('��Jurl'+url)
    browser.find_element_by_id('input').send_keys(url)
    browser.find_element_by_id("mp4").click()
    browser.find_element_by_id('submit').click()

    #�P�_download���s�s�b�P�_
    i1=0
    while (i1==0):
        print ('�i�J�ˬddownload�s�j��:')
        try:
            print ('�M��download')
            browser.find_element_by_id("download").click()
            print ('�s�b���I��')
            i1=1
        except:
            print ('���s�b')

    i2=i2+1
