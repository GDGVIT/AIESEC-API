from modules import *
from utilities import *

secret = "bb9f8f5742f313ab5e6b3d93f96f36ab59955d86b71b4a7c"

class LoginHandler(RequestHandler):

	@coroutine
	def post(self):

		email = self.get_argument("email")
		pswd = self.get_argument("pswd")

		data = yield db.users.find_one({"email" : email})

		if data:

			if pbkdf2_sha256.verify(data["salt"] + pswd, data["pswd"]):
				now = datetime.now()
				time = now.strftime("%d-%m-%Y %I:%M %p")

				token = jwt.encode({"email" : email, "time" : time}, secret, algorithm = 'HS256')
				db.token.insert({"token" : token, "name" : data["name"], "email" : email})

				del(data["_id"])
				del(data["pswd"])
				del(data["salt"])
				self.write({"token" : token, "code" : 200, "status" : "successfull", "user_data" : data})

			else:
				self.write({"code" : 400, "status" : "invalid_password"})

		else:

			self.write({"code" : 400, "status" : "invalid_email"})
