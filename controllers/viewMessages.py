from modules import *

class ViewMessagesHandler(RequestHandler):

    @coroutine
    def post(self):

        token = self.get_argument("token")
        req = int(self.get_argument("req"))
        tk = yield db.token.find_one({"token" : token})

        if tk:
            msgs = db.messages.find({}).skip(req*50).limit(50)

            for msg in msgs:
                del(msg["_id"])

            self.write({"code" : 200, "status" : "successfull", "messages" : msgs})
        else:
            self.write({"code" : 300, "status" : "Invalid_token"})
