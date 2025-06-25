import pytest

from src.utils import filter_vacancies, get_top_vacancies, sort_vacancies
from src.vacancy import Vacancy


@pytest.fixture
def sample_vacancies():
    return [
        Vacancy("Python Developer", "url1", {"from": 100}, "Python experience"),
        Vacancy("Java Developer", "url2", {"from": 200}, "Java experience"),
        Vacancy("DevOps", "url3", {"from": 150}, "Docker experience"),
    ]


def test_filter_vacancies(sample_vacancies):
    """Тест фильтрации по ключевым словам"""
    filtered = filter_vacancies(sample_vacancies, "Python")
    assert len(filtered) == 1
    assert filtered[0].title == "Python Developer"


def test_sort_vacancies(sample_vacancies):
    """Тест сортировки вакансий"""
    sorted_vac = sort_vacancies(sample_vacancies)
    assert [v.title for v in sorted_vac] == [
        "Java Developer",
        "DevOps",
        "Python Developer",
    ]


def test_get_top_vacancies(sample_vacancies):
    """Тест получения топ-N вакансий"""
    sorted_vac = sort_vacancies(sample_vacancies)
    top = get_top_vacancies(sorted_vac, 2)
    assert len(top) == 2
    assert top[0].title == "Java Developer"
    assert top[1].title == "DevOps"


def test_get_top_more_than_exist(sample_vacancies):
    """Тест запроса больше вакансий чем есть"""
    top = get_top_vacancies(sample_vacancies, 10)
    assert len(top) == 3


def test_get_top_zero(sample_vacancies):
    """Тест запроса 0 вакансий"""
    top = get_top_vacancies(sample_vacancies, 0)
    assert len(top) == 0


def test_get_top_negative(sample_vacancies):
    """Тест отрицательного числа вакансий"""
    top = get_top_vacancies(sample_vacancies, -1)
    assert len(top) == 0
