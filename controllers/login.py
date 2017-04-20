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
		mem = self.get_argument("member")

		# for AIESECer's
		if mem = "aiesec"
			data = yield db.users.find_one({"email" : email})

			if data:

				if pbkdf2_sha256.verify(data["salt"] + pswd, data["pswd"]):

					token = setToken(email, name)

					adm = False

					if data["body"] == "eb":
						adm = True

					del(data["_id"])
					del(data["pswd"])
					del(data["salt"])
					self.write({"token" : token, "code" : 200,
							"status" : "successful", "udata" : data,
							"isAdmin" : adm, "member" : "aiesec"})

				else:
					self.write({"code" : 400, "msg" : "invalid_credentials"})

			else:

				self.write({"code" : 400, "msg" : "invalid_credentials"})

		# for EP
		else:
			data = yield db.ep.find_one({"email" : email})

			if data:

				if pbkdf2_sha256.verify(data["salt"] + pswd, data["pswd"]):

					token = setToken(email, name)

					del(data["_id"])
					del(data["pswd"])
					del(data["salt"])
					self.write({"token" : token, "code" : 200,
							"status" : "successful", "udata" : data,
							"member" : "ep"})

				else:
					self.write({"code" : 400, "msg" : "invalid_credentials"})

			else:

				self.write({"code" : 400, "msg" : "invalid_credentials"})
