class Parser:

    def __init__(self, path):
        self.f = open(path, 'r')
        self.raw_lines = self.f.readlines()
        self.clean_lines = []
        for line in self.raw_lines:
            if (line[:2] == "//") or (line == "\n"):
                continue
            else:
                pass
            # some cleaning
            if '//' in line:
                line = line[:line.find('//')]
            line = line.replace(" ", "")
            # create clean lines
            l = []
            for ch in line:
                if ch not in ['', '\n']:
                    l.append(ch)
            self.clean_lines.append(''.join(l))
        self.i = -1      # address of current command, initialized to -1
        self.command = None     # current command, initialized to None
        self.total_commands = len(self.clean_lines)

    def hasMoreCommands(self):
        return self.i < self.total_commands - 1

    def advance(self):
        if self.hasMoreCommands():
            self.i += 1
            self.command = self.clean_lines[self.i]
            # self.command = self.clean_symbol(self.command)

    def commandType(self):
        if self.command[0] == '@':
            return 'A_COMMAND'
        elif self.command[0] == '(':
            return 'L_COMMAND'
        else:
            return 'C_COMMAND'

    def symbol(self):
        if self.commandType() == 'A_COMMAND':
            return self.command[1:]
        elif self.commandType() == 'L_COMMAND':
            return self.command[1:-1]
        else:
            raise ValueError("Command type should be A or L")

    def dest(self):
        if self.commandType() == 'C_COMMAND':
            ind = self.command.find('=')
            if ind != -1:
                return self.command[:ind]
            else:
                return 'null'
        else:
            raise ValueError("Command type should be C")

    def comp(self):
        if self.commandType() == 'C_COMMAND':
            ind1 = self.command.find('=')
            ind2 = self.command.find(';')
            if (ind1 != -1) and (ind2 != -1):
                return self.command[ind1+1:ind2]
            elif (ind1 != -1) and (ind2 == -1):
                return self.command[ind1+1:]
            elif (ind1 == -1) and (ind2 != -1):
                return self.command[:ind2]
            elif (ind1 == -1) and (ind2 == -1):
                return self.command
        else:
            raise ValueError("Command type should be C")

    def jump(self):
        if self.commandType() == 'C_COMMAND':
            ind = self.command.find(';')
            if ind != -1:
                return self.command[ind+1:]
            else:
                return 'null'
        else:
            raise ValueError("Command type should be C")
