#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:15:34 2018

@author: stoilova
"""

import pysam
import sys
#path = sys.stdin
import logging as L

L.basicConfig(filename = "MyLog.log", level = L.DEBUG)
pairs_count = 0
average_fragmentsize = 0
sum_intervals = 0

path = "/hts/data1/akennedy/SampleSetC_2164/bam/BEL033_1000.bam"
#outf = sys.stdout

bamfile = pysam.AlignmentFile(path, "rb")
#outf = open('BEL033_v2.bed', 'w')

iter = bamfile.fetch() #read through the whole file
initial_count = bamfile.count()
for aln in iter:
    if aln.is_paired and aln.is_read1:
        pairs_count += 1
        fragment_end = str(aln.reference_start + aln.template_length)
        sum_intervals += aln.template_length
        sys.stdout.write(aln.reference_name + '\t' + str(aln.reference_start) + '\t' + fragment_end + '\t' + aln.query_name + '\t.\t.\n')
        
        average_fragmentsize = sum_intervals / pairs_count
L.info("initial_count{}".format(initial_count))
L.info("pairs_count {}".format(pairs_count))
L.info("Average fragment size {:4.2f}".format(average_fragmentsize))
bamfile.close()
#outf.close()


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
   """