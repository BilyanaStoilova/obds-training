#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:15:34 2018

@author: stoilova
"""

path="/hts/data1/akennedy/SampleSetC_2164/bam/BEL033_1000.sam"
Chr=''
Start=0
End=0
list=[]
ID=''
Score=''
Strand='+'
ReadCount=0
PairsCount=0
RawPairedReads=0
PairsCountmax250=0
FileReadCount = 0

outf = open('BEL033.bed', 'w')
with open(path, 'r') as f:
     for line in f:
        if line.startswith('@'):
            pass
        else:
            name = line.split('\t')
            ReadCount+=1
            if name[6]=='=':
                RawPairedReads+=1
                if int(name[8])>0:
                    PairsCount+=1
                    if int(name[8])<250:
                        PairsCountmax250+=1
                        Chr=name[2]
                        Start=int(name[3])
                        End=Start+int(name[8]) 
                        ID=name[0]
                        Score=name[4]
                        list.append(Chr+'\t'+str(Start)+'\t'+str(End)+'\t'+ID+'\t'+Score+'\t'+Strand+'\n')
   
print('The initial number of reads is:', ReadCount)
print('The raw number of paired reads is:', RawPairedReads)
print('The pairs count is:', PairsCount)
print('The pairs count <250 is:', PairsCountmax250)

with open('BEL033.bed', 'r+') as f:
   for x in list:  
      f.write(x+'\n')
      FileReadCount +=1

print('The number of lines in the bed file is:', FileReadCount)
if RawPairedReads/2 == FileReadCount:
   print("We did it!")
else:
   print("Try again!")