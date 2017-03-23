from modules import *

class AddUserHandler(RequestHandler):

    @coroutine
    def post(self):

        auth_token = self.get_argument("auth_token")
        admin_email = self.get_argument("admin_email")
        email = self.get_argument("email")
        tk = db.token.find_one({"token" : auth_token})

        if tk:
            chk_data = db.bodies.find({"eb" : admin_email})

            if chk_data:
                db.users.insert({"email" : email})
                yield {"code" : 200, "status" : "successfull"}
                return

            else:
                yield {"code" : 300, "status" : "Not_a_admin"}
                return
