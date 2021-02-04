#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wednesday Jan 27 16:45:26 2021

@author: Hangyu Chen
"""
# Name: Hangyu Chen
# Student ID: 873552564

# This script count characters in text files and output the results in csv format.

import sys,getopt

islowup=False
filelist=[]
isall=False
outarray=[]
showall=False

listdlow = {
    'a':0,'b':0, 'c':0,'d':0, 'e':0,'f':0, 'g':0,'h':0, 'i':0,'j':0, 'k':0,'l':0, 'm':0,'n':0, 'o':0,'p':0, 'q':0,'r':0, 's':0,'t':0, 'u':0,'v':0, 'w':0,'x':0, 'y':0,'z':0
}

listdup={
     'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'G':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0
}

listdall={
 'a':0,'b':0, 'c':0,'d':0, 'e':0,'f':0, 'g':0,'h':0, 'i':0,'j':0, 'k':0,'l':0, 'm':0,'n':0, 'o':0,'p':0, 'q':0,'r':0, 's':0,'t':0, 'u':0,'v':0, 'w':0,'x':0, 'y':0,'z':0,
 'A':0,'B':0,'C':0,'D':0,'E':0,'F':0,'G':0,'H':0,'I':0,'G':0,'K':0,'L':0,'M':0,'N':0,'O':0,'P':0,'Q':0,'R':0,'S':0,'T':0,'U':0,'V':0,'W':0,'X':0,'Y':0,'Z':0
}


def add_frequencies(): # read file and handle the frequencies of letters
    global islowup
    global filelist
    global isall
    global outarray
    global showall
    global listdall
    global listdlow
    global listdup

    textall=''
   
    for i in filelist: # file reading
        f = open(i)
        textall+=f.read()
        f.close()
    text=textall

    if islowup: # to test lower/upper case
        for i in text:
            if i in listdall:
                listdall[i] += 1
        if len(outarray)==0:
            for i in listdall:
                if showall:
                    print('The letter "' +i+'" appeared ' + str(listdall[i]) +" times.")
                else:
                    if listdall[i] !=0:
                         print('The letter "' +i+'" appeared ' + str(listdall[i]) +" times.")
        else:
            for i in listdall:
                if i in outarray:
                    print('The letter "' +i+'" appeared ' + str(listdall[i]) +" times.")
                    
    else :
        for i in text:
            if i.lower() in listdlow:
                listdlow[i.lower()]+=1
        if len(outarray)==0:
            for i in listdlow:
                if showall:
                    print('The letter "' +i+'" appeared ' + str(listdlow[i]) +" times.")
                else:
                    if listdlow[i] !=0:
                         print('The letter "' +i+'" appeared ' + str(listdlow[i]) +" times.")
        else:
            for i in listdlow:
                if i in outarray:
                    print('The letter "' +i+'" appeared ' + str(listdlow[i]) +" times.")


def main(argv):
    global islowup
    global filelist
    global isall
    global outarray
    global showall
    global listdall
    global listdlow
    global listdup

    try:
        opts, args = getopt.getopt(argv,"cl:z",[])
    except:
        print ('count.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-c':
            islowup = True
        elif opt in ("-l"):
            outarray = arg
        elif opt in ("-z"):
            showall=True
    filelist = args
    add_frequencies()
   
if __name__ == "__main__":
    main(sys.argv[1:])
