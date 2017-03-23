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

                if db.users.find({"email" : email}):
                    self.write({"code" : 405, "status" : "already _a_member"})

                else:
                    db.users.insert({"email" : email})
                    self.write({"code" : 200, "status" : "successfull"})

            else:
                self.write({"code" : 300, "status" : "Not_a_admin"})

        else:
            self.wirte({"code" : 300, "status" : "Invalid_token"})
