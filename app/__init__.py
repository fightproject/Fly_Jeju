from flask import Flask,render_template

app = Flask(__name__)

# @app.route('/')
# def home():
#     return '''
#     <h1>HELLO FLASK</h1>
#     '''

from app.main.index import main as main 
 
app.register_blueprint(main)