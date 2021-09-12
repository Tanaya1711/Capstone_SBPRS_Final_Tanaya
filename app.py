from flask import Flask, render_template, request, redirect, url_for, jsonify
import pickle
from model import Recommendation

recommend = Recommendation()
app = Flask(__name__)  # intitialize the flaks app  # common


@app.route('/', methods=['POST', 'GET'])
def home():
    flag = ""
    data = ""
    org_user = ""
    if request.method == 'POST':
        flag = True
        user = request.form["userid"]
        org_user = request.form["userid"]
        org_user = org_user.replace(" ", "").capitalize()
        if user == "":
            flag = ""
        else:
            user = user.replace(" ", "").lower()
            data = recommend.getTopProducts(user)
            if data == "":
                flag = False
    return render_template('index.html', data=data, flag=flag, org_user=org_user)


if __name__ == '__main__':
    app.run(debug=True)  # this command will enable the run of your flask app or api

    # ,host="0.0.0.0")