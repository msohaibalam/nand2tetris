// push constant 0
@0
D=A
@SP
A=M
M=D
@SP
M=M+1
// pop local 0
@0
D=A
@LCL
D=D+M
@13
M=D
@SP
A=M-1
D=M
@13
A=M
M=D
@SP
M=M-1
// label
(LOOP_START)
// push argument 0
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// push local 0
@0
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// add
@SP
A=M-1
D=M
A=A-1
D=D+M
M=D
@SP
M=M-1
// pop local 0	
@0	
D=A
@LCL
D=D+M
@13
M=D
@SP
A=M-1
D=M
@13
A=M
M=D
@SP
M=M-1
// push argument 0
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// push constant 1
@1
D=A
@SP
A=M
M=D
@SP
M=M+1
// sub
@SP
A=M-1
D=M
A=A-1
D=M-D
M=D
@SP
M=M-1
// pop argument 0
@0
D=A
@ARG
D=D+M
@13
M=D
@SP
A=M-1
D=M
@13
A=M
M=D
@SP
M=M-1
// push argument 0
@0
D=A
@ARG
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
// if-goto
@SP
A=M-1
D=M
@SP
M=M-1
@LOOP_START
D;JNE
// push local 0
@0
D=A
@LCL
A=D+M
D=M
@SP
A=M
M=D
@SP
M=M+1
