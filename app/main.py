from flask import Flask, render_template

app = Flask(__name__, static_url_path="/static")


@app.route('/')
def calendar():
    return render_template('main.html')

@app.route('/filght')
def filght():
    return render_template('filght.html')

@app.route('/dashboard1')
def dashboard1():
    return render_template('dashboard1.html')

@app.route('/dashboard2')
def dashboard2():
    return render_template('dashboard2.html')

if __name__ == '__main__':
    app.run(port='5000', debug=True)