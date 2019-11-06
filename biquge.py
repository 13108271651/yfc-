import requests
from lxml import etree
import random

headers=['Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'"Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",

        "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",

        "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",

        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",

        "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",

        "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",

        "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0",

        "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5"]

def jiexi(url):

    html = requests.get(url, headers={'User-Agent':random.choice(headers)})
    html.encoding = ('utf-8')
    html = html.text
    html = etree.HTML(html)
    url_next=html.xpath('//*[@id="wrapper"]/div[4]/div/div[2]/div[1]/a[4]/@href')
    url_next=url_next[0]
    return url_next


def huoqu(url):

    try:
        html = requests.get(url, headers={'User-Agent':random.choice(headers)})
        html.encoding = ('utf-8')
        html = html.text
        html = etree.HTML(html, etree.HTMLParser())
        txt = html.xpath('//*[@id="content"]/text()')
        title=html.xpath('//*[@id="wrapper"]/div[4]/div/div[2]/h1/text()')
        title=str(title[0])
        txt_zong = '--------'*10+'\n'+title+'\n\n'
        for i in range(len(txt)):
            txt_zong = txt_zong + txt[i] + '\n'
        txt_zong='\n\n\n'+txt_zong
        return txt_zong
    except:
        print('进行到某章网页链接错误或已经到最后一章')
        txt_zong=['不要滥用']
        return txt_zong

def main():
    url=input('请输入小说的起始网页')
    name=input('请输入你要获取的小说名或者文件保存名，不带文件格式后缀')
    name=name+'.txt'
    number=int(input('请输入你要抓取的章数,注意是一个整数.输入负数或0即代表抓取至最新章节'))
    if number>0:
        for i in range(number):
            with open(name,'a+',encoding="utf-8") as w:
                w.write(huoqu(url))
                print(f'写入从起始章开始第{i}章')
            url=jiexi(url)

        print('已经抓取到最新章节')
        input()
    else:
        x=1
        while 1:
            txt=huoqu(url)
            if len(txt)>50:
                with open(name, 'a+',encoding="utf-8") as w:
                    w.write(txt+'\n\n\n\n\n')
                    print(f'写入从起始章开始第{x}章')
                url = jiexi(url)
                x+=1
            else:
                print('已经抓取到最新章节')
                break
    input()
main()
