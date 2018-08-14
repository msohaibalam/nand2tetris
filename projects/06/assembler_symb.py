from parser import Parser
from code import Code
from symbol_table import SymbolTable


class AssemblerSymb:

    def __init__(self, path):
        self.parser = Parser(path)
        self.code = Code()
        self.symb_table = SymbolTable()
        ind1 = path.find('/')
        ind2 = path.find('.')
        writefile = path[:ind1] + "/" + path[ind1+1:ind2]
        self.file = open(writefile + '2.hack', 'w')

    def binary(self, s):
        return "{0:b}".format(int(s))

    def firstPass(self):
        counter = 0
        while self.parser.hasMoreCommands():
            self.parser.advance()
            command_type = self.parser.commandType()
            if command_type in ['A_COMMAND', 'C_COMMAND']:
                counter += 1
            elif command_type == 'L_COMMAND':
                symbol = self.parser.symbol()
                self.symb_table.addEntry(symbol, counter)
            else:
                raise ValueError("Unexpected command type encountered")

    def secondPass(self):
        ram_address = 16
        self.parser.i = -1
        while self.parser.hasMoreCommands():
            self.parser.advance()
            command_type = self.parser.commandType()
            if command_type == 'A_COMMAND':
                symbol = self.parser.symbol()
                if (not symbol.isdigit()) and (not self.symb_table.contains(symbol)):
                    self.symb_table.addEntry(symbol, ram_address)
                    ram_address += 1

    def createOutput(self):
        self.parser.i = -1
        while self.parser.hasMoreCommands():
            self.parser.advance()
            command_type = self.parser.commandType()
            # if A command
            if command_type == 'A_COMMAND':
                symbol = self.parser.symbol()
                if symbol.isdigit():
                    bin_symbol = self.binary(symbol)
                else:
                    symb_add = self.symb_table.getAddress(symbol)
                    bin_symbol = self.binary(symb_add)
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
    for path in ["add/Add.asm", "max/Max.asm", "pong/Pong.asm", "rect/Rect.asm"]:
        assemb_symb = AssemblerSymb(path)
        assemb_symb.firstPass()
        assemb_symb.secondPass()
        assemb_symb.createOutput()
