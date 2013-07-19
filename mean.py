#!/usr/bin/env python

def mean(numlist):
    """Calculate the mean of the values in numlist

    Input
    =====
    `numlist` (`list` or `tuple`) - List of values whose mean will be calculated

    Output
    ======
    (`float`) - Mean of the values in numlist
    
    """
    try :
        total = sum(numlist)
        length = 1.0*len(numlist)
        retmean = total/length
    except TypeError :
        raise TypeError("The list was not numbers.")
    except ZeroDivisionError : 
        raise ZeroDivisionError("The list is empty")
    except :
        print "Something unknown happened with the list."
    return retmean