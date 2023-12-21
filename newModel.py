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
        return f"Student(id={self.id}, studentID='{self.studentID}', firstName='{self.firstName}', lastName='{self.lastName}', address='{self.address}',) emailAddress='{self.emailAddress}', (DC {self.dateCreated} DD {self.dateDeleted})"
    
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
    cred =          db.Column ( db.Interg)


    def __repr__(self):
        return f"Instructor(id={self.id}, firstName='{self.firstName}', lastName='{self.lastName}', cred='{self.cred}' (DC {self.dateCreated} DD {self.dateDeleted})"
    
    def delete(self):
        self.dateDeleted = datetime.now()
        db.session.commit()

    @classmethod
    def add(cls, firstName, lastName, cred, id=None, log=False):
        if id is not None:
            newRecord = cls(id=id, firstName=firstName, lastName=lastName, cred=cred)
        else:
            newRecord = cls(       firstName=firstName, lastName=lastName, cred=cred)
        db.session.add(newRecord)
        db.session.commit()
        if log: logging.info(newRecord)
        return newRecord

    @classmethod
    def build(cls, log=False):
        # Used for building EXAMPLE data only DO NOT use for production
        cls.add("Iles", "Wade",     45,         log=log)
        cls.add('Ali',  "M",        67,         log=log)

        return