"""
module to import all necessary modules
"""

from tornado.ioloop import IOLoop
from tornado.escape import json_encode
from tornado.web import RequestHandler, Application
from tornado.httpserver import HTTPServer
from tornado.gen import coroutine
from tornado.options import define, options

import jwt
import json
import requests
import os, uuid, sys
from motor import MotorClient
from passlib.hash import pbkdf2_sha256
from datetime import datetime

secret = os.environ['SECRET']

"""
collections :
        users   [for AIESECer's]
        ep      [for External Participant]
        token   [for storing all tokens]
"""

db = MotorClient().aiesec
