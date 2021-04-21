class check(object):
    """This class contains all functions to check the sub_sections in the json file"""
    def check_sub_sectionsL11(data):
        '''This function check L11 part with the difinition in json file, same for later functions in this class
        '''
        list=['L1','L11','','digits','',1,'']
        list[4]=len(data)     
        message_template=''
        if data.isdigit():
            list[2]='digits'
            if len(data)<=1:
                list[6]='E01'
                message_template='L11 field under segment L1 passes all the validation criteria.'
            else:
                list[6]='E02'
                message_template='''L11 field under section L1 fails the max length (expected: 1) validation, however it passes the data type (digits) validation'''
        else:
            if data.isalpha():
                list[2]='word_characters'
            else:
                list[2]='others'
            if len(data)<=1:
                list[6]='E03'
                message_template='''L11 field under section L1 fails the data type (digit) validation, however it passes the max length (expected: 1) validation'''
            else:
                list[6]='E04'
                message_template='L11 field under section L1 fails all the validation criteria.'
        list.append(message_template)
        return list
    def check_sub_sectionsL12(data):
        list=['L1','L12','','word_characters','',3,'']
        list[4]=len(data)     
        message_template=''
        if data.isalpha():
            list[2]='word_characters'
            if len(data)<=3:
                list[6]='E01'
                message_template='L12 field under segment L1 passes all the validation criteria.'
            else:
                list[6]='E02'
                message_template='''L12 field under section L1 fails the max length (expected: 3) validation, however it passes the data type (word_characters) validation'''
        else:
            if data.isdigit():
                list[2]='digits'
            else:
                list[2]='others'
            if len(data)<=3:
                list[6]='E03'
                message_template='''L12 field under section L1 fails the data type (word_characters) validation, however it passes the max length (expected: 3) validation'''
            else:
                list[6]='E04'
                message_template='L12 field under section L1 fails all the validation criteria.'
        list.append(message_template)
        return list
    def check_sub_sectionsL13(data):
        list=['L1','L13','','word_characters','',2,'']
        list[4]=len(data)     
        message_template=''
        if data.isalpha():
            list[2]='word_characters'
            if len(data)<=2:
                list[6]='E01'
                message_template='L13 field under segment L1 passes all the validation criteria.'
            else:
                list[6]='E02'
                message_template='''L13 field under section L1 fails the max length (expected: 2) validation, however it passes the data type (word_characters) validation'''
        else:
            if data.isdigit():
                list[2]='digits'
            else:
                list[2]='others'
            if len(data)<=2:
                list[6]='E03'
                message_template='''L12 field under section L1 fails the data type (word_characters) validation, however it passes the max length (expected: 3) validation'''
            else:
                list[6]='E04'
                message_template='L12 field under section L1 fails all the validation criteria.'
        list.append(message_template)
        return list
    def check_sub_sectionsL21(data):
        list=['L2','L21','','word_characters','',1,'']
        list[4]=len(data)     
        message_template=''
        if data.isalpha():
            list[2]='word_characters'
            if len(data)<=1:
                list[6]='E01'
                message_template='L21 field under segment L2 passes all the validation criteria.'
            else:
                list[6]='E02'
                message_template='''L21 field under section L2 fails the max length (expected: 1) validation, however it passes the data type (word_characters) validation'''
        else:
            if data.isdigit():
                list[2]='digits'
            else:
                list[2]='others'
            if len(data)<=1:
                list[6]='E03'
                message_template='''L21 field under section L2 fails the data type (word_characters) validation, however it passes the max length (expected: 1) validation'''
            else:
                list[6]='E04'
                message_template='L21 field under section L2 fails all the validation criteria.'
        list.append(message_template)
        return list
    def check_sub_sectionsL22(data):
        list=['L2','L22','','digits','',1,'']
        list[4]=len(data)     
        message_template=''
        if data.isdigit():
            list[2]='digits'
            if len(data)<=1:
                list[6]='E01'
                message_template='L22 field under segment L2 passes all the validation criteria.'
            else:
                list[6]='E02'
                message_template='''L22 field under section L2 fails the max length (expected: 1) validation, however it passes the data type (digits) validation'''
        else:
            if data.isalpha():
                list[2]='word_characters'
            else:
                list[2]='others'
            if len(data)<=1:
                list[6]='E03'
                message_template='''L22 field under section L2 fails the data type (digit) validation, however it passes the max length (expected: 1) validation'''
            else:
                list[6]='E04'
                message_template='L22 field under section L2 fails all the validation criteria.'
        list.append(message_template)
        return list
    def check_sub_sectionsL23(data):
        list=['L2','L23','','word_characters','',2,'']
        list[4]=len(data)     
        message_template=''
        if data.isalpha():
            list[2]='word_characters'
            if len(data)<=2:
                list[6]='E01'
                message_template='L23 field under segment L2 passes all the validation criteria.'
            else:
                list[6]='E02'
                message_template='''L23 field under section L2 fails the max length (expected: 2) validation, however it passes the data type (word_characters) validation'''
        else:
            if data.isdigit():
                list[2]='digits'
            else:
                list[2]='others'
            if len(data)<=2:
                list[6]='E03'
                message_template='''L23 field under section L2 fails the data type (word_characters) validation, however it passes the max length (expected: 2) validation'''
            else:
                list[6]='E04'
                message_template='L22 field under section L2 fails all the validation criteria.'
        list.append(message_template)
        return list
    def check_sub_sectionsL31(data):
        list=['L3','L31','','word_characters','',1,'']
        list[4]=len(data)     
        message_template=''
        if data.isalpha():
            list[2]='word_characters'
            if len(data)<=1:
                list[6]='E01'
                message_template='L31 field under segment L3 passes all the validation criteria.'
            else:
                list[6]='E02'
                message_template='''L31 field under section L3 fails the max length (expected: 1) validation, however it passes the data type (word_characters) validation'''
        else:
            if data.isdigit():
                list[2]='digits'
            else:
                list[2]='others'
            if len(data)<=1:
                list[6]='E03'
                message_template='''L31 field under section L3 fails the data type (word_characters) validation, however it passes the max length (expected: 1) validation'''
            else:
                list[6]='E04'
                message_template='L31 field under section L3 fails all the validation criteria.'
        list.append(message_template)
        return list
    def check_sub_sectionsL41(data):
        list=['L4','L41','','word_characters','',1,'']
        list[4]=len(data)     
        message_template=''
        if data.isalpha():
            list[2]='word_characters'
            if len(data)<=1:
                list[6]='E01'
                message_template='L41 field under segment L4 passes all the validation criteria.'
            else:
                list[6]='E02'
                message_template='''L41 field under section L4 fails the max length (expected: 1) validation, however it passes the data type (word_characters) validation'''
        else:
            if data.isdigit():
                list[2]='digits'
            else:
                list[2]='others'
            if len(data)<=1:
                list[6]='E03'
                message_template='''L41 field under section L4 fails the data type (word_characters) validation, however it passes the max length (expected: 1) validation'''
            else:
                list[6]='E04'
                message_template='L41 field under section L3 fails all the validation criteria.'
        list.append(message_template)
        return list
    def check_sub_sectionsL42(data):
        list=['L4','L42','','digits','',6,'']
        list[4]=len(data)     
        message_template=''
        if data.isdigit():
            list[2]='digits'
            if len(data)<=6:
                list[6]='E01'
                message_template='L42 field under segment L4 passes all the validation criteria.'
            else:
                list[6]='E02'
                message_template='''L42 field under section L4 fails the max length (expected: 6) validation, however it passes the data type (digits) validation'''
        else:
            if data.isalpha():
                list[2]='word_characters'
            else:
                list[2]='others'
            if len(data)<=6:
                list[6]='E03'
                message_template='''L42 field under section L4 fails the data type (digit) validation, however it passes the max length (expected: 6) validation'''
            else:
                list[6]='E04'
                message_template='L42 field under section L4 fails all the validation criteria.'
        list.append(message_template)
        return list