from sqlalchemy import *
import datetime
db = create_engine('sqlite:///tutorial.db') # ToDo : change it to evergreen
db.echo = False 
metadata = MetaData(db)
#### Table Schema #########
users = Table('users', metadata,
    Column('user_id', String(20), primary_key=True),
    Column('name', String(40)),
    Column('age', Integer),
    Column('password', String),
    Column('email', String(32))
)

vendors = Table('vendors', metadata,
    Column('vendor_id', String(20), primary_key=True),
    Column('name', String(40)),
    Column('location', String(50)),
    Column('password', String),
    Column('reward_type', String(30))
)

rewards = Table('rewards', metadata,
    Column('id', String(20), primary_key=True),
    Column('name', String(40)),
    Column('type', String(50), ForeignKey('vendors.reward_type')),
    Column('date', DateTime),
    Column('points', Integer),
    Column('vendor_id', String(20), ForeignKey('vendors.vendor_id')),
    Column('user_id', String(20), ForeignKey('users.user_id'))
)
user_point_details = Table('userPointDetails', metadata,
    Column('id', String(20), primary_key=True),
    Column('total_Point', BigInteger),
    Column('user_id', String(20), ForeignKey('users.user_id'))
)
vendor_point_details = Table('vendorPointDetails', metadata,
    Column('id', String(20), primary_key=True),
    Column('total_Point', BigInteger),
    Column('vendor_id', String(20), ForeignKey('vendors.vendor_id'))
)
#########################
#### creation of tables  ################
# users.drop()
# users.create()
# vendors.create()
# rewards.create()
# user_point_details.create()
# vendor_point_details.create()
#####

### insert 
#####
#### select ####

def run(stmt):
    rs = stmt.execute()
    for row in rs:
        print(row)

# This will return more results than you are probably expecting.
s = select([user_point_details])
run(s)

# Base = declarative_base()
# engine = create_engine('postgresql://usr:pass@localhost:5432/sqlalchemy')
# Session = sessionmaker(bind=engine)
# class User(Base):
#     __tablename__ = 'users'
#     id=Column(String(20), primary_key=True)
#     first_name=Column('firstname', String(32))
#     last_name=Column('lastname', String(32))
#     email=Column('email', String(32))

#     def __init__(self, title, release_date):
#         self.title = title
#         self.release_date = release_date

# class Vendor(Base):
#     __tablename__ = 'vendors'
#     id=Column(String(20), primary_key=True)
#     name=Column('name', String(32))
#     address=Column('address', String(100))
#     provice=Column('province', String(2))


# class Rewards(Base):
#     __tablename__ = 'rewards'
#     id=Column(String(20), primary_key=True)
#     type=Column('type', String(30))
#     date=Column('date', Date)
#     point=Column('point', Integer)

# class UserPointDetails(Base):
#     __tablename__ = 'userPointDetails'
#     id=Column(String(20), primary_key=True)
#     user_id=Column('userID', String(20))
#     total=Column('total', Integer)

# class VendorPointDetails(Base):
#     __tablename__ = 'vendorPointDetails'
#     id=Column(String(20), primary_key=True)
#     user_id=Column('vendorID', String(20))
#     total=Column('total', Integer)
