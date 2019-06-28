import requests
from bs4 import BeautifulSoup
import urllib.request

headers = {
    'Referer':'http://music.163.com/',
    'Host':'music.163.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.75 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    }

# 歌单的url地址
play_url = 'https://music.163.com/playlist?id=411796573'

# 获取页面内容
s = requests.session()
response=s.get(play_url,headers = headers).content

#使用bs4匹配出对应的歌曲名称和地址
s = BeautifulSoup(response,'lxml')
main = s.find('ul',{'class':'f-hide'})


lists=[]
for music in main.find_all('a'):
    list=[]
    # print('{} : {}'.format(music.text, music['href']))
    musicUrl='http://music.163.com/song/media/outer/url'+music['href'][5:]+'.mp3'
    musicName=music.text
    # 单首歌曲的名字和地址放在list列表中
    list.append(musicName)
    list.append(musicUrl)
    # 全部歌曲信息放在lists列表中
    lists.append(list)

print(lists)

# 下载列表中的全部歌曲，并以歌曲名命名下载后的文件，文件位置为当前文件夹
for i in lists:
    url=i[1]
    name=i[0]
    try:
        print('正在下载',name)
        urllib.request.urlretrieve(url,'./%s.mp3'% name)
        print('下载成功')
    except:
        print('下载失败')
