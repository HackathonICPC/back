import mysql.connector
  
mydb = mysql.connector.connect(
  host ="localhost",
  user ="root",
  database='icpc',
  passwd ="d08132004D123"
)
 
mycursor = mydb.cursor()

mycursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    pass VARCHAR(255),
    username VARCHAR(255),
    login VARCHAR(255)
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    courseName VARCHAR(255)
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS course_creator (
    creator_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT,
    FOREIGN KEY(creator_id) REFERENCES users(id),
    FOREIGN KEY(course_id) REFERENCES courses(id)
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS admins (
    id INT AUTO_INCREMENT PRIMARY KEY,
    FOREIGN KEY(id) REFERENCES users(id)
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS course_user (
    creator_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT,
    FOREIGN KEY(creator_id) REFERENCES users(id),
    FOREIGN KEY(course_id) REFERENCES courses(id)
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    taskStatement VARCHAR(255),
    maxMark INT,
    deadline date
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS course_tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT,
    FOREIGN KEY(task_id) REFERENCES tasks(id),
    FOREIGN KEY(course_id) REFERENCES courses(id)
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS user_tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    task_id INT,
    user_id INT,
    ref VARCHAR(255),
    FOREIGN KEY(task_id) REFERENCES tasks(id)
)
""")

mycursor.execute("""
CREATE TABLE IF NOT EXISTS user_marks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    marks INT,
    markDate date,
    FOREIGN KEY(id) REFERENCES user_tasks(id)
)
""")

def sign_in (login, password): # вход
    mycursor.execute(f"""SELECT * FROM users WHERE login={login} AND pass={password}""")
    for x in mycursor:
        print(x)
    

def sing_up (login, password, name):
    mycursor.execute(f"""SELECT * FROM users WHERE login={login}""")
    if len (mycursor) >= 1:
        print("Login is already occupied")
        return
    mycursor.execute(f"""INSERT INTO users (login, pass, username)
    VALUES
    f("{login}, {password}, {name}")
    """)

def sign_in (login, password): # вход
    mycursor.execute(f"""SELECT * FROM users WHERE login={login} AND pass={password}""")
    for x in mycursor:
        print(x)

def add_course(id, name):
    mycursor.execute(f"""INSERT INTO courses (courseName)
    VALUES
    f("{name}")
    """)

    mycursor.execute(f"""INSERT INTO course_creator (creator_id, course_id)
    VALUES
    f("{id}, SELECT LAST_INSERT_ID()")
    """)


def to_admin(id):
    mycursor.execute(f"""INSERT INTO admins (id)
    VALUES
    f("{id}")
    """)

def to_course(id_student, id_course):
    mycursor.execute(f"""INSERT INTO course_user (creator_id, course_id)
    VALUES
    f("{id_student}, {id_course}")
    """)


# Disconnecting from the server