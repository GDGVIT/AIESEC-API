from modules import *

__UPLOADS__ = "uploads/"

class UploadsHandler(RequestHandler):

	def post(auth_token, file):

		extn = os.path.splitext(fname)[1]
		cname = str(uuid.uuid4()) + extn
		fh = open(__UPLOADS__ + name + "/" + cname, 'wb')
		fh.write(fileinfo['body'])
		fh.close()
