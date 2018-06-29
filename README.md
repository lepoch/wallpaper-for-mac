# sogou-wallpaper-for-mac
mac，从搜狗获取图片并设置成壁纸

## 配置
```Python
# 这些参数可以取搜狗查看  http://pic.sogou.com/pics/recommend?category=%B1%DA%D6%BD&from=home#%E5%85%A8%E9%83%A8%2610
width = 1440
height = 900
tegory = '壁纸'
tag = '美女'

like_dir = os.path.expanduser('~') + '/wallpaper'
################################################################################
```

## 使用
**用mac自带的terminal.app**
```
python wallpaper.py # 随机一张图片
python wallpaper.py -l like # 把当前图片复制到 like_dir
```

## 快捷键
1、 找到mac自带的软件 "Automater" 也叫 "自动操作"
2、 选择创建"服务"
3、 创建shell脚本，然后保存。 我这里分两次，创建了changeWallpaper、likeWallpaper。  
![changeWallpaper](https://github.com/lepoch/sogou-wallpaper-for-mac/raw/master/img/1.png)
4、 设置快捷键： 系统偏好设置 -> 键盘 -> 快捷键 
![hotKeys](https://github.com/lepoch/sogou-wallpaper-for-mac/raw/master/img/2.png)


## 参考
[https://github.com/KailinLi/Bing-WallPaper-for-Mac](https://github.com/KailinLi/Bing-WallPaper-for-Mac)
