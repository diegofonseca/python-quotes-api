from flask import Flask, render_template
app = Flask(__name__)
APP_NAME = 'Python Quotes API'

@app.route('/')
def home():
    try:
        return render_template('index.html', app_name=APP_NAME)
    except Exception as e:
        return str(e)

@app.route('/about')
def about():
    try:
        return render_template('about.html', app_name=APP_NAME)
    except Exception as e:
        return str(e)

@app.errorhandler(404)
def four_oh_four(e):
    return render_template('error/404.html', app_name=APP_NAME, error = e)

if __name__ == "__main__":
    app.run()
