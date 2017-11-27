
'''
This file provides fast, simple extraction of Rensa assertions from natural text, which may help you write simple assertions in natural text instead of JSON.

Advanced users may want to look into more thorough extractors (e.g. Fader et al., 2011: "Identifying relations for open information extraction") or build their own.
'''
import re
import en
import datetime
from Entity import *


# Returns a list of story assertions gleaned from the string s.
def extract_story_concepts(s):
    current_time_point = 0
    actors, assertions = [], []
    sentence_dictionary = {}
    '''
    extractActors = extract_actors(assertions, s)
    actors = extractActors[0]
    assertions = extractActors[1]
    '''
    start_time = datetime.datetime.now()
    sentences = split_sentences(s)
    for sp,e in enumerate(sentences):
        temp_assertions = extract_possible_actors(assertions, e, sp, current_time_point, sentence_dictionary)
        #assertions = temp_assertions[0]
        #current_time_point = temp_assertions[1]
        sentence_dictionary = temp_assertions[2]

    create_sentence_dictionary_time = datetime.datetime.now()
    #print("==create sentence dictionary: "+ str(create_sentence_dictionary_time - start_time))
    assertions = []

    start_basic = datetime.datetime.now()
    for sp,e in enumerate(sentences):
        ### first get how to describe things
        temp_assertions = extract_time_shift(assertions, e, sp, current_time_point)
        assertions = temp_assertions[0]
        current_time_point = temp_assertions[1]

        extract_location(assertions, e, sp, current_time_point)

        temp_assertions = extract_basic_properties_v2(assertions, e, sp, current_time_point, sentence_dictionary)
        assertions = temp_assertions[0]
        current_time_point = temp_assertions[1]
        sentence_dictionary = temp_assertions[2]

    basic_properties_time_shift = datetime.datetime.now()
    #print("==get basic part: "+ str(basic_properties_time_shift - start_basic))

    #print("*****************************************")
    #print(sentence_dictionary)
    
    i = 0
    actor_count = {}
    while i < len(assertions):
        #print(assertions[i]['l'][0])
        #if assertions[i]['l'][0] not in  actors:
        #    actors.append(assertions[i]['l'][0])
        
        if assertions[i]['l'][0] not in actor_count and assertions[i]['l'][0] in sentence_dictionary:
            actor_count[assertions[i]['l'][0]] = len(sentence_dictionary[assertions[i]['l'][0]])


        i = i+1
    
    #### get time shift
    
    #print("*****************************************")
    #print(actors)

    #print("==DEBUG== actors:")
    #print(actor_count)
    
    #### retrieve actors' actions
    #### retriece actors' propoties
    #assertions = []
    start_actors = datetime.datetime.now()
    for actor_name in actor_count:
        if actor_count[actor_name] >= 1 and actor_name in sentence_dictionary:
        #if actor_name !="" and actor_name in sentence_dictionary and count > 3:
            #print("============= " +actor_name+" ======== " + str(actor_count[actor_name])+ " =======")

            for s in sentence_dictionary[actor_name]:
                #print(s["storypoints"][0]['at'])
                sp = s["storypoints"][0]['at']
                e = str(s["sentence"][0])
                current_time_point = s["timepoint"]
                #print("============= " +actor_name+" ======== " + e+ " =======")

                temp_assertions = extract_actor_actions_v2(assertions, actor_count, e, sp, current_time_point, actor_name)
                assertions = temp_assertions[0]
                current_time_point = temp_assertions[1]

                temp_assertions = extract_actor_properties_v2(assertions, actor_count, e, sp, current_time_point, actor_name)
                assertions = temp_assertions[0]
                current_time_point = temp_assertions[1]
    
    
    get_actor_information = datetime.datetime.now()
    #print("==get actor part: "+ str(get_actor_information - start_actors))

    #suppose all subjects are actors
    return assertions

    
