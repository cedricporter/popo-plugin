#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author:  Hua Liang [ Stupid ET ]
# email:   et@everet.org
# website: http://EverET.org
#


import datetime
from collections import defaultdict
import functools

import tornado.httpserver
import tornado.ioloop
import tornado.web
from gi.repository import Notify


class Record(object):
    def __init__(self, count, last_access_time,
                 last_notify_time):
        self.count = count
        self.last_notify_time = last_notify_time
        self.last_access_time = last_access_time

Record = functools.partial(Record, 0, datetime.datetime(2000, 1, 1),
                           datetime.datetime(2000, 1, 1))

db = defaultdict(Record)

# 静默时间，在这个时间内提醒过就不再提醒了
SILENT_SECONDS = 60 * 2


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        now = datetime.datetime.now()
        title = self.get_argument('title')
        record = db[title]
        record.last_access_time = now

        if record.last_notify_time < now - datetime.timedelta(seconds=SILENT_SECONDS):
            record.last_notify_time = now
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
