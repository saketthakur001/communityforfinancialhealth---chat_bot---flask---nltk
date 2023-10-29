from flask import Flask, render_template, request, jsonify
from chatbot import * # Import the chatbot.py file that contains the functions

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chatbot.html') # Render the chatbot.html template

global chat_no, prevous_selection

chat_no = 11
prevous_selection = ""

@app.route('/chatbot', methods=['POST'])
def chatbot():
    
    message = request.form['message'] # Get the message from the form
    print(message)
    response_data = {
    'message': 'Your response to the previous question has been recorded.',
    'question': '2. Mention your gender',
    'options': ['A. Male', 'B. Female', 'C. Other']}
    global chat_no, prevous_selection
    # Return the selected option, the list of options, the user input, and the actual question
    selected_option, list_of_options, user_input, the_question = survey_time(chat_no, message)

    response_data = {
        'message':'recorded "'+prevous_selection+'" as your previous question.',
        'question': the_question,
        'options' : list_of_options,
    }

    # global prevous_selection 
    chat_no += 1
    prevous_selection = selected_option
    return jsonify(response_data)
    # return jsonify({'message': response}) # Return the response as a JSON object

if __name__ == '__main__':
    app.run(debug=True)