'''    
    for sp,e in enumerate(sentences):
        
        print("==DEBUG== "+e)
        temp_assertions = extract_actor_actions(assertions, actors, e, sp, current_time_point)
        assertions = temp_assertions[0]
        current_time_point = temp_assertions[1]

        #assertions = extract_actor_actions(assertions, actors, e, sp, current_time_point)
        temp_assertions = extract_actor_properties(assertions, actors, e, sp, current_time_point)
        assertions = temp_assertions[0]
        current_time_point = temp_assertions[1]

        #assertions = extract_actor_properties(assertions, actors, e, sp, current_time_point)
'''

# Determine the actors present in the story.
def extract_actors(assertions, s):
    actors = []
    # First, check for nouns that have specified genders.
    matches1 = en.sentence.find(s, "NN is female")
    matches1 += en.sentence.find(s, "NN is male")
    matches1 += en.sentence.find(s, "NN has (DT) gender male")
    matches1 += en.sentence.find(s, "NN has (DT) gender female")
    for match in matches1:
        name = match[0][0]
        for i,m in enumerate(match):
            if m[0]=="female" or m[0]=="male":
                gender = m[0]
        if name not in actors:
            actors.append(name)
            assertion_index = len(assertions)
            newAssertions = [
                {"l":[name], "relation":"instance_of","r":["actor"], "index":[assertion_index], "sentence": [s]},
                {"l":[name], "relation":"has_gender","r":[gender], "index":[assertion_index], "sentence": [s]}
            ]
            assertions.extend([x for x in newAssertions if x not in assertions])

    # Check for general nouns that are known names.
    matches = en.sentence.find(s, "NN")
    for match in matches:
        name = match[0][0]
        if baby_names.__contains__(name):
            if name not in actors:
                actors.append(name)
                gender = guess_gender(name)
                assertion_index = len(assertions)
                newAssertions = [
                    {"l":[name], "relation":"instance_of","r":["actor"], "index":[assertion_index], "sentence": [s]},
                    {"l":[name], "relation":"has_gender","r":[gender], "index":[assertion_index], "sentence": [s]}
                ]
                assertions.extend([x for x in newAssertions if x not in assertions])
    
    
    return [actors, assertions]

# Examples:
# The sea was unpredictable.
def extract_possible_actors(assertions, s, sp, current_time_point, sentence_dictionary):
    matches = en.parser.matches(s, " NN ")
    #print("**********")
    #print(en.parser.sentence_tag(s))
    #matches += en.sentence.find(s, "(DT) J S")
    for match in matches:
        noun = match[0][0].lower()
        #print(noun)
        #determine  = match[0][0]
        if noun!="":
            assertion_index = len(assertions)
            assertion = {"l":[noun], "relation":"has_property","r":["object"],"storypoints":[{"at":sp}], "index":[assertion_index], "sentence": [s], "timepoint": [current_time_point]}
            if assertion not in assertions:
                # add to dictionary
                if noun in sentence_dictionary:
                    sentence_dictionary[noun].append({"sentence": [s], "storypoints":[{"at":sp}], "timepoint": [current_time_point]})
                else:
                    sentence_dictionary[noun] = []
                    sentence_dictionary[noun].append({"sentence": [s], "storypoints":[{"at":sp}], "timepoint": [current_time_point]})

                assertions.append(assertion)
    return [assertions, current_time_point, sentence_dictionary]

def extract_basic_properties(assertions, s, sp, current_time_point):
    matches = en.parser.matches(s, "NN NN")
    matches += en.parser.matches(s, "JJ NN")
    #matches += en.sentence.find(s, "(DT) J S")
    for match in matches:
        noun = match[1][0].lower()
        adj  = match[0][0]
        if noun!="" and adj!="":
            assertion_index = len(assertions)
            assertion = {"l":[noun], "relation":"has_property","r":[adj],"storypoints":[{"at":sp}], "index":[assertion_index], "sentence": [s], "timepoint": [current_time_point]}
            if assertion not in assertions:
                # add to dictionary
                assertions.append(assertion)
    return [assertions, current_time_point]

