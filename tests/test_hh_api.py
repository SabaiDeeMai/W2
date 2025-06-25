from unittest.mock import MagicMock, patch

from src.hh_api import HHAPI
from src.vacancy import Vacancy


@patch("requests.get")
def test_load_vacancies_success(mock_get):
    """Тест успешной загрузки вакансий"""
    mock_response = MagicMock()
    mock_response.json.return_value = {
        "items": [
            {
                "name": "Python Developer",
                "alternate_url": "https://hh.ru/vacancy/123",
                "salary": {"from": 100000},
                "snippet": {"requirement": "Python experience"},
            }
        ]
    }
    mock_response.status_code = 200
    mock_get.return_value = mock_response

    hh_api = HHAPI()
    vacancies = hh_api.load_vacancies("Python")

    assert len(vacancies) == 1
    assert isinstance(vacancies[0], Vacancy)
    assert vacancies[0].title == "Python Developer"


@patch("requests.get")
def test_load_vacancies_failure(mock_get):
    """Тест обработки ошибки API"""
    # Настраиваем mock для вызова исключения
    mock_get.side_effect = Exception("API error")

    hh_api = HHAPI()
    vacancies = hh_api.load_vacancies("Python")

    # Проверяем, что при ошибке возвращается пустой список
    assert vacancies == []
