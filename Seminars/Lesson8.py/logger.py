from data_create import name_data, surname_data, phone_data, address_data

def input_data():
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address}\n\n"
    f"2 Вариант: \n"
    f"{name}; {surname}; {phone}; {address}\n"
    f"Выберите вариант: "))
    
    while var != 1 and var !=2:
        print("Неправильный ввод ")
        var = int(input("Введите число "))
    if var == 1:
        with open("data_first_variant.csv", "a", encoding="utf-8") as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")
    elif var == 2:
        with open("data_second_variant.csv", "a", encoding="utf-8") as f:
            f.write(f"{name}\n{surname}\n{phone}\n{address}\n\n")


def print_data():
    print("Вывожу данные из 1 файла: \n")
    with open("data_first_variant.csv", "r", encoding="utf-8") as f:
        data_first = f.readlines()
        data_first_list = []
        j = 0
        for i in range (len(data_first)):
            if data_first[i] == "\n" or i == len(data_first) - 1:
                data_first_list.append(" ".join(data_first[j:i+1]))
                j = 1
        print("". join(data_first_list))   
        
    print("Вывожу данные из 2 файла: \n")
    with open("data_second_variant.csv", "r", encoding="utf-8") as f:
        data_second = f.readlines()
        print(*data_second)
        
        
def is_menu():
    while True:
        print("\n Меню ")
        print("1. Изменить существующую запись. ")
        print("2. Удалить запись. ")
        n = checking_the_number(input("Выберите пункт меню: "))
        
        if n == 1:
            lg.logging.info('The user has selected item number 6')
            print('1. Найти номер по фамилии.')
            print('2. Найти номер по имени.')
            print('3. Поиск по номеру телефона.')
            change = сhecking_the_number(input('Введите номер пункта: '))

            if change == 1:
                lg.logging.info('The user has selected item number 6.1')
                search = input('Введите фамилию: ')
                lg.logging.info('User entered: {search}')
                cr.retrive(surname=search)
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                new_number = input('Введите новый номер телефона: ')
                lg.logging.info('User entered: {new_number}')
                cr.update(id=user_id, new_number=new_number)

            elif change == 2:
                lg.logging.info('The user has selected item number 6.2')
                search = input('Введите имя: ')
                lg.logging.info('User entered: {search}')
                cr.retrive(name=search)
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                new_number = input('Введите новый номер телефона: ')
                lg.logging.info('User entered: {new_number}')
                cr.update(id=user_id, new_number=new_number)

            elif change == 3:
                lg.logging.info('The user has selected item number 6.3')
                search = input('Введите номер телефона: ')
                lg.logging.info('User entered: {search}')
                cr.retrive(number=search)
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                new_number = input('Введите новый номер телефона: ')
                lg.logging.info('User entered: {new_number}')
                cr.update(id=user_id, new_number=new_number)

            else:
                lg.logging.info('User entered an invalid menu value')
                print(
                    '\n Такого пункта меню не существует.\n Введите цифру, соответствующую пункту меню.')

        elif n == 2:
            lg.logging.info('The user has selected item number 7')
            print('1. Найти номер по фамилии.')
            print('2. Найти номер по имени.')
            print('3. Поиск по номеру телефона.')
            deleting = сhecking_the_number(input('Введите номер пункта: '))

            if deleting == 1:
                lg.logging.info('The user has selected item number 7.1')
                search = input('Введите фамилию: ')
                lg.logging.info('User entered: {search}')
                print(cr.retrive(surname=search))
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                cr.delete(id=user_id)

            elif deleting == 2:
                lg.logging.info('The user has selected item number 7.2')
                search = input('Введите имя: ')
                lg.logging.info('User entered: {search}')
                print(cr.retrive(name=search))
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                cr.delete(id=user_id)

            elif deleting == 3:
                lg.logging.info('The user has selected item number 7.3')
                search = input('Введите номер телефона: ')
                lg.logging.info('User entered: {search}')
                print(cr.retrive(number=search))
                user_id = input('Введите id записи: ')
                lg.logging.info('User entered: {user_id}')
                new_number = input('Введите новый номер телефона: ')
                cr.delete(id=user_id)

            else:
                lg.logging.info('User entered an invalid menu value')
                print(
                    '\n Такого пункта меню не существует.\n Введите цифру, соответствующую пункту меню.')
        

print_data()