import datetime
import os
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    try:
        # Correctly retrieve the MongoDB URI from environment variables
        client = MongoClient(os.getenv("MONGODB_URI"))
        app.db = client.microblog
        print("Connected to the database successfully")
    except Exception as e:
        print(f"Error connecting to the database: {e}")

    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            entry_content = request.form.get("content")
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
            
            app.db.entries.insert_one({"content": entry_content, "date": formatted_date})
            
            return redirect(url_for('home'))

        entries_with_date = [
            (entry["content"], entry["date"], datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d"))
            for entry in app.db.entries.find()
        ]
        
        return render_template("home.html", entries=entries_with_date)
    
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
