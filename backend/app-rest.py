from flask import Flask, request, jsonify
from flask_cors import CORS
from langchain_community.llms import Ollama

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

llm = Ollama(model="llama3")

print("Starting server...")

def send_message(message):
    response = llm.invoke(message)
    return response

@app.route('/api/message', methods=['POST'])
def handle_message():
    data = request.get_json()
    if not data or 'message' not in data:
        return jsonify({'error': 'Invalid request'}), 400
    
    try:
        message = data['message']
        print(f"-Client request: {message}")
        result = send_message(message)
        print(f"-AI Response: {result}")
        return jsonify({'response': result}), 200
    except Exception as e:
        print(e)
        return jsonify({'error': 'Operation failed'}), 500


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
