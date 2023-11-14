from flask import Flask, render_template, request, jsonify
from chatbot import * 
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
# from icecream import ic

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///USER_RESPONSE.sqlite3'

db = SQLAlchemy(app)

class UserResponse(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    questionNo = db.Column(db.Integer, nullable=False)
    question = db.Column(db.String(250), nullable=False)
    options = db.Column(db.String(250), nullable=False)
    # user_response = db.Column(db.String, nullable=False)
    # q1 = db.Column(db.Integer, nullable=False)
    # q2 = db.Column(db.Integer, nullable=False)
    score = db.Column(db.Integer, nullable=True)
    # for i in range(1, 38):
    #     locals()[f'q{i}'] = db.Column(db.Integer, nullable=False)

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    phoneNo = db.Column(db.String(10), nullable=False)
    date_registered = db.Column(db.DateTime, nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('chatbot.html') # Render the chatbot.html template
global chat_no, prevous_selection, first_chat, the_question, user_input, chat_mode, user_wants_to_do_the_survey, score

chat_no = 1
temp_chat_on = None
first_chat = False
prevous_selection = ""
user_input = ""
chat_mode = True
user_wants_to_do_the_survey = True
question = questions[chat_no - 1]
the_question = get_options(question)[0]

score = []
user_responses = []

@app.route('/chatbot', methods=['POST'])
def chatbot():
    global chat_no, prevous_selection, first_chat, the_question, user_input, chat_mode, user_wants_to_do_the_survey
    # chat_mode = True
    message = request.form['message'].split('__VOICE__')[-1]
    user_message = request.form.get('message')
    dropdown_value = request.form.get('dropdownValue')
    if dropdown_value:
        chat_no = int(dropdown_value)
        temp_chat_no = True                 
    else:
        temp_chat_no = False

    # message
    print(dropdown_value, 'dropdown value'*10)
    print(message, 'message!!'*10)
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
            the_question = the_question+'\n   Do you wanna start a survey?'
        options = [i.split('-=//=-')[0] for i in list_of_options]
        print(options)
        try:
            if options[0]=='user_input_required':
                options = ' '
        except:
            options = ''
        response_data = {
            'message':the_question,
            # 'message': 
            # 'question': the_question,
            # also spliting the option with the score
            'options' : options,
            'user_input' : user_input,
        }
        print('1-1-'*10)

        for i in list_of_options:
                print(i)
        if not chat_mode: first_chat = True

        return jsonify(response_data)

    # Return the selected option, the list of options, the user input, and the actual questionselected_option, list_of_options, user_input, the_question = survey_time(chat_no-1, message)
    print('user text input required is ', user_text_input_required, 'and the message is ','attention required'*10)

    if user_text_input_required:
        selected_option = message
        print('user text input required is ', user_text_input_required, 'and the message is ', message)
        print(selected_option)

    if selected_option:
        list_of_options, the_question = get_the_question(chat_no)
        options = [i.split('-=//=-')[0] for i in list_of_options]
        try:
            if options[0]=='user_input_required':
                options = ' '
        except:
            options = ''
        msg = 'You have selected "'+selected_option.split('-=//=-')[0]+'" as your previous response.'

        if chat_no == 18:
            print(round(sum(score)/18), 'error!'*100)
            if round(sum(score)/18) < 39:
                status = 'you are financially vulnerable.'
            elif round(sum(score)/18) < 80:
                status = 'you are financially coping.'
            elif round(sum(score)/18) < 100:
                status = 'you are financially healthy'
            msg = 'You have selected "'+selected_option.split('-=//=-')[0]+f'" as your previous response. you are {status}'

        response_data = {
            'message':msg,
            # 'message': 
            'question': the_question,
            # also spliting the option with the score
            'options' : options,
        }

        if len(selected_option.split('-=//=-')) == 2:
            final_selection = selected_option.split('-=//=-')[1]
            score.append(int(final_selection))

        else: final_selection = None
        list_of_options, the_question = get_the_question(chat_no-1)

        response = {"question":the_question, "qNo":chat_no-1 ,"options":selected_option.split('-=//=-')[0], "score":final_selection}
        response_entry = UserResponse(question=the_question, questionNo=chat_no-1 ,options=selected_option.split('-=//=-')[0], score=final_selection)

        db.session.add(response_entry)
        db.session.commit()

        print('2-2-'*10)
        for i in list_of_options:
                print(i)
        user_input = message
        prevous_selection = selected_option

        # global prevous_selection 
        chat_no += 1

    else:
        options = [i.split('-=//=-')[0] for i in list_of_options]
        try:
            if options[0]=='user_input_required':
                options = ' '
        except:
            options = ' '
        response_data = {
            'message':'Please try again with the correct option',
            # 'message': 
            'question': the_question,
            # also spliting the option with the score
            'options' : options,
        }
        print('3-3-'*10)
        for i in list_of_options:
                print(i)
    print(sum(score)/18, 'score'*10)
    return jsonify(response_data)
    # return jsonify({'message': response}) # Return the response as a JSON object
app.run(debug=True)

# if __name__ == ""