def extract_basic_properties_v2(assertions, s, sp, current_time_point, sentence_dictionary):
    matches = en.parser.matches(s, "NN NN")
    #matches += en.sentence.find(s, "(DT) J S")
    for match in matches:
        noun = match[1][0].lower()
        noun2  = match[0][0]
        if noun!="" and noun2!="":
            assertion_index = len(assertions)
            assertion = {"l":[noun], "relation":"has_property","r":[noun2],"storypoints":[{"at":sp}], "index":[assertion_index], "sentence": [s], "timepoint": [current_time_point]}
            if assertion not in assertions:
                # add to dictionary
                if noun in sentence_dictionary:
                    sentence_dictionary[noun].append({"sentence": [s], "storypoints":[{"at":sp}], "timepoint": [current_time_point]})
                else:
                    sentence_dictionary[noun] = []
                    sentence_dictionary[noun].append({"sentence": [s], "storypoints":[{"at":sp}], "timepoint": [current_time_point]})

                if noun2 in sentence_dictionary:
                    sentence_dictionary[noun2].append({"sentence": [s], "storypoints":[{"at":sp}], "timepoint": [current_time_point]})
                else:
                    sentence_dictionary[noun2] = []
                    sentence_dictionary[noun2].append({"sentence": [s], "storypoints":[{"at":sp}], "timepoint": [current_time_point]})
            
                
                assertions.append(assertion)

    matches = en.parser.matches(s, "JJ NN")
    for match in matches:
        noun = match[1][0].lower()
        adj  = match[0][0]
        if noun!="" and adj!="":
            assertion_index = len(assertions)
            assertion = {"l":[noun], "relation":"has_property","r":[adj],"storypoints":[{"at":sp}], "index":[assertion_index], "sentence": [s], "timepoint": [current_time_point]}
            if assertion not in assertions:
                # add to dictionary
                if noun in sentence_dictionary:
                    sentence_dictionary[noun].append({"sentence": [s], "storypoints":[{"at":sp}], "timepoint": [current_time_point]})
                else:
                    sentence_dictionary[noun] = []
                    sentence_dictionary[noun].append({"sentence": [s], "storypoints":[{"at":sp}], "timepoint": [current_time_point]})

                assertions.append(assertion)
    
    return [assertions, current_time_point, sentence_dictionary]
# Examples:
# Harry looked ill.
# Ariel was really happy.
def extract_time_shift(assertions, s, sp, current_time_point):
    matches = []
    # add time rule in here
    matches = en.parser.matches(s, "after")
    for match in matches:
        time_shift_noun = match[0][0]
        if time_shift_noun!="":
            assertion_index = len(assertions)
            time_shift_number = 1
            current_time_point = current_time_point + time_shift_number
            assertion = {"l":["after"], "relation":"time_shift","r":[time_shift_number],"storypoints":[{"at":sp}], "index":[assertion_index], "sentence": [s], "timepoint": [current_time_point]}
            if assertion not in assertions:
                assertions.append(assertion)
    matches = en.parser.matches(s, "before")
    for match in matches:
        time_shift_noun = match[0][0]
        if time_shift_noun!="":
            assertion_index = len(assertions)
            time_shift_number = -1
            current_time_point = current_time_point + time_shift_number
            assertion = {"l":["before"], "relation":"time_shift","r":[time_shift_number],"storypoints":[{"at":sp}], "index":[assertion_index], "sentence": [s], "timepoint": [current_time_point]}
            if assertion not in assertions:
                assertions.append(assertion)

    matches = en.parser.matches(s, "yesterday")
    for match in matches:
        time_shift_noun = match[0][0]
        if time_shift_noun!="":
            assertion_index = len(assertions)
            time_shift_number = -1
            current_time_point = current_time_point + time_shift_number
            assertion = {"l":["yesterday"], "relation":"time_shift","r":[time_shift_number],"storypoints":[{"at":sp}], "index":[assertion_index], "sentence": [s], "timepoint": [current_time_point]}
            if assertion not in assertions:
                assertions.append(assertion)  

    matches = en.parser.matches(s, "today")
    for match in matches:
        time_shift_noun = match[0][0]
        if time_shift_noun!="":
            assertion_index = len(assertions)
            time_shift_number = 0
            current_time_point = current_time_point + time_shift_number
            assertion = {"l":["today"], "relation":"time_shift","r":[time_shift_number],"storypoints":[{"at":sp}], "index":[assertion_index], "sentence": [s], "timepoint": [current_time_point]}
            if assertion not in assertions:
                assertions.append(assertion)  

    matches = en.parser.matches(s, "tomorrow")
    for match in matches:
        time_shift_noun = match[0][0]
        if time_shift_noun!="":
            assertion_index = len(assertions)
            time_shift_number = 2
            current_time_point = current_time_point + time_shift_number
            assertion = {"l":["tomorrow"], "relation":"time_shift","r":[time_shift_number],"storypoints":[{"at":sp}], "index":[assertion_index], "sentence": [s], "timepoint": [current_time_point]}
            if assertion not in assertions:
                assertions.append(assertion)  


    return [assertions, current_time_point]

