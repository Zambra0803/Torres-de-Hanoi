from hanoi1 import *

def mover_torre(a,b):

    if a== 1 and b== 2:
        mover1_2()
    elif a== 1 and b== 3 :
            mover1_3()
    elif a== 2 and b== 3 :
            mover2_3()
    elif a== 2 and b== 1 :
            mover2_1()
    elif a== 3 and b== 1 :
            mover3_1()
    elif a== 3 and b== 2 :
            mover3_2()