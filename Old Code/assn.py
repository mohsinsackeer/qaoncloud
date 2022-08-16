from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)


@app.route('/',methods=['POST','GET'])
def details():
    if request.method=='POST':
        details=request.form
        return render_template('details.html',details_dict=details)
    else:
        return render_template('registration.html')
if __name__=='__main__':
    app.run(debug=True)
