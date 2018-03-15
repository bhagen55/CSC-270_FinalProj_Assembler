# Assembler for csc-270 final project. Based on John Rieffel's skeleton code
# Modified by Blair Hagen

import sys

from helperfunctions import *

# Constants
regBits = 4
jBits = 12

logHeader = "v2.0 raw"

opcodeDict = {'add':    '0000',
              'addi':   '0001',
              'sub':    '0010',
              'subi':   '0011',
              'and':    '0100',
              'andi':   '0101',
              'or':     '0110',
              'ori':    '0111',
              'sw':     '1000',
              'lw':     '1001',
              'beq':    '1010',
              'j':      '1011',
              'slt':    '1100',
              'sgt':    '1101',
			  'slti':	'1110',
			  'sgti':	'1111'}

iOps = ['addi', 'subi', 'andi', 'ori', 'beq', 'slti', 'sgti']

memOps = ['sw', 'lw']

jOps = ['j']


def GetOffset(partialins):
    splitIns = partialins.split('(')
    return splitIns[0]


def GetMemAddr(partialins):
    splitIns = partialins.split('(')
    return splitIns[1].strip(')')[1:]


def ConvertAssemblyToMachineCode(inline):
    '''given a string corresponding to a line of assembly,
    strip out all the comments, parse it, and convert it into
    a string of binary values'''

    outstring = ''

    if inline.find('#') != -1:
        inline = inline[0:inline.find('#')]  # get rid of anything after a comment
    if inline != '':
        words = inline.split()  # assuming syntax words are separated by space, not comma
        operation = words[0]
        operands = words[1:]
        outstring += opcodeDict[operation]

        # i type instructions:
        if operation in iOps:
            outstring += int2bs(operands[0][1:], regBits)
            outstring += int2bs(operands[1][1:], regBits)
            outstring += int2bs(operands[2][0:], regBits)

        # load/save instructions
        elif operation in memOps:
            outstring += int2bs(operands[0][1:], regBits)
            outstring += int2bs(GetMemAddr(operands[1]), regBits)
            outstring += int2bs(GetOffset(operands[1]), regBits)

        # jump instructions
        elif operation in jOps:
            outstring += int2bs(operands[0], jBits)

        # r type instructions:
        else:
            for oprand in operands:
                if oprand[0] == '$':
                    outstring += int2bs(oprand[1:], regBits)
    return outstring


def AssemblyToHex(infilename, outfilename):
    '''given an ascii assembly file , read it in line by line and convert each line of assembly to machine code
    then save that machinecode to an outputfile'''
    outlines = []
    with open(infilename) as f:
        lines = [line.rstrip() for line in f.readlines()]  # get rid of \n whitespace at end of line
        # if you are a python ninja, use list comprehension. and replace the for loop below
        # with this expression
        # outlines = [ConvertAssemblyToMachineCode(curline) for curline in lines]
        # but, no judgement if you prefer explicit for loops
        for curline in lines:
            outstring = ConvertAssemblyToMachineCode(curline)
            if outstring != '':
                outlines.append(bs2hex(outstring))

    f.close()

    with open(outfilename, 'w') as of:
        # Write in logisim header file
        of.write(logHeader + "\n")
        for outline in outlines:
            of.write(outline + "\n")
    of.close()


if __name__ == "__main__":
    # in order to run this with command-line arguments
    # we need this if __name__ clause
    # and then we need to read in the subsequent arguments in a list.

    #### These two lines show you how to iterate through arguments ###
    #### You can remove them when writing your own assembler
    # print 'Number of arguments:', len(sys.argv), 'arguments.'
    # print 'Argument List:', str(sys.argv)

    ## This is error checking to make sure the correct number of arguments were used
    ## you'll have to change this if your assembler takes more or fewer args
    if (len(sys.argv) != 3):
        print('usage: python assembler.py inputfile.asm outputfile.hex')
        exit(0)
    inputfile = sys.argv[1]
    outputfile = sys.argv[2]
    AssemblyToHex(inputfile, outputfile)
