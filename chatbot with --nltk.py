englih_survay = open('English QA.txt', 'r').read()
hindi_questions = open('Hindi QA.txt', 'r').read().split('//-')[1:]

def get_options(QA):
    QA = QA.split('\n')
    the_question = QA[0]
    options = [_ for _ in QA[1:] if _ != '' and _ !="Please Select"]
    if len(options) == 0: options=None
    return the_question, options

questions = englih_survay.split('//-')[1:]

english_QnA = {}

for question in questions:
    questions = get_options(question)
    # print(questions[0], '\n\n')
    english_QnA[questions[0]] = questions[1]

# for question in hindi_questions:
    
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello", "Hey there",]
    ], 
    [
        r"sorry (.*)",
        ["Its alright","Its OK, I don't mind",]
    ],
    # [
    #     r"i'm (.*) doing good",
    #     ["Nice to hear that.",]
    # ],
    [
        r"(.*) age?",
        ["I a few years old.",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["I am a bot crated by i3access","top secret ;)",]
    ],
    # [
    #     r"(.*) (location|city) ?",
    #     ['Indore, Madhya Pradesh',]
    # ],
    # [
    #     r"how is weather in (.*)?",
    #     ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    # ],
    # [
    #     r"i work in (.*)?",
    #     ["%1 is an Amazing company, I have heard about it. But they are in huge loss these days.",]
    # ],
    # [
    #     r"(.*)raining in (.*)",
    #     ["No rain since last week here in %2","Damn its raining too much here in %2"]
    # ],
    # [
    #     r"how (.*) health(.*)",
    #     ["I'm a computer program, so I'm always healthy ",]
    # ],
    [
        r"(.*) (sports|game) ?",
        ["Well, I'm a very big fan of Football",]
    ],
    # [
    #     r"who (.*) sportsperson ?",
    #     ["Messy","Ronaldo","Roony"]
    # ],
    # [
    #     r"who (.*) (moviestar|actor)?",
    #     ["Brad Pitt"]
    # ],
    [
        r"quit",
        ["Bye take care. :) ","It was nice talking to you. See you soon :)"]
    ],
]

def chat():
    print("Hi! I am a chatbot")
    chat = Chat(pairs, reflections)
    chat.converse()
#initiate the conversation
if __name__ == "__main__":
    chat()
