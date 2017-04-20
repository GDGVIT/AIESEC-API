from modules import *
from utilities import *


class LoginHandler(RequestHandler):
	"""
	class resposible to handle the login functions

	route : /login
	parameter : email, pswd
	"""
	@coroutine
	def post(self):

		email = self.get_argument("email")
		pswd = self.get_argument("pswd")

		data = yield db.users.find_one({"email" : email})

		if data:

			if pbkdf2_sha256.verify(data["salt"] + pswd, data["pswd"]):
				now = datetime.now()
				time = now.strftime("%d-%m-%Y %I:%M %p")

				token = jwt.encode({"email" : email, "time" : time}, secret,
								algorithm = 'HS256')

				yield db.token.insert({"token" : token,
				 					"name" : data["name"],
									"email" : email})

				adm = False
				isAdmin = yield db.bodies.find_one({"body" : "eb", "email": email})

				if bool(isAdmin):
					adm = True

				del(data["_id"])
				del(data["pswd"])
				del(data["salt"])
				self.write({"token" : token, "code" : 200,
						"status" : "successful", "udata" : data,
						"isAdmin" : adm})

			else:
				self.write({"code" : 400, "status" : "invalid_password"})

		else:

			self.write({"code" : 400, "status" : "invalid_email"})
