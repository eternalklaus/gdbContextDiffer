.global main

main:
# 1-operand instruction
  call get_pc_thunk.si
  lea mydata, %esi 
  mov $0x20202020, %edx
  mov $0xf9f9f9f9, %eax
here: 
 call  0x0804100
 decb   0x0804100
 divb   0x0804100
 idivb  0x0804100
 imulb  0x0804100
 incb   0x0804100
 jmp   0x0804100
 mulb   0x0804100
 negb   0x0804100
 notb   0x0804100
 pop   0x0804100
 push  0x0804100
 salb   0x0804100
 sarb   0x0804100
 shlb   0x0804100
 shrb   0x0804100















get_pc_thunk.si:
 mov (%esp), %esi
 ret 

.data
mydata:
 .byte 0xff, 0xff, 0xff, 0xff
