first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [first_str for first_str in first_strings if len(first_str)>=5]
second_result = [(first_str, second_str) for first_str in first_strings for second_str in second_strings if len(first_str) == len(second_str)]
first_and_second  = first_strings + second_strings
third_result = {fas:len(fas) for fas in first_and_second if len(fas)%2 == False}

print (first_result)
print (second_result)
print(third_result)