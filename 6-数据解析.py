import encodings
import bs4
import lxml.etree
import requests
'''
# Xpath爬取起点中文网
url = 'https://www.qidian.com/rank/yuepiao/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'}

#发送请求
resp = requests.get(url,headers)
e = lxml.etree.HTML(resp.text) # 类型转换,把str转换成树形元素
names = e.xpath('//div[@class="book-mid-info"]/h2/a/text()')
authors = e.xpath('//p[@class="author"]/a[1]/text()')
for name,author in zip(names,authors):
    print(name,":",author)
'''
"""
# BeautifulSoup简介
from bs4 import BeautifulSoup
html = '''
    <html>
        <head>
            <title>这是标题</title>
        </head>
        <body>
        <h1 class="这是属性 info bg" float="left" id="gb">hello!</h1>
        <span>好好学习</span>
        <a href="www.baidu.com"></a>
        </body>
    </html>
'''
bs = BeautifulSoup(html, 'html.parser')
# bs = BeautifulSoup(html, 'lxml')
print(bs.title) # 获取title标签
print(bs.h1.attrs) # 获取h1标签的所有属性

print(bs.h1.get('class')) # 获取h1标签单个属性class的值
print(bs.h1['class']) # 获取h1标签单个属性class的值
print(bs.a['href']) # 获取a标签单个属性href的值

print(bs.title.text) # 获取title标签文本内容

# BeautifulSoup具体使用
from bs4 import BeautifulSoup
html = '''
    <html>
        <head>
            <title>这是标题</title>
        </head>
        <body>
            <h1 class="这是属性 info bg" float="left" id="gb">hello!</h1>
            <h1 class="info">world!</h1>
            <span>好好学习</span>
            <a href="www.baidu.com"></a>
        </body>
    </html>
'''
bs = BeautifulSoup(html, 'lxml')
print('find:',bs.find('h1',class_='info')) # 获取第一个class属性值包括info的h1标签
print('find all:',bs.find_all('h1',class_='info')) # 获取所有class属性值包括info的h1标签
print('find_all:',bs.find_all('h1',attrs={'float':'left'})) # 获取所有float属性值包括left的h1标签

# CSS选择器
print('CSS选择器:',bs.select("#gb")) # "#"在CSS中对应id
print('CSS选择器:',bs.select(".info")) # "."在CSS中对应class
print('CSS选择器:',bs.select('h1[class="info"]')) # 获取第一个class属性值包括info的h1标签
print('CSS选择器:',bs.select('body>h1')) # 获取body标签下h1标签的内容
print('CSS选择器:',bs.select('body>h1.bg')) # 获取body标签下含属性值bg的h1标签的内容
print('CSS选择器:',bs.select('body>h1#gb')) # 获取body标签下含ID值gb的h1标签的内容

# BeautifulSoup爬取淘宝网
from bs4 import BeautifulSoup
import requests
url = 'https://www.taobao.com/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'}

#发送请求
resp = requests.get(url,headers)
print(resp.text)
bs = BeautifulSoup(resp.text,'lxml')
a_list = bs.find_all('a')

for a in a_list:
    url = a.get('href')
    if url==None:
        continue
    if url.startswith('http') or url.startswith('https'):
        #完整网址
        print(url)

# 正则表达式基本使用
import re
s = 'I study Python3.6.4 every day.'

# match方法
print(re.match('I',s).group()) # 匹配字母I
print(re.match('\w',s).group()) # 匹配任意数字,字母,下划线
print(re.match('.\D',s).group()) # "."匹配任意字符,"\D"匹配所有非十进制数的字符

# search方法
print(re.search('study',s).group()) # 在字符串s中寻找study
print(re.search('s\w',s).group()) 

# findall方法
print(re.findall('Py\w+.\d',s)) # Py开头,紧接着多个字母/数字/下划线,然后任意字符,最后数字结尾

# sub方法
print(re.sub('study','learn',s)) #替换

# 下载视频
import requests,re
url = 'https://www.qiushibaike.com' #链接已失效
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47'}
#发送请求
resp = requests.get(url,headers=headers)
resp.encoding = 'utf-8'
print(resp.text)
# 在网页中找到视频链接地址,跟获取的text对比,若存在于html的text中则正确,然后用正则
info = re.findall('<source src="(.*)> type=\'video/mp4\' />', resp.text) # 多个视频
lst = []
for item in info:
    lst.append('https:'+item)

count = 0
for item in lst:
    count = count + 1
    resp = requests.get(item,headers=headers)
    with open('video/'+str(count)+'.mp4','wb') as f:
        f.write(resp.content)
print('下载完毕')

# CJK爬取快手疫情短视频
url = 'https://v2.kwaicdn.com/upic/2022/05/05/09/BMjAyMjA1MDUwOTExNDRfMTc3MzUzMzM5NV83MzY4NDQxMjg0MF8wXzM=_b_B30a6ced7ffa463f67b8f8f71780819ed.mp4?pkey=AAURhNMPPLAX8Nlz3DMkYIQsHgOphrGT4VW9Q7SPCfBECRlqhjxLL4BV5qR-t6eFU4KhrCKOVm_8hGoXuTA0A1n2Ri-MZ2AZAhe3XyTxeV0akp9797OX34IpD4STUuh5BCg&amp;tag=1-1652606808-unknown-0-1buzqvzool-2ab5e50737b72e9c&amp;clientCacheKey=3xx873f3949nntw_b.mp4'
resp = requests.get(url,headers=headers)
with open('1.mp4','wb') as f:
    f.write(resp.content)
print('下载完毕')

# pyquery初始化方式1:字符串
from pyquery import PyQuery as py_query
html = '''
    <html>
        <head>
            <title>这是标题</title>
        </head>
        <body>
            <h1 class="这是属性 info bg" float="left" id="gb">hello!</h1>
            <h1 class="info">world!</h1>
            <span>好好学习</span>
            <a href="www.baidu.com"></a>
        </body>
    </html>
'''
doc = py_query(html) # 创建pyquery对象
# doc = py_query(fielname='XXX.html') # pyquery初始化方式2: 本地HTML文件
print(doc('title'))

# pyquery初始化方式3: URL
doc = py_query(url='https://www.baidu.com', encoding='utf-8')
print(doc('title'))

# pyquery方法
from pyquery import PyQuery as py_query
html = '''
    <html>
        <head>
            <title>这是标题</title>
        </head>
        <body>
            <div id="main">
                <a href="http://www.baidu.com">百度一下</a>
            </div>
            <h1>world!</h1>
        </body>
    </html>
'''

doc = py_query(html) # 创建pyquery对象
# 获取当前节点:
print('当前节点:',doc('#main')) # id="main"
# 获取父节点:
print('父节点:',doc('#main').parent())
# 获取子节点:
print('子节点:',doc('#main').children())
# 获取兄弟节点:
print('兄弟节点:',doc('#main').siblings())
# 获取属性
print('a标签属性:',doc('a').attr('href'))
# 获取标签的内容
print('标签的内容-HTML:',doc('#main').html())
print('标签的内容-TEXT:',doc('#main').text())

# pyquery爬取起点中文网
from pyquery import PyQuery as py_query
import requests

url = 'https://www.qidian.com/rank/yuepiao' #链接已失效
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.47'}
# 发送请求
resp = requests.get(url,headers=headers)
resp.encoding = 'utf-8'
# print(resp.text)
doc = py_query(resp.text) # 创建返回的HTML的pyquery对象

novel_list = doc('h2 a')
#print(a_tag)
novels = [a.text for a in novel_list] # 作品列表
print(novels)

author_list = doc('p.author a') # 只要class="author"的p标签
authors_tmp = [a.text for a in author_list] # 作者列表+类型
authors = []
for i in range(len(authors_tmp)):
    if(i%3==0): #去除类型,只保留作者
        authors.append(authors_tmp[i])
print(authors)
"""
