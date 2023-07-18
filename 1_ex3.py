def find_sigfigs(a):
    '''Returns the number of significant digits in a number. This takes into account
       strings formatted in 1.23e+3 format and even strings such as 123.450'''
    # change all the 'E' to 'e'
    a = a.lower()
    if ('e' in a):
        # return the length of the numbers before the 'e'
        myStr = a.split('e')
        return len( myStr[0] ) - 1 # to compensate for the decimal point
    else:
        # put it in e format and return the result of that
        m = ('%.*e' %(20, float(a))).split('e')
        # remove and count the number of removed user added zeroes. (these are sig figs)
        if '.' in a:
            s = a.replace('.', '')
            #number of zeroes to add back in
            l = len(s) - len(s.rstrip('0'))
            #strip off the python added zeroes and add back in the ones the user added
            m[0] = m[0].rstrip('0') + ''.join(['0' for num in range(l)])
        else:
            #the user had no trailing zeroes so just strip them all
            m[0] = m[0].rstrip('0')
        #pass it back to the beginning to be parsed
    return find_sigfigs('e'.join(m))

n = 0
a = 1
while a > 0:
    n = n+1
    print(a)
    print('Number of significant numbers:',find_sigfigs(str(a)))
    a = (1.0+2.0**(-n))-1.0