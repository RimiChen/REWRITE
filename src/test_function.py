import re
import en


if __name__ == "__main__":
    print(en.is_adjective("accomplished"))
    print(en.is_noun("wizard"))
    print(en.is_verb("accomplish"))
    #en.parser.sentence_tag("An accomplished wizard once lived on the top floor of a tenement \
    #house and passed his time in thoughtful study and studious thought.")
    en.parser.matches("THE GLASS DOG      An accomplished wizard once lived on the top floor of a tenement  house and passed his time in thoughtful study and studious thought", "JJ NN")