from parser import Parser


class CodeWriter:

    def __init__(self, path):
        self.parser = Parser(path)
        # just perform the logic of the recommended setFileName constructor here
        ind1 = path.find('/')
        ind2 = path.find('.')
        writefile = path[:ind1] + "/" + path[ind1+1:ind2]
        self.filename = writefile + '.asm'
        self.file = open(self.filename, 'w')
        # self.stack = []

    def writePushPop(self):   # no need to pass in command as an argument
        assert self.parser.commandType() in ['C_PUSH', 'C_POP']
        arg1 = self.parser.arg1()
        arg2 = self.parser.arg2()
        if arg1 == 'constant':
            if self.parser.commandType() == 'C_PUSH':
                # # push to stack
                # self.stack.append(int(arg2))
                # write to file
                # e.g. push constant 7
                self.file.write('@%s\n' % arg2)
                self.file.write('D=A\n')    # D = 7
                self.file.write('@SP\n')
                self.file.write('A=M\n')
                self.file.write('M=D\n')    # M[M[0]] = 7
                self.file.write('@SP\n')
                self.file.write('M=M+1\n')  # M[0] = M[0] + 1
            else:
                # TODO
                pass
        else:
            # TODO
            pass

    def writeArithmetic(self):   # no need to pass in command as an argument
        assert self.parser.commandType() == 'C_ARITHMETIC'
        command = self.parser.arg1()
        if command == 'add':
            # # stack operation
            # x = self.stack.pop()
            # y = self.stack.pop()
            # result = x + y
            # self.stack.append(result)
            # write to file
            self.file.write('@SP\n')
            self.file.write('A=M-1\n')
            self.file.write('D=M\n')
            self.file.write('A=A-1\n')
            self.file.write('D=D+M\n')
            self.file.write('M=D\n')
            self.file.write('@SP\n')
            self.file.write('M=M-1\n')
        elif command == 'sub':
            # # stack operation
            # x = self.stack.pop()
            # y = self.stack.pop()
            # result = y - x
            # self.stack.append(result)
            # write to file
            self.file.write('@SP\n')
            self.file.write('A=M-1\n')
            self.file.write('D=M\n')
            self.file.write('A=A-1\n')
            self.file.write('D=M-D\n')
            self.file.write('M=D\n')
            self.file.write('@SP\n')
            self.file.write('M=M-1\n')
        elif command == 'eq':
            # # stack operation
            # x = self.stack.pop()
            # y = self.stack.pop()
            # result = (x == y)
            # d_bool = {False: 0, True: -1}
            # result_int = d_bool[result]
            # self.stack.append(result_int)
            # write to file
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

            # self.file.write('@SP\n')
            # self.file.write('A=M-1\n')
            # self.file.write('A=A-1\n')
            # self.file.write('M=%s\n' % result_int)
            # self.file.write('@SP\n')
            # self.file.write('M=M-1\n')
        elif command == 'gt':
            # # stack operation
            # x = self.stack.pop()
            # y = self.stack.pop()
            # result = (y > x)
            # d_bool = {False: 0, True: -1}
            # result_int = d_bool[result]
            # self.stack.append(result_int)
            # write to file
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

            # self.file.write('@SP\n')
            # self.file.write('A=M-1\n')
            # self.file.write('A=A-1\n')
            # self.file.write('M=%s\n' % result_int)
            # self.file.write('@SP\n')
            # self.file.write('M=M-1\n')
        elif command == 'lt':
            # # stack operation
            # x = self.stack.pop()
            # y = self.stack.pop()
            # result = (y < x)
            # d_bool = {False: 0, True: -1}
            # result_int = d_bool[result]
            # self.stack.append(result_int)
            # write to file
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

            # self.file.write('@SP\n')
            # self.file.write('A=M-1\n')
            # self.file.write('A=A-1\n')
            # self.file.write('M=%s\n' % result_int)
            # self.file.write('@SP\n')
            # self.file.write('M=M-1\n')
        elif command == 'and':
            # # stack operation
            # x = self.stack.pop()
            # y = self.stack.pop()
            # result = (x & y)    # bit-wise and
            # self.stack.append(result)
            # write to file
            self.file.write('@SP\n')
            self.file.write('A=M-1\n')
            self.file.write('D=M\n')
            self.file.write('A=A-1\n')
            self.file.write('M=D&M\n')
            # self.file.write('D=D&M\n')
            # self.file.write('M=D\n')
            self.file.write('@SP\n')
            self.file.write('M=M-1\n')

            # self.file.write('@%s\n' % result)
            # self.file.write('D=A\n')
            # self.file.write('@SP\n')
            # self.file.write('A=M-1\n')
            # self.file.write('A=A-1\n')
            # self.file.write('M=D\n')
            # self.file.write('@SP\n')
            # self.file.write('M=M-1\n')
        elif command == 'or':
            # # stack operation
            # x = self.stack.pop()
            # y = self.stack.pop()
            # result = (x | y)    # bit-wise or
            # self.stack.append(result)
            # write to file
            self.file.write('@SP\n')
            self.file.write('A=M-1\n')
            self.file.write('D=M\n')
            self.file.write('A=A-1\n')
            self.file.write('M=D|M\n')
            # self.file.write('D=D|M\n')
            # self.file.write('M=D\n')
            self.file.write('@SP\n')
            self.file.write('M=M-1\n')

            # self.file.write('@%s\n' % result)
            # self.file.write('D=A\n')
            # self.file.write('@SP\n')
            # self.file.write('A=M-1\n')
            # self.file.write('A=A-1\n')
            # self.file.write('M=D\n')
            # self.file.write('@SP\n')
            # self.file.write('M=M-1\n')
        elif command == 'neg':
            # # stack operation
            # x = self.stack.pop()
            # result = -x
            # self.stack.append(result)
            # write to file
            self.file.write('@SP\n')
            self.file.write('A=M-1\n')
            self.file.write('M=-M\n')
            # self.file.write('D=-M\n')
            # self.file.write('M=D\n')

            # self.file.write('@%s\n' % x)
            # self.file.write('D=-A\n')
            # self.file.write('@SP\n')
            # self.file.write('A=M-1\n')
            # self.file.write('M=D\n')
        elif command == 'not':
            # # stack operation
            # x = self.stack.pop()
            # result = ~x
            # self.stack.append(result)
            # write to file
            self.file.write('@SP\n')
            self.file.write('A=M-1\n')
            self.file.write('M=!M\n')
            # self.file.write('D=!M\n')
            # self.file.write('M=D\n')

            # self.file.write('@%s\n' % x)
            # self.file.write('D=!A\n')
            # self.file.write('@SP\n')
            # self.file.write('A=M-1\n')
            # self.file.write('M=D\n')
        else:
            raise ValueError("Unrecognized command for C_ARITHMETIC command type")

    def createOutput(self):
        # initially set the SP address to 256 (the address for the stack)
        self.file.write('@256\n')
        self.file.write('D=A\n')
        self.file.write('@SP\n')
        self.file.write('M=D\n')
        self.parser.i = -1
        while self.parser.hasMoreCommands():
            self.parser.advance()
            c_type = self.parser.commandType()
            if c_type == 'C_PUSH':
                self.writePushPop()
            elif c_type == 'C_ARITHMETIC':
                self.writeArithmetic()
        # close file
        self.file.close()


if __name__ == "__main__":
    for path in ["StackArithmetic/SimpleAdd/SimpleAdd.vm", "StackArithmetic/StackTest/StackTest.vm"]:
    # for path in ["StackArithmetic/StackTest/try_random.vm"]:
        codewriter = CodeWriter(path)
        codewriter.createOutput()
