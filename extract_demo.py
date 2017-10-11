'''
This example demonstrates how to extract simple Rensa assertions from natural text.
'''
import sys
import os
import pprint
sys.path.append(os.path.join(os.path.dirname(__file__), '.', 'src'))
from Brain import *
from ConceptExtractor_v2 import *

def rensa_test(input_story_name):
    print("\nPrepare to process "+input_story_name)
    text_file = open("./Storys/"+input_story_name+".txt", "r")
    #print text_file.read()
    inputString = text_file.read()
    text_file.close()
    main(inputString, input_story_name+".txt")

def save_story(story_path, story_content):
    print("\nPrepare to process "+story_path)
    #print(story_content)
    text_file = open("./"+story_path, "w")
    text_file.write(story_content)
    text_file.close()

def main(inputString, file_name):
    ''' Extract story assertions. '''
    # Here is an example string.
    #string = "Once upon a time, Ariel was a mermaid.  Ariel has the gender female.  Ariel had a shell.  Ariel loved the land. Ariel happily sang a song.  Ariel also loved Eric. So, Ariel gave her voice to Ursula."
    string = inputString
    # Extract Rensa assertions with extract_story_concepts().
    #print "I'm reading: " + string + "\n* * * "
    learned = extract_story_concepts(string)

    #print("==================")
    #print(type(learned))
    #for elem in learned:
        #print("==================")
        #print(elem)     
    #print("\n".join(learned))

    # Store the assertions in a brain.
    Rensa = make_brain(learned)

    # Realize the assertions we learned.
    file_name =file_name.replace(".txt" , ".json")
    target = open("./Storys/"+file_name, 'w')               
    #print( "Here's what I learned:")
    #target.write("[")
    record_story = []
    for a in Rensa.get_assertions():
        print " > " + a.realize(Rensa,False)
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
    #target.write("[")
    target.write(json.dumps([{
        "r": str(item['r']),
        "relation": str(item['relation']),
        "l": str(item['l']),
        "index": str(item['index']),
        "sentence": str(item['sentence']),
        "is_verb": str(item['is_verb']),
        "timepoint" : str(item['timepoint']),
        "storypoints": str(item['storypoints'])} for item in record_story]))
    target.close()    

    print "* * *\nProcess completed."

