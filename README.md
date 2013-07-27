popo-plugin
===========

Python实现的网易泡泡外挂，用于通知虚拟机外的Linux

# 更新
配合AutoHotKey使用，抛弃了以前的大部分方案。Windows部分主要由AutoHotKey处理。



## 使用方法

1.在linux下运行 python notifier.py。

2.在windows下安装python2.7，地址是http://www.python.org/ftp/python/2.7.5/python-2.7.5.msi。

3.安装Dependency目录下的AutoHotKey.exe。

4.修改win-notify.py文件，将LINUX_HOST后的ip地址改为你本机linux的ip地址。

5.修改AutoHotKey.ahk里面的win-notify.py的路径。

6.将AutoHotKey.ahk载入到AutoHotKey中，让AutoHotKey开机自动运行。


## Tips
Linux下的依赖项: libnotify, python-gobject
