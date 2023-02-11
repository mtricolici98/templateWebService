from flask import Flask

from api_views.example_blueprint import example_blueprint
from api_views.user_views import auth_view

app = Flask(__name__)

app.register_blueprint(auth_view)
app.register_blueprint(example_blueprint)

app.run(port=8080)
