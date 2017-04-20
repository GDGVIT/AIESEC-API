from modules import *
from utilities import *


class SignupHandler(RequestHandler):

	"""
	class resposible to handle the signup functions of external participant

	route : /ep/signup
	parameter : email, pswd, name, ctNo, raisedby, cpf1, cpf2, cpf3
	"""

	@coroutine
	def post(self):

		email = self.get_argument("email")
		pswd = self.get_argument("pswd")
		name = self.get_argument("name")
		ctNo = self.get_argument("ctNo")
		raisedby = self.get_argument("raisedby")
		cpf1 = self.get_argument("cpf1")
		cpf2 = self.get_argument("cpf2")
		cpf3 = self.get_argument("cpf3")

		password, salt = hashingPassword(pswd)

        res = yield db.ep.find({"email" : email})

        if res:
            self.write({"code" : 402, "msg" : "already_a_member"})
        else:
    		ret = yield db.ep.insert({"email" : email,
    								"name" : name,
    								"pswd" : password,
    								"contact" : ctNo,
    								"raisedBy" : raisedby,
    								"country_pref" : [cpf1, cpf2, cpf3],
    								"status" : "raised",
    								"files" : [],
    								"salt" : salt,
                                    "body" : "ep"
    								})

    		token = setToken(email, name)

    		self.write({"token" : token,
    					"code" : 200,
    					"msg" : "successful",
    					"udata" : {	"email" : email,
    								"name" : name,
    								"contact" : ctNo,
    								"raisedBy" : raisedby,
    								"country_pref" : [cpf1, cpf2, cpf3],
    								"status" : "raised",
    								"files" : [],
                                    "body" : "ep"
    							  }
    					})
