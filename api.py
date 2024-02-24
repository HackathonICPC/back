import mysql.connector

class api_class:

    def __init__(self):

        self.mydb = mysql.connector.connect(
            host ="localhost",
            user ="root",
            database='icpc',
            passwd ="d08132004D123"
        )

        self.mycursor = self.mydb.cursor(buffered=True)
        #self.mycursor.execute("""DROP TABLE users""")

        self.mycursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            pass VARCHAR(255),
            username VARCHAR(255),
            login VARCHAR(255)
        )
        """)

        self.mycursor.execute("""
        CREATE TABLE IF NOT EXISTS courses (
            id INT AUTO_INCREMENT PRIMARY KEY,
            courseName VARCHAR(255)
        )
        """)

        self.mycursor.execute("""
        CREATE TABLE IF NOT EXISTS course_creator (
            creator_id INT AUTO_INCREMENT PRIMARY KEY,
            course_id INT,
            FOREIGN KEY(creator_id) REFERENCES users(id),
            FOREIGN KEY(course_id) REFERENCES courses(id)
        )
        """)

        self.mycursor.execute("""
        CREATE TABLE IF NOT EXISTS admins (
            id INT AUTO_INCREMENT PRIMARY KEY,
            FOREIGN KEY(id) REFERENCES users(id)
        )
        """)

        self.mycursor.execute("""
        CREATE TABLE IF NOT EXISTS course_user (
            creator_id INT AUTO_INCREMENT PRIMARY KEY,
            course_id INT,
            FOREIGN KEY(creator_id) REFERENCES users(id),
            FOREIGN KEY(course_id) REFERENCES courses(id)
        )
        """)

        self.mycursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            taskStatement VARCHAR(255),
            maxMark INT,
            deadline date
        )
        """)

        self.mycursor.execute("""
        CREATE TABLE IF NOT EXISTS course_tasks (
            task_id INT AUTO_INCREMENT PRIMARY KEY,
            course_id INT,
            FOREIGN KEY(task_id) REFERENCES tasks(id),
            FOREIGN KEY(course_id) REFERENCES courses(id)
        )
        """)

        self.mycursor.execute("""
        CREATE TABLE IF NOT EXISTS user_tasks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            task_id INT,
            user_id INT,
            ref VARCHAR(255),
            FOREIGN KEY(task_id) REFERENCES tasks(id)
        )
        """)

        self.mycursor.execute("""
        CREATE TABLE IF NOT EXISTS user_marks (
            id INT AUTO_INCREMENT PRIMARY KEY,
            marks INT,
            markDate date,
            FOREIGN KEY(id) REFERENCES user_tasks(id)
        )
        """)

    def get_id(self, login):
        self.mycursor.execute(f"""SELECT id FROM users WHERE login='{login}'""")
        for x in self.mycursor:
            return x
        


    def sign_in (self, login, password): # вход
        self.mycursor.execute(f"""SELECT * FROM users WHERE login='{login}' AND pass='{password}'""")
        for x in self.mycursor:
            print(x)
        

    def sign_up (self, login, password, name):
        self.mycursor.execute(f"""SELECT * FROM users WHERE login='{login}'""")
        for x in self.mycursor:
            print("Login is already occupied")
            return

        self.mycursor.execute(f"""INSERT INTO users (login, pass, username) VALUES ('{login}', '{password}', '{name}') """)
        self.mydb.commit()
        

    def sign_in (self, login, password): # вход
        self.mycursor.execute(f"""SELECT id FROM users WHERE login='{login}' AND pass='{password}'""")
        for x in self.mycursor:
            return x
        return 0

    def add_course(self, id, name):
        self.mycursor.execute(f"""INSERT INTO courses (courseName)
        VALUES
        f("{name}")
        """)

        self.mycursor.execute(f"""INSERT INTO course_creator (creator_id, course_id)
        VALUES
        f("{id}, SELECT LAST_INSERT_ID()")
        """)


    def to_admin(self, id):
        self.mycursor.execute(f"""INSERT INTO admins (id)
        VALUES
        f("{id}")
        """)

    def to_course(self, id_student, id_course):
        self.mycursor.execute(f"""INSERT INTO course_user (creator_id, course_id)
        VALUES
        f("{id_student}, {id_course}")
        """)






# Disconnecting from the server