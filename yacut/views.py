import random
import string

from flask import flash, redirect, render_template, url_for

from . import app, db
from .forms import URL_mapForm
from .models import URL_map


def get_unique_short_id():
    letters_and_digits = string.ascii_letters + string.digits
    while True:
        output = ''.join(random.sample(letters_and_digits, 6))
        if not URL_map.query.filter_by(short=output).first():
            return output


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URL_mapForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data or get_unique_short_id()
        url_map = URL_map(
            original=form.original_link.data,
            short=custom_id,
        )
        db.session.add(url_map)
        db.session.commit()
        flash(url_for('yacut_view', short=custom_id, _external=True))
    return render_template('index.html', form=form)


@app.route('/<string:short>')
def yacut_view(short):
    return redirect(
        URL_map.query.filter_by(short=short).first_or_404().original)
