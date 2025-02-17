from flask import Flask, jsonify
import pyodbc
import pandas as pd

app = Flask(__name__)

# Database Connection
conn = pyodbc.connect("DRIVER={SQL Server};SERVER=PresHacks;DATABASE=HealthDB;Trusted_Connection=yes")

@app.route('/api/appointments', methods=['GET'])
def get_appointments():
    try:
        query = """
        SELECT p.FullName AS Patient, d.FullName AS Doctor, a.AppointmentDate
        FROM Appointments a
        JOIN Patients p ON a.PatientID = p.PatientID
        JOIN Doctors d ON a.DoctorID = d.DoctorID
        """
        df = pd.read_sql(query, conn)
        return jsonify(df.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
