from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    Integer,
    String,
    UniqueConstraint,
    Boolean,
    ForeignKey
)
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(
    'postgres://maks_test1:qwedc@localhost:5432/homework_14'
)

metadata = MetaData()
BaseModel = declarative_base(bind=engine)


class AppUsers(BaseModel):
    __tablename__ = 'app_users'
    id = Column(Integer, primary_key=True),
    users = Column(String, nullable=False),

    def __str__(self):
        return f'{self.id}{self.users}'
    __repr__ = __str__


class Tests(BaseModel):
    __tablename__ = 'tests'
    id = Column(Integer, primary_key=True),
    number = Column(Integer, nullable=False),
    test = Column(String, nullable=False)

    def __str__(self):
        return f'{self.id}{self.number}{self.test}'

    __repr__ = __str__


class Questions(BaseModel):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True),
    number = Column(Integer, nullable=False),
    text = Column(String, nullable=False)

    def __str__(self):
        return f'{self.id}{self.number}{self.text}'

    __repr__ = __str__


class TestsQuestions(BaseModel):
    __tablename__ = 'tests_questions'
    id = Column(Integer, primary_key=True),
    test_id = Column(Integer, ForeignKey('Tests.id'), primary_key=True)
    question_id = Column(Integer, ForeignKey('Questions.id'), primary_key=True)
    UniqueConstraint('test_id', 'question_id')

    def __str__(self):
        return f'{self.id}{self.test_id}{self.question_id}'

    __repr__ = __str__


class Answers(BaseModel):
    __tablename__ = 'answers'
    id = Column(Integer, primary_key=True),
    text = Column(String, nullable=False),
    is_correct = Column(Boolean, default=False),
    question_id = Column(ForeignKey('questions.id'), nullable=False)

    def __str__(self):
        return f'{self.id}{self.text}{self.is_correct}{self.question_id}'

    __repr__ = __str__


class UserAnswers(BaseModel):
    __tablename__ = 'user_answers'
    id = Column(Integer, primary_key=True),
    test_quest_id = Column(ForeignKey('test_questions.id')),
    user_id = Column(ForeignKey('app_users.id')),
    answer_id = Column(ForeignKey('answers.id'))
    UniqueConstraint('test_quest_id', 'user_id')

    def __str__(self):
        return f'{self.id}{self.test_quest_id}{self.user_id}{self.answer_id}'

    __repr__ = __str__


BaseModel.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()
