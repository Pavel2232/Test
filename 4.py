from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.joinpath('test.json')

def count_questions(data: dict):
    # вывести количество вопросов (questions)
    pass


def print_right_answers(data: dict):
    # вывести все правильные ответы (correct_answer)
    pass


def print_max_answer_time(data: dict):
    # вывести максимальное время ответа (time_to_answer)
    pass


def main(args):
    data = {BASE_DIR.joinpath('test.json')} # загрузить данные из test.json файла
    count_questions(data)
    print_right_answers(data)
    print_max_answer_time(data)
#
#
if __name__ == '__main__':
    # передать имя файла из аргументов командной строки
    a = ...
    main(a)
