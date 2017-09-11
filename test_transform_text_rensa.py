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
    string = inputString
    # Extract Rensa assertions with extract_story_concepts().
    
    ## remove this line for speed up process
    #print "I'm reading: " + string + "\n* * * "
    learned = extract_story_concepts(string)
    #learned = extract_story_concepts_no_print(string)
    
    
    Rensa = make_brain(learned)
    for a in Rensa.get_assertions():
        #print " > " + a.realize(Rensa,False)
        print " > "
        print str(a.prettyprint())
                #assertion_index_dict[str(list_count)]
        target.write(json.dumps(a.realize(Rensa,False)))
        target.write("\n")
                
    target.close()
        #Rensa = make_brain(sum(learned_separate[key],[]))
    #print "* * *\nProcess completed."
    
def delete_assertion(old_list, Rensa):
    # this function keep reading user input to delete assertion_index_dict

    text = ""
    while text != "END" and len(old_list) > 0:
        print_asseartions(old_list, Rensa)
        print("\n enter numbers: ")
        text = raw_input()
        if text != "END":
            try:
                val = int(text)
                old_list.pop(int(text))
            except ValueError:
                print("That's not an int!")
        else:
            print("return new assertions!")

    new_list = old_list
    print_asseartions(new_list, Rensa)
    
    return new_list
    
def print_asseartions(current_list, Rensa):
    for i, j in enumerate(current_list):
        print("["+str(i)+"]: "+j.realize(Rensa,False))
        
def get_actor_assertions(actor_key, Rensa):


    # Realize the assertions we learned.
    #print "Here's what I learned:"
    file_name = actor_key+"_out.txt"
    #target = open(file_name, 'w')
    #for a in Rensa.get_assertions():
        #assertion_index_dict[str(list_count)]
        #target.write(json.dumps(a.realize(Rensa,False)))
        #target.write("\n")
        
    #target.close()
        
        #print " > " + a.realize(Rensa,False)
        #print " > "
        #print str(a.prettyprint())
        #print " > " + str(a)
    return Rensa.get_assertions()

def main_function(input_file_name):
    #text_file = open("./Storys/"+sys.argv[1], "r")
    text_file = open("./Storys/"+input_file_name, "r")
    #print text_file.read()
    inputString = text_file.read()
    text_file.close()
    main(inputString)
'''    
if __name__ == '__main__':
    #read a text file and separate to sentences
    #for number of sentences
    text_file = open("./Storys/"+sys.argv[1], "r")
    #print text_file.read()
    inputString = text_file.read()
    text_file.close()
    main(inputString)
'''