
def pull_contacts():
    result = {}
    with open("contacts.txt", "r", encoding="UTF-8") as file:
        for line in file:
            k, v = line.strip().split(':')
            result[k] = v
    return result


def push_contact(result):
    with open('contacts.txt', 'w', encoding="UTF-8") as file:
        tmp = ''
        for k, v in result.items():
            tmp += k + ':' + v + '\n'
        file.write(tmp)


def search_contact(n, rslt):
    if n.isdigit():
        flag = True
        for k, v in rslt.items():
            if v == n or n in v:
                print(f'Телефон {v} принадлежит абоненту {k}')
                flag = False
        else:
            if flag:
                print(f'Не найдено абонента с номером {n}')
    else:
        flag = True
        for i in rslt:
            if n.lower() in i.lower():
                print(f'Абонент: {i}''\n'f'Номер телефона: {rslt[i]}')
                flag = False
        else:
            if flag:
                print(f'Нет такого абонента! {n}')


def main():
    while 1:
        result = pull_contacts()
        print("""Меню опций:
        # 1 - Посмотреть список абонентов
        # 2 - Поиск по ФИО или телефону
        # 3 - Добавить абонента
        # 4 - Удалить абонента
        # 5 - Изменить абонента
        # 6 - Выключить программу""")

        if (choice := input()) not in '123456': continue

        match choice:
            case '1': print("\nСписок абонентов: ", *result.items(), sep='\n')
            case '2': search_contact(input('Введите имя/фамилию/отчество/телефон: '), result)
            case '3':
                input_items = input('Введите "фамилию имя отчество:телефон": ').split(':')
                result[input_items[0]] = input_items[1]
                push_contact(result)
            case '4':
                del_item = input('Введите ФИО для удаления: ')
                del result[del_item]
                push_contact(result)
            case '5':
                del_items = input('Для замены введите ФИО абонента: ')
                input_items = input('Введите новые данные "фамилию имя отчество:телефон": ').split(':')
                result[input_items[0]] = input_items[1]
                del result[del_items]
                push_contact(result)
            case '6': break


if __name__ == '__main__':
    main()