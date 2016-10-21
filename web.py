import tornado.ioloop
import tornado.web
import os

def SpidApp():

	settings = {
		"debug": True,
		"cookie_secret": "DFGHFCTHJUYTDRESHJUYTDRESTYUHIYTREFGTHJMYTDGHJMHVNGCF",
		"static_path": os.path.join(os.path.dirname(__file__), "static")
	}

	app = tornado.web.Application([
		(r"/", MainHandler),
		(r"/main", MainServerHandler),
		(r"/patreon", PatreonServerHandler),
	], **settings)

	return app

class MainHandler(tornado.web.RequestHandler):

    def get(self):
    	self.render("templates/index.html")

class MainServerHandler(tornado.web.RequestHandler):

    def get(self):
    	self.render("templates/main.html")

class PatreonServerHandler(tornado.web.RequestHandler):

    def get(self):
    	self.render("templates/patreon.html")



app = SpidApp()

if __name__ == "__main__":
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()