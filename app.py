from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    try:
        a = float(data['a'])
        b = float(data['b'])
        op = data['operation']
        
        if op == '+':
            result = a + b
        elif op == '-':
            result = a - b
        elif op == '*':
            result = a * b
        elif op == '/':
            if b != 0:
                result = a / b
            else:
                return jsonify({'error': 'Division by zero'}), 400
        else:
            return jsonify({'error': 'Invalid operation'}), 400

        return jsonify({'result': result})
    except KeyError:
        return jsonify({'error': 'Invalid input'}), 400
    except ValueError:
        return jsonify({'error': 'Invalid number format'}), 400

@app.route('/')
def index():
    return send_from_directory('', 'index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('', filename)

if __name__ == '__main__':
    app.run(debug=True)
