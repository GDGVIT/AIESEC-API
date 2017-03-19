from modules import *
from utilities import *

secret = "bb9f8f5742f313ab5e6b3d93f96f36ab59955d86b71b4a7c"

class LoginHandler(RequestHandler):

	@coroutine
	def post(self):

		email = self.get_argument("email")
		pswd = self.get_argument("pswd")

		password = hashingPassword(pswd)
		password = hashlib.sha256(pswd).hexdigest()

		data = yield db.users.find_one({"email" : email, "pswd" : password})

		if bool(ret):

			token = jwt.encode({"email" : email}, secret, algorithm = 'HS256')
			db.token.insert({"token" : token, "name" : data["name"], "email" : email})

			del(data["_id"])
			self.write({"token" : token, "code" : 200, "status" : "successfull", "user_data" : data})

		else:

			self.write({"code" : 400, "status" : "invalid_credentials"})
