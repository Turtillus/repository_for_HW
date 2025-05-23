from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(account_card_number: str) -> str:
    """принимает на вход тип и номер карты или счета и возвращает их маску"""
    index_first_digit = next (i for i, char in enumerate(account_card_number) if char.isdigit())
    digit_counter = 0
    for i in account_card_number:
        if i.isdigit():
            digit_counter += 1
    if digit_counter == 16:
        mask_card_number = get_mask_card_number(account_card_number[index_first_digit:])
        return (f"{account_card_number[:index_first_digit-1]} {mask_card_number}")
    elif digit_counter == 20:
        mask_account_number = get_mask_account(account_card_number[index_first_digit:])
        return f"{account_card_number[:index_first_digit-1]} **{mask_account_number}"
    else:
        print("Проверьте правильность ввода")


mask_number = mask_account_card('Maestro 1596837868705199')
print(mask_number)


def get_date(date: str) -> str:
    """меняет тип записи даты"""
    return f"{date[8:10]}.{date[5:7]}.{date[:4]}"


date_test = get_date("2024-03-11T02:26:18.671407")
print (date_test)