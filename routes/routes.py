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
        r"/aiesec/signup",
        aiesec_signup.SignupHandler
    ),
    (
        r"/ep/signup",
        ep_signup.SignupHandler
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
        adduser.AddUserHandler
    ),
    (
        r"/removeUser",
        removeuser.RemoveUserHandler
    )
]
