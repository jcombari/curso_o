#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 18:47:28 2016

@author: oscar
"""


def is_adult2(year,month,day):
    from datetime import  datetime 
    today_minus_18years=datetime(datetime.now().year-18, datetime.now().month, datetime.now().day)
    birth_date = datetime(year, month, day)
    print birth_date,  today_minus_18years
    if birth_date > today_minus_18years:
        return False
    else:
        return True
print is_adult2(1998,10,18)