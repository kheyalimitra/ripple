import random
import string
from enum import Enum
import json
from sqlalchemy.ext.declarative import DeclarativeMeta
class Common:

    def __init__(self, uuid_length=''):
        self.uuid_length = uuid_length
    def generate_uuid(self):
        range_set = string.ascii_letters + string.digits
        random_str = []
        for i in range(20):
            random_str.append(random.choice(range_set))
        return ''.join(random_str) 
    
    def new_alchemy_encoder(self):
        _visited_objs = []

        class AlchemyEncoder(json.JSONEncoder):
            def default(self, obj):
                if isinstance(obj.__class__, DeclarativeMeta):
                    # don't re-visit self
                    if obj in _visited_objs:
                        return None
                    _visited_objs.append(obj)

                    # an SQLAlchemy class
                    fields = {}
                    for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                        fields[field] = obj.__getattribute__(field)
                    # a json-encodable dict
                    return fields

                return json.JSONEncoder.default(self, obj)

        return AlchemyEncoder 
        
class RewardTypes(Enum):
    BAG = 500
    CONTAINER = 300
    CUP = 200
    CUTLERY = 100
