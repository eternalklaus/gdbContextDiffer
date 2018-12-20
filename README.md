## gdbContextDiffer
Compare register context before/after executing the instruction.  
<br>

## Prepare  
Set symbol *"here"* 1 step before the inspecting instruction.  
For example, in case of *bsf*, set symbol like below.   
  
    here:
       nop
       bsf MYSYM, %ebx
  
*(Why 1 step before? Because some registers are dependent on being debugged or not.)*    
<br>

## Run gdbdiff
    $ sudo apt-get install meld # graphical diff tools
    $ git clone https://github.com/eternalklaus/gdbContextDiffer.git
    $ python gdbdiff.py test.s
<br>
Enjoy gdbContextDiffer!  



