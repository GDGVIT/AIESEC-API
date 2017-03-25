from modules import *

class AddUserHandler(RequestHandler):

    @coroutine
    def post(self):

        token = self.get_argument("token")
        aemail = self.get_argument("aemail")
        uemail = self.get_argument("uemail")
        tk = yield db.token.find_one({"token" : token})

        if tk:
            chk_data = yield db.bodies.find_one({"body" : "eb", "email": aemail})

            if chk_data and (aemail == tk["email"]):

                isUser = yield db.users.find_one({"email" : uemail})
                if isUser:
                    self.write({"code" : 405, "status" : "already _a_member"})

                else:
                    db.users.insert({"email" : uemail})
                    self.write({"code" : 200, "status" : "successfull"})

            else:
                self.write({"code" : 300, "status" : "Not_a_admin"})

        else:
            self.write({"code" : 300, "status" : "Invalid_token"})

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
                    self.write({"code" : 200, "status" : "successfull"})

                else:
                    self.write({"code" : 400, "status" : "not_a_member"})

            else:
                self.write({"code" : 300, "status" : "Not_a_admin"})

        else:
            self.write({"code" : 300, "status" : "Invalid_token"})

class PostMessageHandler(RequestHandler):

    @coroutine
    def post(self):

        token = self.get_argument("token")
        email = self.get_argument("email")
        msg = self.get_argument("message")

        tk = yield db.token.find_one({"token" : token})

        if tk:
            chk_data = yield db.bodies.find_one({"body" : "eb", "email": aemail})

            if chk_data and (aemail == tk["email"]):

                yield db.messages.insert({"email" : email, "msg" : msg})

            else:
                self.write({"code" : 300, "status" : "Not_a_admin"})

        else:
            self.write({"code" : 300, "status" : "Invalid_token"})
