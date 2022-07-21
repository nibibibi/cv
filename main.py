from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return render_template('index.html',
                           the_title="nbitell")

@app.route('/website')
def ab_website():
    return "There will be about website section."

@app.route('/cv')
def vitae():
    return "There will be my cv."

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
