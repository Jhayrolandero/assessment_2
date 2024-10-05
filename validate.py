from datetime import datetime
import re
class Validate:
    
    def validateRequired(self, user_input):
        if(user_input == ""):
            return False
        return user_input
    
    def validateInteger(self, user_input):
        if "." in user_input:
            return False
        if not user_input.isnumeric():
            return False
        return user_input

    def validateDateFormat(self, user_input):
        try:
            datetime.strptime(user_input, "%m-%d-%Y")
        except ValueError:
            return False

    def validateTimeFormat(self, user_input):
        try:
            datetime.strptime(user_input, "%I:%M %p")
        except ValueError:
            return False
        
    def validateSpecialCharacters(self, user_input):
        pattern = r'[!@#$%^&*(),.?":{}|<>]'
        
        if re.search(pattern, user_input):
            return False
        return user_input