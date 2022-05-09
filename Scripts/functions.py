from datetime import datetime
import requests


def import_api_exchange_items():
    """
    importa datos desde la API de Stack Exchange
    :return: regresa la información que se encuentra en la llave items
    """
    # Importando Datos
    url = 'https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow'
    response = requests.get(url)
    data = response.json()
    # Contenido de items
    content = data['items']
    return content


def answers(content):
    """
    Examina cuantas preguntas estan contestadas y cuantas no lo estan
    :param content: datos de la API en structura de diccionario
    :return: answered: total de respuestas contestadas
            not_answered: total de respuestas NO contestadas
    """
    answered = 0
    not_answered = 0
    for entry in content:
        if entry['is_answered']:
            answered += 1
        else:
            not_answered += 1
    return answered, not_answered


def less_viewed(content):
    """
    Regresa datos de la respuesta con menores vistas
    :param content: datos de la API en structura de diccionario
    :return: user_id: id de usuario
        vmin: numero de vistas
        name: nombre de usuario
        vlink: link de perfil
    """
    vmin = 999999999999999
    for entry in content:
        if vmin > entry['view_count']:
            name = entry['owner']['display_name']
            user_id = entry['owner']['user_id']
            vlink = entry['owner']['link']
            vmin = entry['view_count']
    return user_id, vmin, name, vlink


def new_old_answer(content):
    """
    Regresa la fecha y el link de la respuesta más actual y más antigua
    :param content: datos de la API en structura de diccionario
    :return: max_date: fecha de respuesta más actual
            link_max: link de respuesta
            min_date: fecha de respuesta más antigua
            link_min: link de respuesta
    """
    max_date = datetime(1970, 1, 1, 0, 0, 0)
    for entry in content:
        creation = datetime.fromtimestamp(entry['creation_date'])
        if max_date < creation:
            link_max = entry['link']
            max_date = creation

    min_date = datetime.now()
    for entry in content:
        creation = datetime.fromtimestamp(entry['creation_date'])
        if min_date > creation:
            link_min = entry['link']
            min_date = creation
    return max_date, link_max, min_date, link_min


def best_rep(content):
    """
    Regresa los datos del owner con mejor reputación
    :param content: datos de la API en structura de diccionario
    :return: user_id, max_rep, answer
    """
    max_rep = -1
    for entry in content:
        if entry['owner']['user_type'] != 'does_not_exist':
            if max_rep < entry['owner']['reputation']:
                max_rep = entry['owner']['reputation']
                user_id = entry['owner']['user_id']
                answer = entry['link']
    return user_id, max_rep, answer