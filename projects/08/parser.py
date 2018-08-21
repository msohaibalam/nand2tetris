class Parser:

    def __init__(self, path):
        # TODO: Create some logic that checks whether path ends in .vm, or is a directory
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

    def commandType(self):
        # C_ARITHMETIC, C_PUSH, C_POP, C_LABEL, C_GOTO, C_IF, C_FUNCTION, C_RETURN, C_CALL
        # Returns the type of the current VM command. C_ARITHMETIC is returned for all the arithmetic commands.
        if self.command in ['add', 'sub', 'neg', 'eq', 'gt', 'lt', 'and', 'or', 'not']:
            return 'C_ARITHMETIC'
        elif 'push' in self.command:
            return 'C_PUSH'
        elif 'pop' in self.command:
            return 'C_POP'
        elif 'label' in self.command:
            return 'C_LABEL'
        elif 'if-goto' in self.command:
            return 'C_IF'
        elif 'goto' in self.command:
            return 'C_GOTO'
        elif 'function' in self.command:
            return 'C_FUNCTION'
        elif 'call' in self.command:
            return 'C_CALL'
        elif 'return' in self.command:
            return 'C_RETURN'
        else:
            raise ValueError("Unrecognized command type")

    def arg1(self):
        if self.commandType() == 'C_ARITHMETIC':
            return self.command
        elif self.commandType() == 'C_PUSH':
            # push segment index
            s = self.command.split('push')[1]
            for ch in s:
                if ch.isdigit():
                    ind = s.index(ch)
                    break
            return s[:ind]
        elif self.commandType() == 'C_POP':
            # pop segment index
            s = self.command.split('pop')[1]
            for ch in s:
                if ch.isdigit():
                    ind = s.index(ch)
                    break
            return s[:ind]
        elif self.commandType() == 'C_FUNCTION':
            # function functionName nLocals
            s = self.command.split('function')[1]
            for i, ch in enumerate(s):
                if not ch.isdigit():
                    ind = i
            return s[:ind+1]
        elif self.commandType() == 'C_CALL':
            # call functionName nArgs
            s = self.command.split('call')[1]
            for i, ch in enumerate(s):
                if not ch.isdigit():
                    ind = i
            return s[:ind+1]
        elif self.commandType() == 'C_LABEL':
            # label symbol
            return self.command.split('label')[1]
        elif self.commandType() == 'C_IF':
            # if-goto symbol
            return self.command.split('if-goto')[1]
        elif self.commandType() == 'C_GOTO':
            # goto symbol
            return self.command.split('goto')[1]
        elif self.commandType() == 'C_RETURN':
            pass
        else:
            raise ValueError("Unrecognized command type when trying to obtain arg1")

    def arg2(self):
        if self.commandType() in ['C_PUSH', 'C_POP']:
            for ch in self.command:
                if ch.isdigit():
                    ind = self.command.index(ch)
                    break
            return self.command[ind:]
        elif self.commandType() == 'C_FUNCTION':
            s = self.command.split('function')[1]
            for i, ch in enumerate(s):
                if not ch.isdigit():
                    ind = i
            return s[ind+1:]
        elif self.commandType() == 'C_CALL':
            s = self.command.split('call')[1]
            for i, ch in enumerate(s):
                if not ch.isdigit():
                    ind = i
            return s[ind+1:]
