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
