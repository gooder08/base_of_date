import psycopg2
from pprint import pprint
import numpy as np
import pandas as pd

# Функция, создающая структуру БД (таблицы).
def create_db(conn):
    with conn.cursor() as cur:
        cur.execute("""CREATE TABLE IF NOT EXISTS people(
            id SERIAL PRIMARY KEY,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            email VARCHAR(60) UNIQUE NOT NULL,
            mobile VARCHAR(60) UNIQUE
            );""")
        conn.commit()
        
        
# Функция, позволяющая добавить нового клиента.    
def add_client(conn, first_name, last_name, email, phones):
    with conn.cursor() as cur:
        cur.execute(""" INSERT INTO people(name, surname, email, mobile) VALUES (%s, %s, %s, %s)""", (first_name.upper(), last_name.upper(), email.upper(), phones))     
        conn.commit()
        print('Данные успешно добавлены в базу')
        

# Функция, позволяющая добавить телефон для существующего клиента.
def add_phone(conn, client_id):
    with conn.cursor() as cur:
        cur.execute("""SELECT id FROM people WHERE id = %s""", (client_id, ))
        a = cur.fetchall()
        if len(a) == 0:
            print(f'Клиент с id {client_id} не найден.')
        else:
            phone = int(input('Введите телефон: '))
            cur.execute("""UPDATE people SET mobile = CONCAT(mobile, ' %s') WHERE id = %s""", (phone, client_id))
            conn.commit()
            print(f'Телефон успешно добавлен клиенту с id {client_id}')


# Показать баззу данных
def show_db(conn):
    with conn.cursor() as cur:
        cur.execute("""SELECT * FROM people """)
        b = cur.fetchall()
        d = pd.DataFrame(b, columns=['id', 'name', 'surname', 'email', 'mobile'])
        print(d)
        
# Функция, позволяющая изменить данные о клиенте.
def change_client(conn):
    while True:
        client_id = input("Введите id клиента: ")
        if (not client_id.isdigit() and client_id != 'q'):
            print("id клиента должен быть числовой")
        if client_id == 'q':
            break
        if client_id.isdigit():
            with conn.cursor() as cur:
                cur.execute("""SELECT id FROM people WHERE id = %s""", (client_id, ))
                a = cur.fetchall()
                if len(a) == 0:
                    print(f'Клиент с id {client_id} не найден.')
                else:
                    first_name = input("Введите имя: ")
                    last_name = input("Введите фамилию: ")
                    email = input("Введите email: ")
                    phones = input("Введите номер мобильного: ")
                    cur.execute("""UPDATE people SET name = %s, surname = %s, email = %s, mobile = %s WHERE id = %s """, (first_name.upper(), last_name.upper(), email.upper(), phones, client_id, )) 
                    conn.commit()
                    print(f'Данные клиента с id {client_id} успешно изменены')
                    break


# Функция, позволяющая удалить телефон для существующего клиента.
def delete_phone(conn):
    while True:
        client_id = input("Введите id клиента, у которго надо удалить телефон: ")
        if (not client_id.isdigit() and client_id != 'q'):
            print("id клиента должен быть числовой")
        if client_id == 'q':
            break
        if client_id.isdigit():
            with conn.cursor() as cur:
                cur.execute("""SELECT id FROM people WHERE id = %s""", (client_id, ))
                a = cur.fetchall()
                if len(a) == 0:
                    print(f'Клиент с id {client_id} не найден.')
                else:
                    cur.execute("""UPDATE people SET mobile = NULL WHERE id = %s """, (client_id, )) 
                    conn.commit()
                    print(f'Телефон клиента с id {client_id} успешно удален')
                    break

# Функция, позволяющая удалить существующего клиента.
def delete_client(conn):
    while True:
        client_id = input("Введите id клиента, которго надо удалить: ")
        if (not client_id.isdigit() and client_id != 'q'):
            print("id клиента должен быть числовой")
        if client_id == 'q':
            break
        if client_id.isdigit():
            with conn.cursor() as cur:
                cur.execute("""SELECT id FROM people WHERE id = %s""", (client_id, ))
                a = cur.fetchall()
                if len(a) == 0:
                    print(f'Клиент с id {client_id} не найден.')
                else:
                    cur.execute("""DELETE FROM people WHERE id = %s """, (client_id, )) 
                    conn.commit()
                    print(f'Клиент с id {client_id} успешно удален')
                    break

# Функция, позволяющая найти клиента по его данным: имени, фамилии, email или телефону.
def find_client(conn):
    while True:
        print('По каким параметрам будем искать:\n'
                '1 - по email\n'
                '2 - по телефону\n'
                'q - выход\n')
        req = input('Введите параметр: ')        
        if req == '1':
            email = input("Введите email клиента: ")
            with conn.cursor() as cur:
                cur.execute("""SELECT id, name, surname, email, mobile FROM people WHERE email = %s""", (email, ))
                a = cur.fetchall()
                if len(a) == 0:
                    print(f'Клиент с почтой {email} не найден.')
                else:
                    d = pd.DataFrame(a, columns=['id', 'name', 'surname', 'email', 'mobile'])
                    print(f"Клиент с почтой {email} найден:\n{d}")
                    break
        if req == '2':
            mobile = input("Введите телефон клиента: ")
            with conn.cursor() as cur:
                cur.execute("""SELECT id, name, surname, email, mobile FROM people WHERE mobile = %s""", (mobile, ))
                a = cur.fetchall()
                if len(a) == 0:
                    print(f'Клиент с телефоном {mobile} не найден.')
                else:
                    d = pd.DataFrame(a, columns=['id', 'name', 'surname', 'email', 'mobile'])
                    print(f"Клиент с телефоном {mobile} найден:\n{d}")
                    break
        if req == 'q':
            break
        
print("\nКоманды:\n"
            "1 - Добавить нового клиента\n"
            "2 - Добавить телефон для существующего клиента\n"
            "3 - Изменить данные о клиента\n"
            "4 - Удалить телефон для существующего клиента\n"
            "5 - Удалить существующего клиента\n"
            "6 - Найти клиента, зная его Имя, Фамилию, email или мобильный телефон\n"
            "7 - Показать базу данных\n"
            "q - Выход\n")
# try:
conn = psycopg2.connect(database='listofpeople', user='postgres', password='Telega_13')
create_db(conn)  
while True:
    com = input("\nВведите команду: ")
    if (com == '1' or com == '2' or com == '3' or com == '4' or com == '5' or com == '6' or com == '7' or com == 'q'):
        if com == '1':
            try:
                first_name = input("Введите имя: ")
                last_name = input("Введите фамилию: ")
                email = input("Введите email: ")
                phones = input("Введите номер мобильного: ")
                add_client(conn, first_name, last_name, email, phones)
            except:
                print('Такая почта или телефон уже сществует. Клиент не добавлен в базу')
                continue 
        if com == '2':
            client_id = int(input('Укажите id клиента: '))
            add_phone(conn, client_id)   
        if com == '3':
            change_client(conn)
        if com == '4':
            delete_phone(conn)
        if com == '5':
            delete_client(conn)
        if com == '6':
            find_client(conn)
        if com == '7':
            show_db(conn)                      
        if com =='q':
            print('Выход из программы')
            break
    else:
        print('Недопустимое значение, попробуйте еще раз')
conn.close()
# except:
#     print('Непредвиденная ошибка')
        
   

    
    



