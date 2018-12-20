.global main

main:
    nop
    nop
here: # set this symbol. because in nexti mode, some flags canbe different with normal r status.
    mov $0x1, %ebx
    bsf MYSYM, %ebx
    nop
    nop
    nop
    nop
    nop
    nop
MYSYM:
    .byte 0xff, 0xff, 0x00, 0x00
