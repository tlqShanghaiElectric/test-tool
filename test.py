# -*- coding: utf-8 -*-
"""
Created on Tue May 29 15:36:56 2018

@author: 12600771
"""

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
    
