 	#!/usr/bin/python
# -*- coding: utf-8 -*-
import pwnlib
from pwnlib import *
from pwnlib.gdb import attach, debug, debug_assembly, debug_shellcode
from pwnlib.tubes.process import process, PTY, PIPE, STDOUT
import subprocess
import os
import sys
from time import sleep


if __name__=='__main__':
	if len(sys.argv) is not 2:
		print '[*] usage : python gdbdiff.py [executable]'
		sys.exit(1)

	pid = os.fork()
	
	if pid == 0: # child
		filename = sys.argv[1]
		myprocess = process(filename)
		gdb.attach(myprocess, '''
		b here
		r
		nexti
		
		echo context before instruction\n
		set logging file 1
		set logging overwrite
		set logging on
		i r
		set logging off
		
		nexti
		echo context after instruction\n
		set logging file 2
		set logging overwrite
		set logging on
		i r
		set logging off
		
		quit
		''')
	
	else: # parant
		sleep(1.5)
		os.system('meld 1 2')
		os.system('rm 1 2')