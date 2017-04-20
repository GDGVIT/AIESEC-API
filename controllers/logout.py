from modules import *

class LogoutHandler(RequestHandler):

    """
	class resposible to handle the logout functions

	route : /logout
	parameter : token
	"""

    @coroutine
    def post(self):

        token = self.get_argument("token")

        db.token.remove({"token" : token})
        self.write({"code" : 200, "msg" : "successful"})
