def menuHello(phonebook):
    print("1.Добавить")
    print("2.Вывести всех")
    print("3.Поиск по фамилии")
    print("4.Изменить данные")
    print("5.Удалить по фамилии")
    print("6.Выход")
    userInput = int(input())
    if userInput == 1:
        phonebook.addData()
        return True
    if userInput == 2:
        phonebook.printAll()
        return True
    if userInput == 3:
        phonebook.find(input("Введите фамилию: "))
        return True
    if userInput == 4:
        phonebook.change(input("Введите имя или фамилию: "))
        return True
    if userInput == 5:
        phonebook.delete(input("Введите имя или фамилию: "))
        return True    
    if userInput == 6:
        return False