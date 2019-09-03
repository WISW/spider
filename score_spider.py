from bs4 import BeautifulSoup
import requests

url ="http://search.gradschool.ustc.edu.cn/download/yzbgs/2019tkssgs.htm"

data =requests.get(url)
data.encoding="gbk"
# print(data.text)


# # with open("temp.html","wb") as file:
# #     file.write(data)
# data =str(data)
soup =BeautifulSoup(data.text,"html.parser")
for i in soup.find_all("p"):
    print(str(i.text))

# results =soup.findAll()
# print(results)
# print(results)