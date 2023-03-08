from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
from .models import Entries, Bmi
import json


views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        age = request.form.get('age')
        height = request.form.get('height')
        weight = request.form.get('weight')

        if weight == 0:
            flash('Weight is too low', category='error')
        else:
            new_bmi = Bmi(age=age, height=height, weight=weight, user_id=current_user.id)
            db.session.add(new_bmi)
            db.session.commit()
            flash('BMI calculated', category='success')
    return render_template("home.html", user=current_user)

@views.route('/entries', methods=['GET', 'POST'])
@login_required
def entries():
    if request.method == 'POST':
        entry = request.form.get('entry')

        if len(entry) < 1:
            flash('Journal entry is too short!', category='error')
        else:
            new_entry = Entries(data=entry, user_id=current_user.id)
            db.session.add(new_entry)
            db.session.commit()
            flash('Journal entry added!', category='success')
    return render_template("entries.html", user=current_user)

@views.route('/delete-entry', methods=['POST'])
def delete_entry():
    entry = json.loads(request.data)
    entryId = entry['entryId']
    entry = Entries.query.get(entryId)
    if entry:
        if entry.user_id == current_user.id:
            db.session.delete(entry)
            db.session.commit()
    return jsonify({})
