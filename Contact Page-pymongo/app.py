from flask import Flask, render_template, request, redirect, url_for
import pymongo

app = Flask(__name__)

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["contact"]
col = db["contactinfos"]

@app.route("/", methods=["GET", "POST"])
def contact():
    message_saved = False  # Flag to indicate success message

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]

        col.insert_one({"name": name, "email": email, "message": message})

        message_saved = True  # Set flag to True after saving

    return render_template("contact.html", message_saved=message_saved)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
