# Module 1 Knowledge Check - Embarking on Your Codewars Journey |
#--------------------------------------------------------------

# Even or Odd Challenge |
#----------------------
def even_or_odd(number):
    if(number % 2) == 0:
        return "Even"
    else:
        return "Odd"
    

# Convert a Number to a String Challenge |
#---------------------------------------
def number_to_string(num):
    return(str(num))


# Vowel Count Challenge |
#----------------------
def get_count(sentence):
    vowel_count = sentence.count("a") + sentence.count("e") + sentence.count("i") + sentence.count("o") + sentence.count("u")
    return vowel_count