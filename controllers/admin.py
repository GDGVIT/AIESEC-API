from modules import *

class AddUserHandler(RequestHandler):

    @coroutine
    def post(self):

        auth_token = self.get_argument("auth_token")
        admin_email = self.get_argument("admin_email")
        email = self.get_argument("uemail")
        tk = yield db.token.find_one({"token" : auth_token})

        if tk:
            chk_data = yield db.bodies.find_one({"body" : "eb", "email": admin_email})

            if chk_data and (admin_email == tk["email"]):

                isUser = yield db.users.find_one({"email" : uemail})
                if isUser:
                    self.write({"code" : 405, "status" : "already _a_member"})

                else:
                    db.users.insert({"email" : uemail})
                    self.write({"code" : 200, "status" : "successfull"})

            else:
                self.write({"code" : 300, "status" : "Not_a_admin"})

        else:
            self.wirte({"code" : 300, "status" : "Invalid_token"})

class RemoveUserHandler(RequestHandler):

    @coroutine
    def post(self):

        auth_token = self.get_argument("auth_token")
        admin_email = self.get_argument("admin_email")
        email = self.get_argument("uemail")

        tk = yield db.token.find_one({"token" : auth_token})

        if tk:
            chk_data = yield db.bodies.find_one({"body" : "eb", "email": admin_email})

            if chk_data and (admin_email == tk["email"]):

                isUser = yield db.users.remove({"email" : uemail})
                if isUser:
                    self.write({"code" : 200, "status" : "successfull"})

                else:
                    self.write({"code" : 400, "status" : "not_a_member"})

            else:
                self.write({"code" : 300, "status" : "Not_a_admin"})

        else:
            self.wirte({"code" : 300, "status" : "Invalid_token"})
