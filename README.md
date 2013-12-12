popo-plugin
===========

Python实现的网易泡泡外挂，用于通知虚拟机外的Linux



## 使用方法

1.在linux下运行 python notifier.py。

2.在windows下安装python2.7，地址是http://www.python.org/ftp/python/2.7.5/python-2.7.5.msi。

3.安装Dependency目录下的AutoHotKey.exe。或者去官网下载最新的。

4.修改win-notify.py文件，将LINUX_HOST后的ip地址改为你本机linux的ip地址。

5.修改AutoHotKey.ahk里面的win-notify.py的路径，以及在team_white_list中添加您需要的组白名单。

6.将AutoHotKey.ahk载入到AutoHotKey中，让AutoHotKey开机自动运行。


## Tips
Linux下的依赖项: libnotify, python-gobject


## Change Log

### 2013-12-13
加上了静默时间，在制定时间内，提醒过的消息不再提醒。一是可以避免消息疯狂弹出，另外可以减少自己被打扰的频率。

### 2013-08-04
配合AutoHotKey使用，抛弃了以前的大部分方案。Windows部分主要由AutoHotKey处理。
