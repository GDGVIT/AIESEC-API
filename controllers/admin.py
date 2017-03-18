from modules import *

class AddUserHandler(RequestHandler):

    def post(auth_token, admin_email, email):

        chk_data = db.emails.find({"eb" : admin_email})

        if chk_data:

            db.users.insert({"email" : emails})

            return {"code" : 200, "status" : "successfull"}

        else:
            return {"code" : 300, "status" : "Not_a_admin"}


class
