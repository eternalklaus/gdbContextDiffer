.global main

main:
    nop
    nop
here:
    lea WRITABLE_1, %ebx 
    xor $0x22, 0x1(%ebx)
    ret



.section .data
.align 64
WRITABLE_1:
    .byte 0x00
WRITABLE:
    .byte 0x44, 0x33, 0x22, 0x11
