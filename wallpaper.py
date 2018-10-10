#!/usr/bin/python
# -*-coding:utf-8 -*-

from optparse import OptionParser
import os
import urllib2
import random
import json
import shutil
import re

############################ 配置区域 #########################################

config_width = 1440
config_height = 900
config_word = '壁纸 美女 模特'

config_like_dir = os.path.expanduser('~') + '/wallpaper'
################################################################################

# help
parser = OptionParser()
parser.add_option("-l", "--like", dest="like", default=False,
                  help="save the current image to " + config_like_dir)

(options, args) = parser.parse_args()


def get_so_wallpaper(i_word, i_width, i_height):
    i_img_url = ''
    i_file_name = ''

    repeat = 3
    while repeat > 0:
        try:
            url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&cl=&lm' \
                  '=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&s=&se=&tab=&face=0&istype=2&qc=&nc=&fr=&expermode' \
                  '=&itg=1&gsm=96'

            page_size = 30
            start = random.randint(0, 20) * page_size

            url += 'queryWord=%s&' % urllib2.quote(i_word)
            url += 'word=%s&' % urllib2.quote(i_word)
            url += 'width=%s&' % i_width
            url += 'height=%s&' % i_height
            url += 'pn=%s&' % start
            url += 'rn=%s&' % page_size

            response = urllib2.urlopen(url)
            res = response.read()
            res = json.loads(res)

            if 'data' in res:
                items = res['data']
                if len(items) > 0:
                    r = random.randint(0, len(items) - 1)
                    item = items[r]

                    # 从详情页获取大图url
                    url = 'https://image.baidu.com/search/detail?tn=baiduimagedetail&ipn=d&'
                    url += 'word=%s&' % urllib2.quote(i_word)
                    url += 'width=%s&' % i_width
                    url += 'height=%s&' % i_height
                    url += 'os=%s&' % item['os']

                    response = urllib2.urlopen(url)
                    res = response.read()
                    res = re.search('hdFirstImgObj.*?src="(.*?)" ', res)
                    if res is not None:
                        i_img_url = res.group(1)
                        # 去掉特殊参数
                        i_img_url = re.sub('&quality=\d+?&', '&', i_img_url)

                        i_file_name = item['os'] + '.' + item['type']
                        break

        except Exception as e:
            print e
            repeat -= 1
            pass

    return i_img_url, i_file_name


def save_img(i_img_url, i_file_name, file_path):
    # noinspection PyBroadException
    try:
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
            'Cookie': 'AspxAutoDetectCookieSupport=1',
        }
        request = urllib2.Request(i_img_url, None, header)
        response = urllib2.urlopen(request)
        f = open(file_path + '/' + i_file_name, 'wb')
        f.write(response.read())
        f.close()

    except Exception as e:
        pass


def save_paper_file(i_img_url, i_file_name, i_tmp_dir):
    if os.path.exists(i_tmp_dir):
        shutil.rmtree(i_tmp_dir)

    os.makedirs(i_tmp_dir)

    save_img(i_img_url, i_file_name, i_tmp_dir)


def set_paper(picture):
    os.popen('osascript -e \'tell application "Finder" to set desktop picture to POSIX file "' + picture + '"\'')


def like_cur_paper(i_tmp_dir, i_like_dir):
    if not os.path.exists(i_like_dir):
        os.makedirs(i_like_dir)

    for f_path, dirs, fs in os.walk(i_tmp_dir):
        for f in fs:
            i_file_name = os.path.join(f_path, f)
            shutil.copy(i_file_name, i_like_dir)


# var
tmp_dir = '/tmp/wallpaper/'

if options.like:
    like_cur_paper(tmp_dir, config_like_dir)
    pass
else:
    img_url, file_name = get_so_wallpaper(config_word, config_width, config_height)
    if img_url and file_name:
        save_paper_file(img_url, file_name, tmp_dir)
        set_paper(tmp_dir + '' + file_name)
