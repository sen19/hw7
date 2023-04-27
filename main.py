import utils

print("Здравствуйте! Предлагаю сегодня сыграть в 'Свою игру'")
print("Введите подходящую категорию и стоимость вопроса\n")
questions = utils.load_questions()
points, correct, incorrect = 0, 0, 0
questions_asked = 0
questions_total = utils.get_number_of_questions(questions)
while correct + incorrect < questions_total:
    utils.show_table(questions)
    user_input = input().title()
    user_data = utils.price_input(user_input)
    if not user_data:
        print("Нет такой категории или вопроса")
        continue
    category, price = user_data["category"], user_data["price"]
    question = questions[category][price]
    if question["asked"]:
        print("Ты уже это спрашивал )")
        continue
    utils.print_question(question["question"])
    user_answer = input().lower()
    if user_answer != question["answer"]:
        print("Ответ неверный")
        points -= int(price)
        incorrect += 1
    else:
        print("Ответ верный")
        points += int(price)
        correct += 1
    question["asked"] = True
    questions_asked += 1

utils.show_stats(points, correct, incorrect)
utils.save_results_to_file(points, correct, incorrect)
