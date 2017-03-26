from controllers import *

routes = [
    (
        r"/ep/login",
        login.LoginHandler
    ),
    (
        r"/ep/signup",
        signup.SignupHandler
    ),
    (
        r"/ep/uploads",
        uploads.UploadsHandler
    ),
    (
        r"/logout",
        logout.LogoutHandler
    ),
    (
        r"/ep/admin/addUser",
        admin.AddUserHandler
    ),
    (
        r"/ep/admin/removeUser",
        admin.RemoveUserHandler
    ),
    (
        r"/ep/admin/postmessage",
        admin.PostMessageHandler
    ),
    (
        r"/ep/messages",
        viewMessages.ViewMessagesHandler
    )
]
