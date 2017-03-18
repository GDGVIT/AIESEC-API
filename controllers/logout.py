from modules import *

class LogoutHandler(RequestHandler):

    def post(auth_token):

        db.token.remove({"token" : auth_token})
        return {"code" : 200, "status" : "successfull"}
