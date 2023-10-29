from flask import Flask, render_template, request, jsonify
from chatbot import * # Import the chatbot.py file that contains the functions

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chatbot.html') # Render the chatbot.html template

@app.route('/chatbot', methods=['POST'])
def chatbot():
    message = request.form['message'] # Get the message from the form
    print(message)
    response_data = {
    # 'message': 'Your response to the previous question has been recorded.',
    'question': '2. Mention your gender',
    'options': ['A. Male', 'B. Female', 'C. Other']
}

    return jsonify(response_data)

    # return jsonify({'message': response}) # Return the response as a JSON object

if __name__ == '__main__':
    app.run(debug=True) # Run the app in debug mode
