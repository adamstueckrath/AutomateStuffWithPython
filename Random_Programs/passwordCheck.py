
# coding: utf-8
#! python3
# test for secure password 

# ^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*(_|[^\w])).+$
securePasswordCheck = re.compile(r''' 
                ^           # the start of the string
                (?=.*[a-z]) # use positive look ahead to see if at least one lower case letter exists
                (?=.*[A-Z]) # use positive look ahead to see if at least one upper case letter exists
                (?=.*\d)    # use positive look ahead to see if at least one digit exists
                (?=.*[-+_!@#$%^&*.,?]) # look ahead to see if at least one non-word character 
                .+          # gobble up the entire string
                $           # the end of the string
                ''',re.VERBOSE)
# Unit test 
print(securePasswordCheck.findall('testid_Ddsad1'))
print(securePasswordCheck.findall('1111_reast'))
print(securePasswordCheck.findall('testi!@#d_reast'))

