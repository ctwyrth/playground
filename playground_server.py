from flask import Flask

from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/play')
def playground():
    return render_template('play.html', times = 3)

@app.route('/play/<int:val>')
def multi_play(val):
    return render_template('play.html', val)

@app.route('/play/<int:val>/<string:color>')
def multi_play_color(val, color):
    return render_template('play.html', times = val, color = color)

if __name__ == '__main__':
    app.run(debug=True)
