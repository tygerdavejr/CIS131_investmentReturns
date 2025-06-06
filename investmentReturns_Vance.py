'''
    script: investmentReturns.py
    action: a. Calculates interest on $1000 for 10, 20 and 30 years at 7%
            b. Display results
    author: David Vance
    date: 20 January 2025
'''


#global variables
'''
    You can change your values for some of the program here.
    Adjust principle and rate as you need.
'''
PRINCIPLE = 1000
RATE = .07


def calculateInterestRates(time):
    '''
    Calculates the amount at the end of the interest period

    action: Receives principle, rate and time when called
            Completes the interest calculation
            Returns the amount accrued
    input:  None      
    output: None
    return: amount accrued   
    '''
    # Complete the interest calculation
    amountAccrued = PRINCIPLE * (1 + RATE) ** time

    # return amount accrued
    return amountAccrued


def main():
    '''
    Displays the accumulated amount to the user

    action: displays the accumulated amount to the user
    input:  none
    output: message to user
    return: none
    '''
    
    #local variables
    '''
        You can change your times here.  The module is designed
        to process the amountAccrued at 10, 20 and 30 years.
        You can change this by modifying your multiplier vs loopCounter
        and down below in the while loop.

        A more elegant solution would be to build a list with the year
        values you wanted to use and then cycle through the list values,
        but I didn't think about that when I wrote this.
    '''
    loopCounter = 1
    time = loopCounter * 10
    
    print('The following output displays the investment returns as years and amount accrued')
    print(f'on a principle of ${PRINCIPLE} at a rate of {(RATE * 100):.0f}%.\n')

    # call function while time <= 30 years
    while time <= 30:
        amountAccrued = calculateInterestRates(time)
        
        print(f'{time} years:  ${amountAccrued:.2f}')
        loopCounter += 1
        time = loopCounter * 10
    return


if __name__ == '__main__':
    main()
