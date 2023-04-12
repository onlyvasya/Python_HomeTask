def add_person():
    last_name = input('Введите фамилию: ')  
    name = input('Введите имя: ')           
    surname = input('Введите отчество: ')   
    phone = input('Введите номер телефона: ') 
    data = open('C:\\Users\\952987653211\\Desktop\\Python\\HomeTask\\HomeTask8\\Files\\phonebook.txt','a', encoding='utf-8')
    data.writelines([last_name,' ',  name, ' ',  surname, ' ', phone, '\n']) 
    data.close()
def print_data():
    with open('C:\\Users\\952987653211\\Desktop\\Python\\HomeTask\\HomeTask8\\Files\\phonebook.txt','r', encoding='utf-8') as data:
        print(data.read())
def search():
    search_name = input('Введите данные: ')
    with open('C:\\Users\\952987653211\\Desktop\\Python\\HomeTask\\HomeTask8\\Files\\phonebook.txt','r', encoding='utf-8') as data:
        for line in data:
            if search_name in line:
                print(line)
def load_data():
    with open('C:\\Users\\952987653211\\Desktop\\Python\\HomeTask\\HomeTask8\\Files\\phonebook.txt','r+', encoding='utf-8') as data:
        text_data = data.read().splitlines()
        path = input('Введите адрес файла: ')
        with open(path, 'r', encoding='utf-8') as data_2:
            for line in data_2:
                if line[:-1] not in  text_data:
                    data.write(line)
def del_data():
    data_to_del = input("Введите данные контакта для удаления: ")
    with open('C:\\Users\\952987653211\\Desktop\\Python\\HomeTask\\HomeTask8\\Files\\phonebook.txt', 'r',encoding='utf-8') as data:
        d = data.readlines()
        for i in range(len(d)):
            if data_to_del in d[i]:
                del d[i]
    with open('C:\\Users\\952987653211\\Desktop\\Python\\HomeTask\\HomeTask8\\Files\\phonebook.txt', 'w',encoding='utf-8') as data:
        for line in d:
            data.write(line) 
def change_data():
    data_to_change = input("Введите данные контакта для изменения: ")
    last_name = input('Введите новую фамилию: ')  
    name = input('Введите новое имя: ')           
    surname = input('Введите новое отчество: ')   
    phone = input('Введите новый номер телефона: ')
    with open('C:\\Users\\952987653211\\Desktop\\Python\\HomeTask\\HomeTask8\\Files\\phonebook.txt', 'r', encoding='utf-8') as data:
        d = data.readlines()
        for i in range(len(d)):
            if data_to_change in d[i]:
                d[i] = last_name + ' ' + name + ' ' + surname + ' ' + phone
    with open('C:\\Users\\952987653211\\Desktop\\Python\\HomeTask\\HomeTask8\\Files\\phonebook.txt', 'w', encoding='utf-8') as data:
        for line in d:
            data.write(line)            






def ui():
    print('''1 - добавить контакт
2 - поиск
3 - импорт данных
4 - вывод в консоль
5 - удаление контакта
6 - изменение контакта''')
    user_input = input('Введите нужный вариант: ')
    if user_input == '1':
        add_person()
    elif user_input == '2':
        search()
    elif user_input == '3':
        load_data()
    elif user_input == '4':
        print_data()
    elif user_input == '5':
        del_data()    
    elif user_input == '6':
        change_data()        

def main():
    ui()

if __name__ == "__main__":
    main()                    