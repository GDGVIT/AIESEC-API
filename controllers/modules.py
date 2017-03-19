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
from passlib.hash import sha256_crypt as scrypt

secret = "bb9f8f5742f313ab5e6b3d93f96f36ab59955d86b71b4a7c"

db = MotorClient().aiesec
