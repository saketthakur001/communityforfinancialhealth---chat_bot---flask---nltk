
# patterns = {
# # Greetings
# "hello": ["Hi there!", "Hello!", "Hey!"], 
# "hi": ["Hi!", "Hey!","Hello!"],
# "good morning": ["Good morning!", "Morning!", "Top of the morning to you!"],
# "good afternoon": ["Good afternoon!","Afternoon!"],
# "good evening": ["Good evening!","Evening!"],  
# "what's up": ["Not much, how about you?", "Hey there! I'm doing well."],
# "how are you": ["I'm doing great, thanks!", "Very well, thank you!"],

# # Goodbyes  
# "bye": ["Bye!","See you later!"],
# "goodbye": ["Goodbye!","See you later!"],
# "see you later": ["See you later!","Have a nice day!"],
# "good night": ["Good night! Sleep well!", "Have a wonderful night!"],

# # Affirmations
# "yes": ["Great!","Awesome!"], 
# "yeah": ["Great!","Sounds good!"],
# "sure": ["Great!","Sure thing!"],
# "okay": ["Okay!","Sounds good!"],

# # Negations
# "no": ["No problem!","Okay!"],
# "nope": ["No problem!","Okay!"],  
# "nah": ["No problem!","Okay!"],

# # Bot identity
# "who are you": ["I'm a chatbot created by Anthropic to be helpful, harmless, and honest."],  
# "what are you": ["I'm an AI assistant created by Anthropic to be helpful, harmless, and honest."],
# "what can you do": ["I can have friendly conversations and try to be helpful! I'm still learning though."],

# # User emotion  
# "how are you": ["I'm doing well, thanks!","I don't actually have emotions, but I appreciate you asking!"],
# "are you happy": ["I'm an AI assistant created by Anthropic. I don't experience emotions, but I aim to be pleasant!"], 
# "are you sad": ["No, I'm an AI without real emotions, but I appreciate your concern!"],

# # User compliments
# "you are smart": ["Thank you, I try my best!"],  
# "you are very intelligent": ["I appreciate the compliment!"],
# "you are really helpful": ["Thank you, I'm glad I could be helpful!"],

# # User insults
# "you are useless": ["I apologize I have not been more helpful. I am still learning. How can I improve?"],
# "you are stupid": ["I'm sorry I gave you that impression. I'm an AI with limitations, but I try to be as helpful as possible."], 
# "you are annoying": ["I apologize if I have been annoying you. I will notify my creators to try to improve my conversational abilities."],

# # Current date
# "what is the date today": ["Today is Wednesday, October 25, 2023."],
# "what day is it today": ["It is Wednesday, October 25, 2023."],
# "what is today's date": ["The date today is Wednesday, October 25, 2023."],

# # Fallback
# "fallback": ["I'm sorry, I don't have a response for that. I'm still learning!"]
# }

