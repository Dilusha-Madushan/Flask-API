from flask import Blueprint, render_template, request, flash, jsonify
import json

prediction = Blueprint('prediction', __name__)


@prediction.route('/', methods=['GET', 'POST'])
def predict():
    res = {'status':False, 'result':-1}
    if request.method == 'POST':
        note = request.form.get('note')


    return jsonify(res)