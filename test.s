.global main

get_pc_thunk.si:
   mov (%esp), %esi
   ret


main:
   mov $0x71231284, %eax
   mov $0xfff01239, %esi
   mov $0x0, %edx 
here:
   imul    %esi


.section .data
MYDATA:
  .byte 0x11, 0x11, 0x11, 0x11
