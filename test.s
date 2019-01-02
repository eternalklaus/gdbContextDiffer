.global main

get_pc_thunk.si:
   mov (%esp), %esi
   ret


main:
   mov $0x777, %edx 
   mov $0x777, %eax
   mov $0x3, %esi
here:
   not    %esi
   pop    %esi
   push   %esi
   sal    %esi
   sar    %esi
   shl    %esi
   shr    %esi


.section .data
MYDATA:
  .byte 0x11, 0x11, 0x11, 0x11
