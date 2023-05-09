#--------------------------------------------------------------------#
# Name: Pratik Antoni Patekar | Student id: 1001937948               #
#--------------------------------------------------------------------#
# Submission date: 5th April 2023 | OS: Windows 11                   #
#--------------------------------------------------------------------#

import os

# This is an object type stack that I have created.
# This object type basically creates a stack array that supports
# operations such as push and pop along with printing the stack 
# contents 
class Stack:
    # stack initialization
    # the print_flag basically enables us to check the status of
    # stack after every push or pop operation.
    def __init__(self, print_flag = True):
        self.stack_arr = []
        self.print_flag = print_flag

    # Push operation on stack. 
    # Returns 0 on successful push operation else -1
    def push(self, elem):
        # if the given elem element is number then push on stack
        if is_num(elem): # is_alnum is defined below
            if self.print_flag == True:
                print("\nBefore push:", self.stack_arr)
            
            # add the element to the stack
            self.stack_arr.append(float(elem))

            if self.print_flag == True:
                print("After push:", self.stack_arr)
            
            return 0 # return 0 on successful push on stack
        
        else: # if the elem is not number/ operand then print error
            print("ERROR: The element pushed on stack is not valid number.")
            print("Element being tried to add: " + str(elem))
            return -1 # return -1 if push operation not successful
    
    # Pop operation on stack.
    # Returns the popped element if pop operation was successful
    # else returns "error" as string
    def pop(self):
        # Try popping element from the stack
        try:
            # read the last element of the stack to be popped
            return_elem = self.stack_arr[len(self.stack_arr)-1]

            if self.print_flag == True:
                print("\nBefore pop:", self.stack_arr)
            
            # remove the last element from the stack
            self.stack_arr = self.stack_arr[:len(self.stack_arr)-1]

            if self.print_flag == True:
                print("After pop:", self.stack_arr)
            
            # return the popped element
            return return_elem
        
        except:
            # If there is any error then return error
            return_elem = "error"
            print("\nERROR: The stack is empty!!")

            # return error
            return return_elem
    
    # Function to return True if stack is empty or else False
    def is_empty(self):
        if self.stack_arr == []:
            return True
        else:
            return False

    # Function to print the status of stack
    def __str__(self):
        # print the stack array
        print("Stack stat:", self.stack_arr)
        return ""

# Function to check if the variable s is numeric value
# i.e. float or integer
# Returns True if s is float or integer otherwise returns False
def is_num(s):
    try:
        float(s)
        return True
    except:
        return False

# Function to remove any empty strings present in the arr
def remove_empty_string(arr):
    ret_arr = []
    warning_flag = False
    for i in arr:
        if i != "":
            ret_arr.append(i)
        else:
            warning_flag = True
    
    if warning_flag == True:
        print("WARNING: The input expression contains more spaces between operands and operators than required.")
    return ret_arr

# Main function
def main():
    # List of operations that are supported by this program
    expression_list = ["+", "-", "*", "/"]
    
    # stack print flag status
    # change to True if you want to print the stack after 
    # every push and pop operation
    stack_print_flag = False 
    
    # Read the input file 'input_RPN.txt' from same directory 
    with open(os.path.join(os.getcwd(), '.\input_RPN.txt'), 'r') as file:
        lines = file.readlines()
        rpn_expressions = []

        for line in lines:
            rpn_expressions.append(line.rstrip('\n'))
            # rpn_expressions array will contain RPN expressions
            # from each line in the file

    # counter for line number 
    counter = 1

    # for every RPN expression present on each line in the input file
    # do the following
    for rpn_in in rpn_expressions:
        # 1. Split the input expression by spaces
        rpn_in_split = remove_empty_string(rpn_in.split(" "))
        
        # 2. Create an empty stack
        stack = Stack(stack_print_flag)

        # 3. Iterate over the rpn expression rpn_in_split
        for i in rpn_in_split:
            # a. If it is a number or digit then push on stack
            if i not in expression_list:
                stat = stack.push(i)
                if stat == -1:
                    print("Exiting code. Error at line " + str(counter) + " in input file.")
                    return
            # b. If it is an operation then do the following
            else:
                # i. pop the last two elements added to stack
                elem1 = stack.pop()
                elem2 = stack.pop()

                # if the stack is not poppable or if stack is empty
                # then print error and exit the code execution
                if elem1 == "error" or elem2 == "error":
                    print("Stack is empty and can not be popped.") 
                    print("Please check the expression entered at line " + str(counter) + ".")
                    return
                
                # ii. Perform the operation on popped elements
                # and push it back to stack
                # Addition operation
                if i == "+":
                    result = elem1 + elem2
                    stack.push(result)
                # Subraction operation
                elif i == "-":
                    result = elem2 - elem1
                    stack.push(result)
                # Multiplication operation
                elif i == "*":
                    result = elem1 * elem2
                    stack.push(result)
                # Division operation
                elif i == "/":
                    if elem1 != 0:
                        result = elem2 / elem1
                        stack.push(result)
                    else:
                        print("ERROR: Divide by zero error.")
                        return
                # print error if there is any operation found
                else:
                    print("ERROR: Invalid operation.")
                    return # exit code execution
        
        # 4. Print the final result available on stack
        final_result = stack.pop()

        # If stack is not empty then it means that the number of operands are more 
        # compared to operators present in the input
        if stack.is_empty() == False:
            print("\nWARNING: The RPN expression contains more operands than operators.")
            print("Check line " + str(counter) + " for input errors.")

        print("Result of line " + str(counter) + ":", final_result) # printing the result
        counter += 1 # increment the line count

main()