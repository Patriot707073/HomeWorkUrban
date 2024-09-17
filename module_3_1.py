calls = 0

def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    b= []
    b.append(len(string))
    b.append(string.upper())
    b.append(string.lower())
    return tuple(b)


def is_contains (string, list_to_search):
    count_calls()
    flag = False
    for i in list_to_search:
        if string.lower() == i.lower():
            flag = True
            break
    return flag

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)
