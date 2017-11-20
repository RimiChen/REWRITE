'''
This example demonstrates how to extract simple Rensa assertions from natural text.
'''

import sys
import os
from pprint import pprint
import json
import codecs

memory_path = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '.', 'src'))
sys.path.insert(0, memory_path)
from Brain import *
from ConceptExtractor_v2 import *


def main(inputString):
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

def main_easy_read(inputString):
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
        
        record_story.append(a.realize(Rensa,False))
    return record_story

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

    return Rensa.get_assertions()



####PREPROCESSING separeate chapters
class CustomType:
    def __init__(self, line_number, text):
        self.line_number = line_number
        self.text = text

    def toJSON(self):
        '''
        Serialize the object custom object
        '''
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)

def saveChapters2Json(chapter_dictionary):
    for chapter in chapter_dictionary:
        #print(chapter)
        result = []
        #target = open("./Storys/"+str(chapter)+".json", 'w')
        with open("./Storys/"+str(chapter)+".json", 'w') as outfile:
            line_number = 0
            for item in chapter_dictionary[chapter]:
                obj = CustomType(str(line_number),item)
                result.append(json.loads(obj.toJSON()))
                line_number += 1
            json.dump(result, outfile, indent=2)        

def separateChapters( whole_lines):
    #### only work for obvious chapter signs
    dictionary_chapter_lines = {}
    
    i= 0
    chapter_count = 0
    temp_lines = []
    while i < len(whole_lines):
        temp = whole_lines[i].split(' ', 1)[0]
        if temp == "Chapter":
            # next chapter
            if(len(temp_lines)>0):
                dictionary_chapter_lines["Chapter_"+str(chapter_count)] = temp_lines

            # initial for next chapter
            chapter_count += 1
            temp_lines = []
        else:
            temp_lines.append(whole_lines[i])

        # while i < line number
        i += 1
    
    return dictionary_chapter_lines

#### PREPROCESSING get paragraphs
def readParagraphsFromChapters(chapter_file_name, paragraph_list):
    # read json, get paragraph
    data = json.load(open("./Storys/"+chapter_file_name+".json"))
    #pprint(data)
    current_paragraph = ""
    current_paragraph_count = 0
    for item in data:
        #print(item["text"])
        if item["text"] == "\n":
            # new paragraph
            current_paragraph_count += 1

            if current_paragraph != "":
                #print(current_paragraph)
                #paragraph_dictionary["paragraph_"+str(current_paragraph_count)] = current_paragraph
                paragraph_list.append({"paragraph" : current_paragraph, "number": current_paragraph_count})
            current_paragraph = ""

        else:
           #print(item["text"])
            new_string = str(item["text"]).replace("\n", " ")
            current_paragraph = current_paragraph + new_string 
        
    return paragraph_list
def saveParagraph2Json(chapter, paragraph_list):
    with open("./Storys/"+str(chapter)+"_paragraph.json", 'w') as outfile:
        json.dump(paragraph_list, outfile, indent=2)  

#### get assertions
def readParagraphs(chapter):
    data = json.load(open("./Storys/"+chapter+"_paragraph.json"))
    #pprint(data)
    return data
def getAssertions(paragraph):
    #print("\n\n"+paragraph)
    result = main(paragraph)
    #print (type(result))
    return result
def saveAssertion2Json(chapter, paragraph_assertion_dictionary):
    with open("./Storys/"+str(chapter)+"_paragraph_assertions.json", 'w') as outfile:
        json.dump(paragraph_assertion_dictionary, outfile, indent=2)      

def getAssertions_easy_read(paragraph):
    #print("\n\n"+paragraph)
    result = main_easy_read(paragraph)
    #print (type(result))
    return result
def saveAssertion2Json_easy_read(chapter, paragraph_assertion_dictionary):
    with open("./Storys/"+str(chapter)+"_paragraph_assertions_easy.json", 'w') as outfile:
        json.dump(paragraph_assertion_dictionary, outfile, indent=2)  

if __name__ == '__main__':
    #read a text file and separate to sentences
    #for number of sentences
    #text_file = open("./Storys/"+sys.argv[1], "r")
    #text_file = open("./Storys/"+"AROUND_THE_WORLD_IN_EIGHTY_DAYS.txt", "r")

    #print text_file.read()
    #inputString = text_file.read()

    #### test the property of the text file
    #### PROCESSING the text file
    #print("The total length is: "+inputString)



    #with open("./Storys/"+"AROUND_THE_WORLD_IN_EIGHTY_DAYS.txt", "r") as myfile:
    #    count = sum(1 for line in myfile if line.rstrip('\n'))
    #    print("The total line number is: "+str(count))

    #    count = sum(1 for line in myfile if line.rstrip('\n\n'))
    #    print("The total paragraph number is: "+str(count))
        
    #### PREPROCESSING text file:
    # separate the whole text by chapters, and save to json files
    # read chapters from json and separate to paragraphs
    # output to json file
    ####

    #### PREPROCESSING text file 1:
    # separate the whole text by chapters, and save to json files
    fichier = codecs.open("./Storys/"+"AROUND_THE_WORLD_IN_EIGHTY_DAYS.txt", "r", encoding="utf-8")
    unicode_story_content = fichier.read()
    fichierTemp = codecs.open("./Storys/"+"AROUND_THE_WORLD_IN_EIGHTY_DAYS_2.txt", "w", encoding="ascii", errors="ignore")
    fichierTemp.write(unicode_story_content)
    
    text_file = open("./Storys/"+"AROUND_THE_WORLD_IN_EIGHTY_DAYS_2.txt", "r")
    input_whole_text = text_file.read()
    text_file.close()

    whole_lines = input_whole_text.splitlines(True)

    chapter_dictionary = separateChapters(whole_lines)
    #### DEBUG: print chapter dictioanry
    #if "Chapter_1" in chapter_dictionary:
    #    print("=".join(chapter_dictionary["Chapter_1"]))
    saveChapters2Json(chapter_dictionary)


    #### PREPROCESSING text file 2:
    # read chapters from json and separate to paragraphs
    for chapter in chapter_dictionary:
        paragraph_list = []
        paragraph_list = readParagraphsFromChapters(chapter, paragraph_list)
        #pprint(paragraph_list)
        saveParagraph2Json(chapter,paragraph_list)
    #pprint(paragraph_dictionary)

    #### get assertion for each paragraph:
    #
    
    for chapter in chapter_dictionary:
        paragraphs = readParagraphs(chapter)
        paragraph_assertion_dictionary = {}
        paragraph_assertion_dictionary_easy = {}
        for paragraph in paragraphs:
            # get assertions
            #print(paragraph["number"])
            
            assertion_list = getAssertions(paragraph["paragraph"])
            assertion_list_easy = getAssertions_easy_read(paragraph["paragraph"])
            paragraph_assertion_dictionary[paragraph["number"]] = assertion_list
            paragraph_assertion_dictionary_easy[paragraph["number"]] = assertion_list_easy

        #pprint(paragraph_assertion_dictionary)

        saveAssertion2Json(chapter, paragraph_assertion_dictionary)
        saveAssertion2Json_easy_read(chapter, paragraph_assertion_dictionary_easy)




        

    #print(len(paragraphs))
    #print("========".join(paragraphs[0:10]))


    

    #print()    

    

    #main(inputString)
