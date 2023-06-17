def load_phonebook():
    phonebook = []
    try:
        with open('phonebook.txt', 'r') as file:
            for line in file:
                surname, name, patronymic, phone = line.strip().split(',')
                contact = {'surname': surname, 'name': name,
                           'patronymic': patronymic, 'phone': phone}
                phonebook.append(contact)
    except FileNotFoundError:
        pass
    return phonebook


def save_phonebook(phonebook):
    with open('phonebook.txt', 'w') as file:
        for contact in phonebook:
            line = f"{contact['surname']},{contact['name']},{contact['patronymic']},{contact['phone']}\n"
            file.write(line)


def add_contact(phonebook):
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone = input("Введите номер телефона: ")
    contact = {'surname': surname, 'name': name,
               'patronymic': patronymic, 'phone': phone}
    phonebook.append(contact)
    print("Контакт добавлен.")


def find_contact(phonebook):
    key = input("Введите фамилию или имя для поиска: ")
    found_contacts = []
    for contact in phonebook:
        if key.lower() in contact['surname'].lower() or key.lower() in contact['name'].lower():
            found_contacts.append(contact)
    if found_contacts:
        print("Найденные контакты:")
        for contact in found_contacts:
            print_contact(contact)
    else:
        print("Контакты не найдены.")


def print_contact(contact):
    print(f"Фамилия: {contact['surname']}")
    print(f"Имя: {contact['name']}")
    print(f"Отчество: {contact['patronymic']}")
    print(f"Номер телефона: {contact['phone']}")
    print()


def edit_contact(phonebook):
    key = input("Введите фамилию или имя контакта, который хотите изменить: ")
    found_contacts = []
    for contact in phonebook:
        if key.lower() in contact['surname'].lower() or key.lower() in contact['name'].lower():
            found_contacts.append(contact)
    if found_contacts:
        print("Найденные контакты:")
        for i, contact in enumerate(found_contacts):
            print(f"{i+1}.")
            print_contact(contact)
        choice = int(
            input("Введите номер контакта, который хотите изменить: "))
        if 1 <= choice <= len(found_contacts):
            contact = found_contacts[choice - 1]
            new_surname = input(
                "Введите новую фамилию (оставьте пустым для сохранения текущего значения): ")
            if new_surname:
                contact['surname'] = new_surname
            new_name = input(
                "Введите новое имя (оставьте пустым для сохранения текущего значения): ")
            if new_name:
                contact['name'] = new_name
            new_patronymic = input(
                "Введите новое отчество (оставьте пустым для сохранения текущего значения): ")
            if new_patronymic:
                contact['patronymic'] = new_patronymic
            new_phone = input(
                "Введите новый номер телефона (оставьте пустым для сохранения текущего значения): ")
            if new_phone:
                contact['phone'] = new_phone
            print("Контакт изменен.")
        else:
            print("Неправильный выбор.")
    else:
        print("Контакты не найдены.")


def delete_contact(phonebook):
    key = input("Введите фамилию или имя контакта, который хотите удалить: ")
    found_contacts = []
    for contact in phonebook:
        if key.lower() in contact['surname'].lower() or key.lower() in contact['name'].lower():
            found_contacts.append(contact)
    if found_contacts:
        print("Найденные контакты:")
        for i, contact in enumerate(found_contacts):
            print(f"{i+1}.")
            print_contact(contact)
        choice = int(input("Введите номер контакта, который хотите удалить: "))
        if 1 <= choice <= len(found_contacts):
            contact = found_contacts[choice - 1]
            phonebook.remove(contact)
            print("Контакт удален.")
        else:
            print("Неправильный выбор.")
    else:
        print("Контакты не найдены.")


def main():
    phonebook = load_phonebook()
    while True:
        print("Телефонный справочник")
        print("1. Вывести все контакты")
        print("2. Добавить контакт")
        print("3. Поиск контакта")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("6. Выйти")
        choice = input("Выберите действие: ")
        if choice == '1':
            if phonebook:
                print("Все контакты:")
                for contact in phonebook:
                    print_contact(contact)
            else:
                print("Справочник пуст.")
        elif choice == '2':
            add_contact(phonebook)
        elif choice == '3':
            find_contact(phonebook)
        elif choice == '4':
            edit_contact(phonebook)
        elif choice == '5':
            delete_contact(phonebook)
        elif choice == '6':
            save_phonebook(phonebook)
            break
        else:
            print("Неправильный выбор.")


if __name__ == '__main__':
    main()
