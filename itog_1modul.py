grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sorted = sorted(students)
grades_avg=[]
for i in grades:
    a=sum(i)/len(i)
    grades_avg.append(a)
dictionary = dict(zip(students_sorted,grades_avg))
print(dictionary)





