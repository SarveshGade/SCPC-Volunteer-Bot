from flask import jsonify, Flask
import pandas as pd

app = Flask(__name__)
@app.route('/get-emails', methods=['GET'])
def get_emails():
    df = pd.read_csv('volunteer_sheet.csv', skiprows=6, encoding='ISO-8859-1')
    print(df.head())
    email_array = df['Name'].dropna().tolist()
    return jsonify(email_array)

if __name__ == "main":
    app.run(debug=True)
    