# wallpaper-for-mac
mac，获取图片并设置成壁纸

## 配置
```Python
config_width = 1440
config_height = 900

config_sogou_tag = '美女'


config_source = "sogou"
config_baidu_word = '壁纸 性感'

config_like_dir = os.path.expanduser('~') + '/wallpaper'
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


## 问题
### 没效果
1. 取消 桌面与屏幕保护程序 -> 更改图片
2. 用浏览器打开 http://image.so.com/z?ch=wallpaper


## 参考
[https://github.com/KailinLi/Bing-WallPaper-for-Mac](https://github.com/KailinLi/Bing-WallPaper-for-Mac)



https://image.baidu.com/search/detail?tn=baiduimagedetail&ipn=d&word=%E5%A3%81%E7%BA%B8%20%E4%B8%8D%E5%90%8C%E9%A3%8E%E6%A0%BC%20%E5%8F%AF%E7%88%B1&os=3139768851,2123875696&width=1440&height=900

https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E5%A3%81%E7%BA%B8%20%E4%B8%8D%E5%90%8C%E9%A3%8E%E6%A0%BC%20%E5%8F%AF%E7%88%B1&step_word=&hs=0&pn=1&spn=0&di=104635664540&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=&lm=-1&st=-1&cs=239729543%2C2730030954&os=3139768851%2C2123875696&simid=3231448673%2C140033455&adpicid=0&lpn=0&ln=1110&fr=&fmq=1526269427171_R&fm=&ic=0&s=undefined&se=&sme=&tab=0&width=1440&height=900&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fimg.pconline.com.cn%2Fimages%2Fupload%2Fupc%2Ftx%2Fwallpaper%2F1301%2F22%2Fc1%2F17619771_1358836511629.jpg&fromurl=ippr_z2C%24qAzdH3FAzdH3Ftpkkf_z%26e3Brv5gstgj_z%26e3Bv54_z%26e3BvgAzdH3Fcamlamld_z%26e3Bip4s&gsm=78&rpstart=0&rpnum=0&islist=&querylist=

https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=%E5%A3%81%E7%BA%B8%20%E4%B8%8D%E5%90%8C%E9%A3%8E%E6%A0%BC%20%E5%8F%AF%E7%88%B1&step_word=&hs=0&pn=42&spn=0&di=176168206721&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&istype=2&ie=utf-8&oe=utf-8&in=&cl=&lm=-1&st=-1&cs=1019347495%2C2051026871&os=2196539922%2C3097340835&simid=0%2C0&adpicid=0&lpn=0&ln=1110&fr=&fmq=1526269427171_R&fm=&ic=0&s=undefined&se=&sme=&tab=0&width=1440&height=900&face=undefined&ist=&jit=&cg=&bdtype=0&oriquery=&objurl=http%3A%2F%2Fdik.img.lgdsy.com%2Fpic%2F18%2F12371%2F5dda6a833987ca21_1440x900.png&fromurl=ippr_z2C%24qAzdH3FAzdH3Fooo_z%26e3B157thwg_z%26e3Bv54AzdH3FfpysjAzdH3Fs545AzdH3F8dn08_z%26e3Bip4s&gsm=1e&rpstart=0&rpnum=0&islist=&querylist=