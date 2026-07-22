'''
包管理工具pip
Python 标准库中的json模块在数据序列化和反序列化时性能并不是非常理想，
为了解决这个问题，可以使用三方库ujson来替换json
'''
# import requests


# response = requests.get("https://www.baidu.com")

# print(response)

# import requests


# url = "https://jsonplaceholder.typicode.com/posts"

# response = requests.get(url)


# print(response.status_code)

# data = response.json()

# print(data[:3])

import requests

url="https://apis.tianapi.com/guonei/index"

API_KEY="e04f25e568c2cfc65df4630ae4240ec5"

params={
    "key":API_KEY,
    "num":10
}

response=requests.get(url,params=params)

#print(response.url)
if response.status_code == 200:
    data_model = response.json()
    for news in data_model['result']['newslist']:
        print(news['title'])
        print(news['url'])
        print('-' * 60)

# data=response.json()

# print(data)