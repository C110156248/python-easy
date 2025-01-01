from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Competition(db.Model):
    __tablename__ = 'competitions'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cName = db.Column(db.String(100), nullable=False)
    cTime = db.Column(db.DateTime, nullable=False)
    cType = db.Column(db.String(50), nullable=False)
    Place = db.Column(db.String(100), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'cName': self.cName,
            'cTime': self.cTime.isoformat(),
            'cType': self.cType,
            'Place': self.Place
        }

class TeachInfo(db.Model):
    __tablename__ = 'teachinfos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tName = db.Column(db.String(100), nullable=False)
    tType = db.Column(db.String(50), nullable=False)
    tContact = db.Column(db.String(100), nullable=False)
    tResume = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'tName': self.tName,
            'tType': self.tType,
            'tContact': self.tContact,
            'tResume': self.tResume
        }

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Name = db.Column(db.String(100), nullable=False)
    Password = db.Column(db.String(100), nullable=False)
    Account = db.Column(db.String(100), nullable=False)
    Level = db.Column(db.String(50), nullable=False)
    Mail = db.Column(db.String(100), nullable=False)
    Phone = db.Column(db.String(20), nullable=False)
    Age = db.Column(db.Integer, nullable=False)
    Gender = db.Column(db.String(10), nullable=False)
    Birthday = db.Column(db.Date, nullable=False)
    Dance_age = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'Name': self.Name,
            'Password': self.Password,
            'Account': self.Account,
            'Level': self.Level,
            'Mail': self.Mail,
            'Phone': self.Phone,
            'Age': self.Age,
            'Gender': self.Gender,
            'Birthday': self.Birthday.isoformat(),
            'Dance_age': self.Dance_age
        }

class Video(db.Model):
    __tablename__ = 'videos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Score = db.Column(db.Float, nullable=False)
    vTime = db.Column(db.DateTime, nullable=False)
    Style = db.Column(db.String(50), nullable=False)
    Introduction = db.Column(db.Text, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'Score': self.Score,
            'vTime': self.vTime.isoformat(),
            'Style': self.Style,
            'Introduction': self.Introduction
        }