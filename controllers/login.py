from modules import *

import jwt

secret = "bb9f8f5742f313ab5e6b3d93f96f36ab59955d86b71b4a7c"

class LoginHandler(RequestHandler):

	def post(email, pswd):

		password = hashnigrPassword(pswd)
		password = hashlib.sha256(password).hexdigest()

		ret = yield db.users.find_one({"email" : email, "pswd" = password})

		if bool(ret):

			token = jwt.encode({"email" : email}, secret, algorithm = 'HS256')
			db.token.insert({{"token" : token, "name" : ret["name"]}})

			return {"token" : token, "code" : 200, "status" : "successfull"}

		else:

			return {"code" : 400, "status" : "invalid_credentials"}