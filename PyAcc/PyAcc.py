# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 14:01:02 2019
This is a module to help handle accounting of any camp or short term event

@author: Elucidator
"""

class Account():
    '''class to represent the Income and expenditure'''
    
    def __init__(self,filename,filetype):
        file = open(filename,'r')
        self.data = file.readlines()
        self.backup = file.readlines()
        file.close()
        if filetype == 'csv':
            for i in range(len(L)):
                self.data[i] = self.data[i].strp('\n')
                seperate = self.data[i].split(',')
                self.data[i] = seperate
        #other file type TO DO
        self.columns = dict()
        self.rows = dict()
        
    def __repr__(self,condition = None):
        '''
        methos to print data of this account
        condition can be used to add condition 
        '''
        if condition == None:    
            for line in self.data:
                print(line)
        #TO DO
    def delete_row(self,*args):
        args = list(args)
        args.sort()
        try:
            for i in range(len(args)):
                del self.data[i]
                for i in range(len(args)):
                    args[i] -= 1
        except TypeError:
            print('the inupt row numbers must be integers not float or string\n')
    
    def add_column(self,name):
        '''
        method to add new column name to this data
        '''
        
        
        
        