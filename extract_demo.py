'''
This example demonstrates how to extract simple Rensa assertions from natural text.
'''

import sys
import os
import pprint

memory_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '.', 'src'))

sys.path.insert(0, memory_path)
from Brain import *
from ConceptExtractor import *

def main(inputString):
    ''' Extract story assertions. '''
    # Here is an example string.
    #string = "Once upon a time, Ariel was a mermaid.  Ariel has the gender female.  Ariel had a shell.  Ariel loved the land. Ariel happily sang a song.  Ariel also loved Eric. So, Ariel gave her voice to Ursula."
    string = inputString
    # Extract Rensa assertions with extract_story_concepts().
    #print "I'm reading: " + string + "\n* * * "
    learned = extract_story_concepts(string)

    # Store the assertions in a brain.
    Rensa = make_brain(learned)

    # Realize the assertions we learned.

    file_name =sys.argv[1].replace(".txt" , ".json")
    target = open("./Storys/"+file_name, 'w')
                
    print( "Here's what I learned:")
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
        record_story.append(dict(temp_dict));
    #target.write("[")
    target.write(json.dumps([{"r": str(item['r']), "relation": str(item['relation']), "l": str(item['l'])} for item in record_story]))
    target.close()    

    print "* * *\nProcess completed."

if __name__ == '__main__':
    text_file = open("./Storys/"+sys.argv[1], "r")
    #print text_file.read()
    inputString = text_file.read()
    text_file.close()
    main(inputString)
