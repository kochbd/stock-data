from flask import Flask, render_template
import datetime
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/stuff", methods=['GET'])
def hello():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
            'title' : ' Hello!',
            'time' : timeString
        }
    return render_template('main.html', **templateData)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
