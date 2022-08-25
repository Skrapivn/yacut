import random
import string

from flask import abort, flash, redirect, render_template, url_for

from . import app, db
from .forms import URL_mapForm
from .models import URL_map


def get_unique_short_id():
    letters_and_digits = string.ascii_letters + string.digits
    output = ''.join(random.sample(letters_and_digits, 6))
    return output

#  <a href="{{ url_for('index_view', id=custom_id.id) }}">{{ url_for('index_view', id=custom_id.id, _external=True) }}</a>

@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URL_mapForm()
    if form.validate_on_submit():
        custom_id = form.custom_id.data
        if custom_id is None:
            new_url = get_unique_short_id()
            url_map = URL_map(
                original=form.original_link.data,
                short=url_for(new_url),
            )
        if URL_map.query.filter_by(short=custom_id).first():
            flash('Такая ссылка уже существует в базе!')
            return render_template('index.html', form=form)
        url_map = URL_map(
            original=form.original_link.data,
            short=form.custom_id.data,
        )
        db.session.add(url_map)
        db.session.commit()
        flash(f'Ваша новая ссылка готова {custom_id}')
        # return redirect(url_for('opinion_view', id=url_map.id))
    return render_template('index.html', form=form)
