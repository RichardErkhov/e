import e.translator
#e is print
eee = print
#ee is one
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
#len
def eeeE(e): return len(e)
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
#printer function
def EeeE(e, ifd=False): return translator.printer(e, ifd=ifd)
#executer of any code
def EeeEEeeEEeeeeEEEeeeEee(e): exec(EeeE(eeee(e), ifd=True))
#global a variable, name and then value
eeeeeeeeeeeeeeeeeee = []
def EEEEe(e): global eeeeeeeeeeeeeeeeeee; eeeeeeeeeeeeeeeeeee.append(e)
def eeeeeeeeeeeeeeeeeeeE(): return eeeeeeeeeeeeeeeeeee
def eeeeeeeeeeeeeeeeeeeEE(): eee(eeeeeeeeeeeeeeeeeeeE())
def eeeeeeeeeeE(path='code.txt'):
    with open(path, mode='r') as code:
        code = code.read()
        exec(code)