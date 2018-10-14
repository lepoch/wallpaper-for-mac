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


# 1搜狗tag， 2搜狗搜索， 3百度搜索
config_source = 2

# 1搜狗tag
config_sogou_tag = '美女'

# 2搜狗搜索
config_sogou_word = '诱惑'

# 3百度搜索
config_baidu_word = '性感'


# 保存目录
config_like_dir = os.path.expanduser('~') + '/wallpaper'
################################################################################

# help
parser = OptionParser()
parser.add_option("-l", "--like", dest="like", default=False,
                  help="save the current image to " + config_like_dir)

(options, args) = parser.parse_args()

header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.114 Safari/537.36',
    'Cookie': 'AspxAutoDetectCookieSupport=1',
}


def get_sogou_wallpaper_by_tag(category, tag, width, height):
    inner_img_url = ''
    inner_file_name = ''

    if isinstance(tag, list):
        tag = tag[random.randint(0, len(tag) - 1)]

    limit = 0
    page_size = 15
    repeat = 10
    while repeat > 0:
        repeat -= 1
        # noinspection PyBroadException
        try:
            url = 'https://pic.sogou.com/pics/channel/getAllRecomPicByTag.jsp?'

            if limit > 0:
                start = random.randint(0, limit)
            else:
                start = 0

            url += 'category=%s&' % urllib2.quote(category)
            url += 'tag=%s&' % urllib2.quote(tag)
            url += 'start=%s&' % start
            url += 'len=%s&' % page_size
            url += 'width=%s&' % width
            url += 'height=%s&' % height

            request = urllib2.Request(url, None, header)
            response = urllib2.urlopen(request)
            res = response.read()
            res = res.decode('gbk').encode('utf8')
            res = json.loads(res)

            if limit == 0:
                limit = res['maxEnd']
                if limit == 0:
                    break
                continue

            if 'all_items' in res:
                items = res['all_items']
                if len(items) > 0:
                    r = random.randint(0, len(items) - 1)
                    item = items[r]
                    inner_img_url = item['pic_url']
                    inner_file_name = bytes(item['id']) + '.jpg'
                    break

        except Exception as e:
            print e
            pass

    return inner_img_url, inner_file_name


def get_sogou_wallpaper(word, width, height):
    inner_img_url = ''
    inner_file_name = ''

    limit = 0
    page_size = 15
    repeat = 10
    while repeat > 0:
        repeat -= 1
        # noinspection PyBroadException
        try:
            url = 'https://pic.sogou.com/pics?&mode=1&dm=4&leftp=44230501&st=0&reqType=ajax&reqFrom=result&tn=0&'

            if limit > 0:
                start = random.randint(0, limit)
            else:
                start = 0

            url += 'query=%s&' % urllib2.quote(word)
            url += 'start=%s&' % start
            url += 'len=%s&' % page_size
            url += 'cwidth=%s&' % width
            url += 'cheight=%s&' % height

            request = urllib2.Request(url, None, header)
            response = urllib2.urlopen(request)
            res = response.read()
            res = res.decode('gbk', errors="ignore").encode('utf8')
            res = json.loads(res)

            if limit == 0:
                limit = res['maxEnd']
                if limit == 0:
                    break
                continue

            if 'items' in res:
                items = res['items']
                if len(items) > 0:
                    r = random.randint(0, len(items) - 1)
                    item = items[r]
                    inner_img_url = item['pic_url']

                    print inner_img_url

                    if not img_exists(inner_img_url):
                        inner_img_url = ''
                        continue

                    inner_file_name = bytes(item['mf_id']) + '.jpg'
                    break

        except Exception as e:
            print e
            pass

    return inner_img_url, inner_file_name


def get_baidu_wallpaper(i_word, i_width, i_height):
    i_img_url = ''
    i_file_name = ''

    page_size = 30
    limit = 0

    repeat = 5

    while repeat > 0:
        repeat -= 1
        # noinspection PyBroadException
        try:
            url = 'https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&ct=201326592&is=&fp=result&cl=&lm' \
                  '=-1&ie=utf-8&oe=utf-8&adpicid=&st=-1&z=&ic=0&s=&se=&tab=&face=0&istype=2&qc=&nc=&fr=&expermode' \
                  '=&itg=1&gsm=96'

            if limit > 0:
                start = random.randint(0, limit)
            else:
                start = 0

            url += 'queryWord=%s&' % urllib2.quote(i_word)
            url += 'word=%s&' % urllib2.quote(i_word)
            url += 'width=%s&' % i_width
            url += 'height=%s&' % i_height
            url += 'pn=%s&' % start
            url += 'rn=%s&' % page_size

            response = urllib2.urlopen(url)
            res = response.read()
            res = unicode(res, errors='ignore')
            res = json.loads(res)

            if limit == 0:
                limit = res['listNum']
                if limit == 0:
                    break
                continue

            if 'data' in res:
                items = res['data']
                if len(items) > 0:
                    r = random.randint(0, len(items) - 1)
                    item = items[r]
                    if len(item) == 0:
                        continue

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

                        if not img_exists(i_img_url):
                            i_img_url = ''
                            continue

                        i_file_name = item['os'] + '.' + item['type']
                        break

        except Exception as e:
            print e
            pass

    return i_img_url, i_file_name


def img_exists(i_img_url):
    try:
        # header 判断
        request = urllib2.Request(i_img_url, None, header)
        urllib2.urlopen(request)
        return True
    except urllib2.HTTPError, e:
        print e
        return False


def save_img(i_img_url, i_file_name, file_path):
    # noinspection PyBroadException
    try:
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
    os.system('osascript -e \'tell application "Finder" to set desktop picture to POSIX file "' + picture + '"\'')


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
    img_url, file_name = '', ''
    try:
        if config_source == 1:
            img_url, file_name = get_sogou_wallpaper_by_tag("壁纸", config_sogou_tag, config_width, config_height)
        elif config_source == 3:
            img_url, file_name = get_baidu_wallpaper(config_baidu_word, config_width, config_height)
        else:
            img_url, file_name = get_sogou_wallpaper(config_sogou_word, config_width, config_height)

        if img_url and file_name:
            save_paper_file(img_url, file_name, tmp_dir)
            set_paper(tmp_dir + '' + file_name)

    except Exception as e:
        print 'err', e, img_url, file_name
