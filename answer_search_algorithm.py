'''
This example demonstrates how to extract simple Rensa assertions from natural text.
'''

import sys
import os
from pprint import pprint
import json
import codecs
from nltk.corpus import wordnet as wn
from sets import Set

memory_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '.', 'src'))
sys.path.insert(0, memory_path)
from Brain import *
from ConceptExtractor_v2 import *


def get_assertions_sentence(inputString):
    print("echo: "+inputString)
    ''' Extract story assertions. '''
    # Here is an example string.
    #string = "Once upon a time, Ariel was a mermaid.  Ariel has the gender female.  Ariel had a shell.  Ariel loved the land. Ariel happily sang a song.  Ariel also loved Eric. So, Ariel gave her voice to Ursula."
    string = inputString
    # Extract Rensa assertions with extract_story_concepts().
    #print "I'm reading: " + string + "\n* * * "
    learned = extract_story_concepts(string)
    
    Rensa = make_brain(learned)

    # Realize the assertions we learned.
    record_story = []
    for a in Rensa.get_assertions():
        #print " > " + a.realize(Rensa,False)
        #print str(a.prettyprint())
        #target.write(json.dumps(a.realize(Rensa,False)))

        #target.write(json.dumps(a.to_dict(), indent=2))
        #target.write(",\n")
        
        #print(type(a))
        #target.write("\n")
        temp_dict = {}
        temp_dict['r'] = a.to_dict()['r'][0]
        temp_dict['relation']= a.to_dict()['relation']
        temp_dict['l']= a.to_dict()['l'][0]
        temp_dict['index']= a.to_dict()['index'][0]
        temp_dict['sentence']= a.to_dict()['sentence'][0]
        temp_dict['timepoint']= a.to_dict()['timepoint'][0]

        if 'tense' in a.to_dict():
            #not action
            temp_dict['is_verb']= "true"
        else:
            temp_dict['is_verb']= "false"

        if 'storypoints' in a.to_dict():
            temp_dict['storypoints'] = a.to_dict()['storypoints'][0]['at']
            #print(a.to_dict()["storypoints"][0]['at'])
        else:
            temp_dict['storypoints'] = -1

        record_story.append(dict(temp_dict))
    return record_story

def analyize_question(input_question):
    print("analyize_question")
    analized_question = get_assertions_sentence(input_question)
    return analized_question

def get_answer(analyized_question):
    target_assertions = load_assertion("Chapter_1")

    answer = []
    keyword_set = set()
    if len(analyized_question) >0:
        print("get answer for the question: ")
        print(analyized_question[0])
        question_assertion = analyized_question[0]
        keyword_set.add(question_assertion['r'])
        keyword_set.add(question_assertion['l'])
        #print(keyword_set)

        #print(keyword_set)

        ## search target assertions

        iterator_target = 0
        for item in target_assertions:
            #print(target_assertions[item])
            #print(len(target_assertions[item]))
            #print(type(target_assertions[item]))
            if len(target_assertions[item]) > 0:
                print("l: "+target_assertions[item][0]['l'])
                print("r: "+str(target_assertions[item][0]['r']))
                if target_assertions[item][0]['l'] in keyword_set:
                    keyword_set.add(str(target_assertions[item][0]['r']))
                if target_assertions[item][0]['r'] in keyword_set:
                    keyword_set.add(str(target_assertions[item][0]['l']))
                
                
            iterator_target = iterator_target+1

        for item in target_assertions:
            if len(target_assertions[item]) > 0:
                if target_assertions[item][0]['l'] in keyword_set:
                    answer.append(target_assertions[item][0])
                if target_assertions[item][0]['r'] in keyword_set:
                    answer.append(target_assertions[item][0])  

        #print(keyword_set)

    return(answer)

def load_assertion(chapter):
    data = json.load(open("./Storys/"+str(chapter)+"_paragraph_assertions.json", 'r'))
    #print(data)
    return data

if __name__ == '__main__':
    #print("Input question:")
    input_question = raw_input('input question: ')
    analyized_question = analyize_question(input_question)
    #print(analyized_question)
    answer = get_answer(analyized_question)
    #print("Show answer: "+answer)
    print(answer)