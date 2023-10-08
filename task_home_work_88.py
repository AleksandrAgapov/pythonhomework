from os.path import exists
from csv import DictReader, DictWriter



def get_info():
    info = []
    first_name = input('введите фамилию:      ')
    last_name = input('введите имя:    ')
    info.append(first_name)
    info.append(last_name)
    flag = False
    while not flag:
        try:
            phone_number =  int(input('Введите номер телефона:    '))
            if len(str(phone_number)) != 11:
                print('wrong number')
            else:
                flag = True
        except ValueError:
            print('not valid number')
    info.append(phone_number)
    return info

def create_file():
    with open('phone_2.csv', 'w', encoding='utf-8') as data:
        # data.write('Фамилия;Имя;Номер\n')
        f_n_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()

def write_file(lst):
    with open('phone_2.csv', 'r', encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        res = list(f_n_reader)
    with open('phone_2.csv', 'w', encoding='utf-8') as f_n:
        obj = {'Фамилия': lst[0], 'Имя': lst[1], 'Номер': lst[2]}
        res.append(obj)
        f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()
        for el in res:
            f_n_writer.writerow(el)

def read_file(file_name):
    # with open(file_name, encoding='utf-8') as data:
    #     phone_book = data.readlines()
    with open(file_name, encoding='utf-8') as f_n:
        f_n_reader = DictReader(f_n)
        phone_book = list(f_n_reader)
    return phone_book


def record_info():
    lst = get_info()
    write_file(lst)


def update_data(file_name, old_name, new_data):
    data = read_file(file_name)
    for entry in data:
        if entry['Имя'] == old_name or entry['Фамилия'] == old_name:
            entry.update(new_data)
    with open(file_name, mode='w', encoding='utf-8', newline="") as data_file:
        f_writer = DictWriter(data_file, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()
        f_writer.writerows(data)


def delete_data(file_name, name):
    data = read_file(file_name)
    updated_data = [entry for entry in data if entry['Имя'] != name and entry['Фамилия'] != name]
    with open(file_name, mode='w', encoding='utf-8', newline="") as data_file:
        f_writer = DictWriter(data_file, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()
        f_writer.writerows(updated_data)

def main():
    while True:
        command = input(' r - чтение, w - запись, u - обновление, d - удаление, q - выход')
        if command == 'q':
            break
        elif command == 'r':
            if not exists('phone_2.csv'):
                print('Файл не создан')
                break
            print(*read_file('phone_2.csv'))
        elif command == 'w':
            if not exists('phone_2.csv'):
                create_file()
                record_info()
            else:
                record_info()
        elif command == "u":
                name_to_update = input('Введите имя или фамилию для обновления: ')
                new_name = input('Введите новое имя: ')
                new_surname = input('Введите новую фамилию: ')
                new_number = input('Введите новый номер: ') 
                if new_name and new_surname and new_number:
                  new_data = {"Фамилия": new_surname, "Имя": new_name, "Номер": new_number}
                  update_data("phone_2.csv", name_to_update, new_data)
                  print("Данные обновлены.")
                else:
                    print("Неверный ввод. Попробуйте снова.") 
        elif command == "d":
                    
                      name_to_delete = input('Введите имя или фамилию для удаления: ')
                      delete_data("phone_2.csv", name_to_delete)
                      print("Данные удалены.")
        else:
                  print("Неверная команда. Попробуйте снова.") 

main()   

