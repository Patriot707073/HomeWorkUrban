team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2
challenge_result = 'Победа команды Волшебники данных!'



print("В команде Мастера кода участников: %(team1_num)s! "% {'team1_num' :5}) # использование %
print("Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s! "% {'team1_num' :5,'team2_num' :6 }) # использование %

print ("Команда Волшебники данных решила задач: {score_2}!".format(score_2 = 42)) # использование format
print("Волшебники данных решили задачи за {team1_time} c".format(team1_time = 18015.2)) # использование format

print (f"Команды решили {score_1} и {score_2} задач") # использование f-строк

print (f"Результат битвы: {challenge_result}") # использование f-строк

print (f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!.")
