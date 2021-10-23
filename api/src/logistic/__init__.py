# -*- coding: utf-8 -*-

from flask import jsonify
from flask import Blueprint
from src.logistic.models import Venicle

logistic = Blueprint('logistic', __name__)


@logistic.route('/api/venicle', methods=['GET'])
def get_venicles():
    venicles = [venicle.as_dict() for venicle in Venicle.query.all()]
    return jsonify(venicles)
