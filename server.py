#Tornado Libraries
from tornado.ioloop import IOLoop
from tornado.escape import json_encode
from tornado.web import RequestHandler, Application, asynchronous
from tornado.httpserver import HTTPServer
from tornado.httpclient import AsyncHTTPClient
from tornado.gen import engine, Task
from tornado.options import define, options

import jwt
from motor import MotorClient
import json
import requests
import os, uuid, sys
from passlib.hash import sha256_crypt as scrypt

define("port", default = 8000, help="Contact the One who made it Contact PIYUSH :P", type = int)

secret = "bb9f8f5742f313ab5e6b3d93f96f36ab59955d86b71b4a7c"

db = MotorClient().aiesec

#overloading the Application 
class Application(Application):

	def __init__(self):

		handlers = []
		settings = dict(debug = True)
		Application.__init__(self, handlers, **settings)