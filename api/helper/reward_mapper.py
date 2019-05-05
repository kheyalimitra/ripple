from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker
import json

db = create_engine('sqlite:///tutorial.db')
db.echo = True
metadata = MetaData(db)
rewards = Table('rewards', metadata, autoload=True)
Session = sessionmaker(bind=db)
class Reward:
    def __init__(self, req):
        self.id = req['uuid'] if 'uuid' in req else ''
        self.name = req['name'] if 'name' in req else ''
        self.type = req['type'] if 'type' in req else ''
        self.date =  req['date'] if 'date' in req else ''
        self.points = req['points'] if 'points' in req else ''
        self.vendor_id = req['vendor_id'] if 'vendor_id' in req else ''
        self.user_id = req['user_id'] 
        
    def __repr__(self):
        return self

    def save_data(self):
        session = Session()
        try:
            # record = session.query(Reward).filter_by(user_id=self.user_id, vendor_id=self.vendor_id, type=self.type).first()
            # if record is None:
            session.add(self)
            # # else:
            #     session.query(Reward).filter_by(user_id=self.user_id, vendor_id=self.vendor_id, type=self.type).]]update()
            # #     session.update(Reward).where(user_id=self.user_id, vendor_id=self.vendor_id, type=self.type).values(points=self.points)
            session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def get_reward_details(self):
        session = Session()
        records = None
        try:
            # records = session.query(Reward.type,func.sum(Reward.points)).filter_by(user_id=self.user_id).group_by(Reward.type).all()
            records = session.query(Reward).filter_by(user_id=self.user_id).all()
            if records is None:
                    return None
        except:
            session.rollback()
            raise
        finally:
            session.close()
            return records





vendormapper = mapper(Reward, rewards)
