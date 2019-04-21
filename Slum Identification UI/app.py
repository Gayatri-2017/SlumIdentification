from flask import Flask, render_template, request, flash
from ReplaceWithFileName import ReplaceWithFunctionName

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('HomePage.html')

@app.route('/HomePage.html')
def homepage():
    ReplaceWithFunctionName()
    return render_template('HomePage.html')

@app.route('/Step2.html')
def step2():
    ReplaceWithFunctionName()
    return render_template('Step2.html')

@app.route('/Step3.html')
def step3():
    ReplaceWithFunctionName()
    return render_template('Step3.html')

if __name__ == '__main__':
    app.run(debug = True)

    