from modules import *

class LogoutHandler(RequestHandler):

    @coroutine
    def post(self):

        auth_token = self.get_argument("auth_token")

        db.token.remove({"token" : auth_token})
        self.write({"code" : 200, "status" : "successfull"})
