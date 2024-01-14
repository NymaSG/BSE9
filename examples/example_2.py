if __name__ == "__main__":
    classes = {}

    while True:
        command = input("$ ").lower()

        if command == 'exit':
            break

        elif command == 'add' or command == "modified":
            name = input("Bведите название класса: ").upper()
            count_stud = int(input("Введите колличество учащихся в классе: "))
            classes[name] = count_stud

        elif command == "del":
            name = input("Введите класс, который хотите удалить: ").upper() 
            del classes [name]

        elif command == "list":
            line = '+-{}-+-{}-+-{}-+'.format('-' * 4, '-' * 10, '-' * 12)
            print(line)
            print('| {:^4} | {:^10} | {:^12} |'.format("N", "Название", "Количество")) 
            print(line)
            a = 1
            for name, count_stud in classes.items():
                print('| {:^4} | {:^10} | {:^12} |'.format(a, name, count_stud))
                a += 1
            print(line)