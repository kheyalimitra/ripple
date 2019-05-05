import random
import string
from enum import Enum
class Common:

    def __init__(self, uuid_length):
        self.uuid_length = uuid_length
    def generate_uuid(self):
        range_set = string.ascii_letters + string.digits
        random_str = []
        for i in range(20):
            random_str.append(random.choice(range_set))
        return ''.join(random_str) 
        
class RewardTypes(Enum):
    BAG = 500
    CONTAINER = 300
    CUP = 200
    CUTLERY = 100
