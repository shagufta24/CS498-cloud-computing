from flask import Flask, request, jsonify
app = Flask(__name__)

num = 0

@app.route('/', methods=['POST'])
def update_number():
    global num
    data = request.get_json()
    new_num = data.get('num')
    if new_num is not None:
        num = new_num
        return jsonify({'message': 'Number updated successfully'}), 200
    else:
        return jsonify({'error': 'Invalid data provided'}), 400
    
@app.route('/', methods=['GET'])
def get_number():
    global num
    return str(num), 200

if __name__ == '__main__':
   app.run(host="0.0.0.0")