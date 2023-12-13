from flask import Flask, request, render_template, jsonify
import mysql.connector

app = Flask(__name__)


def get_db_connection():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="129238905ad",
        database="exp2"
    )
    return db


@app.route('/')
def index():
    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("SELECT * FROM student")
    students = cursor.fetchall()

    cursor.execute("SELECT * FROM course")
    courses = cursor.fetchall()

    cursor.execute("SELECT * FROM sc")
    grades = cursor.fetchall()

    db.close()

    return render_template('index.html', students=students, courses=courses, grades=grades)


# Add Student API
@app.route('/addStudent', methods=['POST'])
def add_student():
    sno = request.form['sno']
    sname = request.form['sname']
    ssex = request.form['ssex']
    sage = request.form['sage']
    sdept = request.form['sdept']

    db = get_db_connection()
    cursor = db.cursor()

    # 执行插入操作
    insert_query = "INSERT INTO student (sno, sname, ssex, sage, sdept) VALUES (%s, %s, %s, %s, %s)"
    values = (sno, sname, ssex, sage, sdept)
    cursor.execute(insert_query, values)
    db.commit()

    db.close()

    result = "Student added successfully"
    return jsonify({'result': result})

# Update Student API
@app.route('/updateStudent', methods=['POST'])
def update_student():
    sno = request.form['sno']
    sname = request.form['sname']
    ssex = request.form['ssex']
    sage = request.form['sage']
    sdept = request.form['sdept']

    db = get_db_connection()
    cursor = db.cursor()

    # 执行更新操作
    update_query = "UPDATE student SET sname=%s, ssex=%s, sage=%s, sdept=%s WHERE sno=%s"
    values = (sname, ssex, sage, sdept, sno)
    cursor.execute(update_query, values)
    db.commit()

    db.close()

    result = "Student updated successfully"
    return jsonify({'result': result})

# Delete Student API
@app.route('/deleteStudent', methods=['POST'])
def delete_student():
    sno = request.form['sno']

    db = get_db_connection()
    cursor = db.cursor()

    # 执行删除操作
    delete_query = "DELETE FROM student WHERE sno=%s"
    values = (sno,)
    cursor.execute(delete_query, values)
    db.commit()

    db.close()

    result = "Student deleted successfully"
    return jsonify({'result': result})

# Add Course API
@app.route('/addCourse', methods=['POST'])
def add_course():
    cno = request.form['cno']
    cname = request.form['cname']
    ccredit = request.form['ccredit']

    db = get_db_connection()
    cursor = db.cursor()

    # 执行插入操作
    insert_query = "INSERT INTO course (cno, cname, ccredit) VALUES (%s, %s, %s)"
    values = (cno, cname, ccredit)
    cursor.execute(insert_query, values)
    db.commit()

    db.close()

    result = "Course added successfully"
    return jsonify({'result': result})

# Update Course API
@app.route('/updateCourse', methods=['POST'])
def update_course():
    cno = request.form['cno']
    cname = request.form['cname']
    ccredit = request.form['ccredit']

    db = get_db_connection()
    cursor = db.cursor()

    # 执行更新操作
    update_query = "UPDATE course SET cname=%s, ccredit=%s WHERE cno=%s"
    values = (cname, ccredit, cno)
    cursor.execute(update_query, values)
    db.commit()

    db.close()

    result = "Course updated successfully"
    return jsonify({'result': result})

# Delete Course API
@app.route('/deleteCourse', methods=['POST'])
def delete_course():
    cno = request.form['cno']

    db = get_db_connection()
    cursor = db.cursor()

    # 执行删除操作
    delete_query = "DELETE FROM course WHERE cno=%s"
    values = (cno,)
    cursor.execute(delete_query, values)
    db.commit()

    db.close()

    result = "Course deleted successfully"
    return jsonify({'result': result})

# Add Grade API
@app.route('/addGrade', methods=['POST'])
def add_grade():
    sno = request.form['sno']
    cno = request.form['cno']
    grade = request.form['grade']

    db = get_db_connection()
    cursor = db.cursor()

    # 执行插入操作
    insert_query = "INSERT INTO sc (sno, cno, grade) VALUES (%s, %s, %s)"
    values = (sno, cno, grade)
    cursor.execute(insert_query, values)
    db.commit()

    db.close()

    result = "Grade added successfully"
    return jsonify({'result': result})

# Update Grade API
@app.route('/updateGrade', methods=['POST'])
def update_grade():
    sno = request.form['sno']
    cno = request.form['cno']
    grade = request.form['grade']

    db = get_db_connection()
    cursor = db.cursor()

    # 执行更新操作
    update_query = "UPDATE sc SET grade=%s WHERE sno=%s AND cno=%s"
    values = (grade, sno, cno)
    cursor.execute(update_query, values)
    db.commit()

    db.close()

    result = "Grade updated successfully"
    return jsonify({'result': result})

# Delete Grade API
@app.route('/deleteGrade', methods=['POST'])
def delete_grade():
    sno = request.form['sno']
    cno = request.form['cno']

    db = get_db_connection()
    cursor = db.cursor()

    # 执行删除操作
    delete_query = "DELETE FROM sc WHERE sno=%s AND cno=%s"
    values = (sno, cno)
    cursor.execute(delete_query, values)
    db.commit()

    db.close()

    result = "Grade deleted successfully"
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)
