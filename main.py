import os
import re
import csv
import unittest
from check_and_summary import check_and_summary

def readfile(inputfile):
    ''' This function is used to read the input file and store splited elements in list'''
    
    linelist=[]
    with open(inputfile) as f:
        for eachline in f:
            eachline = eachline.replace('\n','')
            newline=re.split(r'&',eachline)
            linelist.append(newline)
    return linelist

if __name__ == '__main__':

    listnew=readfile('input_file.txt')
    with open('report.csv',mode='a+',newline="") as report_file:
        # create report.csv and start writing elements to the csv file
        report_writer=csv.writer(report_file)
        report_writer.writerow(['Section','Sub-Section','Given DataType','Expected DataType','Given Length','Expected MaxLength','Error Code'])
        for x in listnew:
            #call the function in check_and_summary.py to create summary.txt
            temp=check_and_summary.check_definition(x)
            for x in temp:
                report_writer.writerow(x)
    unittest.main(verbosity=1) # run unit-test

