#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 17:21:09 2018
@author: krishna
"""
import glob2
import re

# Creating a list of path for each python file
jsFilesPath = glob2.glob('/home/krishna/Desktop/fall 2018-19/Research/incubator-echarts-master/**/*.js')

# Reading the libraries from each of the javascript files
firstTierList = []
for file in jsFilesPath:
    with open(file) as fs:
        for line in fs:
            if len(line) >= 2:
                match = line.split(' ')[0]
                if match == "import":
                    libMatch = re.search(r'(?<=\')(.*?)(?=\')', line)
                    if libMatch is not None:
                        libMatch = libMatch.group(1)
                        cnt = 0
                    for item in firstTierList:
                        if item == libMatch:
                            cnt = 1
                    if cnt == 0:
                        firstTierList.append(libMatch)
with open("firstTierLibraries.txt", "w") as f:
    for item in firstTierList:
        f.write("%s\n" % item)

##Extract only pakages from the list and exclude classes
# checkChar='.'
# finalList=[]
# for item in firstTierList:
#    flag=0
#    for charecter in item:
#        if charecter==checkChar:
#            flag=1
#            break
#    if flag==0:
#        finalList.append(item)
#    else:
#        wordSplit=item.split('.')[0]
#        finalList.append(wordSplit)
# finalList=list(set(finalList))
