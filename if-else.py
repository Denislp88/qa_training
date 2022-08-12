
i = 4
if i == 1:
    print("Один")
elif i == 2:
    print("Два")
elif i == 3:
    print("Три")
elif i == 4:
    print("Четыре")

################################################## https://pythoninfo.ru/osnovy/if-else-python

x = 15
print(x // 7) if x % 3 >= 5 else print(x) if x % 4 < 2 else print(x * -1)

################################################# https://pythoninfo.ru/osnovy/if-else-python

стакан = 1
print("Быть") if стакан / 2 >= 0.5 else print("Не быть")

################################################ https://pythoninfo.ru/osnovy/if-else-python

глаза = "голубые"
характер = "мягкий"
if глаза == "карие":
    print('Познакомлюсь')
elif глаза == "голубые":
    if характер == "мягкий":
        print('Женюсь!')
    else:
        pass
else:
    pass

################################################ https://pythoninfo.ru/osnovy/if-else-python

x = 'коняга'
if x == 'конь':
    print('поскакали')
else:
    print('стоим')