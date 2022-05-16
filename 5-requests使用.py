import requests
'''
# 不带参数的get请求
url = "https://www.baidu.com"
resp = requests.get(url)#设置响应的经编码格式
resp.encoding = 'utf-8'
print('响应状态码:', resp.status_code)
print('请求后的cookie:', resp.cookies)
print('获取请求的网址:', resp.url)
print('响应头:', resp.headers)
print('响应内容:', resp.text)

# 带参数的get请求
url = 'https://www.so.com/s' # 请求网址是问号之前的字符串
params = {'q':'python'} # 观察搜索网址可知,对于360搜索,搜索内容名字为q,对于百度则为oq 
resp = requests.get(url,params=params)
resp.encoding = 'utf-8'
print('响应内容:\n', resp.text)


# 获取JSON数据
# 找到ajax请求: F12->Network->XHR即可查看Ajax数据,把其中的url地址放在浏览器地址栏中,可以看到ajax的json数据(可以登录json解析网站进行格式化)
url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&logid=6489607287013406757&ipn=rj&ct=201326592&is=&fp=result&fr=&word=java&queryWord=java&cl=2&lm=-1&ie=utf-8&oe=utf-8&adpicid=&st=&z=&ic=&hd=&latest=&copyright=&s=&se=&tab=&width=&height=&face=&istype=&qc=&nc=1&expermode=&nojc=&isAsync=&pn=120&rn=30&gsm=78&1652580999634='
#同时在Network中也可以看到请求方式为GET
resp = requests.get(url)
json_data = resp.json()
print(json_data)

#post登录
url = 'https://www.xslou.com/login.php'
data = {'username':"123456",'password':'123456','action':'login'}
resp = requests.post(url,data=data)
resp.encoding = 'gb2312'
print('响应状态码:', resp.status_code)
print('响应内容:', resp.text) #显示登录成功 

# session登录
url = 'https://www.xslou.com/login.php'
data = {'username':"123456",'password':'123456','action':'login'}
session = requests.session()
resp = session.post(url,data=data)
resp.encoding = 'gb2312'
print('响应内容:', resp.text) #显示登录成功 
# 收藏小说
collection_url = 'https://www.xslou.com/modules/article/uservote.php?id=71960'
resp2 = session.get(collection_url)
resp2.encoding = 'gb2312'
print(resp2.text) #显示收藏成功
'''