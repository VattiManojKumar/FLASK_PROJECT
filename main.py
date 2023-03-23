from flask import Flask,redirect,url_for,render_template

app=Flask(__name__)


@app.route('/')
def welcome():
    return render_template('index.html')

@app.route('/success/<int:score>')
def success(score):
    return " The score is verified and found  passed as te score is "+str(score)

@app.route('/Fail/<int:score>')
def Fail(score):
    return " The score is verified and found failed as the score is  "+str(score)

@app.route('/results/<int:marks>')
def results(marks):
    result=""
    if marks>50:
       result="success"
    else:
        result="Fail"
    
    return redirect(url_for(result,score=marks))




if __name__=='__main__':
    app.run(debug=True)