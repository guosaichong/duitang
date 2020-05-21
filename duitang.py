import requests
import jsonpath
import os
import urllib.parse

def get_img(word,path):
    kw=urllib.parse.quote(word)
    num=1
    for i in range(0,25,24):
        url="https://www.duitang.com/napi/blog/list/by_search/?kw={}&type=feed&start={}".format(kw,i)
        headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3947.100 Safari/537.36",
        }
        response=requests.get(url,headers=headers)
        # print(response.json())
        img_urls=jsonpath.jsonpath(response.json(),"$..path")
        for img_url in img_urls:
            resp=requests.get(img_url,headers=headers)
            content=resp.content
            with open(path+"\\"+"{}".format(num)+"."+img_url.split(".")[-1],"wb")as f:
                f.write(content)
                print("正在保存第{}张".format(num))
            num+=1
if __name__=="__main__":
    word='汽车'
    if not os.path.isdir("E:\\"+word):
        os.mkdir("E:\\"+word)
    path="E:\\"+word
    get_img(word=word,path=path)