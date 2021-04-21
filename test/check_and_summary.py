
from check import check

class check_and_summary(object):
    """This class contain the function to write the summary.txt file."""
    def check_definition(list):
        '''This function will check the list for different L and will write the summary.txt '''
        temp=[]
        with open('summary.txt', 'a+', encoding='utf-8') as f:
            #create and write on summary.txt
            if list[0]=='L1':
                #check the line start with L1
                try:
                    temp.append(check.check_sub_sectionsL11(list[1]))
                except :
                    temp.append(['L1','L11','','digits','',1,'E05','L11 field under section L1 is missing.'])
                f.write(temp[0][7]+'\n')
                del temp[0][7]
                try:
                    temp.append(check.check_sub_sectionsL12(list[2]))
                except :
                    temp.append(['L1','L12','','word_characters','',3,'E05','L12 field under section L1 is missing.'])
                f.write(temp[1][7]+'\n')
                del temp[1][7]

                try:
                    temp.append(check.check_sub_sectionsL13(list[3]))
                except :
                    temp.append(['L1','L13','','word_characters','',2,'E05','L13 field under section L1 is missing.'])
                f.write(temp[2][7]+'\n')
                del temp[2][7]


            elif list[0]=='L2':
                #check the line start with L2
                try:
                    temp.append(check.check_sub_sectionsL21(list[1]))
                except :
                    temp.append(['L2','L21','','word_characters','',1,'E05','L21 field under section L1 is missing.'])
                f.write(temp[0][7]+'\n')
                del temp[0][7]

                try:
                    temp.append(check.check_sub_sectionsL22(list[2]))
                except :
                    temp.append(['L2','L22','','digits','',1,'E05','L22 field under section L1 is missing.'])
                f.write(temp[1][7]+'\n')
                del temp[1][7]

                try:
                    temp.append(check.check_sub_sectionsL23(list[3]))
                except :
                    temp.append(['L2','L23','','word_characters','',2,'E05','L23 field under section L1 is missing.'])
                f.write(temp[2][7]+'\n')
                del temp[2][7]


            elif list[0]=='L3':
                #check the line start with L3
                try:
                    temp.append(check.check_sub_sectionsL31(list[1]))
                except :
                    temp.append(['L3','L31','','word_characters','',1,'E05','L31 field under section L1 is missing.'])
                f.write(temp[0][7]+'\n')
                del temp[0][7]
            elif list[0]=='L4':
                #check the line start with L4
                try:
                    temp.append(check.check_sub_sectionsL41(list[1]))
                except :
                    temp.append(['L4','L41','','word_characters','',1,'E05','L41 field under section L1 is missing.'])
                f.write(temp[0][7]+'\n')
                del temp[0][7]

                try:
                    temp.append(check.check_sub_sectionsL42(list[2]))
                except :
                    temp.append(['L4','L42','','digits','',6,'E05','L42 field under section L1 is missing.'])
                f.write(temp[1][7]+'\n')
                del temp[1][7]

        return temp


