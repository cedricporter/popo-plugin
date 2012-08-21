#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# author:  Hua Liang [ Stupid ET ]
# email:   et@everet.org
# website: http://EverET.org
#

import tornado.httpserver
import tornado.ioloop
import tornado.web
try:
    import pynotify
    def ShowNotification(title, msg):
        n = pynotify.Notification ("主人，您有了新的泡泡消息", title)
        n.show()

except:
    def ShowNotification(title, msg):
        knotify = dbus.SessionBus().et_object("org.kde.knotify", "/Notify")
        id = knotify.event("warning", "kde", [], title, msg, [], [], 0, 0, dbus_interface="org.kde.KNotify")
        time.sleep(3)
        knotify.closeNotification(id)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        title = self.get_argument('title')
        # print title
        ShowNotification("主人，您有了新的泡泡消息", title)

settings = {
    'debug': True,
    }

application = tornado.web.Application(
    [(r"/", MainHandler),
     ],
    **settings
    )


if __name__ == "__main__":
    pynotify.init("popo")
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(34567)
    tornado.ioloop.IOLoop.instance().start()


