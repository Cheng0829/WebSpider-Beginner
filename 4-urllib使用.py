
import urllib.parse,urllib.request
from urllib.request import build_opener,ProxyHandler
from http import cookiejar
import urllib.request,urllib.error
'''
# urllib.parse(用于解析URL,将输入的地址栏URL中的中文转换为%x%x%x)
kw={'wd':'汤姆'}
result_encode = urllib.parse.urlencode(kw)
print(result_encode)
result_decode = urllib.parse.unquote(result_encode)
print(result_decode)

# urllib.request用于打开和读取URL,模拟浏览器发起一个HTTP请求,并获取请求响应的结果
# data为空,用Get请求
url = 'https://www.cnblogs.com/'
result = urllib.request.urlopen(url,timeout=3,) # urlopen打开请求
result_read = result.read().decode('utf-8') #read对返回结果进行读取,decode把bytes类型转成str类型
# print(result_read)

# data非空,用Post请求
data={'username':'111','password':'222','action':'login'}
resp = urllib.request.urlopen(url,data=bytes(urllib.parse.urlencode(data),encoding='utf-8'))
html = resp.read().decode('utf-8')
#print(html)

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36 Edg/101.0.1210.39'}
#构建请求对象:
req = urllib.request.Request(url,headers)
#使用urlopen打开请求
resp = urllib.request.urlopen(req)
html =resp.read().decode('utf-8')
print(resp)

# IP代理

#ProxyHandler({协议:IP地址:端口})
proxy = ProxyHandler({'http':'120.42.46.226:6666'})
opener = build_opener(proxy)
url = 'https://www.cnblogs.com/'
result = opener.open(url,timeout=3,) # urlopen打开请求
result_read = result.read().decode('utf-8') # read对返回结果进行读取
print(result_read)


#cookie
def get_cookie(filename):
    #(1)实例化一个MozillaCookieJar(用于保存cookie)
    cookie = cookiejar.MozillaCookieJar(filename)
    #(2)创建handler对象
    handler = urllib.request.HTTPCookieProcessor(cookie)
    #(3)创建opener对象
    opener = urllib.request.build_opener(handler)
    #(4)请求网址
    url = 'https://www.baidu.com/'
    resp = opener.open(url)
    cookie.save(filename)

def use_cookie(filename):
    #(1)实例化一个MozillaCookieJar（用于保存cookie)
    cookie = cookiejar.MozillaCookieJar(filename)
    #(2)加载cookie.txt文件
    cookie.load(filename)
    print(cookie)

filename = 'D:/爬虫/cookie.txt'
get_cookie(filename)
use_cookie(filename)


url = 'https://movie.douban.com/'
#请求
try: 
    resp = urllib.request.urlopen(url, timeout=3)
except urllib.error.URLError as e:
    print('原因:',e.reason)
try: 
    resp = urllib.request.urlopen(url, timeout=3)
except urllib.error.HTTPError as e:
    print('原因:',e.reason)
    print("响应状态码:",e.code)
    print("响应头数据:",e.headers)
'''