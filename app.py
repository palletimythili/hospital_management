
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="YOUR_MYSQL_PASSWORD",
        database="hospital"
    )

# Home page API
@app.route("/")
def home():
    return "Hospital Management System Backend Running"

# View patients
@app.route("/patients", methods=["GET"])
def get_patients():
    db = get_db_connection()
    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()

    cursor.close()
    db.close()

    return jsonify(patients)

# Add patient
@app.route("/patients", methods=["POST"])
def add_patient():
    data = request.get_json()

    db = get_db_connection()
    cursor = db.cursor()

    sql = """INSERT INTO patients
             (name, age, gender, disease)
             VALUES (%s, %s, %s, %s)"""

    values = (
        data["name"],
        data["age"],
        data["gender"],
        data["disease"]
    )

    cursor.execute(sql, values)
    db.commit()

    cursor.close()
    db.close()

    return jsonify({"message": "Patient Added Successfully"}), 201

# Delete patient
@app.route("/patients/<int:id>", methods=["DELETE"])
def delete_patient(id):
    db = get_db_connection()
    cursor = db.cursor()

    cursor.execute("DELETE FROM patients WHERE id=%s", (id,))
    db.commit()

    deleted = cursor.rowcount

    cursor.close()
    db.close()

    if deleted == 0:
        return jsonify({"message": "Patient not found"}), 404

    return jsonify({"message": "Patient Deleted Successfully"})

if __name__ == "__main__":
    app.run(debug=True, port=5000)
