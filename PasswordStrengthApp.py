import gradio as gr
import pickle
from Orange.data import * 

def make_prediction(password):
    
    list = detailsFunction(password)
    
    PasswordLength = DiscreteVariable("PasswordLength")
    VowelCount = DiscreteVariable("VowelCount")
    ConsonantCount = DiscreteVariable("ConsonantCount")
    NumberCount = DiscreteVariable("NumberCount")
    SpecialCharacterCount = DiscreteVariable("SpecialCharacterCount",values=["0","1"])
    IsPalindrome = DiscreteVariable("IsPalindrome",values=["0","1"])
    lowercaseLetterCount = DiscreteVariable("lowercaseLetterCount")
    uppercaseLetterCount = DiscreteVariable("uppercaseLetterCount") 

    IsPalindromeToString = str(list[5])

    domain=Domain([PasswordLength,VowelCount,ConsonantCount,NumberCount,SpecialCharacterCount,IsPalindrome,lowercaseLetterCount,uppercaseLetterCount])
		
    data=Table(domain,[[list[0],list[1],list[2],list[3],list[4],IsPalindromeToString,list[6],list[7]]])
	
    with open("PasswordModel.pkcls", "rb") as f:	
        clf  = pickle.load(f)
        ar=clf(data)
        preds=clf.domain.class_var.str_val(ar)
        preds="$"+preds
        return preds
    
def detailsFunction(str): # This function calculates the variable fields for the password and retruns an array with a count or condition for each password passed through by reference

    list = [0] * 8
    character = ""

    list[0] = len(str)-1;#PasswordLength
    list[1] = 0;#VowelCount
    list[2] = 0;#ConsonantCount
    list[3] = 0;#NumberCount
    list[4] = 0;#SpecialCharacterCount
    list[5] = is_palindrome(str);#IsPalindrome
    list[6] = 0;#lowercaseLetterCount
    list[7] = 0;#uppercaseLetterCount

    for element in range(0, len(str)):
        character = str[element]

        if character == 'A':
            list[7] += 1
            list[1] += 1
        elif character == 'B':
            list[7] += 1
            list[2] += 1
        elif character == 'C':
            list[7] += 1
            list[2] += 1
        elif character == 'D':
            list[7] += 1
            list[2] += 1
        elif character == 'E':
            list[7] += 1
            list[1] += 1
        elif character == 'F':
            list[7] += 1
            list[2] += 1
        elif character == 'G':
            list[7] += 1
            list[2] += 1
        elif character == 'H':
            list[7] += 1
            list[2] += 1
        elif character == 'I':
            list[7] += 1
            list[1] += 1
        elif character == 'J':
            list[7] += 1
            list[2] += 1
        elif character == 'K':
            list[7] += 1
            list[2] += 1
        elif character == 'L':
            list[7] += 1
            list[2] += 1
        elif character == 'M':
            list[7] += 1
            list[2] += 1
        elif character == 'N':
            list[7] += 1
            list[2] += 1
        elif character == 'O':
            list[7] += 1
            list[1] += 1
        elif character == 'P':
            list[7] += 1
            list[2] += 1
        elif character == 'Q':
            list[7] += 1
            list[2] += 1
        elif character == 'R':
            list[7] += 1
            list[2] += 1
        elif character == 'S':
            list[7] += 1
            list[2] += 1
        elif character == 'T':
            list[7] += 1
            list[2] += 1
        elif character == 'U':
            list[7] += 1
            list[1] += 1
        elif character == 'V':
            list[7] += 1
            list[2] += 1
        elif character == 'W':
            list[7] += 1
            list[2] += 1
        elif character == 'X':
            list[7] += 1
            list[2] += 1
        elif character == 'Y':
            list[7] += 1
            list[2] += 1
        elif character == 'Z': 
            list[7] += 1
            list[2] += 1
        elif character == 'a': #Lowercase alphabet begins
            list[6] += 1
            list[2] += 1
        elif character == 'b':
            list[6] += 1
            list[2] += 1
        elif character == 'c':
            list[6] += 1
            list[2] += 1
        elif character == 'd':
            list[6] += 1
            list[2] += 1
        elif character == 'e':
            list[6] += 1
            list[1] += 1
        elif character == 'f':
            list[6] += 1
            list[2] += 1
        elif character == 'g':
            list[6] += 1
            list[2] += 1
        elif character == 'h':
            list[6] += 1
            list[2] += 1
        elif character == 'i':
            list[6] += 1
            list[1] += 1
        elif character == 'j':
            list[6] += 1
            list[2] += 1
        elif character == 'k':
            list[6] += 1
            list[2] += 1
        elif character == 'l':
            list[6] += 1
            list[2] += 1
        elif character == 'm':
            list[6] += 1
            list[2] += 1
        elif character == 'n':
            list[6] += 1
            list[2] += 1
        elif character == 'o':
            list[6] += 1
            list[1] += 1
        elif character == 'p':
            list[6] += 1
            list[2] += 1
        elif character == 'q':
            list[6] += 1
            list[2] += 1
        elif character == 'r':
            list[6] += 1
            list[2] += 1
        elif character == 's':
            list[6] += 1
            list[2] += 1
        elif character == 't':
            list[6] += 1
            list[2] += 1
        elif character == 'u':
            list[6] += 1
            list[1] += 1
        elif character == 'v':
            list[6] += 1
            list[2] += 1
        elif character == 'w':
            list[6] += 1
            list[2] += 1
        elif character == 'x':
            list[6] += 1
            list[2] += 1
        elif character == 'y':
            list[6] += 1
            list[2] += 1
        elif character == 'Z':
            list[6] += 1
            list[2] += 1 
        elif character == '1' or character =='2' or character == '3' or character =='4' or character == '5' or character =='6'or character == '7' or character =='8' or character == '9' or character =='0': # Numbers start here
            list[3] += 1
        elif character == '`' or character =='~'or character == '!' or character =='@' or character == '#' or character =='$' or character == '%' or character =='^' or character == '&' or character =='*': # Special Characters start here
            list[4] += 1
        elif character == '(' or character ==')'or character == '-' or character =='_' or character == '=' or character =='+' or character == '%' or character =='[' or character == '|' or character ==';':
            list[4] += 1
        elif character == ':' or character ==''or character == '"' or character ==',' or character == '<' or character =='>' or character == '.' or character =='/' or character == '?':
            list[4] += 1
                 

    return list;
def is_palindrome(s): # This method verifies if a given string value is a palindrome
    s = s.lower()  # convert to lowercase for case-insensitive comparison
    s = ''.join(filter(str.isalnum, s))  # remove non-alphanumeric characters
    return int(s == s[::-1])


password=gr.Textbox(label= "Enter a password:")

output = gr.Textbox(label="Password Strength:")

app = gr.Interface(fn = make_prediction, inputs=[password], outputs=output)
app.launch()