from schema import users, vendors, vendor_point_details, user_point_details, rewards
import datetime
# if __name__ == "__main__":
user_insert = users.insert()
user_insert.execute(
    {'user_id': 'ABCD123asda','name': 'test', 'age': 30, 'password': 'abcd@1234', 'email': 'test@gmail.com' },
    {'user_id': 'ABCD123asda1','name': 'test1', 'age': 35, 'password': 'abcd@1234', 'email': 'test@gmail.com' },
    {'user_id': 'ABCD123asda123','name': 'test2', 'age': 40, 'password': 'abcd@1234', 'email': 'test@gmail.com' }
)

vendor_insert = vendors.insert()
vendor_insert.execute(
    {'vendor_id': 'ABCD123asda','name': 'tim', 'location': 'Robson st, Van','password': 'abcd@1234', 'reward_type': 'cup' },
    {'vendor_id': 'ABCD123asda1','name': 'superstore', 'location': 'schoolhouse st, Coq','password': 'abcd@1234', 'reward_type': 'bag' }
)

reward_insert = rewards.insert()
reward_insert.execute(
    {'id': 'ABCD123asda','name': 'reward for mug/tumbler', 'type': 'cup','date': datetime.now(), 'points': 200, 'vendor_id': 'ABCD123asda', 'user_id': 'ABCD123asda' },
    {'id': 'ABCD123asda','name': 'reward for mug/tumbler', 'type': 'cup','date': datetime.now(), 'points': 200, 'vendor_id': 'ABCD123asda', 'user_id': 'ABCD123asda1' }
)

upd_insert = user_point_details.insert()
upd_insert.execute(
    {'id': 'ABCD123asda','total_points': 200,'user_id': 'ABCD123asda' },
    {'id': 'ABCD123asda1','total_points': 200,'user_id': 'ABCD123asda1' })

vpd_insert = vendor_point_details.insert()
vpd_insert.execute(
    {'id': 'ABCD123asda','total_points': 400,'vendor_id': 'ABCD123asda' },
    {'id': 'ABCD123asda1','total_points': 0,'vendor_id': 'ABCD123asda1' })
