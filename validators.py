# -*- coding: utf-8 -*-

from utils import get_diff_days

def validate_diff_days(date_from, date_to):
    response = {
        'status': False
    }

    diff_days = get_diff_days(date_from, date_to)
    if diff_days > 7:
        response['response'] = "Ambas as datas nao podem ter uma diferenca maior que 7 dias em relacao a data atual."
    elif diff_days < 0:
        response['response'] = "A data atual nao pode ser maior em relacao a ultima data."
    else:
        response['status'] = True

    return response