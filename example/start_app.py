from flask import Flask, render_template

app = Flask(__name__)

@app.route('/loopindex')
def loopindex():
    items = ['a', 'b', 'c', 'd']
    return render_template('loopindex.html', items=items)

app.run()