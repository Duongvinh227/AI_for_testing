from flask import Flask, request, jsonify
import json

app = Flask(__name__)

try:
    with open("users.json", "r") as file:
        users_data = json.load(file)
except FileNotFoundError:
    users_data = {"users": []}

def save_users_to_json(data):
    with open("users.json", "w") as file:
        json.dump(data, file)

@app.route('/create_user', methods=['POST'])
def create_user():
    user_data = request.get_json()

    if 'username' not in user_data or 'password' not in user_data:
        return jsonify({"message": "Dữ liệu không hợp lệ"}), 400

    user_id = len(users_data["users"]) + 1

    new_user = {"id": user_id, "username": user_data['username'], "password": user_data['password']}
    users_data["users"].append(new_user)
    save_users_to_json(users_data)

    return jsonify({"message": "Thông tin người dùng đã được tạo thành công"}), 201

@app.route('/login', methods=['POST'])
def login():
    login_data = request.get_json()

    if 'username' not in login_data or 'password' not in login_data:
        return jsonify({"message": "Dữ liệu không hợp lệ"}), 400

    username = login_data['username']
    password = login_data['password']

    for user in users_data["users"]:
        if user['username'] == username and user['password'] == password:
            return jsonify({"message": "Đăng nhập thành công"}), 200

    return jsonify({"message": "Tên người dùng hoặc mật khẩu không đúng"}), 401

if __name__ == '__main__':
    app.run(debug=True)
