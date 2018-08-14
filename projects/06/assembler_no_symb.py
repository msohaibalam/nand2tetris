from parser import Parser
from code import Code


class AssemblerNoSymb:

    def __init__(self, path):
        self.parser = Parser(path)
        self.code = Code()
        ind1 = path.find('/')
        ind2 = path.find('.')
        writefile = path[:ind1] + "/" + path[ind1+1:ind2]
        self.file = open(writefile + '1.hack', 'w')

    def binary(self, s):
        return "{0:b}".format(int(s))

    def createOutput(self):
        while self.parser.hasMoreCommands():
            self.parser.advance()
            command_type = self.parser.commandType()
            # if A command
            if command_type == 'A_COMMAND':
                symbol = self.parser.symbol()
                bin_symbol = self.binary(symbol)
                a_command = '0' * (16 - len(bin_symbol)) + bin_symbol
                self.file.write(a_command + '\n')
            elif command_type == 'C_COMMAND':
                dest_mnem = self.parser.dest()
                dest = self.code.dest(dest_mnem)
                comp_mnem = self.parser.comp()
                comp = self.code.comp(comp_mnem)
                jump_mnem = self.parser.jump()
                jump = self.code.jump(jump_mnem)
                c_command = '111' + comp + dest + jump
                self.file.write(c_command + '\n')
            else:
                pass
        self.file.close()


if __name__ == "__main__":
    for path in ["add/Add.asm", "max/MaxL.asm", "pong/PongL.asm", "rect/RectL.asm"]:
        assemb_nosymb = AssemblerNoSymb(path)
        assemb_nosymb.createOutput()
