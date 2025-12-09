# Type hints untuk fungsi

# bentuk standar fungsi yang udah kita pelajari

'''
def fungsi(parameter):
    hasil = parameter ** 2
    print(hasil)

fungsi(1)
fungsi("ucup")
fungsi(True)
'''

# penggunaan type hints

def sepuluh_pangkat(argument:int) -> int:
    '''FUNGSI DENGAN HINTS'''
    output = 10 ** argument
    return output

hasil = sepuluh_pangkat(2)
print(hasil)

import string

def display(argument:string):
    print(argument)

display("ucup")