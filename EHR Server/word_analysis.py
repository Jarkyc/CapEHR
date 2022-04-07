def analyze_command(sentence):
    if "open" in sentence or "get" in sentence:
        #<open the patient file>
        #user can say commands in form of file sections
        #mode for just saying the string of requests? i.e. "open 123 birthday" or "open 321 procedure 41 doctor"