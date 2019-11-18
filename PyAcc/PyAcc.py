# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 14:01:02 2019
This is a module to help handle accounting of any camp or short term event

@author: Elucidator
"""
import string
import copy

class Account():
    '''class to represent the Income and expenditure'''
    def __init__(self,filename,filetype):
        file = open(filename,'r')
        self.data = file.readlines()
        file.close()
        if filetype == 'csv':
            for i in range(len(self.data)):
                self.data[i] = self.data[i].strip('\n')
                seperate = self.data[i].split(',')
                self.data[i] = seperate
        # other file type TO DO
        self.col = dict()
        self.version = []
        self.version.append(copy.deepcopy(self.data))
        self.time = []
        # self.time.append(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))
        
    def __len__(self):
        '''
        return the size of data as form of (columns,rows)
        '''
        return (len(self.data[0]),len(self.data))
    def __repr__(self):
        '''
        methods to print data 
        '''
        for line in self.data:
            print(line)
        return ''
    def ColIndex(self,RowNum):
        '''
        method to choose a row as the index for searching
        the choosen row will be saved into the col and delete from data
        RowNum : the index of row user want to use as index of column
        '''
        for elem in self.data[RowNum]:
            # check if there are whitespace or repeat term
            if self.data[RowNum].count(elem) > 1:
                self.col = dict()
                raise Exception('it cant exist more than one same index')
            if elem in string.whitespace:
                self.col = dict()
                raise Exception('it cant exist whitespace')
            # assign the choosen column into self.col
            self.col[elem] = self.data[RowNum].index(elem)
        del self.data[RowNum]
    def add_column(self,name = None,default = None):
        '''
        method to add new column
        default : the default for added elements
        '''
        if name == None or type(name) == int or type(name) == float:
            raise ValueError('Name of new column cant be None or integer or float')
        if name not in self.col:
            self.col[name] = len(self.col)
            for row in self.data:
                row.append(default)
        else:
            raise ValueError(f'{name} has been in columns')
    def add_row(self,newData):
        '''
        method to add a new row
        newData : the added data
        '''
        if type(newData) != list or type(newData) != tuple:
            raise TypeError('newData type must be list or tuple',newData)
        elif len(newData) != len(self.col):
            raise KeyError('Length of newData is not equal to ',len(self.col))
        else:
            self.data.append(newData)
    def del_row(self,RowNum):
        '''
        method to delete one row from data
        RowNum : position of remove row
        '''
        if type(RowNum) != int:
            raise TypeError('index must be integer')
        elif (RowNum < 0 and len(self.data) + RowNum < 0) or (RowNum >= len(self.data)):
            raise KeyError('index out of range ',f'range: 0 to {len(self.data)}')
        del self.data[RowNum]
    def del_col(self,ColNum):
        '''
        method to delete one column from data
        ColNum : position of remove column
        '''
        if type(ColNum) != int:
            raise TypeError('index must be integer')
        elif (ColNum < 0 and len(self.col) + ColNum < 0) or (ColNum >= len(self.col)):
            raise KeyError('index out of range',f'range: 0 to {len(self.col)}')
        for line in self.data:
            del line[ColNum]
    def SumofCol(self,ColNum,condition = None):
        '''
        '''
        if ColNum != int:
            raise TypeError('index must be integer')
        if condition = None:
            Sum = 0
            for row in self.data:
                Sum += row[ColNum]
        if condition != None:
            
    def search(row = None,column = None):
        '''
        method to search the data with determined row and column
        or 
        '''

        
        
        
        
        
        
        
        
        
        
        
        
        
        