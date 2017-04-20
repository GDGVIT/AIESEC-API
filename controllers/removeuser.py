from modules import *

class RemoveUserHandler(RequestHandler):

	"""
	class resposible to handle the remove user functions

	route : /removeUser
	parameter : token, amail (admin_email), uemail (user_email)
	"""

    @coroutine
    def post(self):

        token = self.get_argument("token")
        aemail = self.get_argument("aemail")
        uemail = self.get_argument("uemail")

        tk = yield db.token.find_one({"token" : token})

        if tk:
            chk_data = yield db.bodies.find_one({"body" : "eb", "email": aemail})

            if chk_data and (aemail == tk["email"]):

                yield db.users.remove({"email" : uemail})
                yield db.bodies.remove({"email" : uemail})
                
                self.write({"code" : 200, "msg" : "successful"})

            else:
                self.write({"code" : 101, "msg" : "Not_a_admin"})

        else:
            self.write({"code" : 100, "msg" : "Invalid_token"})
