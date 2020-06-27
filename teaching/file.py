
import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(a):
    a = a.lower()
    if a in data:
        return data[a]
    elif len(get_close_matches(a,data.keys()))>0:
        yn =  input("Did you mean %s instead? Enter Y if yes or N if no: " % get_close_matches(a,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(a,data.keys())[0]]
        elif yn == "N":
            return "word doesn't exist"
        else:
            return "Hein??"
    else:
        return "word doesn't exist"

a = input("Enter the word:")

output = translate(a)

if type(output) == list:  
    for item in output:
        print(item)
else:
    print(output)
