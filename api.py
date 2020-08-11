from flask import Flask, request, render_template
from pymongo import MongoClient

# Configure app
app = Flask(__name__)

# Configure mongo
# client = MongoClient(environ.get('MONGODB_URI'))
# db = client.study_connect

students = {}

# home
@app.route("/")
def home():
  return render_template("profile.html")


@app.route("/form")
def createUser():
  return render_template("form.html")
    # print(request.json)
    user = request.json['username']
    pw = request.json['password']

    # check if student already exists (name twins)
    # if db.course.find_one({ "full_name": name }):
    #    return 

    # add student to database
    student_object = {
        "full_name": name,
        "available_day": days,
        "group_size": size,
        "comfort_with_material": comfort, 
        "focus_scale": focus
        "comfort_with_helping": comfort
    }
    db.course.insert_one(student_object)

    return {"status": "success"}, status.HTTP_200_OK