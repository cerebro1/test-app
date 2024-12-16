from flask import Flask
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def show_date():
    # Get today's date
    today = datetime.now().strftime('%Y-%m-%d')
    return f"<h1>Hi Sonali! Today's Date: {today}</h1>"

if __name__ == '__main__':
    app.run(debug=True)
