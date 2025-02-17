### Health Data Analytics Dashboard 

This project is a Flask-based API that retrieves health appointment data from Microsoft SQL Server and a Dash dashboard that visualizes the data interactively.

🚀 Features

📊 Fetches appointment data from SQL Server using Flask API.

📈 Displays interactive graphs with Dash & Plotly.

🔍 Allows filtering by doctor and date range.

💬 Enables user engagement via a comment section.

📌 Setup Instructions

1️⃣ Install Dependencies

Ensure Python is installed, then run:

pip install flask dash plotly pandas pyodbc requests


2️⃣ Set Up SQL Server Connection

Modify app.py to match your database configuration:

conn = pyodbc.connect("DRIVER={SQL Server};SERVER=YourServerName;DATABASE=YourDB;Trusted_Connection=yes")

3️⃣ Run the Flask API

Start the backend API server:

python app.py

✅ The API will be available at:

🔗 http://127.0.0.1:5000/api/appointments

4️⃣ Run the Dash Dashboard

Start the dashboard interface:

python dashboard.py

✅ The dashboard will be available at:

🔗 http://127.0.0.1:8050


🔧 Future Enhancements

🔐 User authentication

📊 More advanced data insights

☁️ Cloud deployment



![Screenshot 2025-02-17 135417](https://github.com/user-attachments/assets/73e29a22-a7a6-4806-9d30-ba8b9c601c4a)

![Screenshot 2025-02-17 135436](https://github.com/user-attachments/assets/b19a62f2-fe0a-4a37-92d7-f8517b3ec4e6)


![Screenshot 2025-02-17 135452](https://github.com/user-attachments/assets/7f60ec35-ec8a-4180-a930-d27d6d751d12)

