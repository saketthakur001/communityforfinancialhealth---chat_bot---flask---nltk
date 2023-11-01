from flask import Flask, render_template, request, jsonify
from chatbot import * # Import the chatbot.py file that contains the functions

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chatbot.html') # Render the chatbot.html template

global chat_no, prevous_selection, first_chat, the_question, user_input, chat_mode

chat_no = 12
first_chat = True
prevous_selection = ""
user_input = ""
chat_mode = True

question = questions[chat_no - 1]
the_question = get_options(question)[0]

@app.route('/chatbot', methods=['POST'])
def chatbot():
    global chat_no, prevous_selection, first_chat, the_question, user_input, chat_mode
    chat_mode = True
    message = request.form['message'] # Get the message from the form
    print(message)
    if first_chat: 
        # response_data['message'] = ""
        first_chat = False
        response_data = {
        'message':'Hi there I am a chatbot, and it\'s time to take a survey.',
        # 'question': the_question,
        # 'options' : list_of_options,
        }
        return jsonify(response_data)

    # Return the selected option, the list of options, the user input, and the actual question
    selected_option, list_of_options, user_input, the_question = survey_time(chat_no-1, message)
    if selected_option:
        list_of_options, the_question = get_the_question(chat_no)
        response_data = {
            'message':'You have selected"'+selected_option+'" as your previous response.',
            # 'message': 
            'question': the_question,
            'options' : list_of_options,
        }
        user_input = message
        prevous_selection = selected_option

        # global prevous_selection 
        chat_no += 1
    else:
        response_data = {
            'message':'Please try again with the correct option',
            # 'message': 
            'question': the_question,
            'options' : list_of_options,
        }
    return jsonify(response_data)
    # return jsonify({'message': response}) # Return the response as a JSON object

if __name__ == '__main__':
    app.run(debug=True)