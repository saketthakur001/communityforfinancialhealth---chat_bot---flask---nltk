from bot_response import patterns
import random
import spacy
nlp = spacy.load("en_core_web_lg")

# Lemmatize a sentence
def lemmatize(sentence):
    # string to a spacy document
    doc = nlp(sentence)

    return " ".join([token.lemma_ for token in doc])

#return similarity score
def compare(sent1, sent2):
    # convert to spacy docs
    doc1 = nlp(sent1)
    doc2 = nlp(sent2)

    return doc1.similarity(doc2)

# patterns = {
#   "you are annoying": ["I apologize if I have been annoying you. I will notify my creators to try to improve my conversational abilities."],
# }

didnt_get = {"4" : "I couldn't understand that, can you please rephrase your question?", "5" :"couldn't understand what you are saying.", "5.5" : "Can you make it more clear?"}


# def survey_time():

#get the best response for a user input
def get_response(user_input):
    scores = []
    responses = []

    # Loop through the patterns
    for pattern in patterns:
        # lemmatize the pattern and the user_input
        pattern_ = lemmatize(pattern)
        user_input_ = lemmatize(user_input)
        scores.append(compare(pattern_, user_input_))
        responses.append(patterns[pattern])

    #  index of the best score
    best_score = max(scores)
    print(best_score)
    best_index = scores.index(best_score)

    return_ = random.choice(responses[best_index])
    if return_ == "survey time":
        survey_time()
    return return_

# print(get_response(''))
count = 0
for i in range(20):
    print(get_response(input("what is it? :"))+"\n"+'Do you wanna take a survay?')
    count+=1

