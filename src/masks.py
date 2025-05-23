from typing import Union


def get_mask_card_number(card_number: Union[int, str]) -> str:
    """принимает на вход номер карты и возвращает ее маску"""
    card_number = str(card_number)
    return f"{card_number[:4]} {card_number[4:6]}** **** {card_number[-4:]}"


mask_card_number = get_mask_card_number(7000792289606361)
print(mask_card_number)


def get_mask_account(account_number: Union[int, str]) -> str:
    """принимает на вход номер счета и возвращает его маску"""
    account_number = str(account_number)
    account_number = account_number.replace(" ", "")
    account_number_mask = str(account_number[-4:])
    return f"**{account_number_mask}"


print(get_mask_account(73654108430135874305))
