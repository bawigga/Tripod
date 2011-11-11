import tornado.ioloop
import tornado.web
import tornado.options
import logging
import os

import handlers

handlers = [
    (r"/", handlers.MainHandler),
    (r"/admin", handlers.AdminHandler)
]

settings = dict(
    debug=True,
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
)

application = tornado.web.Application(handlers, **settings)

if __name__ == "__main__":
    tornado.options.parse_command_line() 
    port = 8888
    application.listen(port)
    logging.info("Tornado listening on port %s", port)
    tornado.ioloop.IOLoop.instance().start()