def extract_location(assertions, s, sp, current_time_point):
    matches = []
    # add time rule in here
    matches += en.sentence.find(s, " at (DT) NN")
    matches += en.sentence.find(s, " on (DT) NN")
    matches += en.sentence.find(s, " in (DT) NN")
    matches += en.sentence.find(s, " to (DT) NN")
        #matches += en.sentence.find(s, actor + " looked (RB) JJ")
    #for match in matches:
        #[place] = ""
    #    for i,m in enumerate(match):
        #    if m[0][0:2]=="NN":
        #        place = m[0]
    #        print(i)
    #        print(m)
        #assertion_index = len(assertions)
        #assertion = {"l":[actorName], "relation":"has_property","r":[adj],"storypoints":[{"at":sp}], "index":[assertion_index], "sentence": [s], "timepoint": [current_time_point]}
        #if assertion not in assertions:
        #    assertions.append(assertion)
    return [assertions, current_time_point]

def extract_actor_properties(assertions, actors, s, sp, current_time_point):
    matches = []
    for actor in actors:
        matches += en.sentence.find(s, actor + " is (DT) (RB) JJ")
        matches += en.sentence.find(s, actor + " was (DT) (RB) JJ")
        matches += en.sentence.find(s, actor + " looked (RB) JJ")
        #matches += en.sentence.find(s, actor + " looked (RB) JJ")
    for match in matches:
        actorName, adj = "", ""
        for i,m in enumerate(match):
            if m[0] in actors:
                if i==0:
                    actorName = m[0]
            elif m[1][0:2]=="JJ":
                adj = m[0]
        assertion_index = len(assertions)
        assertion = {"l":[actorName], "relation":"has_property","r":[adj],"storypoints":[{"at":sp}], "index":[assertion_index], "sentence": [s], "timepoint": [current_time_point]}
        if assertion not in assertions:
            assertions.append(assertion)
    return [assertions, current_time_point]

def extract_actor_properties_v2(assertions, actors, s, sp, current_time_point, actor_name):
    actor = actor_name
    #print(actor+"    "+s)
    matches = []
    matches += en.sentence.find(s, actor + " is (DT) (RB) JJ")
    matches += en.sentence.find(s, actor + " was (DT) (RB) JJ")
    matches += en.sentence.find(s, actor + " looked (RB) JJ")
        #matches += en.sentence.find(s, actor + " looked (RB) JJ")
    for match in matches:
        actorName, adj = "", ""
        #print("==see====")
        #print(match)
        #print(match[0])
        #print(match[0][0])
        for i,m in enumerate(match):
            if m[0][0] in actors:
                if i==0:
                    actorName = m[0][0]
            elif m[1][0:2]=="JJ":
                adj = m[0]
        assertion_index = len(assertions)
        assertion = {"l":[actorName], "relation":"has_property","r":[adj],"storypoints":[{"at":sp}], "index":[assertion_index], "sentence": [s], "timepoint": [current_time_point]}
        if assertion not in assertions:
            assertions.append(assertion)
    return [assertions, current_time_point]
