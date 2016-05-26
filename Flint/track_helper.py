
def Additive_for_Log_Chart(value):
    try:        
        d = float(value)
        if d < 1:
            c = (len(str(value)) - 2)
            #print('Additive calc: ' + str(value) + '\tC: ' + str(c))
            y = '0.'
            for i in range(1,c):
                y += '0'
            y += '1'
            return float(y)
        else:
            index = str(value).index('.')
            y = '1'
            for i in range(1, index):
                y += '0'
            return float(y)
    except:
        print('Unable to determine number of significant digits for ' + str(value))
