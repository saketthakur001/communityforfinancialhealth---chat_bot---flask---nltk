from flask import Flask, render_template, request, jsonify
from chatbot import *

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("chatbot.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_input = request.form.get("user_input")
    question_number = 6 # You can change this to any question number you want
    selected_option, options, user_response, the_question = survey_time(question_number, user_input)
    bot_response = "You have selected " + selected_option
    return jsonify(bot_response=bot_response, question=the_question, options=options, option_selected=selected_option)

if __name__ == "__main__":
    app.run(debug=True)
