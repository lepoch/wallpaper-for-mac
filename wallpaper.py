#!/usr/bin/python
# -*-coding:utf-8 -*-

from optparse import OptionParser
import os
import urllib2
import random
import json
import shutil

############################ 配置区域 #########################################

# 这些参数可以取搜狗查看  http://pic.sogou.com/pics/recommend?category=%B1%DA%D6%BD&from=home#%E5%85%A8%E9%83%A8%2610
width = 1440
height = 900
category = '美女'
tag = '诱惑'

like_dir = os.path.expanduser('~') + '/wallpaper'
################################################################################

# help
parser = OptionParser()
parser.add_option("-l", "--like", dest="like", default=False,
                  help="save the current image to " + like_dir)

(options, args) = parser.parse_args()


def get_sogou_wallpaper(category, tag, width, height):
    img_url = ''
    file_name = ''

    repeat = 3
    while repeat > 0:
        url = 'http://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?'

        url += 'category=%s&' % urllib2.quote(category)
        url += 'tag=%s&' % urllib2.quote(tag)
        url += 'start=%s&' % random.randint(0, 100)
        url += 'len=%s&' % random.randint(1, 666)
        url += 'width=%s&' % width
        url += 'height=%s&' % height

        response = urllib2.urlopen(url)
        res = json.load(response, 'gbk')
        if 'all_items' in res:
            l = len(res['all_items'])
            if l >= 0:
                item = res['all_items'][random.randint(0, l - 1)]
                img_url = item['pic_url']
                file_name = bytes(item['id']) + '.jpg'
                break
        repeat -= 1

    return img_url, file_name


def save_img(img_url, file_name, file_path):
    try:
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
            'Cookie': 'AspxAutoDetectCookieSupport=1',
        }
        request = urllib2.Request(img_url, None, header)  # 刻意增加头部header，否则本行与下一行可以写为：response = urllib2.urlopen(imgurl)
        response = urllib2.urlopen(request)
        f = open(file_path + '/' + file_name, 'wb')
        f.write(response.read())
        f.close()

    except Exception as e:
        print(e)


def save_paper_file(img_url, file_name, tmp_dir):
    if os.path.exists(tmp_dir):
        shutil.rmtree(tmp_dir)

    os.makedirs(tmp_dir)

    save_img(img_url, file_name, tmp_dir)


def set_paper(picture):
    print(picture)
    output = os.popen(
        'osascript -e \'tell application "Finder" to set desktop picture to POSIX file "' + picture + '"\'')

    print output.read()


def like_cur_paper(tmp_dir, like_dir):
    if not os.path.exists(like_dir):
        os.makedirs(like_dir)

    for f_path, dirs, fs in os.walk(tmp_dir):
        for f in fs:
            file_name = os.path.join(f_path, f)
            shutil.copy(file_name, like_dir)


# var
tmp_dir = '/tmp/wallpaper/'

if options.like:
    like_cur_paper(tmp_dir, like_dir)
    pass
else:
    img_url, file_name = get_sogou_wallpaper(category, tag, width, height)
    save_paper_file(img_url, file_name, tmp_dir)
    set_paper(tmp_dir + '' + file_name)
