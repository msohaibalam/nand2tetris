from parser import Parser


class CodeWriter:

    def __init__(self, path):
        self.parser = Parser(path)
        # just perform the logic of the recommended setFileName constructor here
        ind1 = path.find('/')
        ind2 = path.find('.')
        self.writefile = path[:ind1] + "/" + path[ind1+1:ind2]
        self.filename = self.writefile + '.asm'
        self.file = open(self.filename, 'w')
        self.writefile_ind = self.writefile.rfind('/')
        self.static_var = self.writefile[self.writefile_ind + 1:]   # useful in declaring static variables

    def writePushPop(self):   # no need to pass in command as an argument
        assert self.parser.commandType() in ['C_PUSH', 'C_POP']
        arg1 = self.parser.arg1()
        arg2 = self.parser.arg2()
        if self.parser.commandType() == 'C_PUSH':
                # stack operation
                if arg1 == 'constant':
                    # e.g. push constant 7
                    self.file.write('@%s\n' % arg2)
                    self.file.write('D=A\n')    # D = 7
                    self.file.write('@SP\n')
                    self.file.write('A=M\n')
                    self.file.write('M=D\n')    # M[M[base_address]] = 7
                elif arg1 in ['temp', 'pointer', 'local', 'argument', 'this', 'that']:
                    self.file.write('@%s\n' % arg2)
                    self.file.write('D=A\n')
                    if arg1 == 'temp':
                        self.file.write('@5\n')
                        self.file.write('A=D+A\n')
                    elif arg1 == 'pointer':
                        self.file.write('@3\n')
                        self.file.write('A=D+A\n')
                    elif arg1 == 'local':
                        self.file.write('@LCL\n')
                        self.file.write('A=D+M\n')
                    elif arg1 == 'argument':
                        self.file.write('@ARG\n')
                        self.file.write('A=D+M\n')
                    elif arg1 == 'this':
                        self.file.write('@THIS\n')
                        self.file.write('A=D+M\n')
                    elif arg1 == 'that':
                        self.file.write('@THAT\n')
                        self.file.write('A=D+M\n')
                    else:
                        pass
                    self.file.write('D=M\n')
                    self.file.write('@SP\n')
                    self.file.write('A=M\n')
                    self.file.write('M=D\n')
                elif arg1 == 'static':
                    # declare a new symbol file.j in "push static j"
                    self.file.write('@%s.%s\n' % (self.static_var, arg2))
                    self.file.write('D=M\n')
                    # push D's value to the stack
                    self.file.write('@SP\n')
                    self.file.write('A=M\n')
                    self.file.write('M=D\n')
                else:
                    # TODO
                    pass
                # increase address of stack top
                self.file.write('@SP\n')
                self.file.write('M=M+1\n')  # M[base_address] = M[base_address] + 1

        elif self.parser.commandType() == 'C_POP':
            # pop the stack value and store it in segment[index]
            # use general purpose RAM[13] to store the value of 'segment_base_address + index'
            self.file.write('@%s\n' % arg2)
            self.file.write('D=A\n')
            if arg1 in ['temp', 'pointer', 'local', 'argument', 'this', 'that']:
                if arg1 == 'local':
                    self.file.write('@LCL\n')
                    self.file.write('D=D+M\n')
                elif arg1 == 'argument':
                    self.file.write('@ARG\n')
                    self.file.write('D=D+M\n')
                elif arg1 == 'this':
                    self.file.write('@THIS\n')
                    self.file.write('D=D+M\n')
                elif arg1 == 'that':
                    self.file.write('@THAT\n')
                    self.file.write('D=D+M\n')
                elif arg1 == 'temp':
                    self.file.write('@5\n')
                    self.file.write('D=D+A\n')
                elif arg1 == 'pointer':
                    self.file.write('@3\n')
                    self.file.write('D=D+A\n')
                else:
                    # TODO
                    pass
                # self.file.write('D=D+M\n')
                self.file.write('@13\n')      # general purpose register
                self.file.write('M=D\n')
                self.file.write('@SP\n')
                self.file.write('A=M-1\n')
                self.file.write('D=M\n')        # pop command
                self.file.write('@13\n')
                self.file.write('A=M\n')
                self.file.write('M=D\n')        # write to appropriate address
                self.file.write('@SP\n')
                self.file.write('M=M-1\n')      # adjust address of stack top
            elif arg1 == 'static':
                self.file.write('@SP\n')
                self.file.write('A=M-1\n')
                self.file.write('D=M\n')    # pop command
                self.file.write('@%s.%s\n' % (self.static_var, arg2))
                self.file.write('M=D\n')    # write to appropriate address
                self.file.write('@SP\n')
                self.file.write('M=M-1\n')      # adjust address of stack top
        else:
            # TODO
            pass

    def writeArithmetic(self):   # no need to pass in command as an argument

        assert self.parser.commandType() == 'C_ARITHMETIC'
        command = self.parser.arg1()

        if command == 'add':
            # stack operation
            self.file.write('@SP\n')
            self.file.write('A=M-1\n')
            self.file.write('D=M\n')
            self.file.write('A=A-1\n')
            self.file.write('D=D+M\n')
            self.file.write('M=D\n')
            self.file.write('@SP\n')
            self.file.write('M=M-1\n')

        elif command == 'sub':
            # stack operation
            self.file.write('@SP\n')
            self.file.write('A=M-1\n')
            self.file.write('D=M\n')
            self.file.write('A=A-1\n')
            self.file.write('D=M-D\n')
            self.file.write('M=D\n')
            self.file.write('@SP\n')
            self.file.write('M=M-1\n')

        elif command == 'eq':
            # stack operation
            self.file.write('@SP\n')
            self.file.write('A=M-1\n')
            self.file.write('D=M\n')
            self.file.write('A=A-1\n')
            self.file.write('D=M-D\n')
            self.file.write('@IF_TRUE_%s\n' % self.parser.i)  # there could be more than one 'eq' command
            self.file.write('D;JEQ\n')
            self.file.write('@SP\n')
            self.file.write('A=M-1\n')
            self.file.write('A=A-1\n')
            self.file.write('M=0\n')
            self.file.write('@END_%s\n' % self.parser.i)  # there could be more than one 'eq' command
            self.file.write('0;JMP\n')
            self.file.write('(IF_TRUE_%s)\n' % self.parser.i)
            self.file.write('@SP\n')
            self.file.write('A=M-1\n')
            self.file.write('A=A-1\n')
            self.file.write('M=-1\n')
            self.file.write('(END_%s)\n' % self.parser.i)
            self.file.write('@SP\n')
            self.file.write('M=M-1\n')

        elif command == 'gt':
            # stack operation
            self.file.write('@SP\n')
            self.file.write('A=M-1\n')
            self.file.write('D=M\n')
            self.file.write('A=A-1\n')
            self.file.write('D=M-D\n')
            self.file.write('@IF_TRUE_%s\n' % self.parser.i)  # there could be more than one 'gt' command
            self.file.write('D;JGT\n')
            self.file.write('@SP\n')
            self.file.write('A=M-1\n')
            self.file.write('A=A-1\n')
            self.file.write('M=0\n')
            self.file.write('@END_%s\n' % self.parser.i)  # there could be more than one 'gt' command
            self.file.write('0;JMP\n')
            self.file.write('(IF_TRUE_%s)\n' % self.parser.i)
            self.file.write('@SP\n')
            self.file.write('A=M-1\n')
            self.file.write('A=A-1\n')
            self.file.write('M=-1\n')
            self.file.write('(END_%s)\n' % self.parser.i)
            self.file.write('@SP\n')
            self.file.write('M=M-1\n')

        elif command == 'lt':
            # stack operation
            self.file.write('@SP\n')
            self.file.write('A=M-1\n')
            self.file.write('D=M\n')
            self.file.write('A=A-1\n')
            self.file.write('D=M-D\n')
            self.file.write('@IF_TRUE_%s\n' % self.parser.i)  # there could be more than one 'lt' command
            self.file.write('D;JLT\n')
            self.file.write('@SP\n')
            self.file.write('A=M-1\n')
            self.file.write('A=A-1\n')
            self.file.write('M=0\n')
            self.file.write('@END_%s\n' % self.parser.i)  # there could be more than one 'lt' command
            self.file.write('0;JMP\n')
            self.file.write('(IF_TRUE_%s)\n' % self.parser.i)
            self.file.write('@SP\n')
            self.file.write('A=M-1\n')
            self.file.write('A=A-1\n')
            self.file.write('M=-1\n')
            self.file.write('(END_%s)\n' % self.parser.i)
            self.file.write('@SP\n')
            self.file.write('M=M-1\n')

        elif command == 'and':
            # stack operation
            self.file.write('@SP\n')
            self.file.write('A=M-1\n')
            self.file.write('D=M\n')
            self.file.write('A=A-1\n')
            self.file.write('M=D&M\n')
            self.file.write('@SP\n')
            self.file.write('M=M-1\n')

        elif command == 'or':
            # stack operation
            self.file.write('@SP\n')
            self.file.write('A=M-1\n')
            self.file.write('D=M\n')
            self.file.write('A=A-1\n')
            self.file.write('M=D|M\n')
            self.file.write('@SP\n')
            self.file.write('M=M-1\n')

        elif command == 'neg':
            # stack operation
            self.file.write('@SP\n')
            self.file.write('A=M-1\n')
            self.file.write('M=-M\n')

        elif command == 'not':
            # stack operation
            self.file.write('@SP\n')
            self.file.write('A=M-1\n')
            self.file.write('M=!M\n')

        else:
            raise ValueError("Unrecognized command for C_ARITHMETIC command type")

    def createOutput(self):
        # initially set the SP address to 256 (the address for the stack)
        self.file.write('@256\n')
        self.file.write('D=A\n')
        self.file.write('@SP\n')
        self.file.write('M=D\n')
        # set the local address to 300
        self.file.write('@300\n')
        self.file.write('D=A\n')
        self.file.write('@LCL\n')
        self.file.write('M=D\n')
        # set the argument address to 400
        self.file.write('@400\n')
        self.file.write('D=A\n')
        self.file.write('@ARG\n')
        self.file.write('M=D\n')
        # set the this address to 3000
        self.file.write('@3000\n')
        self.file.write('D=A\n')
        self.file.write('@THIS\n')
        self.file.write('M=D\n')
        # set the that address to 3010
        self.file.write('@3010\n')
        self.file.write('D=A\n')
        self.file.write('@THAT\n')
        self.file.write('M=D\n')
        self.parser.i = -1
        while self.parser.hasMoreCommands():
            self.parser.advance()
            c_type = self.parser.commandType()
            if c_type in ['C_PUSH', 'C_POP']:
                self.writePushPop()
            elif c_type == 'C_ARITHMETIC':
                self.writeArithmetic()
        # close file
        self.file.close()


if __name__ == "__main__":
    for path in ["StackArithmetic/SimpleAdd/SimpleAdd.vm", "StackArithmetic/StackTest/StackTest.vm",
                 "MemoryAccess/BasicTest/BasicTest.vm", "MemoryAccess/PointerTest/PointerTest.vm",
                 "MemoryAccess/StaticTest/StaticTest.vm"]:
        codewriter = CodeWriter(path)
        codewriter.createOutput()
