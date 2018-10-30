# http://yunqi.qq.com/bk
from urllib import request
import chardet
import os

# ===================================================

for p in range(1,6):
    url = "http://yunqi.qq.com/bk/so2/n10p"
    # word1 = {"kw": name}
    # word2 = {"ie": "utf-8"}
    # word3 = {"pn": str(p)}
    # word1 = parse.urlencode(word1)
    # word2 = parse.urlencode(word2)
    # word3 = parse.urlencode(word3)
    newUrl = url + str(p)
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}

    # 定义代理ip
    proxy = {'http':'106.14.47.5:80'}
    # 1、定义代理处理器对象
    proxy_handler = request.ProxyHandler(proxy)
    # 2、创建opener对象
    opener = request.build_opener(proxy_handler)
    # 使用UserAgent
    opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')]
    # 3、安装opener
    request.install_opener(opener)


    req = request.Request(newUrl, headers=headers)
    response = request.urlopen(req)
    html = response.read()

    charset = chardet.detect(html)["encoding"]

    # 转存至文件
    HtmlPage = html.decode(charset)
    if not os.path.exists("./data/yunqi_"+str(p)+".txt"):
        with open("./data/yunqi_"+str(p)+".txt","w+",encoding="gb18030") as f_w:
            f_w.write(HtmlPage)
            f_w.close()
    print(HtmlPage)