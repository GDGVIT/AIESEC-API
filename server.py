import routes
from controllers.modules import *

define("port",
  default = 8000,
  help = "Contact the One who made it Contact PIYUSH :P",
  type = int)

#overloading the Application
class Application(Application):

	def __init__(self):

		handlers = routes.routes
		settings = dict(debug = True)
		Application.__init__(self, handlers, **settings)

if __name__ == '__main__':
    options.parse_command_line()
    http_server = HTTPServer(Application())
    http_server.listen(options.port)
    IOLoop.instance().start()
