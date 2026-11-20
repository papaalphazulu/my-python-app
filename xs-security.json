from flask import Flask, request, abort
from cfenv import AppEnv
from sap import xssec

app = Flask(__name__)
uaa = AppEnv().get_service(name='my-python-xsuaa').credentials

def get_context():
    """Return the user's security context, or refuse with 401."""
    auth = request.headers.get('Authorization', '')
    if not auth.startswith('Bearer '):
        abort(401)
    try:
        return xssec.create_security_context(auth[7:], uaa)
    except Exception:
        abort(401)

@app.route('/')
def hello():
    ctx = get_context()
    if not ctx.check_local_scope('Display'):
        abort(403)                      # logged in, but no Viewer role
    access = [s for s in ('Display', 'Admin') if ctx.check_local_scope(s)]
    return (f"Hello {ctx.get_given_name()} ({ctx.get_email()})! "
            f"Your permissions: {', '.join(access)}. "
            f"Try the admin page at /api/admin")

@app.route('/admin')
def admin():
    ctx = get_context()
    if not ctx.check_local_scope('Admin'):
        abort(403)                      # needs the Administrator role
    return "Admin area: only users with the Administrator role can see this page."