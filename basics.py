"""from flask import Flask

#Creates WSGI Application refers notes
app=Flask(__name__)

 #decorator(Its URL) when we access this URl  the home function will be called.
@app.route('/') 
def home():
    return "Hello Home! my name is vijay iam sreendhi i am cse branch i am 2nd year"

@app.route('/personal')
def personal():
    return "my full name is Sriloju vijay varma"



if __name__ == "__main__":
    app.run(debug=True)

    """


###Building Url Dynamically
###Variable Rules and URL Building

from flask import Flask,redirect,url_for

ob=Flask(__name__)


@ob.route('/')  #---> this is root URL 
def welcome():
    return "Hello world!"

@ob.route('/passed/<int:score>')
def passed(score):
    """return "The Person has Passed and the marks is"+str(score)"""
                               #or
    return "<html><body><h1> The Result is PASSED! </h1></body></html>"

@ob.route('/failed/<int:score>')
def failed(score):
    return "The Person has failed and the marks is "+str(score)


###result checker
@ob.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks <= 30:
        result='failed'
    else:
        result='passed'
    "return result"
    return redirect(url_for(result,score=marks))

if __name__ == '__main__':
    ob.run(debug=True)