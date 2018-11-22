def konversi_suhu (C=0, F=0):
    if C != 0 :
        x = ((9/5*C) + 32)
        print ('suhu',C, 'celcius setara dengan', x, 'fahrenheit')
    elif F != 0 :
        y = (5/9 *(F-32))
        print ('suhu',F, 'fahrenheit setara dengan', y, 'celcius')
    else :
        print('suhu 0 celciusnsetara dengan 32 fahrenheit')
    return ;
        
