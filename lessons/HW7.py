import sqlite3

connect = sqlite3.connect('Client.db')
cursor = connect.cursor()
cursor.execute('''
   CREATE TABLE IF NOT EXISTS users(
        name TEXT,
        age INTEGER NOT NULL,
        birthday TEXT
   )
''')

cursor.execute('INSERT INTO users (name, age, birthday) VALUES (?, ?, ?)',
               ('Alice', 30, '1999-01-25'))
#cursor.execute('INSERT INTO users (name, age) VALUES (?, ?)', ('Alex', 27, '2001-07-12'))
connect.commit()

#Сreate

def create_user(name, age, birthday):
    cursor.execute(
        'INSERT INTO users(name, age, birthday) VALUES(?,?,?)',
   )

    connect.commit()
    print(f'Добавлен пользователь: {name}, возраст: {age}, дата рождения {birthday}')

#Read

def read_users():
    cursor.execute('SELECT * FROM users')
    return cursor.fetchall()

#users = cursor.fetchall()
#print(users)

#if users:
#    print("Список всех пользователей!!!")
#for i in users:
#    print(f"NAME: {i[0]}, AGE:{i[1]}, BIRTHDAY: {i[2]}")
#else:
#    print("Список пуст!!!")


#Update
def update_user(new_birthday, new_name, new_age):
    cursor.execute('UPDATE users SET name = ?, age = ? WHERE id = ?', (new_name, new_age, new_birthday))
    connect.commit()
    print(f'Обновлён пользователь с ID {new_birthday}')

# Delete
    def delete_user(user_id):
        cursor.execute('DELETE FROM users WHERE id = ?', (new_name, new_age, new_birthday,))
        connect.commit()
        print(f'Удалён пользователь с ID {user_id}')

