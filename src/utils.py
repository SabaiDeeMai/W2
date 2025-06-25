from typing import List

from src.vacancy import Vacancy


def filter_vacancies(vacancies: List[Vacancy], keywords: str) -> List[Vacancy]:
    """Фильтрация вакансий по ключевым словам"""
    if not keywords or not vacancies:
        return vacancies

    keywords_lower = keywords.lower().split()
    filtered = []

    for vacancy in vacancies:
        if not isinstance(vacancy, Vacancy):
            continue

        text = f"{vacancy.title} {vacancy.description}".lower()
        if all(keyword in text for keyword in keywords_lower):
            filtered.append(vacancy)

    return filtered


def sort_vacancies(vacancies: List[Vacancy]) -> List[Vacancy]:
    """Сортировка вакансий по зарплате (от большей к меньшей)"""
    return sorted(vacancies, key=lambda x: x.get_salary_from(), reverse=True)


def get_top_vacancies(vacancies: List[Vacancy], top_n: int) -> List[Vacancy]:
    """Возвращает топ N вакансий"""
    if top_n <= 0:
        return []
    return vacancies[:top_n]


def print_vacancies(vacancies: List[Vacancy]) -> None:
    """Вывод вакансий"""
    if not vacancies:
        print("Нет вакансий для отображения")
        return

    for i, vacancy in enumerate(vacancies, 1):
        salary = vacancy.salary or {}
        salary_str = (
            f"{salary.get('from', '?')}-{salary.get('to', '?')} {salary.get('currency', '')}"
            if salary
            else "Не указана"
        )

        print(f"{i}. {vacancy.title}")
        print(f"   Зарплата: {salary_str}")
        print(f"   Описание: {vacancy.description}")
        print(f"   Ссылка: {vacancy.url}\n")
