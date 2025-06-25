from src.hh_api import HHAPI
from src.json_saver_vacancy import JSONSaver
from src.utils import filter_vacancies, sort_vacancies, get_top_vacancies, print_vacancies


def user_interaction():
    hh_api = HHAPI()
    storage = JSONSaver()

    query = input("Введите поисковый запрос: ")
    vacancies = hh_api.load_vacancies(query)

    if not vacancies:
        print("По вашему запросу вакансий не найдено.")
        return

    storage.save_vacancies(vacancies)
    print(f"Найдено {len(vacancies)} вакансий")

    try:
        top_n = int(input("Введите количество вакансий для вывода в топ: "))
        if top_n <= 0:
            raise ValueError
    except ValueError:
        print("Ошибка: введите положительное число")
        return

    keyword = input("Введите ключевое слово для фильтрации (или Enter чтобы пропустить): ")
    filtered = filter_vacancies(vacancies, keyword) if keyword else vacancies

    sorted_vacancies = sort_vacancies(filtered)
    top_vacancies = get_top_vacancies(sorted_vacancies, top_n)

    print("\nРезультаты поиска:")
    print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()
