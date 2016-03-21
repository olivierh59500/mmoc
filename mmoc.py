#!/usr/bin/env python
# -*- coding: utf-8 -*-
# example: ./mmoc.py -f1 fil1.exe -f2 file2.exe -cs 32
import argparse
import binascii

# ARGUMENTS PARSING
parser = argparse.ArgumentParser(description="-= mmoc - find similarities in binary files  =-")
parser.add_argument('-f1','--filename', help='File 1', required=True)
parser.add_argument('-f2','--filename2', help='File 2', required=True)
parser.add_argument('-cs','--chunksize', help='Chunk size', default=32)

args = parser.parse_args()
myfile1=open(str(args.filename),'r')
myfile2=open(str(args.filename2),'r')
chunksize=int(args.chunksize)


# read the two files
text1_bin = myfile1.read()
text2_bin = myfile2.read()

# convert bin to hex
text1_hex=binascii.hexlify(text1_bin)
text2_hex=binascii.hexlify(text2_bin)


# chunkstring function, take the whole hex string (the file) and separate that in chunks
def chunkstring(string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))

# decide which file is smaller, to take that and test its strings against the bigger file
if len(text2_hex)>len(text1_hex):
    filetoparse=text1_hex
    filetocheckagainst=text2_hex
elif len(text2_hex)<len(text1_hex):
    filetoparse=text2_hex
    filetocheckagainst=text1_hex
elif len(text2_hex)==len(text1_hex):
    filetoparse=text1_hex
    filetocheckagainst=text2_hex

# actiually split lines in chunks
lines = (i.strip() for i in filetoparse.splitlines())

for line in lines:
    for chunk in chunkstring(line, chunksize):
        #avoiding code caves
        if chunk != '0'*chunksize:
            # if chunk matches, then print it in ascii plus hex version
            if chunk in filetocheckagainst:
                print chunk.decode("hex"),chunk
