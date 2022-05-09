from datetime import datetime
import pytest
from Scripts.functions import answers, less_viewed, new_old_answer, best_rep


@pytest.fixture
def input_content():
    content = [{'view_count': 2, 'is_answered': True,
                'owner': {'reputation': 1, 'display_name': 'name_12', 'user_id': '12', 'link':
                    'www.link_12.com', 'user_type': 'registered'}, 'creation_date': 1609467264,
                'link': 'www.link_12.com'},

               {'view_count': 1, 'is_answered': False,
                'owner': {'reputation': 2, 'display_name': 'name_34', 'user_id': '34', 'link':
                    'www.link_34.com', 'user_type': 'registered'}, 'creation_date': 1262312064,
                'link': 'www.link_34.com'},

               {'view_count': 0, 'is_answered': False,
                'owner': {'reputation': 5, 'display_name': 'name_56', 'user_id': '56', 'link':
                    'www.link_56.com', 'user_type': 'registered'}, 'creation_date': 1577844864,
                'link': 'www.link_56.com'},

               {'view_count': 3, 'is_answered': True,
                'owner': {'reputation': 3, 'display_name': 'name_78', 'user_id': '78', 'link':
                    'www.link_78.com', 'user_type': 'registered'}, 'creation_date': 1577844865,
                'link': 'www.link_78.com'},

               {'view_count': 4, 'is_answered': True,
                'owner': {'reputation': 2, 'display_name': 'name_91', 'user_id': '91', 'link':
                    'www.link_91.com', 'user_type': 'registered'}, 'creation_date': 1577844866,
                'link': 'www.link_91.com'}]
    return content


def test_answers(input_content):
    expected_answer = 3
    expected_no_answer = 2
    contestadas, no_contestadas = answers(input_content)

    assert (expected_answer, expected_no_answer) == (contestadas, no_contestadas)


def test_less_viewed(input_content):
    expected_user_id = '56'
    expected_vmin = 0
    expected_name = 'name_56'
    expected_vlink = 'www.link_56.com'
    user_id, vmin, name, vlink = less_viewed(input_content)

    assert (expected_user_id, expected_vmin, expected_name, expected_vlink) == (user_id, vmin, name, vlink)


def test_new_old_answer(input_content):
    expected_freciente = datetime(2020, 12, 31, 20, 14, 24)
    expected_link_actual = 'www.link_12.com'
    expected_fantigua = datetime(2009, 12, 31, 20, 14, 24)
    expected_link_antigua = 'www.link_34.com'
    f_reciente, link_actual, f_antigua, link_antigua = new_old_answer(input_content)

    assert (expected_freciente, expected_link_actual, expected_fantigua, expected_link_antigua) \
           == (f_reciente, link_actual, f_antigua, link_antigua)


def test_best_rep(input_content):
    expected_id_usuario = '56'
    expected_reputacion_max = 5
    expected_respuesta = 'www.link_56.com'
    id_usuario, reputacion_max, respuesta = best_rep(input_content)

    assert (expected_id_usuario, expected_reputacion_max, expected_respuesta) \
           == (id_usuario, reputacion_max, respuesta)
