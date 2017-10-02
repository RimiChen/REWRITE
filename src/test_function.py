import re
import en


if __name__ == "__main__":
    print(en.is_adjective("accomplished"))
    print(en.is_noun("wizard"))
    print(en.is_verb("accomplish"))
    print(en.parser.sentence_tag("The day after today, before yesterday. And in pase years, later"))
    en.parser.matches("The day after today, before yesterday. And in pase years, later", "JJ NN")