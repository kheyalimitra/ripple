from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker

db = create_engine('sqlite:///tutorial.db')
db.echo = True
metadata = MetaData(db)
users = Table('users', metadata, autoload=True)
Session = sessionmaker(bind=db)
class User:
    def __init__(self, req, uuid=''):
        self.user_id = uuid
        self.name = req['name'] if 'name' in req  else ''
        self.age = req['age'] if 'age'in req else 0
        self.password = req['password']
        self.email = req['email']
        
    def __repr__(self):
        return self

    def save_data(self):
        session = Session()
        try:
            session.add(self)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()
        
    def verify_login(self):
        session = Session()
        record = None
        try:
            record = session.query(User).filter_by(password=self.password, email=self.email).first()
            if record is None:
                return ''
        except:
            session.rollback()
            raise
        finally:
            session.close()
            return '' if record is None else record.user_id

        
usermapper = mapper(User, users)
