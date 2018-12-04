import sys

#the dynamic part
FIB_SAVE = {0:0, 1:1}
LUC_SAVE = {0:2, 1:1}

def fibonacci(n, save = {0:0,1:1}):
    """
    in: a non-negative integer
    out: an integer from fibonacci

    Given input n, this function returns the nth value in the fibonacci series.
    """
    try:
        # dynamic call - if we have calculated this value before,
        # get the value directly from the save.
        if n in save:
            return save[n]

        save[n] = fibonacci(n-1,save) + fibonacci(n-2,save)

        # otherwise, make a recursive call to calculate the value to return
        return save[n]
    except:
        return("Problems in input, please input a non-negative int.")

def lucas(n, save = {0:2, 1:1}):
    """
    in: a non-negative integer
    out: an integer from fibonacci

    Given input n, this function returns the nth value in the Lucas Numbers series.
    """
    try:
        # dynamic call - if we have calculated this value before,
        # get the value directly from the save.
        if n in save:
            return save[n]

        # otherwise, make a recursive call to calculate the value to return
        save[n] = lucas(n-1,save) + lucas(n-2,save)
        return save[n]
    except:
        return("Problems in input, please input a non-negative int.")


def sum_series(n, value1 = 0, value2 = 1):
    """
    in: a non-negative integer, and optional, value1 and value2
    out: an integer from the defined series

    Given a non-negative integer n, and two optional values to define
    the starting base cases, we return the nth value for the series who
    satisfies the fomular as a_n = a_{n-1} + a_{n-2} for n >= 3.

    """
    try:
        # base case 1: when n = 0, return value 1
        if n == 0:
            return value1
        # base case 2: when n = 1, return value 2
        if n == 1:
            return value2

        # the tricky part here, we need to pass along value1 and value2
        # for the recurssive calls.
        return sum_series(n-1, value1, value2) + sum_series(n-2, value1, value2)
    except:
        return("Problems in input, please input a non-negative int.")



def run():
    welcome()

    # initilize for the while loop torun smoothly
    user_input = "None"

    # dynamic part to speed up fib and luc
    FIB_SAVE = {0:0, 1:1}
    LUC_SAVE = {0:2, 1:1}

    while user_input.lower() != 'quit':
        # allow users to quit via control+c nicely.
    # try:
        user_input = ask_question()
    # except KeyboardInterrupt:
        # print("\nQuit program...")
        # exit()

        if 'fibonacci' in user_input.lower():
            # grab input numeric value
            num = (user_input.replace(")","").split("("))
            print("", fibonacci(int(num[-1]),FIB_SAVE),"\n")

        if 'lucas' in user_input.lower():
            # grab input numeric value
            num = (user_input.replace(")","").split("("))
            print("", lucas(int(num[-1]),LUC_SAVE),"\n")

        if 'sum_series' in user_input.lower():
            n, v1, v2 = (user_input.replace(")","").split("("))[-1].split(",")
            print("", sum_series(int(n), float(v1), float(v2)),"\n")

    # print quit info as user exit the while loop
    print("\nQuit program...Bye" )

def ask_question():
    """
    prompt out messages to ask input from user.
    """
    print('type in fibonacci(n) or lucas(n) or sum_series(n, value1, value2) to find out their values; \ntype "quit" to quit.\n\n')
    print('>>>', end = ' ')
    return input()

def welcome():
    """
    print out welcome information when user run the program.
    """
    print("This module defines functions that implement mathematical series...")
    print("\n\n")
    print("fibonacci(n):\n")
    print("\tGiven input n, this function returns the nth value in the fibonacci series.\n\n")
    print("lucas(n):\n")
    print("\tGiven input n, this function returns the nth value in the Lucas Numbers series.\n\n")
    print("sum_series(n, value 1, value 2):\n")
    print("\tGiven input n, the first value of the series <value 1>, the second"\
    "value of the series <value 2>,\n\tthis function returns the nth value in this series."\
    "based on the formalar such that the nth value \n\tequals to the sum of previous 2 values.\n\n")

if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print("\nQuit program...Bye")
        exit()

