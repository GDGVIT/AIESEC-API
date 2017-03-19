from modules import *

class LogoutHandler(RequestHandler):

    @coroutine
    def post(auth_token):

        db.token.remove({"token" : auth_token})
        yield {"code" : 200, "status" : "successfull"}
        return
