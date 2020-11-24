# -*- coding:utf-8 -*-
# Author: Syaoran@SC33.TOP


import requests
from lxml import etree
import os

requests.urllib3.disable_warnings()


# 获取最新一期链接
def get_newest_url():
    url = 'http://news.cyol.com/node_67071.htm'
    response = requests.get(url, verify=False)
    html = etree.HTML(response.text)
    newest_url = html.xpath(
        '/html/body/div[@class="mianbody"]/dl[@class="listMM"]/dd[@class="picB"]/ul[@class="movie-list"]/li[1]/a/@href')[
        0]

    return newest_url


# 获取最新一期标题
def get_title_text():
    url = get_newest_url()
    response = requests.get(url, verify=False)
    response.encoding = 'utf-8'
    html = etree.HTML(response.text)
    title = html.xpath('/html/head/title/text()')[0]

    return title


# 获取完成图片
def get_endPic():
    url = get_newest_url()
    img_url = url.replace('m.html', 'images/end.jpg').replace('index.html', 'images/end.jpg')
    try:
        os.mkdir('images', 777)
    except:
        pass
    with open('images/end.jpg', 'wb') as f:
        img = requests.get(img_url)
        f.write(img.content)
        f.close()


# 生成HTML文件
def html_gener():
    title = get_title_text()

    html = """
    <html>
    <head>
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="viewport" content="initial-scale=1, maximum-scale=1, user-scalable=no, width=device-width">
        <title>{}</title>
    </head>
    <body style="margin: 0;">
        <img style='width: 100%;height: 100%;' src='end.jpg'>
    </body>
    </html>
    """.format(title)

    with open('daxuexi.html', 'w', encoding='utf-8') as f:
        f.write(html);
        f.close()


if __name__ == "__main__":
    print('[*]成功获取新一期：' + get_title_text())
    get_endPic()
    print('[*]成功下载图片')
    html_gener()
    print('[*]成功生成网页')