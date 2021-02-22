from best_fit_line import *
from polynomial_roots import *
from fractions import Fraction

def take_input(f):
    file = open('Input.txt','r')
    content = file.readlines()

    if f != 'curve fitting':
        for i, line in enumerate(content):
            content[i] = line.strip().split(',')
        for i in content:
            for j in range(len(i)):
                i[j] = float(Fraction(i[j]))
        return content
    
    for i, line in enumerate(content):
        content[i] = line.strip().split(',')
    for i in content:
        for j in range(len(i)):
            i[j] = float(i[j])
    points = content[:-1]
    degree = content[-1]
    
    return points, int(degree[0])


def pr_matrix(result, mode, limit):
    for vec in result:
        for i in range(len(vec)):
            if mode == 'frac':
                if limit == None:
                    limit = 1000
                vec[i] = Fraction(vec[i]).limit_denominator(limit)

            if mode == 'dec':
                if limit == None:
                    dec = 4
                elif limit == 0:
                    dec = None
                else:
                    dec = limit 
                vec[i] = round(vec[i], dec)

                
            vec[i] = str(vec[i])
        output = ''
        for i in vec:
            output += i+', '
        print('['+output[:-2]+']')


def calculate(f, mode = 'frac', limit = None):
    '''
    (str) -> None
    print the result
    '''
    data = take_input(f)
    if f == 'polynomial':
        data = data[0]
        roots = sorted(find_roots(data))
        print('The roots of polynomial y = ', end = '')
        for i, c in enumerate(data):
            if i != 0:
                print(' + ', end = '')
            if len(data)-i-1 != 0:
                print(str(c)+'x^'+str(len(data)-i-1), end = '')
            else:
                print(str(c), end = '')
        print(' are:')
            
        for i, x in enumerate(roots):
            print('x' + str(i) + ' = ' + str(x))
    
    if f == 'determinant':
        print(det_calc(data))
        
    if f == 'rref':
        pr_matrix(rref(data), mode, limit)
        
    if f == 'inverse':
        pr_matrix(inverse(data), mode, limit)
        
    if f == 'curve fitting':
        result = curve_fitting(data[0],data[1])
        if type(result[0]) == list:
            print('There are infinitely many best-fit lines!')
            print('Here is the RREF of the augmented matrix. The original y\
vector was input as the rightmost column.')
            pr_matrix(result)
        
        else:
            output = 'y = '
            if mode == 'frac':
                if limit == None:
                    limit = 1000
                for i in range(len(result)):
                    result[i] = Fraction(result[i]).limit_denominator(limit)
                    result[i] = str(result[i])
                for i in range(len(result)):
                    if i != len(result)-1:
                        output += (result[i]) + 'x^' + str(data[1]-i)\
                                  + ' + '
                    else:
                        output = output[:-5] + ' + ' + result[i]
                        
            if mode == 'dec':
                if limit == None:
                    dec = 4
                elif limit == 0:
                    dec = None
                else:
                    dec = limit
                for i in range(len(result)):
                    if i != len(result)-1:
                        output += str(round(result[i],dec)) + 'x^' + \
                                  str(data[1]-i) + ' + '
                    else:
                        output = output[:-5] + ' + ' + str(round(result[i],dec))
            print(output)




 
