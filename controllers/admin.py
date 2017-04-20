from modules import *

class AddUserHandler(RequestHandler):

    @coroutine
    def post(self):

        token = self.get_argument("token")
        aemail = self.get_argument("aemail")
        uemail = self.get_argument("uemail")
        body = self.get_argument("body")
        tk = yield db.token.find_one({"token" : token})

        if tk:
            chk_data = yield db.bodies.find_one({"body" : "eb", "email": aemail})

            if chk_data and (aemail == tk["email"]):

                isUser = yield db.users.find_one({"email" : uemail})
                if isUser:
                    self.write({"code" : 405, "msg" : "already _a_member"})

                else:
                    yield db.users.insert({"email" : uemail})
                    yield db.bodies.insert({"body" : body, "name" : "", "email" : uemail})
                    self.write({"code" : 200, "msg" : "successfull"})

            else:
                self.write({"code" : 300, "msg" : "Not_a_admin"})

        else:
            self.write({"code" : 300, "msg" : "Invalid_token"})

class RemoveUserHandler(RequestHandler):

    @coroutine
    def post(self):

        token = self.get_argument("token")
        aemail = self.get_argument("aemail")
        uemail = self.get_argument("uemail")

        tk = yield db.token.find_one({"token" : token})

        if tk:
            chk_data = yield db.bodies.find_one({"body" : "eb", "email": aemail})

            if chk_data and (aemail == tk["email"]):

                isUser = yield db.users.remove({"email" : uemail})
                if isUser:
                    self.write({"code" : 200, "msg" : "successfull"})

                else:
                    self.write({"code" : 400, "msg" : "not_a_member"})

            else:
                self.write({"code" : 300, "msg" : "Not_a_admin"})

        else:
            self.write({"code" : 300, "msg" : "Invalid_token"})
