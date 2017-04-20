from modules import *

def hashingPassword(password, salt = uuid.uuid4().hex):

    """
    function to hash user password and return the hashed password

    @params
    password    :   unhashed password
    salt        :   user password salt for hashing
    """

    np = salt + password
    return pbkdf2_sha256.hash(np), salt

def setToken(email, name):

    """
    function to set user token and return token

    @params
    email    :   user email
    name     :   user name
    """

    now = datetime.now()
    time = now.strftime("%d-%m-%Y %I:%M %p")

    token = jwt.encode({"email" : email, "time" : time},
                        secret, algorithm = 'HS256')
    yield db.token.insert({"token" : token, "name" : name,
                    "email" : email})

    yield token
    return
