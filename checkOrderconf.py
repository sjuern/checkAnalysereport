# -*- coding: utf-8 -*-
"""
Created on Fri Oct  6 14:12:00 2017

@author: ths
"""
import os.path
import time


lastmod = os.path.getmtime('C:\LW\Prod\Secure Reports\Ordrebekreftelser')


localTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(lastmod))


print ('This is the time: ', localTime)






