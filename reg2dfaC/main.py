import string
# ----------------------------------------------------------------------------------------------------------------------


class Reg2DFAC:
    START = '\2'
    RESERVED = set('()|*+?\0' + START)
    PRINTABLE = set(string.printable)
    ALPHABET = PRINTABLE - RESERVED

    def __init__(self, reg):
        self.reg = reg
        self.graph = {}

    def _find_state(self, idx, prev_state):
        for i in range(idx, len(self.reg)):
            c = reg[i]
            if c in Reg2DFAC.ALPHABET:
                self.graph[prev_state].append(c)
                self.graph[c] = []
            elif c in Reg2DFAC.RESERVED:
                if c == '(':
                    self._find_state(i + 1, prev_state)
                pass
            else:
                raise Exception('Unknown char: %c' % c)

    def create_states(self):
        self.graph = {}
        self._find_state(0, Reg2DFAC.START)
# ----------------------------------------------------------------------------------------------------------------------


reg = '(a|b)*abb(a|b)*'
parser = Reg2DFAC(reg)
parser.create_states()




