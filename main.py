import argparse
import wave

# We are going to start with taking two files. 
# An Audio.wav file and an IR file. 

parser = argparse.ArgumentParser()
sampleWavFile = ''
impulseResponseFile = ''
outputFile  = ''

parser.add_argument('-s', '--audioFile', help='Audio Sample Input File', required=True)
parser.add_argument('-i', '--irFile', help='Impulse Response File', required=True)
parser.add_argument('-o', '--oFile', help='Output File', required=True)


print(parser.parse_args())


