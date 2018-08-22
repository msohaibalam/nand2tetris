// boostrap
@256
D=A
@SP
M=D
@return-address-sysinit
D=A
@SP
A=M
M=D
@SP
M=M+1
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
@SP
D=M
@5
D=D-A
@ARG
M=D
@SP
D=M
@LCL
M=D
@Sys.init
0;JMP
(return-address-sysinit)
// function Main.fibonacci 0
(Main.fibonacci)
@0
D=A
@13
M=D
(LOOP_Main.fibonacci)
@13
D=M
@END_Main.fibonacci
D;JEQ
@SP
A=M
M=0
@SP
M=M+1
@13
M=M-1
@LOOP_Main.fibonacci
0;JMP
(END_Main.fibonacci)
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
// push constant 2
@2
D=A
@SP
A=M
M=D
@SP
M=M+1
// lt
@SP
A=M-1
D=M
A=A-1
D=M-D
@IF_TRUE_3
D;JLT
@SP
A=M-1
A=A-1
M=0
@END_3
0;JMP
(IF_TRUE_3)
@SP
A=M-1
A=A-1
M=-1
(END_3)
@SP
M=M-1
// if-goto
@SP
A=M-1
D=M
@SP
M=M-1
@Main.fibonacci$IF_TRUE
D;JNE
// goto
@Main.fibonacci$IF_FALSE
0;JMP
// label
(Main.fibonacci$IF_TRUE)
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
// return
@LCL
D=M
@13
M=D
@13
D=M
@5
D=D-A
A=D
D=M
@14
M=D
@SP
A=M-1
D=M
@ARG
A=M
M=D
@SP
M=M-1
@ARG
D=M+1
@SP
M=D
@13
A=M-1
D=M
@THAT
M=D
@13
D=M
@2
A=D-A
D=M
@THIS
M=D
@13
D=M
@3
A=D-A
D=M
@ARG
M=D
@13
D=M
@4
A=D-A
D=M
@LCL
M=D
@14
A=M
0;JMP
// label
(Main.fibonacci$IF_FALSE)
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
// push constant 2
@2
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
// call Main.fibonacci 1
// call : push return-address
@RETURN_ADDRESS_13
D=A
@SP
A=M
M=D
@SP
M=M+1
// call : push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// call : push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// call : push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// call : push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// call : ARG = SP - n - 5
@SP
D=M
@1
D=D-A
@5
D=D-A
@ARG
M=D
// call : LCL = SP
@SP
D=M
@LCL
M=D
// call : goto f
@Main.fibonacci
0;JMP
// call : declare label for return-address
(RETURN_ADDRESS_13)
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
// call Main.fibonacci 1
// call : push return-address
@RETURN_ADDRESS_17
D=A
@SP
A=M
M=D
@SP
M=M+1
// call : push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// call : push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// call : push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// call : push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// call : ARG = SP - n - 5
@SP
D=M
@1
D=D-A
@5
D=D-A
@ARG
M=D
// call : LCL = SP
@SP
D=M
@LCL
M=D
// call : goto f
@Main.fibonacci
0;JMP
// call : declare label for return-address
(RETURN_ADDRESS_17)
// add
@SP
A=M-1
D=M
A=A-1
D=D+M
M=D
@SP
M=M-1
// return
@LCL
D=M
@13
M=D
@13
D=M
@5
D=D-A
A=D
D=M
@14
M=D
@SP
A=M-1
D=M
@ARG
A=M
M=D
@SP
M=M-1
@ARG
D=M+1
@SP
M=D
@13
A=M-1
D=M
@THAT
M=D
@13
D=M
@2
A=D-A
D=M
@THIS
M=D
@13
D=M
@3
A=D-A
D=M
@ARG
M=D
@13
D=M
@4
A=D-A
D=M
@LCL
M=D
@14
A=M
0;JMP
// function Sys.init 0
(Sys.init)
@0
D=A
@13
M=D
(LOOP_Sys.init)
@13
D=M
@END_Sys.init
D;JEQ
@SP
A=M
M=0
@SP
M=M+1
@13
M=M-1
@LOOP_Sys.init
0;JMP
(END_Sys.init)
// push constant 4
@4
D=A
@SP
A=M
M=D
@SP
M=M+1
// call Main.fibonacci 1
// call : push return-address
@RETURN_ADDRESS_22
D=A
@SP
A=M
M=D
@SP
M=M+1
// call : push LCL
@LCL
D=M
@SP
A=M
M=D
@SP
M=M+1
// call : push ARG
@ARG
D=M
@SP
A=M
M=D
@SP
M=M+1
// call : push THIS
@THIS
D=M
@SP
A=M
M=D
@SP
M=M+1
// call : push THAT
@THAT
D=M
@SP
A=M
M=D
@SP
M=M+1
// call : ARG = SP - n - 5
@SP
D=M
@1
D=D-A
@5
D=D-A
@ARG
M=D
// call : LCL = SP
@SP
D=M
@LCL
M=D
// call : goto f
@Main.fibonacci
0;JMP
// call : declare label for return-address
(RETURN_ADDRESS_22)
// label
(Sys.init$WHILE)
// goto
@Sys.init$WHILE
0;JMP
