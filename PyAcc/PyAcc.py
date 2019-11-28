# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 14:01:02 2019
This is a module to help handle accounting of any camp or short term event

@author: Elucidator
"""
import string
import copy
import time

class Account():
    '''class to represent the Income and expenditure'''
    def __init__(self,filename,filetype,sepa = None):
        '''
        
        '''
        file = open(filename,'r')
        self.data = file.readlines()
        file.close()
        if filetype == 'csv':
            for i in range(len(self.data)):
                self.data[i] = self.data[i].strip('\n')
                seperata = self.data[i].split(',')
                self.data[i] = seperata
        # other file type TO DO
        self.col = dict()
        self.version = []
        self.version.append(copy.deepcopy(self.data))
        self.time = []
        self.time.append(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))
    
    def __repr__(self):
        '''
        print all data
        '''
        for line in self.data:
            print(line)
        return ''
    def size(self):
        '''
        return the size of data as form of (columns,rows)
        '''
        return (len(self.data[0]),len(self.data))
    def ColIndex(self,RowNum):
        '''
        Choose a row as the index for searching
        The choosen row will be saved into the col and delete from data
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
        Add new column
        name : the name of new added column,also new key of self.col
        default : the default for added elements
        '''
        if type(name) != str:
            raise ValueError('Name of new column must be string')
        if name not in self.col:
            self.col[name] = len(self.col)
            for row in self.data:
                row.append(default)
        else:
            raise ValueError(f'{name} has been in columns')
    def add_row(self,newData):
        '''
        Addi a new row
        newData : the added data
        '''
        if type(newData) != list or type(newData) != tuple:
            raise TypeError('newData type must be list or tuple not ',type(newData))
        elif len(newData) != len(self.col):
            raise KeyError('Length of newData is not equal to ',len(self.col))
        else:
            self.data.append(newData)
    def del_row(self,RowNum):
        '''
        Delete one row from data
        RowNum : position of remove row
        '''
        if type(RowNum) != int:
            raise TypeError('index must be integer')
        elif (RowNum < 0 and len(self.data) + RowNum < 0) or (RowNum >= len(self.data)):
            raise KeyError('index out of range ',f'range: 0 to {len(self.data)}')
        del self.data[RowNum]
    def del_col(self,ColName = None,ColNum = None):
        '''
        Delete one column from data
        ColName : name of remove column
        ColNum : index of remove column
        '''
        # both ColName and ColNum are None or have value
        if (ColName == None and ColNum == None) or (ColName != None and ColNum != None):
            raise Exception('each function call is delete by either ColName or ColNum')
        # using ColName to delete
        if ColName in self.col and ColNum == None:
            ColNum = self.col[ColName]
            for line in self.data:
                del line[ColNum]
            for key in self.col:
                if self.col[key] > self.col[ColName]:
                    self.col[key] -= 1
            del self.col[ColName]
            return None
        elif ColNum == None:
            raise KeyError('no column named ',ColName)
        # using ColNum to delete
        if type(ColNum) != int:
            raise TypeError('index must be integer')
        elif (ColNum < 0 and len(self.col) + ColNum < 0) or (ColNum >= len(self.col)):
            raise KeyError('index out of range',f'range: 0 to {len(self.col)}')
        for line in self.data:
            del line[ColNum]
        del self.col[list(self.col.keys())[list(self.col.values()).index(ColNum)]]
        for key in self.col:
            if self.col[key] > ColNum:
                self.col[key] -= 1       
    def condition_to_index(cond):
        ''''''
        for key in cond:
            if type(cond[key]) != (tuple or str):
                raise TypeError('condition must be tuple or str but ',key,':',cond[key])
            elif type(cond[key]) == tuple:
                try:
                    cond = list(cond)
                    cond[0] = float(cond[0])
                    cond[1] = float(cond[1])
                except:
                    raise KeyError('if using tuple as condition,input must be (lowerbound,upperbount)')
                    
                    
        
        return None
    def SumofCol(self,ColName,condition = None):
        '''
        Return the sum of a column with some special condition
        ColName : the target column's name,which must be a element in self.col
        condition : dictionary to choose data
        '''
        if ColName not in self.col:
            raise KeyError('ColName is not a column')
        if condition == None:
            Sum = 0
            for row in self.data:
                if type(row[self.col[ColName]]) != int or float:
                    raise TypeError(f'{self.col[ColName]} is not a int or float data')
                Sum += row[self.col[ColName]]
            return Sum
        if type(condition) == dict:
            for key in condition.keys():
                if key not in self.col:
                    raise KeyError('condition has key not in column',self.col.keys())
            # TO DO
        else:
            raise TypeError('condition must be a dictionary not ',type(condition))
        
            
            
    def AvgofCol(self,ColName,condition = None):
        '''
        '''
        Sum = self.SumofCol(ColName,condition)
        if condition == None:
            number = len(self.data)
        if condition != None:
            ''''''
            
        return Sum/number
    def count(self,ColNum,condition = None):
        '''
        '''
    
    def ClearOldVer(self):
        '''
        method to clear all backup
        '''
        self.version = []
        self.version.append(copy.deepcopy(self.data))
        self.time = []
        self.time.append(time.strftime("%Y/%m/%d %H:%M:%S", time.localtime()))
    def search(self,condition):
        '''
        '''

A = 55
print(f'{A}')
        
        
        
        
        
        
        