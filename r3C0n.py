#!/usr/bin/env python

import socket
import sys
import getopt

def main(argv):
	file_in = ''
	file_out = ''

	# GET COMMANDLINE ARGUMENTS
   try:
      opts, args = getopt.getopt(argv,"hi:o:")
   except getopt.GetoptError:
      print ('r3C0n.py -i [inputfile] -o [output file]')
      sys.exit(1)
   for opt, arg in opts:
      if opt == '-h':
         print ('r3C0n.py -i [inputfile] -o [output file]')
         sys.exit()
      elif opt in ("-i"):
         in_file = arg
      elif opt in ("-o"):
         out_file = arg

   # OPEN FILE READ LINE BY LINE GET IP ADDRESS
   log = open(out_file, 'w')

   with open(in_file, "r") as hosts:
      for line in hosts:
         log.write("IP Address: " + socket.gethostbyname(line.strip()) + " Host: " + line)

   log.close()

if __name__ == "__main__":
   main(sys.argv[1:])