from modules import *
from utilities import *

secret = "bb9f8f5742f313ab5e6b3d93f96f36ab59955d86b71b4a7c"

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

		if db.users.find_one({"email" : email}):

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
			db.token.insert({"token" : token, "name" : name, "email" : email})

			self.write({"token" : token, "code" : 200, "status" : "successfull", "user_data" : data})

		else:
			self.write({"code" : 401, "status" : "not_given_access"})
