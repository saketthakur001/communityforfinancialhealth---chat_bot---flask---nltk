from flask import Flask, render_template, request, jsonify
from chatbot import * # Import the chatbot.py file that contains the functions
# from icecream import ic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('chatbot.html') # Render the chatbot.html template

global chat_no, prevous_selection, first_chat, the_question, user_input, chat_mode, user_wants_to_do_the_survey

chat_no = 1
first_chat = False
prevous_selection = ""
user_input = ""
chat_mode = True
user_wants_to_do_the_survey = True

question = questions[chat_no - 1]
the_question = get_options(question)[0]

@app.route('/chatbot', methods=['POST'])
def chatbot():
    global chat_no, prevous_selection, first_chat, the_question, user_input, chat_mode, user_wants_to_do_the_survey
    # chat_mode = True
    message = request.form['message'] # Get the message from the form
    print(message)
    selected_option, list_of_options, user_input, the_question, user_text_input_required = survey_time(chat_no-1, message)
    # if first_chat:
    #     # response_data['message'] = ""
    #     first_chat = False
    #     response_data = {
    #     'message':'Hi there, you have entered the Survey',
    #     'question': the_question,
    #     'options' : list_of_options,
    #     }
    #     chat_no+=1
    #     return jsonify(response_data)

    if chat_mode:
        print('chat mode is enabled')
        selected_option, list_of_options, user_input, the_question, chat_mode = get_response(message)
        if not chat_mode: 
            first_chat = True
            list_of_options, the_question = get_the_question(chat_no)
            response_data = {
                'message':'You have entered the survey.',
                # 'message': 
                'question': the_question,
                'options' : ' ',
            } 
            # if list_of_options[0] != "user_input_required":
            #     response_data['options'] = list_of_options
            # else:user_input = message
            prevous_selection = selected_option
            # global prevous_selection 
            chat_no += 1
            return jsonify(response_data)
        if user_wants_to_do_the_survey:
            the_question = the_question+'     Do you wanna start a survey?'
        response_data = {
            'message':the_question,
            # 'message': 
            # 'question': the_question,
            'options' : list_of_options,
            'user_input' : user_input,
        }
        if not chat_mode: first_chat = True
        
        return jsonify(response_data)

    # Return the selected option, the list of options, the user input, and the actual questionselected_option, list_of_options, user_input, the_question = survey_time(chat_no-1, message)
    print('user text input required is ', user_text_input_required, 'and the message is ','attention required'*100)
    if user_text_input_required:
        selected_option = message
        print('user text input required is ', user_text_input_required, 'and the message is ', message)
        print(selected_option)
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