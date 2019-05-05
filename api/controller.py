from flask import Flask, request, jsonify
import json
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
        return jsonify(status='200', body="sucess")
    except Exception as e:
        print(e)
        return jsonify(status='400', body="faliure")

@app.route('/create_vendor', methods=['POST'])
def create_vendor():
    try:
        req = request.get_json()
        common_obj = Common(20)
        v = Vendor(req, common_obj.generate_uuid())
        v.save_data()
        return jsonify(status='200', body="sucess")
    except Exception as e:
        print(e)
        return jsonify(status='400', body="faliure")


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
        return jsonify(status='200', body="sucess")
    except Exception as e:
        print(e)
        return jsonify(status='400', body="faliure")


@app.route('/redeem', methods=['POST'])
def redeem_rewards():
    try:
        req = request.get_json()
        upm = UserPointMapper(req['user_id'])
        score = upm.redeed_reward(req['points'])
        return jsonify(status='200', updated=score)
    except Exception as e:
        print(e)
        return jsonify(status='400', body="faliure")

@app.route('/get_rewards', methods=['GET'])
def get_total_rewards():
    try:
        req = request.get_json()
        upm = UserPointMapper(req['user_id'])
        score = upm.get_total_reward()
        return jsonify(status='200',score=score)
    except Exception as e:
        print(e)
        return jsonify(status='400', body="faliure")

@app.route('/user_login', methods=['GET'])
def get_user_profile():
    try:
        req = request.get_json()
        u = User(req)
        uuid = u.verify_login()
        return jsonify(status='200', uuid=uuid)
    except Exception as e:
        print(e)
        return jsonify(status='400', body="faliure")

@app.route('/vendor_login', methods=['GET'])
def get_vendor_profile():
    try:
        req = request.get_json()
        v = Vendor(req)
        uuid = v.verify_login()
        return jsonify(status='200',uuid=uuid)
    except Exception as e:
        print(e)
        return jsonify(status='400', body="faliure")


@app.route('/user_timeline', methods=['GET'])
def get_user_timeline():
    try:
        req = request.get_json()
        r = Reward(req)
        records = r.get_reward_details()
        response = []
        if records is None:
            return
        for r in records:
            record = {"type": r.type, "points": r.points}
            response.append(record)
        return jsonify(status=200, body=response)
    except Exception as e:
        print(e)
        return jsonify(status='400', body="faliure")
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
    app.run(host='0.0.0.0', port=5000)
