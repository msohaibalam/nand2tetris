// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

// Put your code here.

@k      // k = 0
M=0
@c      // c = 0
M=0
(LOOP)
    @c      // if (c-R1)=0 goto END
    D=M
    @1
    D=D-M
    @END
    D;JEQ
    @0      // k += R0
    D=M
    @k
    M=M+D
    @c
    M=M+1   // c++
    @LOOP   // goto LOOP
    0;JMP
(END)
    @k      // Set R2 = k
    D=M
    @2
    M=D