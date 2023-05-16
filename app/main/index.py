from flask import Blueprint, request, render_template, flash, redirect, url_for,Flask
from flask import current_app as app


main = Blueprint('main', __name__, url_prefix='/')

@main.route('/')
def index():
#     return render_template('main/index.html')
    return render_template('main/index_bootstrap.html')

if __name__ == "__main__":
    app.register_blueprint(main)
    app.run(debug=True)

