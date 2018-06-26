# sogou-wallpaper-for-mac
mac，从搜狗获取图片并设置成壁纸

## 配置
```Python
# 这些参数可以取搜狗查看  http://pic.sogou.com/pics/recommend?category=%B1%DA%D6%BD&from=home#%E5%85%A8%E9%83%A8%2610
width = 1440
height = 900
tag = '优质'

like_dir = os.path.expanduser('~') + '/wallpaper'
################################################################################
```

## 使用
**用mac自带的terminal.app**
```
python wallpaper.py # 随机一张图片
python wallpaper.py -l like # 把当前图片复制到 like_dir
```

## 参考
[https://github.com/KailinLi/Bing-WallPaper-for-Mac](https://github.com/KailinLi/Bing-WallPaper-for-Mac)
