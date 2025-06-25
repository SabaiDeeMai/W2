from unittest.mock import patch

from main import user_interaction
from src.vacancy import Vacancy


@patch("builtins.input", side_effect=["Python", "2", ""])
@patch("src.hh_api.HHAPI.load_vacancies")
@patch("src.json_saver_vacancy.JSONSaver.save_vacancies")
def test_user_interaction(mock_save, mock_load, mock_input, capsys):
    """Интеграционный тест основного сценария"""
    mock_vacancies = [
        Vacancy("Python", "url1", {"from": 100}, "Python"),
        Vacancy("Java", "url2", {"from": 200}, "Java"),
    ]
    mock_load.return_value = mock_vacancies

    user_interaction()

    captured = capsys.readouterr()
    assert "Python" in captured.out
    assert "Java" in captured.out
    mock_save.assert_called_once()
