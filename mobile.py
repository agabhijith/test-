'''
function to check if a mobile number is valid
'''
def is_valid_mobile_number(number):
    if len(number)==10 and number[0] in "987":
        return True
    return False
number =(input("Enter a mobile number:"))
if is_valid_mobile_number(number):
    print(f"The mobile number is {number} is valid")
else:
    print(f"the mobile number is {number} is invalid")
