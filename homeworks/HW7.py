import sqlite3

connect = sqlite3.connect('Client.db')
cursor = connect.cursor()
cursor.execute('''
   CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER NOT NULL,
        birthday TEXT
   )
''')


#Сreate

def create_user(name, age, birthday):
    cursor.execute(
        'INSERT INTO users(name, age, birthday) VALUES(?,?,?)', (name, age, birthday)
   )

    connect.commit()
    print(f'Добавлен пользователь: {name}, возраст: {age}, дата рождения {birthday}')

#Read

def read_users():
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()
    if users:
        print("Список всех пользователей!!!")
    for i in users:
        print(f"NAME: {i[0]}, AGE:{i[1]}, BIRTHDAY: {i[2]}")
    else:
        print("Список пуст!!!")



#Update

def update_user(new_name, new_age, new_birthday, user_id):
    cursor.execute('UPDATE users SET name = ?, age = ?, birthday = ? WHERE id = ?', (new_name, new_age, new_birthday, user_id))
    connect.commit()
    print(f'Обновлён пользователь с ID {user_id}')

#Delete

def delete_user(user_id):
    cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
    connect.commit()
    print(f'Удалён пользователь с ID {user_id}')

# create_user("Peri", 19, "06.06.2005")
# delete_user(3)
# read_users()
update_user('Peri',19, '14.05.2005', 2)