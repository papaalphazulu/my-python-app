import os
from flask import Flask, request, abort
from cfenv import AppEnv
from sap import xssec

app = Flask(__name__)
uaa = AppEnv().get_service(name='my-python-xsuaa').credentials

@app.route('/')
def hello():
    auth = request.headers.get('Authorization', '')
    if not auth.startswith('Bearer '):
        abort(401)          # no login token -> refuse
    try:
        ctx = xssec.create_security_context(auth[7:], uaa)
    except Exception:
        abort(401)          # invalid or expired token -> refuse
    return f"Hello {ctx.get_given_name()} ({ctx.get_email()}), you are logged in!"
