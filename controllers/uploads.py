from modules import *

__UPLOADS__ = "uploads/"

class UploadsHandler(RequestHandler):

	@coroutine
	def post(self):

		token = self.get_argument("token")
		files = self.request.files["file"]

		tk = yield db.token.find_one({"token" : token})
		fl_list = []

		if tk:
			for fl in files:
				extn = os.path.splitext(fl['filename'])[1]
				cname = str(uuid.uuid4()) + extn
				fh = open(__UPLOADS__ + cname, 'w')
				fh.write(fl['body'])
				fh.close()
				fl_list.append({"new_name" : __UPLOADS__ + cname,
						"old_name" : fl['filename']
						})
			db.users.update({"email" : tk["email"]},
				{"$pushAll" : {"files" :fl_list}})

			self.write({"code" : 202, "status" : "successfully_uploaded",
			 		"files" : fl_list})

		else:
			self.write({"code" : 102, "status" : "invalid_token"})
