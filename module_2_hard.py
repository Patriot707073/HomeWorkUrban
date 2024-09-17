def password (n):
  result = ""
  for i in range (1,n):
    for j in range (i+1,n):
      if n%(i+j) == 0:
        result = result + str(i) + str(j)
  return result
n = int(input("Введите целое число от 3 - 20\n"))
print ("Пароль : ",password(n))19