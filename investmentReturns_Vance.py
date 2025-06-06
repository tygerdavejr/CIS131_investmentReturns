'''
    script: investmentReturns.py
    action: a. Calculates interest on $1000 for 10, 20 and 30 years at 7%
            b. Display results
    author: David Vance
    date: 20 January 2025
'''


#global constants and variables
'''
    You can change your values for the program here.
    Adjust principle and rate based on loan parameters.
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
    frequency = [10, 20, 30]

    # Process each year in the list one at a time until the list is complete
    
    for index in range(len(frequency[]));

        amountAccrued = calculateInterestRates(frequency[index])

        print('The following output displays the investment returns as years and amount accrued')
        print(f'on a principle of ${PRINCIPLE} at a rate of {(RATE * 100):.0f}%.\n')
        print(f'{frequency[index]} years:  ${amountAccrued:.2f}')
        
    return



if __name__ == '__main__':
    main()
