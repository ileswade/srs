from flask import Blueprint, render_template, Flask, request, flash, redirect, url_for
from .models import buildAll, populateAll, Student, Instructor, Program, Course, Section, Class, Registration


views = Blueprint('views', __name__)
# from werkzeug import secure_filename

@views.route("/build")
def build():
    buildAll()
    flash (f"Database rebuilt")
    return redirect(url_for("views.home"))

@views.route("/populate")
def populate():
    populateAll()
    flash (f"Database repopulated")
    return redirect(url_for("views.home"))

@views.route("/")
def home():
    flash(f"Here is a message")
    return render_template("index.html")

@views.route("/addStudent", methods=['GET', 'POST'])
def addStudent():
    if request.method=="POST":
        ## Get form data
        studentID = request.form.get("studentid")
        first_name = request.form.get("firstname")
        last_name = request.form.get("lastname")
        address = request.form.get("address")
        emailaddress = request.form.get("emailaddress")
        print(f"S={studentID} F={first_name} L={last_name} A={address} EA={emailaddress}")
        newStudent = Student.add(studentID, firstName=first_name, lastName=last_name, address=address, emailAddress=emailaddress)
        flash(f"Added! {newStudent.id}")
    return render_template("addStudent.html")


@views.route("/addCourse")
def addCourse():
    c=input("Name")

    return c

@views.route("/register")
def register():
    c=input("Name")

    return c