# Examples:
#  - Ariel is an instance of mermaid.
#  - Ariel loved the land.
#  - Ariel loved Eric.
#  - Ariel gave her voice to Ursula.
#  - Ariel has the shell.
def extract_actor_actions(assertions, actors, s, sp, current_time_point):
    matches = []
    for actor in actors:
        # Example: Ariel (sadly) hated (the) (unpredictable) (sea).
        #print("==DEBUG== actor matches")
        #print(actor+"???")
        #print(s)

        matches += en.sentence.find(s, actor + " (RB) VB .")
        matches += en.sentence.find(s, actor + " (RB) VB")
        #matches += en.sentence.find(s, actor + " (RB) VB NN")
        matches += en.sentence.find(s, actor + " (RB) VB DT (JJ) NN")
        matches += en.sentence.find(s, actor + " (RB) VB DT (JJ) NN .")
        for actor2 in actors:
            # Example: Ariel (happily) loved Eric.
            matches += en.sentence.find(s, actor + " (RB) VB " + actor2)
            # Example: Ariel (sadly) gave (her) (strong) voice to Ursula.
            matches += en.sentence.find(s, actor + " (RB) VB (PRP$) (JJ) NN to " + actor2)

        #print("==DEBUG== actor matches")
        #print(actor)
        #print(matches)

    for match in matches:
        verb, actorName, actionObj, actionRecipient, pronoun, adverb = "", "", "", "", "", ""
        for i,m in enumerate(match):
            if m[1][0:2]=="VB": #or m[1][0:3]=="VBD":
                verb = m[0]
            elif m[0] in actors:
                if i==0:
                    actorName = m[0]
                elif i>=1:
                    actionRecipient = m[0]
            elif m[1][0:2]=="NN":
                actionObj = m[0]
            elif m[1][0:4]=="PRP$":
                pronoun = m[0]
            elif m[1][0:2]=="RB":
                adverb = m[0]
        if verb!="" and actorName!="":
            tense = determine_tense(verb)
            if en.verb.infinitive(verb)=="be":
                assertion_index = len(assertions)
                assertion = {"l":[actorName], "relation":"instance_of","r":[actionObj],"storypoints":[{"at":sp}],"tense":tense, "verb": [verb], "index":[assertion_index], "sentence": [s], "timepoint": [current_time_point]}
            else:
                assertion_index = len(assertions)
                assertion = {"l":[actorName], "relation":"action","r":[verb],"storypoints":[{"at":sp}],"tense":tense, "verb": verb, "index":[assertion_index], "sentence": [s], "timepoint": [current_time_point]}
                if actionObj!="":
                    assertion["action_object"] = [actionObj]
                if actionRecipient!="":
                    assertion["action_recipient"] = [actionRecipient]
                if pronoun!="":
                    if pronoun==get_references(guess_gender(actorName))[2] or {"l":[actorName], "relation":"has_gender","r":[gender_from_reference(pronoun)]} in assertions:
                        assertion["action_object_owner"] = [actorName]
                if adverb!="" and adverb !="also" and adverb !="too":
                    assertion["with_property"] = [adverb]
            assertions.append(assertion)
    return [assertions, current_time_point]

