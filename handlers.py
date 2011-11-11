import tornado.web
import logging

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html");

class AdminHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("admin/index.html")
