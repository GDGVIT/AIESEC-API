from modules import *

secret = "bb9f8f5742f313ab5e6b3d93f96f36ab59955d86b71b4a7c"

class SignupHandler(RequestHandler):

	@coroutine
	def post(file, email, pswd, name, ctNo, raisedby, cpf1, cpf2, cpf3):

		if db.users.find_one({"email" : email}):

			password = hashingPassword(pswd)
			password = hashlib.sha256(password).hexdigest()

			ret = yield db.users.update({"email" : email},{"$set" : {
				"name" : name,
				"pswd" : password,
				"contact" : ctNo,
				"raisedBy" : raisedby,
				"country_pref" : [cpf1, cpf2, cpf3],
				"status" : "raised",
				"files" : []
				}})

			token = jwt.encode({"email" : email}, secret, algorithm = 'HS256')
			db.token.insert({"token" : token, "name" : name, "email" : email})

			yield {"token" : token, "code" : 200, "status" : "successfull"}
			return

		else:
			yield {"code" : 401, "status" : "not_given_access"}
			return
