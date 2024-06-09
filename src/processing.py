from typing import Iterable


def filter_by_state(transactions: Iterable[list], state: str= "EXECUTED") -> Iterable[list]:
    """Фильтрует транзакции по состоянию"""
    return [elem for elem in transactions if elem["state"] == state]


def filter_by_date(transactions: Iterable[list], ascending: bool = True) -> Iterable[list]:
    """Фильтрует транзакции по дате"""
    return sorted(transactions, key=lambda date: date.get("date"), reverse=ascending)

