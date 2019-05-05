from flask import Flask, request, jsonify
from sqlalchemy import *
from helper.common import Common, RewardTypes
from helper.user_mapper import User
from helper.vendor_mapper import Vendor
from helper.reward_mapper import Reward
from helper.user_points_mapper import UserPointMapper
import datetime

app = Flask(__name__)

@app.route('/create_user', methods=['POST'])
def create_user():
    try:
        req = request.get_json()
        common_obj = Common(20)
        u = User(req, common_obj.generate_uuid())
        u.save_data()
        return jsonify(status='200')
    except Exception as e:
        print(e)
        return jsonify(status='400')

@app.route('/create_vendor', methods=['POST'])
def create_vendor():
    try:
        req = request.get_json()
        common_obj = Common(20)
        v = Vendor(req, common_obj.generate_uuid())
        v.save_data()
        return jsonify(status='200')
    except Exception as e:
        print(e)
        return jsonify(status='400')


@app.route('/save_rewards', methods=['POST'])
def save_rewards():
    try:
        req = request.get_json()
        common_obj = Common(20)
        req['date'] = datetime.datetime.now()
        req['uuid'] = common_obj.generate_uuid()
        r_type = req['type'].upper()
        req['points'] = RewardTypes[r_type].value
        r = Reward(req)
        r.save_data()
        upm = UserPointMapper(req['user_id'], common_obj.generate_uuid(), req['points'])
        upm.save_data()
        return jsonify(status='200')
    except Exception as e:
        print(e)
        return jsonify(status='400')


@app.route('/redeem', methods=['POST'])
def redeem_rewards():
    try:
        req = request.get_json()
        upm = UserPointMapper(req['user_id'])
        score = upm.redeed_reward(req['points'])
        return jsonify(updated_score=score)
    except Exception as e:
        print(e)
        return jsonify(status='400')

@app.route('/get_rewards', methods=['GET'])
def get_total_rewards():
    try:
        req = request.get_json()
        upm = UserPointMapper(req['user_id'])
        score = upm.get_total_reward()
        return jsonify(score=score)
    except Exception as e:
        print(e)
        return jsonify(status='400')

@app.route('/user_login', methods=['GET'])
def get_user_profile():
    try:
        req = request.get_json()
        u = User(req)
        uuid = u.verify_login()
        return jsonify(uuid=uuid)
    except Exception as e:
        print(e)
        return jsonify(status='400')

@app.route('/vendor_login', methods=['GET'])
def get_vendor_profile():
    try:
        req = request.get_json()
        v = Vendor(req)
        uuid = v.verify_login()
        return jsonify(uuid=uuid)
    except Exception as e:
        print(e)
        return jsonify(status='400')

# @app.route('/total_rewards', methods=['GET'])
# def get_total_score():
#     try:
#         req = request.get_json()
#         upm = UserPointMapper(req['user_id'])
#         score = upm.get_total_reward()
#         return jsonify(score=score)
#     except Exception as e:
#         print(e)
#         return jsonify(status='400')

if __name__ == '__main__':
    app.run()
