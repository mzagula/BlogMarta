from flask import Flask
from flask_bootstrap import Bootstrap
from flaskext.markdown import Markdown

app = Flask(__name__)
bootstrap = Bootstrap(app)
markdown=Markdown(app)


from app import routes