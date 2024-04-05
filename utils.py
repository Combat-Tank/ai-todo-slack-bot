def BinaryResponseToBool(string):
    string = string.strip()
    if string == "yes" or string == "Yes" or string == "YES":
        return True
    elif string == "no" or string == "No" or string == "NO":
        return False
    else:
        raise ValueError("Invalid response. Please provide a binary response (yes/no).")
