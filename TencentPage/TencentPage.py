from urllib import request
import chardet
import os
import zlib

url = "http://www.qq.com/"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"}

# 定义代理ip
proxy = {'http': '101.65.24.16:8118'}
# 1、定义代理处理器对象
proxy_handler = request.ProxyHandler(proxy)
# 2、创建opener对象
opener = request.build_opener(proxy_handler)
# 使用UserAgent
opener.addheaders = [('User-Agent',
                      'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36')]
# 3、安装opener
request.install_opener(opener)

# req = request.Request(url, headers=headers)
response = request.urlopen(url)

html = response.read()

# 页面解压缩
encoding = response.info().get('Content-Encoding')
print(encoding)
if encoding == 'gzip':
    html = zlib.decompress(html, 16 + zlib.MAX_WBITS)
elif encoding == 'deflate':
    try:
        html = zlib.decompress(html, -zlib.MAX_WBITS)
    except zlib.error:
        html = zlib.decompress(html)


charset = chardet.detect(html)['encoding']
# print(charset)
# 转存至文件
HtmlPage = html.decode(charset, "ignore")
if not os.path.exists("tencentpage1.html"):
    with open("tencentpage1.html", "w+", encoding="gb2312") as f_w:
        f_w.write(HtmlPage)
        f_w.close()
print(HtmlPage)
