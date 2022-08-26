import requests
from flask import Flask,render_template,request,redirect,url_for

app=Flask(__name__)


@app.route('/')
def registration():
    return render_template('registration2.html')


@app.route('/registered/',methods=['POST','GET'])
def details():
    if request.method == 'POST':
        detail = request.form
        return render_template('details.html',details_dict=detail)
    else:
        return render_template('registration2.html')


if __name__=='__main__':
    app.run(host='127.0.0.1', port=5001, debug=True)