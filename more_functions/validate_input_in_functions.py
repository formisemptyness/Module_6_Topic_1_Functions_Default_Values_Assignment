'''
#don't forget your docstring

#Write a function score_input() that takes parameters test_name, test_score, and invalid_message

Program: validate_input_in_functions.py
Author: Joshua M. McGinley
Last Date Modified: 10/05/2022

    docString
    The test_name is a mandatory parameter and will not need validation.
    The test_score is optional, with default value that is negative, eg -1, and will be validated to be between
    0-100
    The invalid_message is optional, with default value 'Invalid test score!'
    Return the string with test name and score if it passes validation; otherwise return the test name with
    invalid_message

    #TRY to cast test_score to an integer
        #Validate if test_score is between 1 and 100 inclusive
            #return string with test_name, and Score #such as 'Test 1: 70'
        #return string with test_name and invalid_message #such as 'Test 2: Invalid Test Score!'
    #exception
        #return string with test_name and invalid_message #such as 'Test 2: Invalid Test Score!'

'''

def score_input(test_name='', test_score=-1, invalid_message = 'Invalid test score!'):
    try:
        int(test_score)
    except:
        print('An evil!')
    if test_score in range(101):
        return(test_name, test_score)
    else:
        return(test_name, invalid_message)

#Write your drive code here
format_string = score_input('Test 4','iam')
display_string = f"{format_string[0]}: {format_string[1]}"
print(display_string)
#the one that starts with if __name__ == '__main__':
if __name__ == '__main__':
    score_input()

#Test 1: 100
#Test 2: Invalid test score!
#Test 3: Invalid test score!
#An evil!
#Test 4: Invalid test score!
