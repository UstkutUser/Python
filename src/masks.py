def mask_card(account_number: str) -> str:
    """
    Функция максирует номер карты
    """
    pay_system = ("Visa", "Maestro", "MasterCard")
    for i in account_number.split():
        if i in pay_system:
            card_name = " ".join([i for i in account_number.split() if i.isalpha()])
    masked_number = account_number[:6] + len(account_number[6:-4]) * "*" + account_number[-4:]

    return card_name
    # return " ".join([masked_number[i : i + 4] for i in range(0, len(account_number), len(account_number) // 4)])


def mask_account(bank_aсcount: str) -> str:
    """
    Функция возвращает маску счета
    """
    return "*" * 2 + bank_aсcount[-4:]


if __name__ == "__main__":
    # print(mask_card("1234567891234356"))
    print(mask_card("Visa Platinum 7000 7922 8960 6361"))
    print(mask_account("73654108430135874305"))
