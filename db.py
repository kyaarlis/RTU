import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS grafiki (
    id INTEGER PRIMARY KEY AUTOINCREMENT,  
    study_program TEXT NOT NULL,
    study_course TEXT NOT NULL,
    study_group TEXT NOT NULL
  )
''')


def insert_data(study_program, study_course, study_group):
    cursor.execute('''	
            INSERT INTO grafiki (study_program, study_course, study_group) 
            VALUES (?, ?, ?)''',
            (study_program, study_course, study_group))
    conn.commit()

def retrieve_data():
    cursor.execute('''SELECT study_program, study_course, study_group FROM grafiki''')
    rows = cursor.fetchall()
    data = []

    for row in rows:
        study_program, study_course, study_group = row

        data.append({
            # 'id': id,
            'study_program': study_program,
            'study_course': study_course,
            'study_group': study_group
        })

    return data

conn.commit()
# conn.close()