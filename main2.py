from flask_sqlalchemy import SQLAlchemy
from flask import render_template, Flask, request, flash, redirect, url_for
import logging
from sqlalchemy.sql import func
from datetime import datetime

# ############################################################################################################
#   Setup
# ############################################################################################################

DB_NAME = "database.db"
app = Flask(__name__)
app.config['SECRET_KEY'] = 'abcd$1234'
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
db =SQLAlchemy()

db.init_app(app)
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

# ############################################################################################################
#    Database builder
# ############################################################################################################
def buildAll():
    logging.basicConfig(level=logging.INFO)
    db.drop_all()
    db.create_all()
    Student.build()
    Instructor.build()
    Program.build()
    Course.build()
    Section.build()
    Class.build()
    Registration.build()
    return

# ############################################################################################################
#   Routes
# ############################################################################################################

@app.route("/build")
def build():
    buildAll()
    flash (f"Database rebuilt")
    return redirect(url_for("home"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/addStudent", methods=['GET', 'POST'])
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

@app.route("/addCourse")
def addCourse():
    c=input("Name")

    return c

@app.route("/register")
def register():
    c=input("Name")

    return c

# ############################################################################################################
#   Notes for future Model upgrades
# ############################################################################################################

    # references
    # userID =        db.Column ( db.Integer,                         db.ForeignKey('user.id'))
    # fieldID =       db.Column ( db.Integer,                         db.ForeignKey('user_field.id'))

# ############################################################################################################
#   Database Models
# ############################################################################################################

class Student(db.Model):
    id =            db.Column ( db.Integer,                         primary_key=True)
    dateCreated =   db.Column ( db.DateTime,    nullable=False,     default=func.now())
    dateDeleted =   db.Column ( db.DateTime,    nullable=True)
    studentID =     db.Column ( db.String(25))
    firstName =     db.Column ( db.String(25))
    lastName =      db.Column ( db.String(25))
    address =       db.Column ( db.String(25))
    emailAddress =  db.Column ( db.String(25))

    def __repr__(self):
        return f"Student(id={self.id}, studentID='{self.studentID}', firstName='{self.firstName}', lastName='{self.lastName}', address='{self.address}', emailAddress='{self.emailAddress}' (DC {self.dateCreated} DD {self.dateDeleted})"
    
    def delete(self):
        self.dateDeleted = datetime.now()
        db.session.commit()

    @classmethod
    def add(cls, studentID, firstName, lastName, address, emailAddress, id=None, log=False):
        if id is not None:
            newRecord = cls(id=id, studentID=studentID, firstName=firstName, lastName=lastName, address=address, emailAddress=emailAddress)
        else:
            newRecord = cls(       studentID=studentID, firstName=firstName, lastName=lastName, address=address, emailAddress=emailAddress)
        db.session.add(newRecord)
        db.session.commit()
        if log: logging.info(newRecord)
        return newRecord

    @classmethod
    def build(cls, log=False):
        # Used for building EXAMPLE data only DO NOT use for production
        cls.add('123123', 'Sally',      'Ostern',   'Apt 233, 123 5 Street NE, Calgary, Alberta, T2P 1T5',          'sallysmithy@telus.net',        log=log)
        cls.add('123123', 'Mike',       'Naerea',   '26 Buffalo Cresent, Calgary, Alberta, T2P 1T5',                'mike.naerea@hotmail.com',      log=log)
        cls.add('123123', 'Frank',      'Pulick',   '233, 2423 12 Ave SW, Calgary, Alberta, T2P 1T5',               'fPulick@msn.com',              log=log)
        cls.add('123123', 'Jennifer',   'Armensta', 'Apt 109, 1212 45 Ave NW, Calgary, Alberta, T2P 1T5',           'jenn.armensta@hotmail.com',    log=log)
        cls.add('123123', 'Lindsey',    'Secrude',  'Basement suite, 9838 26 Street SE, Calgary, Alberta, T2P 1T5', 'linSecrude@proton.me',         log=log)
        cls.add('123123', 'Jacob',      'Quincey',  '3412 5 Stree NE, Calgary, Alberta, T2P 1T5',                   'nabsterBoss@hotmail.com',      log=log)
        cls.add('123123', 'Mimi',       'Nagarm',   '#204, 4322 12 Street SE, Calgary, Alberta, T2P 1T5',           'minimimi@hotmail.com',         log=log)
        cls.add('123123', 'Okland',     'Welton',   'Apartment 2498, 2452 28 Ave SW, Calgary, Alberta, T2P 1T5',    'weltonO@jertu.com',            log=log)
        cls.add('123123', 'Peter',      'Sugar',    '1562 9th Street NE, Calgary, Alberta, T2P 1T5',                'sweetstuff1@gmail.com',        log=log)
        return

class Instructor(db.Model):
    id =            db.Column ( db.Integer,                         primary_key=True)
    dateCreated =   db.Column ( db.DateTime,    nullable=False,     default=func.now())
    dateDeleted =   db.Column ( db.DateTime,    nullable=True)
    firstName =     db.Column ( db.String(25))
    lastName =      db.Column ( db.String(25))

    def __repr__(self):
        return f"Instructor(id={self.id}, firstName='{self.firstName}', lastName='{self.lastName}' (DC {self.dateCreated} DD {self.dateDeleted})"
    
    def delete(self):
        self.dateDeleted = datetime.now()
        db.session.commit()

    @classmethod
    def add(cls, firstName, lastName, id=None, log=False):
        if id is not None:
            newRecord = cls(id=id, firstName=firstName, lastName=lastName)
        else:
            newRecord = cls(       firstName=firstName, lastName=lastName)
        db.session.add(newRecord)
        db.session.commit()
        if log: logging.info(newRecord)
        return newRecord

    @classmethod
    def build(cls, log=False):
        # Used for building EXAMPLE data only DO NOT use for production
        cls.add("Iles", "Wade", log=log)
        cls.add('Ali',  "M",    log=log)
        return
    
class Program(db.Model):
    id =            db.Column ( db.Integer,                         primary_key=True)
    dateCreated =   db.Column ( db.DateTime,    nullable=False,     default=func.now())
    dateDeleted =   db.Column ( db.DateTime,    nullable=True)
    name =          db.Column ( db.String(25))
    
    def __repr__(self):
        return f"Program(id={self.id}, name='{self.name}' (DC {self.dateCreated} DD {self.dateDeleted})"
    
    def delete(self):
        self.dateDeleted = datetime.now()
        db.session.commit()

    @classmethod
    def add(cls, name, id=None, log=False):
        if id is not None:
            newRecord = cls(id=id, name=name)
        else:
            newRecord = cls(       name=name)
        db.session.add(newRecord)
        db.session.commit()
        if log: logging.info(newRecord)
        return newRecord

    @classmethod
    def build(cls, log=False):
        # Used for building EXAMPLE data only DO NOT use for production
        cls.add("SADT",     id=1, log=log)
        cls.add('Business', id=2, log=log)
        return
       
class Course(db.Model):
    id =            db.Column ( db.Integer,                         primary_key=True)
    dateCreated =   db.Column ( db.DateTime,    nullable=False,     default=func.now())
    dateDeleted =   db.Column ( db.DateTime,    nullable=True)
    name        =   db.Column ( db.String(25))
    description =   db.Column ( db.String(100))
    programID =     db.Column ( db.Integer)

    def __repr__(self):
        return f"Course(id={self.id}, name='{self.name}', description='{self.description}', programID='{self.programID}' (DC {self.dateCreated} DD {self.dateDeleted})"
    
    def delete(self):
        self.dateDeleted = datetime.now()
        db.session.commit()

    @classmethod
    def add(cls, name, description, programID, id=None, log=False):
        if id is not None:
            newRecord = cls(id=id, name=name, description=description, programID=programID)
        else:
            newRecord = cls(       name=name, description=description, programID=programID)
        db.session.add(newRecord)
        db.session.commit()
        if log: logging.info(newRecord)
        return newRecord

    @classmethod
    def build(cls, log=False):
        # Used for building EXAMPLE data only DO NOT use for production
        SADTProgramID = 1
        cls.add("CPSY200", 'A course to improve your ability to capture, document, and share business requirements with Stakeholders', SADTProgramID, log=log)
        cls.add('CPRG217', 'A good course, but not as much fun as the CPSY200 course that Iles teaches', SADTProgramID, log=log)
        cls.add('CPRG248', 'A good course, but not as much fun as the CPSY200 course that Iles teaches', SADTProgramID, log=log)
        return

class Section(db.Model):
    id =            db.Column ( db.Integer,                         primary_key=True)
    dateCreated =   db.Column ( db.DateTime,    nullable=False,     default=func.now())
    dateDeleted =   db.Column ( db.DateTime,    nullable=True)
    sectionCode =   db.Column ( db.String(3))
    dateStart =     db.Column ( db.DateTime,    nullable=True)
    dateEnd =       db.Column ( db.DateTime,    nullable=True) 
    programID =     db.Column ( db.Integer)
    
    def __repr__(self):
        return f"Section(id={self.id}, sectionCode='{self.sectionCode}', dateStart='{self.dateStart}', dateEnd='{self.dateEnd}', programID='{self.programID}',  (DC {self.dateCreated} DD {self.dateDeleted})"
    
    def delete(self):
        self.dateDeleted = datetime.now()
        db.session.commit()

    @classmethod
    def add(cls, sectionCode, dateStart, dateEnd, programID, id=None, log=False):
        if id is not None:
            newRecord = cls(id=id, sectionCode=sectionCode, dateStart=dateStart, dateEnd=dateEnd, programID=programID)
        else:
            newRecord = cls(       sectionCode=sectionCode, dateStart=dateStart, dateEnd=dateEnd, programID=programID)
        db.session.add(newRecord)
        db.session.commit()
        if log: logging.info(newRecord)
        return newRecord

    @classmethod
    def build(cls, log=False):
        # Used for building EXAMPLE data only DO NOT use for production
        SADTProgramID = 1
        cls.add("23-3-A", datetime(2023, 9, 5), datetime(2023, 12, 15), SADTProgramID, log=log)
        cls.add("23-3-B", datetime(2023, 9, 5), datetime(2023, 12, 15), SADTProgramID, log=log)
        cls.add("23-3-C", datetime(2023, 9, 5), datetime(2023, 12, 15), SADTProgramID, log=log)
        cls.add("23-3-D", datetime(2023, 9, 5), datetime(2023, 12, 15), SADTProgramID, log=log)
        return
    
class Class(db.Model):
    id =            db.Column ( db.Integer,                         primary_key=True)
    dateCreated =   db.Column ( db.DateTime,    nullable=False,     default=func.now())
    dateDeleted =   db.Column ( db.DateTime,    nullable=True)
    courseID =      db.Column ( db.Integer)
    sectionID =     db.Column ( db.Integer)
    instructorID =  db.Column ( db.Integer)
    roomNumber =    db.Column ( db.Integer)
    
    def __repr__(self):
        return f"Class(id={self.id}, courseID='{self.courseID}', sectionID='{self.sectionID}', instructorID='{self.instructorID}', roomNumber='{self.roomNumberroom}',  (DC {self.dateCreated} DD {self.dateDeleted})"
    
    def delete(self):
        self.dateDeleted = datetime.now()
        db.session.commit()

    @classmethod
    def add(cls, courseID, sectionID, instructorID, roomNumber, id=None, log=False):
        if id is not None:
            newRecord = cls(id=id, courseID=courseID, sectionID=sectionID, instructorID=instructorID, roomNumber=roomNumber)
        else:
            newRecord = cls(       courseID=courseID, sectionID=sectionID, instructorID=instructorID, roomNumber=roomNumber)
        db.session.add(newRecord)
        db.session.commit()
        if log: logging.info(newRecord)
        return newRecord

    @classmethod
    def build(cls, log=False):
        # Used for building EXAMPLE data only DO NOT use for production
        cls.add(1, 1, 1, 14, log=log)
        cls.add(1, 2, 2, 15, log=log)
        cls.add(1, 3, 1, 14, log=log)
        cls.add(2, 1, 1, 25, log=log)

        return
      
class Registration(db.Model):
    id =            db.Column ( db.Integer,                         primary_key=True)
    dateCreated =   db.Column ( db.DateTime,    nullable=False,     default=func.now())
    dateDeleted =   db.Column ( db.DateTime,    nullable=True)
    studentID =     db.Column ( db.Integer)
    classID =       db.Column ( db.Integer)
    finalGrade =    db.Column ( db.Integer)

    def __repr__(self):
        return f"Registration(id={self.id}, studentID='{self.studentID}', classID='{self.classID}', finalGrade='{self.finalGrade}' (DC {self.dateCreated} DD {self.dateDeleted})"
    
    def delete(self):
        self.dateDeleted = datetime.now()
        db.session.commit()

    @classmethod
    def add(cls, studentID, classID, finalGrade=0, id=None, log=False):
        if id is not None:
            newRecord = cls(id=id, studentID=studentID, classID=classID, finalGrade=finalGrade)
        else:
            newRecord = cls(       studentID=studentID, classID=classID, finalGrade=finalGrade)
        db.session.add(newRecord)
        db.session.commit()
        if log: logging.info(newRecord)
        return newRecord

    @classmethod
    def build(cls, log=False):
        # Used for building EXAMPLE data only DO NOT use for production


        return
    
if __name__ == "__main__":
    app.run(debug=True)