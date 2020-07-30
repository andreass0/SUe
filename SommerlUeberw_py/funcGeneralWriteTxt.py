# -*- coding: utf-8 -*-
"""
Created on Fri May  8 17:59:41 2020

@author: Andreas
"""

# -*- coding: utf-8 -*-
"""
Created on Fri May  8 15:48:26 2020

@author: Andreas
"""

'THIS FUNCTION HAS NO USE IN ITS CURRENT STATE!!!'

# import numpy as np
def generalWriteTxt(fileName, inputValue):
    file = open(fileName, 'w+')
    file.write(str(inputValue)+'\n')
    file.close()
    return file

generalWriteTxt('test.txt', 6)
# array = np.array([1,2,3,4])
# writeTxt('tOP.txt', array)
