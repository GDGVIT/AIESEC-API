"""
module to storing all the routes
"""

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
        r"/addUser",
        admin.AddUserHandler
    ),
    (
        r"/removeUser",
        admin.RemoveUserHandler
    )
]
