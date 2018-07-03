# wallpaper-for-mac
mac，从so.com获取图片并设置成壁纸

## 配置
```Python
# 这些参数可以去so.com查看，如 http://image.so.com/z?ch=wallpaper&t1=93&listtype=hot&width=1440&height=900
width = 1440
height = 900
ch = 'wallpaper'
t1 = '93'

# 默认收藏在 用户家目录的 wallpaper 
like_dir = os.path.expanduser('~') + '/wallpaper'   
################################################################################
```

## 使用
```
python wallpaper.py # 随机一张图片
python wallpaper.py -l like # 把当前图片复制到 like_dir
```

## 快捷键
1. 找到mac自带的软件 "Automater" 也叫 "自动操作"  
2. 选择创建"服务"  
3. 创建shell脚本，然后保存。 我这里分两次，创建了changeWallpaper、likeWallpaper。    
![changeWallpaper](https://github.com/lepoch/wallpaper-for-mac/raw/master/img/1.png)
4. 设置快捷键： 系统偏好设置 -> 键盘 -> 快捷键   
![hotKeys](https://github.com/lepoch/wallpaper-for-mac/raw/master/img/2.png)


## 参考
[https://github.com/KailinLi/Bing-WallPaper-for-Mac](https://github.com/KailinLi/Bing-WallPaper-for-Mac)
