immutable_var = 1,2,3,"Снег", 3.5
print (immutable_var)
# immutable_var[0]=99  т.к это кортеж, элемент изменить не удалось. Кортеж - не изменяемый тип данных
# print (immutable_var)
mutable_list = [1,2,3,"Снег", 3.5]
mutable_list.append("Осень")
print (mutable_list)