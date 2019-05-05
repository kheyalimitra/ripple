from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker

db = create_engine('sqlite:///tutorial.db')
db.echo = True
metadata = MetaData(db)
point_mapper = Table('userPointDetails', metadata, autoload=True)
Session = sessionmaker(bind=db)
class UserPointMapper:
    def __init__(self, user_id, uuid='', score=''):
        self.id = uuid
        self.total_Point = score
        self.user_id = user_id
        
    def __repr__(self):
        return self

    def save_data(self):
        session = Session()
        try:
            record = session.query(UserPointMapper).filter_by(user_id=self.user_id).first()
            if record is not None:
                score =  self.total_Point if record.total_Point == None else record.total_Point + self.total_Point
                session.query(UserPointMapper).update({"total_Point": score})
                session.commit()
            else:
                session.add(self)
                session.commit()
        except:
            session.rollback()
            raise
        finally:
            session.close()

    def get_total_reward(self):
        session = Session()
        record = None
        try:
            record = session.query(UserPointMapper).filter_by(user_id=self.user_id).first()
            if record is None:
                return 0
        except:
            session.rollback()
            raise
        finally:
            session.close()
            return record.total_Point
    
    def redeed_reward(self, point):
        session = Session()
        try:
            record = session.query(UserPointMapper).filter_by(user_id=self.user_id).first()
            if record is not None:
                score =  0 if record.total_Point == None else record.total_Point - point
                session.query(UserPointMapper).update({"total_Point": score})
                session.commit()
                return score
            else:
                return 0
        except:
            session.rollback()
            raise
        finally:
            session.close()
        
user_point_mapper = mapper(UserPointMapper, point_mapper)
