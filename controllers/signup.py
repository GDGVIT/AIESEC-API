from modules import *
from utilities import *


class SignupHandler(RequestHandler):

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

		isUser = yield db.users.find_one({"email" : email})

		if isUser:
			password, salt = hashingPassword(pswd)

			ret = yield db.users.update({"email" : email},{"$set" : {
				"name" : name,
				"pswd" : password,
				"contact" : ctNo,
				"raisedBy" : raisedby,
				"country_pref" : [cpf1, cpf2, cpf3],
				"status" : "raised",
				"files" : [],
				"salt" : salt
				}})

			now = datetime.now()
			time = now.strftime("%d-%m-%Y %I:%M %p")

			token = jwt.encode({"email" : email, "time" : time},
								secret, algorithm = 'HS256')
			yield db.token.insert({"token" : token, "name" : name, "email" : email})
			yield db.bodies.insert({"body" : "gb", "name" : name, "email" : email})

			self.write({"token" : token, "code" : 200, "status" : "successfull",
						"email" : email,
						"name" : name,
						"contact" : ctNo,
						"raisedBy" : raisedby,
						"country_pref" : [cpf1, cpf2, cpf3],
						"status" : "raised",
						"files" : []
						})

		else:
			self.write({"code" : 401, "status" : "not_given_access"})
