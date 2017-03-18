from modules import *

import jwt

secret = "bb9f8f5742f313ab5e6b3d93f96f36ab59955d86b71b4a7c"

class SignupHandler(RequestHandler):

	def post(file, email, pswd, name, ctNo, raisedby, cpf1, cpf2, cpf3):

		if db.mails.find_one(email):

			password = hashingPassword(pswd)
			password = hashlib.sha256(password).hexdigest()

			ret = yield db.users.insert({
				"name" : name,
				"email" : email,
				"pswd" = password,
				"contact" : ctNo,
				"raisedBy" : raisedby,
				"country_pref" : [cpf1, cpf2, cpf3],
				"status" : "raised",
				"files" : []
				})

			token = jwt.encode({"email" : email}, secret, algorithm = 'HS256')
			db.token.insert({"token" : token, "name" : ret["name"], "email" : email})

			return {"token" : token, "code" : 200, "status" : "successfull"}

		else:
			return {"code" : 401, "status" : "not_given_access"}
