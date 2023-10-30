from flask import Flask, request, render_template
from chatbot import *

app = Flask(__name__)

question_num = 1

@app.route("/", methods=["GET", "POST"])  
def index():
  global question_num
  
  if request.method == "POST":
    user_input = request.form["user_input"]
    
    # Call survey bot function
    selected_option, options, user_input, question = survey_time(question_num, user_input)
    
    # Construct bot response
    bot_text = f"You selected: {selected_option}<br>Question {question_num}: {question}" 
    
    question_num += 1
    
    return render_template("chatbot.html", bot_output=bot_text)

  return render_template("chatbot.html")

if __name__ == "__main__":
  app.run()