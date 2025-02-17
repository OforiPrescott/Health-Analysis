import dash
from dash import dcc, html, Input, Output
import requests
import pandas as pd
import plotly.express as px

# Initialize Dash app
app = dash.Dash(__name__)

# Fetch Data from Flask API
api_url = "http://127.0.0.1:5000/api/appointments"
try:
    response = requests.get(api_url)
    data = response.json()
    if isinstance(data, list) and len(data) > 0:
        df = pd.DataFrame(data)
    else:
        df = pd.DataFrame(columns=["Patient", "Doctor", "AppointmentDate"])
        print("⚠️ Warning: No data available from API.")
except Exception as e:
    df = pd.DataFrame(columns=["Patient", "Doctor", "AppointmentDate"])
    print(f"❌ Error fetching data: {e}")

# Dashboard Layout
app.layout = html.Div([
    html.H1("📊 Health Data Dashboard - Fun & Engaging!"),
    html.P("Explore appointments, doctors, and trends interactively."),
    
    # Dropdown to filter by doctor
    html.Label("Select Doctor:"),
    dcc.Dropdown(
        id='doctor-dropdown',
        options=[{'label': doc, 'value': doc} for doc in df['Doctor'].unique()] if not df.empty else [],
        placeholder="Choose a doctor",
        multi=True
    ),
    
    # Date Picker
    html.Label("Select Date Range:"),
    dcc.DatePickerRange(
        id='date-picker',
        start_date=df['AppointmentDate'].min() if not df.empty else None,
        end_date=df['AppointmentDate'].max() if not df.empty else None
    ),
    
    # Graph for appointments over time
    dcc.Graph(id='appointments-trend'),
    
    # Pie chart for doctor distribution
    dcc.Graph(id='doctor-distribution'),
    
    # User engagement - Text area for comments
    html.H3("💬 Share Your Thoughts!"),
    dcc.Textarea(id='user-comments', placeholder="What do you think about the appointment trends?", style={'width': '100%', 'height': 100}),
    html.Button("Submit", id='submit-comment', n_clicks=0),
    html.Div(id='comment-output')
])

# Callbacks for interactivity
@app.callback(
    [Output('appointments-trend', 'figure'),
     Output('doctor-distribution', 'figure')],
    [Input('doctor-dropdown', 'value'),
     Input('date-picker', 'start_date'),
     Input('date-picker', 'end_date')]
)
def update_graphs(selected_doctors, start_date, end_date):
    filtered_df = df.copy()
    if selected_doctors:
        filtered_df = filtered_df[filtered_df['Doctor'].isin(selected_doctors)]
    if start_date and end_date:
        filtered_df = filtered_df[(filtered_df['AppointmentDate'] >= start_date) & (filtered_df['AppointmentDate'] <= end_date)]
    
    trend_fig = px.line(filtered_df, x='AppointmentDate', y='Patient', title="📅 Appointments Over Time", markers=True) if not filtered_df.empty else px.line(title="No Data Available")
    pie_fig = px.pie(filtered_df, names='Doctor', title="👨‍⚕️ Appointments Per Doctor") if not filtered_df.empty else px.pie(title="No Data Available")
    
    return trend_fig, pie_fig

# Comment Section Callback
@app.callback(
    Output('comment-output', 'children'),
    Input('submit-comment', 'n_clicks'),
    Input('user-comments', 'value')
)
def update_comment(n_clicks, comment):
    if n_clicks > 0 and comment:
        return html.P(f"📝 Comment Submitted: {comment}")
    return ""

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
