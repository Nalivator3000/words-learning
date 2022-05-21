import random
import sqlite3
from sqlite3 import Error

path = 'words.sql'


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


connection = create_connection(path)


def add_word(connection):
    cursor = connection.cursor()
    key = input('Enter new word in English: ')
    val = input('Enter new word in Russian: ')
    add = str(f"INSERT INTO words (english, russian) VALUES ('{key}', '{val}')")
    try:
        cursor.execute(add)
        connection.commit()
        print("The pair added successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    return choice_mode()


def show_dict(connection):
    cursor = connection.cursor()
    try:
        print("Here is your dictionary:")
        cursor.execute(f"SELECT english, russian FROM words")
        result = cursor.fetchall()
        for i in range(len(result)):
            print(": ".join(result[i]))
        connection.commit()
    except Error as e:
        print(f"The error '{e}' occurred")
    return choice_mode()


def eng_to_rus(connection):
    cursor = connection.cursor()
    try:
        cursor.execute(f"SELECT english FROM words")
        eng = cursor.fetchall()
        a = random.randint(0, len(eng) - 1)
        next_word = ", ".join(eng[a])
        cursor.execute(f"SELECT russian FROM words")
        rus = cursor.fetchall()
        correct = ", ".join(rus[a])
        print(next_word)
        print('Enter this word in Russian')
        choise = input('')
        if choise == correct:
            print('Excelent! Try more')
            menu = input('Enter to restrat, 0 to main menu: ')
            if menu == '':
                return eng_to_rus(connection)
            else:
                return choice_mode()
            #Можно прикрутить ошибку если menu!=0
        else:
            print(f'Right is {correct}. Try again')
            menu = input('Enter to restrat, 0 to main menu: ')
            if menu == '':
                return eng_to_rus(connection)
            else:
                return choice_mode()
    except Error as e:
        print(f"The error '{e}' occurred")


def rus_to_eng(connection):
    cursor = connection.cursor()
    try:
        cursor.execute(f"SELECT russian FROM words")
        rus = cursor.fetchall()
        a = random.randint(0, len(rus) - 1)
        next_word = ", ".join(rus[a])
        cursor.execute(f"SELECT english FROM words")
        eng = cursor.fetchall()
        correct = ", ".join(eng[a])
        print(next_word)
        print('Enter this word in Russian')
        choise = input('')
        if choise == correct:
            print('Excelent! Try more')
            menu = input('Enter to restrat, 0 to main menu: ')
            if menu == '':
                return rus_to_eng(connection)
            else:
                return choice_mode()
            #Можно прикрутить ошибку если menu!=0
        else:
            print(f'Right is {correct}. Try again')
            menu = input('Enter to restrat, 0 to main menu: ')
            if menu == '':
                return rus_to_eng(connection)
            else:
                return choice_mode()
    except Error as e:
        print(f"The error '{e}' occurred")


def choice_mode():
    print('1 - English to Russian')
    print('2 - Russian to English')
    print('3 - Add a pair of words')
    print('4 - Delete a pair of words')
    print('5 - Show your dictionary')
    mode = input('What do you want to do?: ')
    if mode == '1':
        return eng_to_rus(connection)
    elif mode == '2':
        return rus_to_eng(connection)
    elif mode == '3':
        return add_word(connection)
    elif mode == '4':
        return delete_word(connection)
    elif mode == '5':
        show_dict(connection)
    else:
        print('Try again')
        return choice_mode()


def delete_word(connection):
    cursor = connection.cursor()
    key = input('What word do you want to delete: ')
    delete = str(f"DELETE FROM `words` WHERE `english` = '{key}' OR 'russian' = '{key}'")
    try:
        cursor.execute(delete)
        connection.commit()
        print("The pair deleted successfully")
    except Error as e:
        print(f"The error '{e}' occurred")
    return choice_mode()


choice_mode()
