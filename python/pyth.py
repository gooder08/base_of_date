import psycopg2
from pprint import pprint
import numpy as np
import pandas as pd

# Функция, создающая структуру БД (таблицы).
def create_db(conn):
    cur.execute("""CREATE TABLE IF NOT EXISTS people(
        id SERIAL PRIMARY KEY,
        name TEXT NOT NULL,
        surname TEXT NOT NULL,
        email VARCHAR(60) NOT NULL
        );""")
    cur.execute("""CREATE TABLE IF NOT EXISTS mobilephones(
        id_mp SERIAL REFERENCES people(id) ON DELETE CASCADE ON UPDATE CASCADE,
        mobile VARCHAR(60) 
        );""")
    conn.commit()
        
        
# Функция, позволяющая добавить нового клиента.    
def add_client(conn, first_name, last_name, email, phones):
    cur.execute(""" INSERT INTO people(name, surname, email) VALUES (%s, %s, %s)""", (first_name.upper(), last_name.upper(), email.upper(), )) 
    cur.execute(""" INSERT INTO mobilephones(mobile) VALUES (%s)""", (phones, ))     
    conn.commit()
    print('Данные успешно добавлены в базу')
        

# Функция, позволяющая добавить телефон для существующего клиента.
def add_phone(conn, client_id):
    phone = int(input('Введите телефон: '))
    cur.execute("""INSERT INTO mobilephones(id_mp, mobile) VALUES (%s, %s)""", (client_id, phone, ))
    conn.commit()
    print(f'Телефон успешно добавлен клиенту с id {client_id}')


# Показать баззу данных
def show_db(conn):
    cur.execute("""SELECT id, name, surname, email, mobile FROM people p JOIN mobilephones m ON p.id=m.id_mp""")
    b = cur.fetchall()
    d = pd.DataFrame(b, columns=['id', 'name', 'surname', 'email', 'mobile'])
    print(d)
        
# Функция, позволяющая изменить данные о клиенте.
def change_client(conn, client_id):
    first_name = input("Введите имя: ")
    last_name = input("Введите фамилию: ")
    email = input("Введите email: ")
    phones = input("Введите номер мобильного: ")
    cur.execute("""UPDATE people SET name = %s, surname = %s, email = %s WHERE id = %s """, (first_name.upper(), last_name.upper(), email.upper(), client_id, ))
    cur.execute("""UPDATE mobilephones SET mobile = %s WHERE id_mp = %s """, (phones, client_id, )) 
    conn.commit()
    print(f'Данные клиента с id {client_id} успешно изменены')
    


# Функция, позволяющая удалить телефон для существующего клиента.
def delete_phone(conn, client_id):
    cur.execute("""UPDATE mobilephones SET mobile = NULL WHERE id_mp = %s """, (client_id, )) 
    conn.commit()
    print(f'Телефон клиента с id {client_id} успешно удален')
                    

# Функция, позволяющая удалить существующего клиента.
def delete_client(conn, client_id):
    cur.execute("""DELETE FROM mobilephones WHERE id_mp = %s """, (client_id, ))
    cur.execute("""DELETE FROM people WHERE id = %s """, (client_id, )) 
    conn.commit()
    print(f'Клиент с id {client_id} успешно удален')
                    

# Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону.
def find_client(conn, first_name, last_name, email, phones):
    if email == None and phones == None:
        cur.execute("""SELECT id, name, surname, email, mobile FROM people p JOIN mobilephones m ON p.id=m.id_mp WHERE name=%s and surname=%s""", (first_name, last_name, ))
        a = cur.fetchall()
        d = pd.DataFrame(a, columns=['id', 'name', 'surname', 'email', 'mobile'])
        print(f"Клиент найден:\n{d}")
    if first_name == None and email == None and phones == None:
        cur.execute("""SELECT id, name, surname, email, mobile FROM people p JOIN mobilephones m ON p.id=m.id_mp WHERE surname=%s""", (last_name, ))
        a = cur.fetchall()
        d = pd.DataFrame(a, columns=['id', 'name', 'surname', 'email', 'mobile'])
        print(f"Клиент найден:\n{d}")
    if last_name == None and email == None and phones == None:
        cur.execute("""SELECT id, name, surname, email, mobile FROM people p JOIN mobilephones m ON p.id=m.id_mp WHERE name=%s""", (first_name, ))
        a = cur.fetchall()
        d = pd.DataFrame(a, columns=['id', 'name', 'surname', 'email', 'mobile'])
        print(f"Клиент найден:\n{d}")
    if last_name == None and  first_name == None and phones == None:
        cur.execute("""SELECT id, name, surname, email, mobile FROM people p JOIN mobilephones m ON p.id=m.id_mp WHERE name=%s""", (email, ))
        a = cur.fetchall()
        d = pd.DataFrame(a, columns=['id', 'name', 'surname', 'email', 'mobile'])
        print(f"Клиент найден:\n{d}")
    if last_name == None and first_name == None and email == None:
        cur.execute("""SELECT id, name, surname, email, mobile FROM people p JOIN mobilephones m ON p.id=m.id_mp WHERE name=%s""", (phones, ))
        a = cur.fetchall()
        d = pd.DataFrame(a, columns=['id', 'name', 'surname', 'email', 'mobile'])
        print(f"Клиент найден:\n{d}")



    
    
    
if __name__ == "__main__":
    print("\nКоманды:\n"
                "1 - Добавить нового клиента\n"
                "2 - Добавить телефон для существующего клиента\n"
                "3 - Изменить данные о клиенте\n"
                "4 - Удалить телефон для существующего клиента\n"
                "5 - Удалить существующего клиента\n"
                "6 - Найти клиента, зная его Имя, Фамилию, email или мобильный телефон\n"
                "7 - Показать базу данных\n"
                "q - Выход\n")
    
    conn = psycopg2.connect(database='listofpeople', user='postgres', password='Telega_13')
    with conn.cursor() as cur:
        create_db(conn)  
        while True:
            com = input("\nВведите команду: ")
            if (com == '1' or com == '2' or com == '3' or com == '4' or com == '5' or com == '6' or com == '7' or com == 'q'):
                if com == '1':
                    add_client(conn, first_name='Ivan', last_name='Petrov', email='sobaka@mail.ru', phones=None)
                if com == '2':
                    add_phone(conn, client_id='1')   
                if com == '3':
                    change_client(conn, client_id='1')
                if com == '4':
                    delete_phone(conn, client_id='1')
                if com == '5':
                    delete_client(conn, client_id='3')
                if com == '6':
                    find_client(conn, first_name=None, last_name=None, email=None, phones=None)
                if com == '7':
                    show_db(conn)                      
                if com =='q':
                    print('Выход из программы')
                    break
            else:
                print('Недопустимое значение, попробуйте еще раз')
    conn.close()
 
        
   

    
    



