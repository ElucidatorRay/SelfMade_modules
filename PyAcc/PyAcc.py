# -*- coding: utf-8 -*-
"""
Created on Sat Nov 16 14:01:02 2019
This is a module to help handle accounting of any camp or short term event

@author: Elucidator
"""
import string

class Account():
    '''class to represent the Income and expenditure'''
    
    def __init__(self,filename,filetype):
        file = open(filename,'r')
        self.data = file.readlines()
        self.backup = file.readlines()
        file.close()
        if filetype == 'csv':
            for i in range(len(self.data)):
                self.data[i] = self.data[i].strp('\n')
                seperate = self.data[i].split(',')
                self.data[i] = seperate
        #other file type TO DO
        self.col = dict()
        self.row = dict()
    def __len__(self):
        '''
        return the size of data as form of (columns,rows)
        '''
        return (len(self.data[0]),len(self.data))
    def __repr__(self,condition = None):
        '''
        methos to print data of this account
        condition can be used to add condition 
        '''
        if condition == None:    
            for line in self.data:
                print(line)
        #TO DO
    def ColIndex(self,ColNum):
        '''
        method to choose a column as the index for searching
        the choosen columns will be saved into the col and delete from data
        '''
        for elem in self.data[ColNum]:
            # check if there are whitespace or repeat term
            if self.data[ColNum].count(elem) > 1:
                print('contain repeat elements. Please check again')
                #print('含有重複項，請重新選擇所採用的行 或是檢查輸入資料')
                self.col = dict()
                break
            if elem in string.whitespace:
                print('contain white space. Please check again')
                #print('含有空白，請重新選擇所採用的行 或是檢查輸入資料')
                self.col = dict()
                break
            # assign the choosen column into self.col
            self.col[elem] = self.data[ColNum].index(elem)
        # delete the choosen column
        if self.col != {}:
            del self.data[ColNum]
    def RowIndex(self,RowNum):
        '''
        method to choose a row as the index for searching
        the choosen rows will be saved into the row and delete from data
        '''
        # TO DO
    def delete_row(self,*args):
        '''
        method to delete the choosen row
        '''
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
        
        
        
        