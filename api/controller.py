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
######## user and Vendor, create and login #########
@app.route('/create_user', methods=['POST'])
def create_user():
    try:
        req = request.get_json()
        common_obj = Common(20)
        u = User(req, common_obj.generate_uuid())
        u.save_data()
        return jsonify(status='200', body="success")
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
        return jsonify(status='200', body="success")
    except Exception as e:
        print(e)
        return jsonify(status='400', body="faliure")

@app.route('/user_login', methods=['POST'])
def get_user_profile():
    try:
        req = request.get_json()
        u = User(req)
        uuid = u.verify_login()
        return jsonify(status='200', user_id=uuid)
    except Exception as e:
        print(e)
        return jsonify(status='400', body="faliure")

@app.route('/vendor_login', methods=['POST'])
def get_vendor_profile():
    try:
        req = request.get_json()
        v = Vendor(req)
        uuid = v.verify_login()
        return jsonify(status='200',id=uuid)
    except Exception as e:
        print(e)
        return jsonify(status='400', body="faliure")
#######################################################################
######## Save reward, redeem, get all types, get total ###############
@app.route('/save_rewards', methods=['POST'])
def save_rewards():
    try:
        save_request = request.get_json()
        total_score = 0
        for t in list(save_request):
            if t in ['vendor_id', 'user_id']:
                continue
            req = save_request
            common_obj = Common(20)
            req['date'] = datetime.datetime.now()
            req['uuid'] = common_obj.generate_uuid()
            req['points'] = req[t]
            req['type'] = t
            r = Reward(req)
            r.save_data()

        upm = UserPointMapper(req['user_id'], common_obj.generate_uuid(), total_score)
        upm.save_data()
        return jsonify(status='200', body="success")
    except Exception as e:
        print(e)
        return jsonify(status='400', body="faliure")

@app.route('/get_rewards', methods=['POST'])
def get_total_rewards():
    try:
        req = request.get_json()
        upm = UserPointMapper(req['user_id'])
        score = upm.get_total_reward()
        return jsonify(status='200',score=score)
    except Exception as e:
        print(e)
        return jsonify(status='400', body="faliure")


@app.route('/user_timeline', methods=['POST'])
def get_user_timeline():
    try:
        req = request.get_json()
        r = Reward(req)
        records = r.get_reward_details()
        response = dict()
        if records is None:
            return
        for r in records:
            if r.type in response :
                response[r.type] += r.points
            else:
                response[r.type] = r.points
            # record = {"type": r.type, "points": r.points}
        return jsonify(status=200, body=response)
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
