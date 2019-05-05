from sqlalchemy import *
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker

db = create_engine('sqlite:///tutorial.db')
db.echo = True
metadata = MetaData(db)
vendors = Table('vendors', metadata, autoload=True)
Session = sessionmaker(bind=db)
class Vendor:
    def __init__(self, req, uuid=''):
        self.vendor_id = uuid
        self.name = req['name']
        self.location = req['location'] if 'location' in req else ''
        self.password = req['password']
        self.reward_type = req['reward_type'] if 'reward_type' in req else ''
        
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
            record = session.query(Vendor).filter_by(password=self.password, name=self.name).first()
            if record is None:
                return ''
        except:
            session.rollback()
            raise
        finally:
            session.close()
            return '' if record is None else record.vendor_id
        
vendormapper = mapper(Vendor, vendors)
