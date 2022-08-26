# import requests
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def registration():
    return render_template('registration1.html')


@app.route('/registered/', methods=['POST', 'GET'])
def details():
    if request.method == 'POST':
        form_details = request.form
        return render_template('details.html', details_dict=form_details)
    else:
        return render_template('registration1.html')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
