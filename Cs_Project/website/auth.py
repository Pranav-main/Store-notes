from flask import Blueprint

auth = Blueprint("auth",__name__)

@auth.route("/login")
def login():
    return "<p>LOGIN</p>"

@auth.route("/logout")
def logout():
    return "<p>LOGOUT</p>"

@auth.route("/Sign_up")
def sign_up():
    return "<p>Sign Up</p>"