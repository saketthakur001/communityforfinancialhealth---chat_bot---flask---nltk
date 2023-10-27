from flask import Flask, request, jsonify
import chatbot

app = Flask(__name__)

@app.route('/api/chatbot', methods=['POST'])
def chat():
    user_input = request.json['user_input']
    
    response = chatbot.get_response(user_input)
    
    return jsonify({'bot_response': response}) 

if __name__ == '__main__':
    app.run(debug=True)