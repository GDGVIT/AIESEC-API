from modules import *
from utilities import *


class SignupHandler(RequestHandler):

	"""
	class resposible to handle the signup functions for AIESEC member

	route : /aiesec/signup
	parameter : email, pswd, name, ctNo, dept
	"""

	@coroutine
	def post(self):

		email = self.get_argument("email")
		pswd = self.get_argument("pswd")
		name = self.get_argument("name")
		ctNo = self.get_argument("ctNo")
		dept = self.get_argument("dept")

		isUser = yield db.users.find_one({"email" : email})

		if isUser:
			try:
				ct = isUser["contact"]
			except KeyError:
				password, salt = hashingPassword(pswd)

				ret = yield db.users.update({"email" : email},
									{"$set" : {
										"name" : name,
										"pswd" : password,
										"contact" : ctNo,
										"dept" : dept,
										"salt" : salt
										}})

				token = setToken(email, name)

				self.write({"token" : token,
							"code" : 200,
							"msg" : "successful",
							"udata" : {	"email" : email,
										"name" : name,
										"contact" : ctNo,
										"dept" : dept,
										"position" : isUser["body"]
									  }
							})
			else:
				self.write({"code" : 402, "msg" : "already_a_member"})

		else:
			self.write({"code" : 403, "msg" : "not_aiesec_member"})
