from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from uuid import uuid4
import datetime
db = SQLAlchemy()

def get_uuid():
    return uuid4().hex

class User(db.Model):
    __tablename__ = "user"
    id = Column(String(), primary_key=True, unique=True,default = get_uuid)
    email = Column(String(), unique=True)
    password = Column(Text, nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

class Teacher(db.Model):
    __tablename__ = "teacher"
    id = Column(String(), primary_key= True, unique=True)
    name = Column(String())
    classes = Column(String(), ForeignKey("course.id") )

class Review(db.Model):
    __tablename__ = 'review'
    id = Column(String(), primary_key=True, default= get_uuid)
    course = Column(String(), ForeignKey('course.id'))
    teacher = Column(String(), ForeignKey('teacher.id', ondelete= 'CASCADE'))
    quality = Column(Integer())
    difficulty = Column(Integer())
    review_text = Column(String())
    review_date = Column(DateTime, default=datetime.datetime.now())
    reviewer_id = Column(String(), ForeignKey('user.id', ondelete= 'CASCADE'))
    
    def save(self):
        db.session.add(self)
        db.session.commit()

class Course(db.Model):
    __tablename__ = 'course'
    id = Column(String(), primary_key= True, unique = True)
    name = Column(String())
    code = Column(String())
    subject = Column(String())
