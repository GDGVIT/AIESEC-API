from modules import *

class AddUserHandler(RequestHandler):

    """
    class resposible to handle the add user functions

    route : /addUser
    parameter : token, amail (admin_email), uemail (user_email), body (working body)
    """

    @coroutine
    def post(self):

        token = self.get_argument("token")
        aemail = self.get_argument("aemail")
        uemail = self.get_argument("uemail")
        body = self.get_argument("body")

        tk = yield db.token.find_one({"token" : token})

        if tk:
            chk_data = yield db.users.find_one({"body" : "eb", "email": aemail})

            if chk_data and (aemail == tk["email"]):

                isUser = yield db.users.find_one({"email" : uemail})

                if isUser:
                    self.write({"code" : 402, "msg" : "already_a_member"})

                else:
                    yield db.users.insert({"email" : uemail})
                    
                    self.write({"code" : 200, "msg" : "successful"})

            else:
                self.write({"code" :101, "msg" : "Not_a_admin"})

        else:
            self.write({"code" : 100, "msg" : "Invalid_token"})
