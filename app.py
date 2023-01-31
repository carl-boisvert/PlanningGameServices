from flask import Flask
from flask import jsonify
from flask_dotenv import DotEnv

from models.user import User

app = Flask(__name__)
env = DotEnv(app)
env.init_app(app)
app.config["MONGO_URI"] = env


@app.route('/steam/login')
def steam_login():  # put application's code here
    user = User("CarlBoisvertDev", "3423d32d1212s12")
    user.add_skin(1)
    return jsonify(user.to_dict())


if __name__ == '__main__':
    app.run()
