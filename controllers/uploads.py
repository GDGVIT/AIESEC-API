from modules import *

__UPLOADS__ = "uploads/"

class UploadsHandler(RequestHandler):

	@coroutine
	def post(self, auth_token, files):

		auth_token = self.get_argument("auth_token")
		files = self.get_argument("files")

		tk = yield db.token.find_one({"token" : auth_token})

		if tk:
			for fl in files:
				extn = os.path.splitext(fl)[1]
				cname = str(uuid.uuid4()) + extn
				fh = open(__UPLOADS__ + cname, 'wb')
				fh.write(fl['body'])
				fh.close()
				db.users.update({"email" : tk["email"]},
					{"$push" : {"files" : __UPLOADS__ + cname}})

			self.write({"code" : 202, "status" : "successfully_uploaded"})

		else:
			self.write({"code" : 102, "status" : "invalid_token"})
