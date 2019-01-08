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
import re

def remove_dollor(filename):
	f = open(filename,'r')
	content = f.read()
	replaced = re.sub('\$' + '[0-9a-f]+', '', content)
	f.close()

	# Why? why python cannot read&write one file in the same time?
	f = open(filename,'w')
	f.write(replaced)
	f.close()
	



if __name__=='__main__':
	if len(sys.argv) is not 2:
		print '[*] usage : python gdbdiff.py [disassembly file]'
		print '        ex) python gdbdiff.py test.s'
		sys.exit(1)

    

	# Sanity check
	f = open(sys.argv[1],'r')
	data = f.read()
	if 'here:' not in data:
		 print '[!] Oops! '
		 print '[!] You should set \'here\' named symbol before running gdbinit!'
		 sys.exit(1)
	f.close()


	# gdbdiff hangs after gdb.attach()... ITK how to resume it... Got out of the incident by using fork() method.
	pid = os.fork()
	os.system('gcc -o bin ' + sys.argv[1])

	if pid == 0: # child
		filename = 'bin'
		myprocess = process(filename)
		gdb.attach(myprocess, '''
		b here
		r
		
		echo context before instruction\n
		set logging file 1
		set logging overwrite
		set logging on
		i r
		echo eax 
		p/t $eax
		echo ecx 
		p/t $ecx
		echo edx 
		p/t $edx
		echo ebx 
		p/t $ebx
		echo esp 
		p/t $esp
		echo ebp 
		p/t $ebp
		echo esi 
		p/t $esi
		echo edi 
		p/t $edi
		echo eip 
		p/t $eip
		set logging off
		
		nexti
		echo context after instruction\n
		set logging file 2
		set logging overwrite
		set logging on
		i r
		echo eax 
		p/t $eax
		echo ecx 
		p/t $ecx
		echo edx 
		p/t $edx
		echo ebx 
		p/t $ebx
		echo esp 
		p/t $esp
		echo ebp 
		p/t $ebp
		echo esi 
		p/t $esi
		echo edi 
		p/t $edi
		echo eip 
		p/t $eip
		set logging off
		
		quit
		''')
	
	else: # parant
		# wait suitable time, and diff.
		sleep(1.5)

		remove_dollor('1')
		remove_dollor('2')


		os.system('meld 1 2')
		os.system('rm bin 1 2')
