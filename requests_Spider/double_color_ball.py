import requests
from lxml import etree


headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36"}
response = requests.get("http://zst.aicai.com/ssq/openInfo/", headers=headers)
html = response.content.decode()
# print(results)
# print(type(results))

results = etree.HTML(html).xpath('//form[@name="form1"]')[0]

_results = results.xpath('.//table//tr[position()>2]')

for result in _results:
    # 期号
    date = result.xpath('.//td[1]/text()')[0].strip()
    print("期号", date)
    # 开奖日期
    lottery_date = result.xpath('.//td[2]/text()')[0].strip()
    print("开奖日期", lottery_date)
    # 红色球
    red_balls = result.xpath('.//td[position()>2 and position()<9]/text()')
    # 红色球计数
    rednums = 1
    strA = ""
    for red_ball in red_balls:
        # print("红色球", rednums, red_ball)
        strA+=(str(rednums)+"号："+str(red_ball) + "/")
        rednums +=1
    # 蓝色球
    blue_ball = result.xpath('.//td[9]/text()')[0].strip()
    print("蓝色球", blue_ball)
    # 一等奖
        # 一等奖注数
    First_prize_nums =result.xpath('.//td[11]/text()')[0].strip()
        # 一等奖奖金
    First_prize_money =result.xpath('.//td[12]/text()')[0].strip()
    print("一等奖注数：",First_prize_nums, "一等奖奖金：", First_prize_money)
    # 二等奖
        # 二等奖注数
    Second_prize_nums = result.xpath('.//td[13]/text()')[0].strip()
        # 二等奖奖金
    Second_prize_money = result.xpath('.//td[14]/text()')[0].strip()
    print("二等奖注数：", First_prize_nums, "二等奖奖金：", First_prize_money)
    print("-"*81)

    # 数据存储
    with open("./data/双色球.txt", "a", encoding="utf-8") as f:
        f.write("期号：" + date + "--开奖日期：" + lottery_date + "--红色球" + strA + "--蓝色球：" + blue_ball +
                "--一等奖：注数：" + First_prize_nums + "--奖金：" + First_prize_money + "--二等奖：注数："+ Second_prize_nums + "--奖金：" + Second_prize_money +"\n" + "\n")

