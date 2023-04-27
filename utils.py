import json

price_list = ["100", "200", "300"]


def load_questions():
    with open("questions.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def show_table(questions):
    for category_name, category_questions in questions.items():
        print(category_name.ljust(17), end="")
        for price, question_data in category_questions.items():
            asked = question_data["asked"]
            if not asked:
                print(price.center(5), end=" ")
            else:
                print("   ".center(5), end=" ")
        print()


def price_input(user_input):
    user_data = user_input.split(' ')
    if len(user_data) != 2:
        return False
    elif not user_data[0].isalpha():
        return False
    elif not user_data[1].isdigit():
        return False
    elif not user_data[0] in load_questions():
        return False
    elif user_data[1] not in price_list:
        return False
    return {'category': user_data[0], "price": user_data[1]}


def print_question(question_text):
    print(f"Слово {question_text} в переводе означает ...")


def show_stats(points, correct, incorrect):
    print("У нас закончились вопросы!")
    print("")
    print(f"Ваш счёт: {points}")
    print(f"Верных ответов: {correct}")
    print(f"Неверных ответов: {incorrect}")


def save_results_to_file(points, correct, incorrect):
    with open("results.json", 'r') as file:
        results = json.load(file)
    results.append({"points": points, "correct": correct, "incorrect": incorrect})
    with open("results.json", "w") as file:
        json.dump(results, file)


def get_number_of_questions(questions):
    counter = 0
    for cat_questions in questions.values():
        counter += len(cat_questions)
    return counter
