### Integrate HTML with Flask
### HTTP verb GET And POST




###Jinja2 Template

'''
{%...%} for conditions(for,while) statements
{{    }} expressions to print output
{#....#} this is for comments
'''

from flask import Flask,redirect,url_for,render_template,request


app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/passed/<int:score>')
def passed(score):
    res=""
    if score > 30:
        res="passed"
    else:
        res="failed"
    exp={'score':score,'res':res}
    return render_template('result.html',fres=exp)

@app.route('/failed/<int:score>')
def failed(score):
    res=""
    if score > 30:
        res="PASS"
    else:
        res="FAIL"

    return render_template('result.html',fres=res)
    

@app.route('/results/<int:marks>')
def results(marks):
    res=""
    if marks <=30:
        res ='failed'
    else:
        res='passed'
    return  redirect(url_for(res,score=marks))


### Result checker submit HTML page
@app.route('/submit',methods=['POST','GET'])
def submit():
    ts=0
    if request.method == "POST":
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        ts=(science+maths+c+data_science)/4
        res=""
        return redirect(url_for('passed',score=ts))
    





if __name__ == "__main__":
    app.run(debug=True)