# English honorifics and other abbreviations requiring a period.
abbreviations=["Mr.","Ms.","Mrs.","Mx.", "Mme.", "Mses.", "Mss.", "Mmes.","Dr.","St.","Messrs.","Esq.","Prof.","Jr.","Sr.","Br.","Fr.",
"Rev.","Pr.","Ph.D.","M.D.","M.S.","B.A.","B.S."]
'''
# Split a string into a list of sentences.
def split_sentences(story):
  sentences = []
  tokens = story.split(" ")
  start = 0
  for i,t in enumerate(tokens):
    t = t.strip()
    if t.endswith("."):
      if t in abbreviations:
        continue
      else:
        sentences.append(" ".join(tokens[start:i+1]))
        start = i+1
    elif t.endswith("?") or t.endswith("!"):
      sentences.append(" ".join(tokens[start:i+1]))
      start = i+1
  if start < len(tokens):
    sentences.append(" ".join(tokens[start:]))
  return sentences

'''
def extract_actor_actions_v2(assertions, actors, s, sp, current_time_point, actor_name):
    actor = actor_name
    #print(actor+"    "+s)
    matches = []
    #matches += en.sentence.find(s, actor + " (RB) VB .")
    matches += en.sentence.find(s, actor + " (RB) VB")
        #matches += en.sentence.find(s, actor + " (RB) VB NN")
    matches += en.sentence.find(s, actor + " (RB) VB DT (JJ) NN")
    #matches += en.sentence.find(s, actor + " (RB) VB DT (JJ) NN .")
    for actor2 in actors:
            # Example: Ariel (happily) loved Eric.
        matches += en.sentence.find(s, actor + " (RB) VB " + actor2)
            # Example: Ariel (sadly) gave (her) (strong) voice to Ursula.
        matches += en.sentence.find(s, actor + " (RB) VB (PRP$) (JJ) NN to " + actor2)
        #print("==DEBUG== actor matches")
        #print(actor)
        #print(matches)

    for match in matches:
        #print("==see====")
        #print(match)
        #print(match[0])
        #print(match[0][0])
        verb, actorName, actionObj, actionRecipient, pronoun, adverb = "", "", "", "", "", ""
        for i,m in enumerate(match):
            #print(m)
            #print(m[1])
            #print(m[0][0])

            if m[1][0:2]=="VB": #or m[1][0:3]=="VBD":
                verb = m[0]
                #print(verb)
            elif m[0] in actors:
                if i==0:
                    actorName = m[0]
                    #        print(actorName)
                elif i>=1:
                    actionRecipient = m[0]
            elif m[1][0:2]=="NN":
                actionObj = m[0]
            elif m[1][0:4]=="PRP$":
                pronoun = m[0]
            elif m[1][0:2]=="RB":
                adverb = m[0]
        
        #print("=="+verb+" "+actorName)

        if verb!="" and actorName!="":
            tense = determine_tense(verb)
            if en.verb.infinitive(verb)=="be":
                assertion_index = len(assertions)
                assertion = {"l":[actorName], "relation":"instance_of","r":[actionObj],"storypoints":[{"at":sp}],"tense":tense, "verb": [verb], "index":[assertion_index], "sentence": [s], "timepoint": [current_time_point]}
            else:
                assertion_index = len(assertions)
                assertion = {"l":[actorName], "relation":"action","r":[verb],"storypoints":[{"at":sp}],"tense":tense, "verb": verb, "index":[assertion_index], "sentence": [s], "timepoint": [current_time_point]}
                if actionObj!="":
                    assertion["action_object"] = [actionObj]
                if actionRecipient!="":
                    assertion["action_recipient"] = [actionRecipient]
                if pronoun!="":
                    if pronoun==get_references(guess_gender(actorName))[2] or {"l":[actorName], "relation":"has_gender","r":[gender_from_reference(pronoun)]} in assertions:
                        assertion["action_object_owner"] = [actorName]
                if adverb!="" and adverb !="also" and adverb !="too":
                    assertion["with_property"] = [adverb]
            assertions.append(assertion)
    return [assertions, current_time_point]

# English honorifics and other abbreviations requiring a period.
abbreviations=["Mr.","Ms.","Mrs.","Mx.", "Mme.", "Mses.", "Mss.", "Mmes.","Dr.","St.","Messrs.","Esq.","Prof.","Jr.","Sr.","Br.","Fr.",
"Rev.","Pr.","Ph.D.","M.D.","M.S.","B.A.","B.S."]

def split_sentences(story):
    story = story.replace('\n', ' ').replace('\r', ' ').replace(',', '.').replace('\"', '.')
    sentences = re.split(r' *[\.\?!][\'\"\)\];]* *',story)
    return sentences

# Remove punctuation from a word.
def elim_punk(word):
  return re.sub('[:,;.?!()]', '', word)

# Determine the basic tense of a verb.
def determine_tense(verb):
    t = en.verb.tense(verb)
    if "present participle" in t:
        return "present participle"
    elif "past participle" in t:
        return "past participle"
    elif "past" in t:
        return "past"
    else:
        return "present"