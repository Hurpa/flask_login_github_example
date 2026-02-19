import flask
import flask_login

app = flask.Flask(__name__)
app.secret_key = "super secret string"  # Change this!

login_manager = flask_login.LoginManager()
login_manager.init_app(app)

class User(flask_login.UserMixin):
    def __init__(self, user_identifier, name, email, password):
        self.id = user_identifier
        self.name = name
        self.email = email
        self.password = password

users = {"example_user_1": User("example_user_1", "John Doe", "example@example.com", "secretpassword")}

@login_manager.user_loader
def user_loader(id):
    print(f"User_loader_id: { id }")
    return users.get(id)

@app.get("/login")
def login():
    return """<form method=post>
      Email: <input name="email"><br>
      Password: <input name="password" type=password><br>
      <button>Log In</button>
    </form>"""

@app.post("/login")
def login_form():
    user = next((u for u in users.values() if u.email == flask.request.form["email"]), None)

    if user is None or user.password != flask.request.form["password"]:
        return flask.redirect(flask.url_for("login"))

    flask_login.login_user(user)
    return flask.redirect(flask.url_for("protected"))

@app.route("/protected")
@flask_login.login_required
def protected():
    return flask.render_template_string(
        "Logged in as: {{ user.name }}",
        user=flask_login.current_user
    )

@app.route("/logout")
def logout():
    flask_login.logout_user()
    return "Logged out"

if __name__ == "__main__":
    app.run(debug=True)