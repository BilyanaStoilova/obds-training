#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 11:15:34 2018

@author: stoilova
"""

import pysam
import sys
#path = sys.stdin
outf = sys.stdout

#path="/hts/data1/akennedy/SampleSetC_2164/bam/BEL033_1000.sam"
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
SumIntervals = 0

samfile = pysam.AlignmentFile("-", "r")
iter = samfile.fetch(“chr1", 1000, 2000)


for line in path:
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
                    outf.write(Chr+'\t'+str(Start)+'\t'+str(End)+'\t'+ID+'\t'+Score+'\t'+Strand+'\n')
                    SumIntervals +=int(name[8])
                    
logf = open('SAM_to_BED2.log', 'w')
logf.write('The initial number of reads is\t'+str(ReadCount)+'\n')
logf.write('The raw number of paired reads is\t'+str(RawPairedReads)+'\n')
logf.write('The pairs count is\t'+str(PairsCount)+'\n')
logf.write('The pairs count <250 is\t'+str(PairsCountmax250)+'\n')
AvSize = SumIntervals/PairsCountmax250
logf.write('The average length is\t'+str(AvSize)+'\n')
logf.close()
   
