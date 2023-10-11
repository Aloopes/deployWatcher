import pytest
from datetime import datetime
from deployWatcher.Models.TransitionsModel import TransitionModel


def test_app_initialization(client):
    assert client.get("/transitions").status_code == 200


def test_app_post_response(client, session):
    payload = {'component': 'testApp', 'version': 1.0, 'author': 'automata7', 'status': 'started',
               'sent_timestamp': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')}
    response = client.post('/transitions', data=payload)
    assert response.status_code == 200


def test_basic_db_insert(session):
    payload = {'component': 'testApp', 'version': 1.0, 'author': 'automata7', 'status': 'started',
               'sent_timestamp': datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S.%f')}

    test_transition = TransitionModel(**payload)

    session.add(test_transition)
    session.commit()

    assert test_transition.id > 0
