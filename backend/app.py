from flask import Flask
from flask_socketio import SocketIO, emit
from langchain_community.llms import Ollama

app = Flask(__name__)

# socketio = SocketIO(app, cors_allowed_origins="http://localhost:3000")
socketio = SocketIO(app, cors_allowed_origins="*")

# llm = Ollama(model="gemma")
llm = Ollama(model="llama3")

print("Starting server...")

# def send_message(message):
#     response = llm.invoke(message)
#     return response
    
def generate_response(message):
    completeMessage = '';
    for chunks in llm.stream(message):
        print(f"-Sending chunk: {chunks}")
#        yield chunks
        completeMessage = completeMessage + chunks
        emit('response', {'response': chunks})
        socketio.sleep(0)
    print(f"AI Response: {completeMessage}")

@socketio.on('message')
def handle_socket_message(data):
    try:
        print(f"-Client request: {data}")
        message = data + ". Responda em portugues. Seja breve."
        print(f"-Handled message: {message}")
        print("-- Loading... --")
        generate_response(message)
    except Exception as e:
        print(e)
        emit('response', {'error': 'Operation failed'})

if __name__ == "__main__":
    socketio.run(app, host='0.0.0.0', port=5000)
