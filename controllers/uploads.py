from modules import *

__UPLOADS__ = "uploads/"

class UploadsHandler(RequestHandler):

	"""
	class resposible to handle the uploads functions

	route : /uploads
	parameter : token, files (multipart)
	"""

	@coroutine
	def post(self):

		token = self.get_argument("token")
		fle = self.request.files["file"][0]
		fnm = self.get_argument("fname")

		tk = yield db.token.find_one({"token" : token})

		if tk:
			extn = os.path.splitext(fl['filename'])[1]
			cname = str(uuid.uuid4()) + extn
			fh = open(__UPLOADS__ + cname, 'w')
			fh.write(fl['body'])
			fh.close()
			temp = {"new_name" : __UPLOADS__ + cname,
					"orig_name" : fnm
					}
			_ = yield db.ep.update({"email" : tk["email"]},
				{"$push" : {"files" : temp}})

			self.write({"code" : 200, "msg" : "successfully_uploaded",
			 		"files" : temp})

		else:
			self.write({"code" : 100, "msg" : "invalid_token", "files" : []})
