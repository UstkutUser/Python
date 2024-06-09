from masks import mask_card, mask_account


def mask_card_and_account(acc_number: str) -> str:
    """Возвращет исходную строку с замаскированным номером карты/счета"""
    pay_system = ("Visa", "Maestro", "MasterCard")
    for i in acc_number.split():
        if i in pay_system:
            card_name = " ".join([i for i in acc_number.split() if i.isalpha()])
            card_number = mask_card("".join([i for i in acc_number.split() if i.isdigit()]))
            return f"{card_name + " " + card_number}"
        elif i == "Счет":
            account = "".join([i for i in acc_number if i.isdigit()])
            return f"Счет {mask_account(account)}"


def parse_date(date_and_time: str) -> str:
    """ строку с датой в виде дд.мм.гггг"""
    date = [i for i in date_and_time.split("T")]
    return ".".join(list(reversed([i for i in date[0].split("-")])))


if __name__ == '__main__':
    print(mask_card_and_account("Visa Platinum 7000 7922 8960 6361"))
    print(mask_card_and_account("Счет 73654108430135874305"))
    print(parse_date("2018-07-11T02:26:18.671407"))