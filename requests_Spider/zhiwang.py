import requests
from lxml import etree


# 搜索词条
word = str(input("请输入需要搜索的词条："))
begin_page = int(input("请输入需要爬取的开始页码："))
end_page = int(input("请输入需要爬取的结束页码："))

# 代理ip
proxies = {
  "http": "http://118.190.95.35:9001",
}

# 查找每一页
for p in range(begin_page, end_page+1):
    print("当前页面是第", p, "页")
    url = 'https://search.ehn3.com/search?'
    key = {"keyword":word, "p": p}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
    response = requests.get(url, proxies = proxies, params=key, headers=headers)
    html = response.content.decode()
    # 数据提取,获得每一页的html
    _html = etree.HTML(html)
    # 获得每一个div块
    results = _html.xpath('//div[@class="mdui-row mdui-typo"]')
    for result in results:
        # 论文标题 + 详情链接
        title = result.xpath('.//h3//text()')
        title = "".join(title).strip()
        print("标题：", title)
        detail_url = result.xpath('.//a/@href')[0].strip()
        detail_url = "https://search.ehn3.com" + detail_url
        print("详情链接：", detail_url)
        # 作者
        author = result.xpath('.//div[@class="mdui-col-xs-12"]//span[1]/text()')
        if len(author)>0:
            author = author[0].replace("，", "").strip()
        else:
            author = "匿名"
        print("作者：", author)
        # 论文来源
        article_source = result.xpath('.//div[@class="mdui-col-xs-12"]//span[3]/text()')[0]
        print("论文来源：", article_source)
        # 发表日期
        pub_date = result.xpath('.//div[@class="mdui-col-xs-12"]//span[4]/text()')[0]
        pub_date = pub_date.replace("，", "").strip()
        print("发表日期：", pub_date)
        # 论文摘要
        summary = result.xpath('.//div[@class="mdui-col-xs-12 mdui-typo"]/p/text()')
        summary = "".join(summary).strip()
        print("论文摘要：", summary)
        print("="*80)

        # 数据存储
        with open("./data/"+word+"-"+str(begin_page)+"-"+str(end_page)+".txt", "a") as f:
            f.write(
            word+"--"+"当前页面是第"+str(p)+"页"+"\n"+
            "标题："+title+"\n"+
            "详情链接："+detail_url+"\n"+
            "作者："+ author+"\n"+
            "论文来源："+ article_source+"\n"+
            "发表日期："+ pub_date+"\n"+
            "论文摘要："+summary+"\n"+
            "-"*80+"\n"
            )
