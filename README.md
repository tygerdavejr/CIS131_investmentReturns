# CIS131_investmentReturns
CIS 131: Calculate Investment Returns on $1000 at a rate of 7% interest at 10, 20 and 30 years

PROGRAM Investment Returns
David Vance
CIS 131 - Programming and Problem Solving II
Professor Kevin Chang
20 January 2025

# INITIATIONS
# Import modules, declare CONSTANTS, set variables, build dictionaries and 
# build classes

CONSTANT PRINCIPLE = 1000
CONSTANT RATE = 0.07

    FUNCTION calculate interest rates(time)
        # Calculates interest at specific time periods
        amount accrued = PRINCIPLE * (1 + RATE) ^ time
        RETURN amount accrued
    END FUNCTION


# MAIN PROCESSING
# Call to main() function, intitiate processing, print reports, end program

    FUNCTION main()
        # Display header for report
        PRINT "The following output displays the investment returns as years and amount accrued"
        PRINT "on a principle of $" + principle + " at a rate of " + (rate * 100) + "%."

        # Initialize loop variables
        loop counter = 1
        time = loop counter * 10

        # Loop through time periods at 10-year intervals
        WHILE time <= 30
            amount accrued = calculate interest rates(time) from FUNCTION
            PRINT time + " years: $" + amount accrued (with 2 decimal points)
            loopCounter = loopCounter + 1
            time = loopCounter * 10
        END WHILE
    END FUNCTION


# PROGRAM ENTRY POINT

IF __name__ == "__main__" THEN
    CALL main()
END IF


END PROGRAM


Instructions
7% Investment Return

Some investment advisors say that it’s reasonable to expect a 7% return over the long term in the stock market.
If you begin with $1000 and leave your money invested, calculate, and display how much money you’ll have after 
10, 20 and 30 years. Use the following formula for determining these amounts:

a = p(1 + r)^n
    where
p is the original amount invested (i.e., the principal of $1000),
r is the annual rate of return (7%),
n is the number of years (10, 20 or 30) and
a is the amount on deposit at the end of the
nth year.

You will need to use your IDE to complete this assignment. Once completed, please submit your .py file to D2L.

DESIGN NOTES:
This module could easily be written as one line, but the assignment called for developing this in our IDE, 
so I chose to do a loop in order to calculate the three different values.  For some reason I have a 
compulsion to not write repeated lines of code.

I also prefer to leave room for future modifications by writing a program full-out.  It keeps my logic and
syntax sharp.
