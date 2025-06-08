from datetime import datetime
from typing import Dict, List


def filter_by_state(list_of_dict: List[Dict[str, str]], state: str = 'EXECUTED') -> List[Dict[str, str]]:
    """принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED').
    Функция возвращает новый список словарей, содержащий только те словари, у которых ключ state
    соответствует указанному значению"""
    filtered_list = []
    for dict in list_of_dict:
        for key, value in dict.items():
            if dict.get('state') == state:
                filtered_list.append(dict)
            else:
                continue
    return filtered_list


def sort_by_date(list_of_dict: List[Dict[str, str]], reverse: bool = True) -> List[Dict[str, str]]:
    """Сортирует список словарей по полю 'date' (дате)."""
    sorted_list_of_dict = sorted(list_of_dict, key=lambda x: datetime.fromisoformat(x['date']), reverse=reverse)
    return sorted_list_of_dict
