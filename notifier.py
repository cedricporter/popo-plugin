#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# author:  Hua Liang [ Stupid ET ]
# email:   et@everet.org
# website: http://EverET.org
#

import tornado.httpserver
import tornado.ioloop
import tornado.web 
from gi.repository import Notify


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        title = self.get_argument('title')
        Hello = Notify.Notification.new("主人，您有了新的泡泡消息", title, "dialog-information")
        Hello.show()
        self.write(title)

settings = {
    'debug': True,
    }

application = tornado.web.Application(
    [(r"/", MainHandler),
     ],
    **settings
    )


if __name__ == "__main__":
    Notify.init("popo")
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(34567)
    tornado.ioloop.IOLoop.instance().start()


