import sqlite3

# A4
connect = sqlite3.connect('Users.db')
# рука с ручкой
cursor = connect.cursor()


cursor.execute('''
   CREATE TABLE IF NOT EXISTS users(
        name VARCHAR (50) NOT NULL,
        age INTEGER NOT NULL,
        hobby TEXT 
   )
''')

connect.commit()

# CRUD - create-read-update-delete

def add_user(name, age, hobby):
    cursor.execute(
        'INSERT INTO users(name, age, hobby) VALUES(?,?,?)',
        (name, age, hobby)
    )
    connect.commit()
    print(f"Пользователь добавлен:{name}")
#add_user("Ardager","25","Cпать")
#add_user("Peri","19","плавать")
name = input("Введите ваше имя")

def get_all_user():
    cursor.execute('SELECT * FROM users')

    users = cursor.fetchall()
    print(users)


    if users:
      print("Список всех пользователей!!!")
    for i in users:
        print(f"NAME: {i[0]}, AGE:{i[1]}, HOBBY: {i[2]}")
    else:
        print("Список пуст!!!")


#get_all_user()

def update_user_by_id(name):
    cursor.execute(
    'UPDATE users SET name = ?, WHERE rowid =?',
        (name, id)
    )
    connect.commit()

#update_user_by_id("Arzybek",2)

def delete_users_by_id(id):
    cursor.execute(
        'DELETE FROM users WHERE ROWID =?',
        (name, id)
    )
    connect.commit()
    print('Пользователь обновлен!!')
#delete_user_by_id(2)
