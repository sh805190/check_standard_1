import os
import re
import csv
import json
import unittest
import unit_test

def readfile(inputfile):
    ''' This function is used to read the input file and store splited elements in list'''
    
    linelist=[]
    with open(inputfile) as f:
        for eachline in f:
            eachline = eachline.replace('\n','')
            newline=re.split(r'&',eachline)
            linelist.append(newline)
    return linelist

def check_standard_file(line,standard):
    ''' This function is used to check one line's error and store each small 'L's 
        detail to the list csvlist_for_each_L, then store all list for small 'L'
        to one large list csvlist_for_line
    '''
    csvlist_for_line=[]
    csvlist_for_each_L=[]
    index=-1;
    checkresult={}
    errorcodelist=[]
    
    errorcode=''
    flag=False
    for x in standard:
        if x['key']==line[0]:
            index=standard.index(x);
            gen=[y for y in line[1:]] 
            for each_sub_section in x['sub_sections']:
                temp=x['sub_sections'].index(each_sub_section)
                if temp<len(gen):
                    for index_inline in range(temp,len(gen)):
                        checkresult=check_sub_sections(gen[index_inline],index,index_inline)
                        if each_sub_section['key']==checkresult['key']:
                            if each_sub_section['data_type']==checkresult['data_type']:
                                if  each_sub_section['max_length']>=checkresult['max_length']:
                                    # check E01
                                    errorcode='E01'
                                    csvlist_for_each_L=[x['key'],each_sub_section['key'],checkresult['data_type'],each_sub_section['data_type'],
                                                        checkresult['max_length'],each_sub_section['max_length'],errorcode]
                                    csvlist_for_line.append(csvlist_for_each_L)
                                    break
                                
                                else:
                                    # check E03
                                    errorcode='E03'
                                    csvlist_for_each_L=[x['key'],each_sub_section['key'],checkresult['data_type'],each_sub_section['data_type'],
                                                        checkresult['max_length'],each_sub_section['max_length'],errorcode]     
                                    csvlist_for_line.append(csvlist_for_each_L)
                                    break
                                
                            else:
                                if  each_sub_section['max_length']>=checkresult['max_length']:
                                    # check E02
                                    errorcode='E02'
                                    csvlist_for_each_L=[x['key'],each_sub_section['key'],checkresult['data_type'],each_sub_section['data_type'],
                                                        checkresult['max_length'],each_sub_section['max_length'],errorcode]    
                                    csvlist_for_line.append(csvlist_for_each_L)

                                    break
                                
                                else:
                                    # check E04
                                    errorcode='E04'
                                    csvlist_for_each_L=[x['key'],each_sub_section['key'],checkresult['data_type'],each_sub_section['data_type'],
                                                        checkresult['max_length'],each_sub_section['max_length'],errorcode]
                                    csvlist_for_line.append(csvlist_for_each_L)

                                    break                            
                else:
                    #check if missing E05
                    errorcode='E05'
                    csvlist_for_each_L=[x['key'],each_sub_section['key'],'',each_sub_section['data_type'],
                                        '',each_sub_section['max_length'],errorcode]
                    csvlist_for_line.append(csvlist_for_each_L)
    return csvlist_for_line 


            
def check_sub_sections(string1,index_of_standard,index_of_line):
    '''This function is used to check a string if is digit, word_characters or others,
        then return the definition in a list
    '''

    marker={'key':'','data_type':'','max_length':''}
    marker['key']='L'+str(index_of_standard+1)+str(index_of_line+1)
    if string1.isalpha():
        marker['data_type']='word_characters'
    elif string1.isdigit():
        marker['data_type']='digits'
    else:
        marker['data_type']='others'
    marker['max_length']=len(string1)
    return marker

def write_summary(list,error_codes):
    '''Write summary according to the error_code file
    '''
    strnew=''
    for x in error_codes:
        if list[6]==x['code']:
            strnew=x['message_template'].replace('LXY',list[1]).replace('LX'
                                                ,list[0]).replace('{data_type}',list[3]).replace('{max_length}',str(list[5]))
            return strnew

if __name__ == '__main__':
    with open('standard_definition.json') as f:
        standard=json.load(f)
    listnew=readfile('input_file.txt')
    with open('error_codes.json') as f:
        error_codes=json.load(f)
    with open('report.csv',mode='a+',newline="") as report_file:
        # create report.csv and start writing elements to the csv file
        report_writer=csv.writer(report_file)
        report_writer.writerow(['Section','Sub-Section','Given DataType','Expected DataType','Given Length','Expected MaxLength','Error Code'])
        for x in listnew:
            #call the function check_standard_file 
            temp=check_standard_file(x,standard)
            for x in temp:
                report_writer.writerow(x)
            # create summary.txt and start writing elements to the txt file
            with open('summary.txt', 'a+', encoding='utf-8') as f:
                for y in temp:
                    f.write(write_summary(y,error_codes)+'\n')



