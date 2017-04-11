'''
Created on Apr 14, 2016

@author: Junwen
'''
import os
import string
import re
from _hashlib import new
from _overlapped import NULL
from _ast import Str
from itertools import combinations
from collections import defaultdict
from pip._vendor.distlib.compat import raw_input
#--------------------------------------------------------------------------------
# open a file of film_title into arraylist
#--------------------------------------------------------------------------------
n = 0
num = 4
titlenum = 0
txtnum = 0
fo = open('film_titles.txt', 'r', encoding='ascii', errors='ignore')
data = fo.read();
fo.close()
f = open('film_titles.txt', 'r', encoding='ascii', errors='ignore')
arraylist=[]
for data1 in iter(f):   
    arraylist.append(data1)
alltitle = len(arraylist)
f.close()  
#--------------------------------------------------------------------------------  
# Function list include [filemdiv]
#-------------------------------------------------------------------------------- 
#*****************************************************
#@divide the film title into  single string actuallu del the string /n
def filmtitle(fn):
    new = arraylist[fn]
    srg=''.join(new)
    srg = srg.strip('\n')  
    srg = srg.strip('!')
    srg = srg.strip('"')
    srg = srg.strip('(')
    srg = srg.strip(')')
    srg = srg.strip('[')
    srg = srg.strip(']')
    return srg   
#--------------------------------------------------------------------------------
#open a file for 50000 review files
# 1. this run for testing the existing files
# 2. show how many files can be read
# 3. open each files and read the file into "datareview"
#--------------------------------------------------------------------------------
def searchRv(txtnumber):
    try:
       
        name = str(txtnumber) + ".txt"
        if os.path.exists(name):
            #print(name+" FOUND  --------------DATA Have Installed")
            re = open(name, 'r', encoding='ascii', errors='ignore')
            datareview = re.read();
            re.close()
        else:
            datareview = "NULL"
            #print("review txt file  [" + name + "]  does not exist") 
    except:
        print("Can't get Data")       
    return datareview      
def allsearch(m): 
    n=0
    match=0
    f2=filmtitle(m)
    u=''
    while (n<50000):
        n+=1     
        f1 = searchRv(n)
        u =f1.lower()
        result = u.find(f2.lower())
        if (result >=0):
            match = match + 1
    
    
    
    if match==0:
        print('Film ['+ f2 +'] is not find in the review')
    
    else:       
        print('Film name ['+ f2 + '] in match numbers are = '+ str(match))
#================================================================================
#============================N- Grame Mathch================================
#================================================================================
def nGram(rn,tn):    
    nGreview=searchRv(rn)
    nGfilmtitle=filmtitle(tn)   
    nGf=''
    nGr=''
    lre=len(nGreview)
    lti=len(nGfilmtitle)  
    u=6    
    newGre=[]
    newtitle=[]
    match = 0
    ca = 0
    for i in range(0,lti-u+1):
        nGf=nGfilmtitle[i:i+u]
        newtitle.append(nGf)
    
    for k in range(0,lre-u+1):
        nGr = nGreview[k:k+u]
        newGre.append(nGr)       
    for n in range(0,len(newGre)):
        for m in range(0,len(newtitle)):
            if newGre[n]== newtitle[m]:
                match = match+1                      
    ca = abs(len(newGre)+ len(newtitle)) - abs(2 * match)
    #print('Searching for...................[ '+ nGfilmtitle+' ]') 
    return ca 
#=================================================================
def localEdit(b,txtnumber):
    n=0
    #ls1='lended'
    #ls2='deaden'
    locReview=searchRv(txtnumber)
    locFilmtitle=filmtitle(b) 
    lenthR=len(locReview)+1
    lenthF=len(locFilmtitle)+1
    
    localEd=[[0 for i in range(lenthR)] for j in range(lenthF)]      
    for n in range(lenthF):localEd[n][0] =0
    for m in range(lenthR):localEd[0][m] =0      
    
    for j in range(1,lenthR):
        for i in range(1,lenthF):
            
            if locReview[j-1] == locFilmtitle[i-1]:
                localEd[i][j] = localEd[i-1][j-1]+ 1
            else:
                localEd[i][j] = max(localEd[i-1][j]-1,localEd[i][j-1]-1,localEd[i-1][j-1]-1)
                if localEd[i][j]<0:                                                
                    localEd[i][j]=0
    
    maxx = 0
    for j in range(0,lenthR):
        for i in range(0,lenthF):
            if localEd[i][j] > maxx:
                maxx= localEd[i][j]
    print('Searching for.................[ '+ locFilmtitle+' ]')
    return maxx                         
#================================
#=====FUNCTION RUN AREA==========
#================================
def runNgram(tn,rev):
    print('**********************************************')
    print('*****Thanks for using N-Gram Distance *********')
    print('**********************************************')
    print('  PS:    It will take a while....                                      ')
    mini2=1000000
    filmname = ''
    print('Please Waitting for Reslut...')
    for i in range(rev,rev+1):       
        for j in range(0,tn):
            if searchRv(i)!='NULL':                
                nGram(i, j)
                mini1 = nGram(i, j)
                if mini2 >= mini1:
                    mini2 = mini1
                    filmname = filmtitle(j)           

    print('**********************************************')
    print('*************     Result     *****************')
    print('**********************************************')
    print(" The minimum  is : " + str(mini2) + '    The possible film for this review is [' + filmname +']')

def runLoc(txtber):
    print('**********************************************')
    print('*****Thanks for using Local Distance *********')
    print('**********************************************')
    print('  PS:    This will take a long time....depend on how long the review is                                        ')
    print('Please Waitting for Reslut...')
    maxx2=0
    filmname = ''
    for i in range(0,alltitle):
        localEdit(i, txtber)
        maxx1 = localEdit(i, txtber)
        #maxx1 = maxx1/len(filmtitle(i))
        if maxx1 > maxx2:
            maxx2 = maxx1
            filmname = filmtitle(i)
    print('**********************************************')
    print('*************     Result     *****************')
    print('**********************************************')
    print(" The minimum  is : " + str(maxx2) + '    The possible film for this review is [' + filmname +']') 



#runNgram(alltitle,80)
#runLoc(80)
#================================
#=============RUN ===============
#================================
    
print('Welcome to Test review for films')
print('**********************************************')
print('************Review Tester*********************')
print('*****************************By Junwen xie****')
print('                                              ')
print('                                              ')
print('   -n for N-gram (start,end)                                           ')
print('  -lo for Local Edit Distance                               ')
print('                                              ')
print('                                              ')
print('                                              ')
udp =input('Please enter which methods you like using: ') 

while udp =='-n':
    strn = int(raw_input('please enter which review you want to search >>>start(1-50000) :'))
    #op = int(raw_input('please enter which review you want to search   >>>end  (1-50000) :'))
    print('*******************Please enter a number !!!!!!!!!!!!*************')    
    if 0<strn<50001:       
        runNgram(alltitle,strn)
    else:
        print('Sorry you enter a wrong number')
        strn = ('please enter again')
    
   
while udp =='-lo':
    strn = int(raw_input('please enter which review you want to search (1-50000) :'))
    print('*******************Please enter a number !!!!!!!!!!!!*************')    
    if 0<strn<50001:       
        runLoc(strn)
    else:
        print('Sorry you enter a wrong number')
        strn = ('please enter again')    
    
    
while udp !='-lo' and udp !='-n':
    udp =input('Please enter which methods you like using: ')
    
    
    
    
    
    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