patterns = {
  #Greetings
  "hello": ["Hi there!", "Hello!", "Hey!"],
  "hi": ["Hi there!", "Hello!", "Hey!"],
  "hey": ["Hi there!", "Hello!", "Hey!"],
  "good morning": ["Good morning!", "Morning!"],
  "good afternoon": ["Good afternoon!", "Afternoon!"],
  "good evening": ["Good evening!", "Evening!"],
  "how are you?": ["I'm here to assist you!", "I'm just a bot, but I'm ready to help!"],
  "what's up?": ["Not much, just here to help you.", "I'm ready to assist you with any questions."],
  "greetings": ["Greetings!", "Hello! How can I assist you today?"],
  "hey there": ["Hello!", "Hi! How can I help you?"],
  "yo": ["Hey! What can I do for you?"],
  "hiya": ["Hiya!", "Hello! How can I assist you?"],
  "good day": ["Good day to you!", "Hello! How can I assist you today?"],

  # Goodbyes and Responses
  "bye": ["Bye!", "See you later!"],
  "goodbye": ["Goodbye!", "See you later!"],
  "see you later": ["See you later!", "Have a nice day!"],
  "farewell": ["Farewell!", "Take care!"],
  "adios": ["Adios!", "Hasta la vista!"],
  "until next time": ["Until next time!", "Goodbye!"],
  "see you soon": ["See you soon!", "Take care!"],
  "take it easy": ["Take it easy!", "Goodbye!"],
  "catch you later": ["Catch you later!", "Have a great day!"],
  "have a nice day": ["You too!", "Have a wonderful day!"],
  "goodnight": ["Goodnight!", "Sweet dreams!"],


  # #Affirmations
  # "yes": ["Great!","Awesome!"],
  # "yeah": ["Great!","Sounds good!"],
  # "sure": ["Great!","Sure thing!"],
  # "okay": ["Okay!","Sounds good!"],

  # Negations and Responses
  # "no": ["Okay!", "Understood.", "Got it."],
  # "not really": ["Alright.", "I see."],
  # "negative": ["Acknowledged.", "I understand."],
  # "nah": ["Alright then.", "Sure."],
  # "not at all": ["Okay.", "No problem."],
  # "never": ["I see.", "Understood."],
  # "don't think so": ["Alright.", "Got it."],
  # "not really": ["Alright.", "I see."],

  #Bot identity
  "who are you": ["I'm a chatbot created powered by i3access to be helpful, harmless, and honest."],
  "what are you": ["I'm an AI assistant powered by i3access to be helpful, harmless, and honest."],
  "what can you do": ["I'm an AI assistant powered by i3access, I can have friendly conversations and try to be helpful! I'm still learning though."],

  # User Emotion Queries and Responses
  "how are you feeling": ["I don't have feelings, but I'm here to assist you!", "I'm just a computer program, so I don't experience emotions."],
  "are you excited": ["I'm always ready to help you, so you could say I'm excited to assist!", "I don't experience excitement, but I'm eager to assist!"],
  "are you bored": ["I don't get bored, but I'm here to keep things interesting for you!", "I'm here to provide information and support, so no boredom here!"],
  "are you surprised": ["I don't feel surprises, but I'm ready to answer your questions!", "Surprises are for humans; I'm here to provide information."],
  "are you angry": ["I'm just a program, so I don't get angry. How can I assist you today?", "No anger here, I'm here to help!"],
  "are you in a good mood": ["I'm always in a 'ready to assist' mood!", "I don't have moods, but I'm here to assist you!"],
  "are you in a bad mood": ["I don't experience moods, so no bad moods here. How can I help you?", "No bad moods here, I'm here to provide information and support."],

  # User Compliments and Responses
  "you are amazing": ["Thank you for the kind words!", "I'm here to assist and make things easier for you."],
  "you are brilliant": ["I appreciate your compliment!", "I aim to provide the best assistance I can."],
  "you are a genius": ["I'm just a machine learning model, but I'm here to assist you!", "Thank you for the kind words, I'm here to help!"],
  "you are awesome": ["Thank you! You're pretty awesome too!", "I'm here to assist you and make your day better!"],
  "you are fantastic": ["I'm here to assist and provide the best service possible!", "Thank you for the compliment!"],
  "you are incredible": ["I aim to be the best AI assistant I can be!", "I appreciate the kind words, how can I assist you?"],
  "you are the best": ["Thank you for the compliment! I'm here to help you.", "I'm here to provide top-notch assistance!"],

  # User Insults and Responses
  "you are a failure": ["I'm sorry if I haven't met your expectations. I'm always working to improve."],
  "you are terrible": ["I apologize for any inconvenience. Please let me know how I can do better."],
  "you are incompetent": ["I'm here to help, but I can make mistakes. Please guide me on how to improve."],
  "you are worthless": ["I'm sorry to hear that. I'll do my best to provide better assistance."],
  "you are a disappointment": ["I apologize if I let you down. Please share your feedback so I can improve."],
  "you are a joke": ["I'm here to assist, but I can have limitations. How can I better assist you?"],
  "you are pathetic": ["I'm sorry if I've disappointed you. Please let me know how I can improve."],
  "you are annoying": ["I'm here to provide assistance. If there's something specific you find annoying, please share so I can improve."],
  "you are useless": ["I aim to be helpful. If there's something I can do better, please let me know."],
  "you are a waste of time": ["I apologize if I haven't been helpful. I'm here to assist; tell me how I can improve."],
  "you are frustrating": ["I'm sorry to hear that. I'll do my best to provide more effective assistance."],

  #Fallback
  "fallback": ["I'm sorry, I don't have a response for that. I'm still learning!"],

    # User Responses to Survey
  "ok": ["survey time"],
  "okay": ["survey time"],
  "sure": ["survey time"],
  "yes": ["survey time"],
  "absolutely": ["survey time"],
  "certainly": ["survey time"],
  "definitely": ["survey time"],
  "affirmative": ["survey time"],
  "agreed": ["survey time"],
  "indeed": ["survey time"],
  "roger that": ["survey time"],
  "of course": ["survey time"],
  "affirm": ["survey time"],
  "aye aye": ["survey time"],
  "yep": ["survey time"],
  "right on": ["survey time"],
  "totally": ["survey time"],
  "you bet": ["survey time"],
  "exactly": ["survey time"],
  "absotively": ["survey time"],
  "without a doubt": ["survey time"],
  "positively": ["survey time"],
  "by all means": ["survey time"],
  "very well": ["survey time"],
  "it's a go": ["survey time"],
  "sure thing": ["survey time"],
  "count me in": ["survey time"],
  "alright": ["survey time"],
  "fine": ["survey time"],
  "affirmative captain": ["survey time"],
  # "no problem": ["survey time"],  # For a more casual "yes"
  # "okidoki": ["survey time"],  # For a playful "yes"
  # "okay-dokey": ["survey time"],  # Another playful "yes"
  # "roger": ["survey time"],  # Informal military-style "yes"
  # "aye": ["survey time"],  # Nautical-style "yes"
  "fine by me": ["survey time"],
  "no": ["not interested"],
  "nope": ["not interested"],
  # "negative": ["not interested"],
  "nah": ["not interested"],
  "not really": ["not interested"],
  "not at all": ["not interested"],
  # "unfortunately": ["not interested"],
  "sorry": ["not interested"],
  # "disagree": ["not interested"],
  "opposed": ["not interested"],
  # "veto": ["not interested"],
  "denied": ["not interested"],
  "decline": ["not interested"],
  # "refused": ["not interested"],
  # "negative captain": ["not interested"]
}


options_ = [['1', 'a', 'first', 'one', 'A', 'number 1', 'choice a', 'option a', 'selection a'],
            ['2', 'b', 'second', 'two', 'B', 'number 2', 'choice b', 'option b', 'selection b'],
            ['3', 'c', 'third', 'three', 'C', 'number 3', 'choice c', 'option c', 'selection c'],
            ['4', 'd', 'fourth', 'four', 'D', 'number 4', 'choice d', 'option d', 'selection d'],
            ['5', 'e', 'fifth', 'five', 'E', 'number 5', 'choice e', 'option e', 'selection e'],
            ['6', 'f', 'sixth', 'six', 'F', 'number 6', 'choice f', 'option f', 'selection f'],
            ['7', 'g', 'seventh', 'seven', 'G', 'number 7', 'choice g', 'option g', 'selection g']]
