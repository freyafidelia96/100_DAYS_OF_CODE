
def isvalid(inputString):
    lengthOfString = len(inputString)

    if lengthOfString < 6 or lengthOfString > 16:
        return False
    
    hasLower = hasUpper = hasUpper = hasSpecialChar = False
    specialCharacters = set(["@", "#", "$"])
    
    for element in inputString:
        if element.islower():
            hasLower = True
        
        if element.isupper():
            hasUpper = True

        if element.isnumeric():
            hasNumeric = True
            
        if element in specialCharacters:
            hasSpecialChar = True

    return hasLower and hasUpper and hasNumeric and hasSpecialChar
    

if __name__ == "__main__":
    results = isvalid("5678hU78$#@")
    print(results)