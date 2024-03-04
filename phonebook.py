class Phonebook:
    def __init__(self, data_file) -> None:
        self.data_file = data_file
        try:
            f = open(data_file, "x")
            f.close()
        except:
            pass

    def addData(self):
        data = open(self.data_file, 'a', encoding='utf-8')
        print('\n'*10) 
        first_name = input("Введите имя: ")
        second_name = input("Введите фамилию: ")
        mid_name = input("Введите отчество: ")
        number = input("Введите номер телефона: ")
        item = [first_name, second_name, mid_name, number]
        s = ' '
        data.writelines(s.join(item) + '\n')
        data.close()
        print('\n'*10)


    def delete(self, text):
        fileData = open(self.data_file, 'r', encoding='utf-8')
        data = fileData.readlines()
        fileData.close()

        fileData = open(self.data_file, 'w', encoding='utf-8')
        found = False
        for line in data:
            if line.split(' ')[1] != text and line.split(' ')[0] != text:
                fileData.write(line)
            else:
                found = True
        if found == False:
            print("Не найден")
        else:
            print("Удалено")
        print('\n')
        return

    def change(self, text):
        found = False
        data = open(self.data_file, 'r', encoding='utf-8')
        lines = data.readlines()
        data.close()
        for line in lines:
            if line.split(' ')[1] == text or line.split(' ')[0] == text:
                newline = self.changeMenu(line)
                index = lines.index(line)
                lines[index] = newline
                found = True
        if found == True:
            data = open(self.data_file, 'w+', encoding='utf-8')
            data.writelines(lines)
            print("Изменено")
        else:
            print("Не найдено")
        data.close()

    def find(self, text):
        print('\n'*10)
        data = open(self.data_file, 'r', encoding='utf-8')
        for line in data:
            if line.split(' ')[1] == text:
                print(line)
                data.close()
                return
        print("Не найден!")
        data.close()
        print('\n')

    def printAll(self):
        print('\n'*10)
        data = open(self.data_file, 'r', encoding='utf-8')
        for line in data:
            print(line)
        data.close()
        print('\n')

    def changeMenu(self, line):
        print("1.Изменить имя")
        print("2.Изменить фамилию")
        print("3.Изменить отчество")
        print("4.Изменить телефон")

        userInput = int(input())

        if userInput == 1:
            temp = input("Введите новое имя: ") + " " + \
                line.split(' ')[1] + " " + line.split(' ')[2] + \
                " " + line.split(' ')[3]
            return temp
        if userInput == 2:
            temp = line.split(' ')[0] + " " + input("Введите новую фамилию: ") + \
                " " + line.split(' ')[2] + " " + line.split(' ')[3]
            return temp
        if userInput == 3:
            temp = line.split(' ')[0] + " " + line.split(' ')[1] + " " + \
                input("Введите новое отчество: ") + " " + line.split(' ')[3]
            return temp
        if userInput == 4:
            temp = line.split(' ')[0] + " " + line.split(' ')[1] + " " + line.split(' ')[
                2] + " " + input("Введите новый номер телефона: ") + "\n"
            return temp