import os

import firebase_admin
from firebase_admin import firestore, credentials
from flask import Flask

from api.v1 import initialise_apis
from settings import config


def create_app():
    app = Flask(__name__)
    app.db = initialise_firestore()
    initialise_apis(app)
    return app


def initialise_firestore():
    if os.getenv('GAE_ENV', '').startswith('standard'):
        # Production in the standard environment
        cred = credentials.ApplicationDefault()
        firebase_admin.initialize_app(cred, {'projectId': config.PROJECT_ID})
        print("Running on AppEngine")
    else:
        # Production in the standard environment
        cred = credentials.Certificate(config.GOOGLE_APPLICATION_CREDENTIALS)
        firebase_admin.initialize_app(cred)
        print("Running on Devserver")
    return firestore.client()
