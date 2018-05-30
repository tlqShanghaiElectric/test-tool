# -*- coding: utf-8 -*-
"""
Created on Tue May 29 15:36:56 2018

@author: 12600771
"""

# from prettyNum import prettyNum

def test(actual, expected):
    """ Compare the actual to the expected value,
        and print a suitable message.
    """
    import sys
    linenum = sys._getframe(1).f_lineno   # get the caller's line number.
    if (expected == actual):
        msg = "Test on line {0} passed.".format(linenum)
    else:
        msg = ("Test on line {0} failed. Expected '{1}', but got '{2}'."
                                     . format(linenum, expected, actual))
    print(msg)
    

# test(prettyNum(1820, 1960),(1820, 1960))              
# test(prettyNum(1.21e6, 1.8e6),(1e6, 2e6))              
# test(prettyNum(1.21e6, 1.27e6),(1e6, 2e6))             
# test(prettyNum(-1.8e6, -1.21e6), (-2e6, -1e6))      
# test(prettyNum(-1.25e6, -1.21e6), (-2e6, -1e6))        
# test(prettyNum(-1.25e6, 1.21e6), (-2e6, 2e6))           
# test(prettyNum(8.2e5, 1.8e6), (0, 2e6))
# test(prettyNum(-1.8e6, -8.2e5),(-2e6, 0))
# test(prettyNum(-8.2e6, 1.8e7),(-1e7, 2e7))
# test(prettyNum(-8.2e6, 1.8e9),(-1e9, 2e9))
# test(prettyNum(-8.2e8, 1.8e6),(-9e8, 1e8))

x = np.