from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker

db = create_engine('sqlite:///tutorial.db')
db.echo = True
metadata = MetaData(db)
rewards = Table('rewards', metadata, autoload=True)
Session = sessionmaker(bind=db)
class Reward:
    def __init__(self, req):
        self.id = req['uuid']
        self.name = req['name']
        self.type = req['type']
        self.date =  req['date']
        self.points = req['points']
        self.vendor_id = req['vendor_id']
        self.user_id = req['user_id']
        
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
        
vendormapper = mapper(Reward, rewards)
