from controllers import *

routes = [
    (
        r"/login",
        login.LoginHandler
    ),
    (
        r"/signup",
        signup.SignupHandler
    ),
    (
        r"/uploads",
        uploads.UploadsHandler
    ),
    (
        r"/logout",
        logout.LogoutHandler
    ),
    (
        r"/admin/addUser",
        admin.AddUserHandler
    ),
    (
        r"/admin/removeUser",
        admin.RemoveUserHandler
    )
]
