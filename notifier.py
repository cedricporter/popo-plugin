#!/usr/bin/env python
# -*- coding: utf-8 -*-  
# author:  Hua Liang [ Stupid ET ]
# email:   et@everet.org
# website: http://EverET.org
#

import tornado.httpserver
import tornado.ioloop
import tornado.web
import pynotify

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        title = self.get_argument('title')
        print title
        n = pynotify.Notification ("主人，您有了新的泡泡消息", title)
        n.show()

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
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()


