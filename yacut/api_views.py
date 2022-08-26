from re import match

from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URL_map
from .views import get_unique_short_id


@app.route('/api/id/', methods=['POST'])
def create_id():
    data = request.get_json()
    if not data:
        raise InvalidAPIUsage('Отсутствует тело запроса', 400)
    if 'url' not in data:
        raise InvalidAPIUsage('"url" является обязательным полем!', 400)
    if not match(
            r'^(?P<url>[a-z]+://[^\/\?:]+)(?P<port>:[0-9]+)?(?P<end>\/.*?)?$',
            data['url']):
        raise InvalidAPIUsage('Недопустимый короткий идентификатор', 400)
    if not data.get('custom_id'):
        data['custom_id'] = get_unique_short_id()
    if not match(
            r'^[A-Za-z0-9]{1,16}$', data['custom_id']):
        raise InvalidAPIUsage(
            'Указано недопустимое имя для короткой ссылки', 400)
    if URL_map.query.filter_by(short=data['custom_id']).first():
        raise InvalidAPIUsage(f'Имя "{data["custom_id"]}" уже занято.', 400)

    url_map = URL_map()
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(url_map.to_dict()), 201


@app.route('/api/id/<string:short_id>/')
def get_url(short_id):
    url_map = URL_map.query.filter_by(short=short_id).first()
    if not url_map:
        raise InvalidAPIUsage(
            'Указанный id не найден', 404)
    return jsonify({'url': url_map.original})
