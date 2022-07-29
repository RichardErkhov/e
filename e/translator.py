import e
import ast
"""
#e is print
eee = print
#e is one
e = 1
#eee is two
ee = 2
#eeee is string function
eeee = str
#eeeee is int function
eeeee = int
#eeeeee is float function
eeeeee = float
#=======================
#chr is number to letter
#ord is letter to number
#eeeeeee is chr function
eeeeeee = chr
#eeeeeeee is ord function
eeeeeeee = ord
#========================
#e equal ee
def eEEe(e,ee): return e == ee
#e is bigger than ee
def eEe(e,ee): return e > ee
#multiply e by ee
def EeE(e,ee): return e*ee
#divide e by ee
def eEE(e,ee): return e/ee
#add e and ee
def eE(e,ee): return e+ee
#subtract e from ee
def Eee(e,ee): return e-ee
#len
def eeeE(e): return len(e)
"""
def py_to_e(text):
    new_text = text.replace("print", "e").replace("1", "ee").replace("2", "eee").replace("str", "eeee").replace("int", "eeeee").replace("float", "eeeeee").replace("chr", "eeeeeee").replace("ord", "eeeeeeee").replace("==", "eEEe").replace(">", "eEe").replace("*", "EeE").replace("/", "eEE").replace("+", "eE").replace("-", "Eee")
    return new_text
def translate_string_to_int(text):
    xf = []
    for i in text:
        xf.append(ord(i))
    return xf

def translate_int_to_e(listik):
    #change numbers to e lang numbers
    # where ee = 1 and eee = 2
    new_list = []
    for i in listik:
        temp_str = ""
        j = int(i)
        while j > 0:
            #print(j)
            #if j == 1:
                #new_list.append("ee")
            #    break
            #elif j == 2:
                #new_list.append("eee")
            #    break
            #else:
            if j - 2 >= 0:
                #print("eee")
                temp_str = temp_str + "ee"
                j -= 2
            elif j - 1 >= 0:
                temp_str += "e"
                j -= 1

        new_list.append(temp_str)

    return new_list

def text_to_e(text):
    return translate_int_to_e(translate_string_to_int(text))

def printer(listik, ifd = False):
    if isinstance(listik, str):
        listik = ast.literal_eval(listik)
    aaa = ""
    for i in listik:
        if ifd==False:
            e.eee(e.eeeeeee(e.eeeE(i)),end="")
        else:
            aaa += e.eeeeeee(e.eeeE(i))
    if ifd==True:
        return aaa

def full(stringer):
    printer(translate_int_to_e(translate_string_to_int(stringer)))

def text_to_e_fromfile(filename):
    return translate_int_to_e(translate_string_to_int(open(filename).read()))

def test():
    with open("test.txt", mode='w') as filek:
        filek.write(translate_int_to_e(translate_string_to_int(open(filename).read())))