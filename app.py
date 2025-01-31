### Building URL Dynamically
#### Variable Rules and URL Building

from flask import Flask, redirect, url_for

app=Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to my YT Channel'

@app.route('/success/<int:score>')
def success(score):
    return "<html><body><h1>Congratulations you passed !! </h1></body></html>"

@app.route('/fail/<int:score>')
def fail(score):
    return "The person has failed the exam , and the marks is " + str(score)

### Result checker
@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=marks))



if __name__=='__main__':    
    app.run(debug=True)