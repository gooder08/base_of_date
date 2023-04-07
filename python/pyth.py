import psycopg2

# Функция, создающая структуру БД (таблицы).
def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""CREATE TABLE IF NOT EXISTS people(
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            email VARCHAR(60) UNIQUE NOT NULL,
            mobile VARCHAR(60) 
            );""")
        conn.commit()
        
        
# Функция, позволяющая добавить нового клиента.    
def add_client(conn, first_name, last_name, email, phones):
    with conn.cursor() as cur:
        cur.execute(""" INSERT INTO people(name, surname, email, mobile) VALUES (%s, %s, %s, %s)""", (first_name.upper(), last_name.upper(), email.upper(), phones))     
        conn.commit()
        

# Функция, позволяющая добавить телефон для существующего клиента.
def add_phone(conn, client_id):
    with conn.cursor() as cur:
        cur.execute("""SELECT id FROM people WHERE id = %s""", (client_id, ))
        a = cur.fetchall()
        if len(a) == 0:
            print(f'Клиент с id {client_id} не найден.')
        else:
            phone = int(input('Введите телефон: '))
            cur.execute("""UPDATE people SET mobile = CONCAT(mobile, ', %s') WHERE id = %s""", (phone, client_id))
            conn.commit()
            print(f'Телефон успешно добавлен клиенту с id {client_id}')
            
            
            
        


print("\nКоманды:\n"
            "1 - Добавить  новго клиента\n"
            "2 - Добавить телефон для существующего клиента\n"
            "3 - Изменить данные о клиента\n"
            "4 - Удалить телефон для существующего клиента\n"
            "5 - Удалить существующего клиента\n"
            "6 - Найти клиента, зная его Имя, Фамилию, email или мобильный телефон\n"
            "7 - Выход\n")
# try:
conn = psycopg2.connect(database='listofpeople', user='postgres', password='Telega_13')
create_db(conn)  
while True:
    com = input("\nВведите команду: ")
    if (com == '1' or com == '2' or com == '3' or com == '4' or com == '5' or com == '6' or com == '7'):
        if com == '1':
            try:
                first_name = input("Введите имя: ")
                last_name = input("Введите фамилию: ")
                email = input("Введите email: ")
                phones = input("Введите номер мобильного: ")
                add_client(conn, first_name, last_name, email, phones)
                print('Данные успешно добавлены в базу')
            except:
                print('Такая почта уже сществует. Клиент не добавлен в базу')
                continue
        if com == '2':
            client_id = int(input('Укажите id клиента: '))
            add_phone(conn, client_id)             
        if com =='7':
            print('Выход из программы')
            break
    else:
        print('Недопустимое значение, попробуйте еще раз')
conn.close()
# except:
#     print('Непредвиденная ошибка')
        
   

    
    



