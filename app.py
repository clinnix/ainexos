from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/launch', methods=['POST'])
def launch():
    # 获取 JSON 数据
    data = request.get_json()

    # 提取字段
    blockchain_network = data['blockchain_network']
    token_ca = data['token_ca']
    birth_date = data['birth_date']
    birth_time = data['birth_time']
    birth_place = data['birth_place']
    gender = data['gender']

    # 返回响应
    response = {
        'personnal_fate': f'Based on {birth_place} and {gender}, your fate is optimistic.',
        'token_fate': f'Token {token_ca} on {blockchain_network} shows growth potential.',
        'personal_token': f'Your personal token aligns with {birth_date} {birth_time}.',
        'ai_fusion': 'AI predicts a balanced fusion of personal and token destiny.'
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run()
