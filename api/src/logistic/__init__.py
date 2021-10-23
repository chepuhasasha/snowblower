# -*- coding: utf-8 -*-

from datetime import datetime
from flask import jsonify
from sqlalchemy.orm import joinedload, lazyload, subqueryload
from flask import Blueprint
from src.logistic.models import Route, Venicle, Task
from src import db

logistic = Blueprint('logistic', __name__)


@logistic.route('/api/venicle', methods=['GET'])
def get_venicles():
    venicles = [venicle.as_dict() for venicle in Venicle.query.all()]
    return jsonify(venicles)


@logistic.route('/api/task', methods=['GET'])
def get_tasks():

    data = Task.query.all()

    result = []

    for task in data:
        json_task = task.as_dict()
        json_task['routes'] = []
        for route in task.routes:
            json_task['routes'].append(route.as_dict())

        result.append(json_task)

    return jsonify(result)
