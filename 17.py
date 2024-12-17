from utils import get_input


class Computer:
    def __init__(self):
        self.A = 0
        self.B = 0
        self.C = 0
        self.ip = 0
        self.program = []

    def reset(self):
        self.A = 0
        self.B = 0
        self.C = 0
        self.ip = 0

    def load_program(self, inp):
        inp = inp.strip().split('\n')
        self.A = int(inp[0].split()[-1])
        self.B = int(inp[1].split()[-1])
        self.C = int(inp[2].split()[-1])
        program = inp[4].split()[-1].split(',')
        program = [int(i) for i in program]
        self.program = program

    def get_combo(self, operand):
        if 0 <= operand <= 3:
            return operand
        if operand == 4:
            return self.A
        if operand == 5:
            return self.B
        if operand == 6:
            return self.C
        if operand == 7:
            raise ValueError('Invalid operand')

    def run(self, silent=False):
        output = []
        while True:
            if self.ip >= len(self.program):
                if not silent:
                    print(','.join([str(i) for i in output]))
                return output
            opcode = self.program[self.ip]
            operand = self.program[self.ip + 1]
            if opcode == 0:  # adv
                self.A = self.A // (2 ** self.get_combo(operand))
                self.ip += 2
            elif opcode == 1:  # bxl
                self.B = self.B ^ operand
                self.ip += 2
            elif opcode == 2:  # bst
                self.B = self.get_combo(operand) % 8
                self.ip += 2
            elif opcode == 3:  # jnz
                if self.A != 0:
                    self.ip = operand
                else:
                    self.ip += 2
            elif opcode == 4:  # bxc
                self.B = self.B ^ self.C
                self.ip += 2
            elif opcode == 5:  # out
                output.append(self.get_combo(operand) % 8)
                self.ip += 2
            elif opcode == 6:  # bdv
                self.B = self.A // (2 ** self.get_combo(operand))
                self.ip += 2
            elif opcode == 7:  # bdv
                self.C = self.A // (2 ** self.get_combo(operand))
                self.ip += 2


def a():
    c = Computer()
    # c.reset()
    # c.load_program(get_input(17, True, 1))
    # c.run()
    # assert c.B == 1
    # c.reset()
    # c.load_program(get_input(17, True, 2))
    # c.run()
    # c.reset()
    # c.load_program(get_input(17, True, 3))
    # c.run()
    # assert c.A == 0, c.A
    # c.reset()
    # c.load_program(get_input(17, True, 4))
    # c.run()
    # assert c.B == 26, c.B
    # c.reset()
    # c.load_program(get_input(17, True, 5))
    # c.run()
    # assert c.B == 44354, c.B
    # c.reset()
    # c.load_program(get_input(17, True, 6))
    # c.run()
    c.load_program(get_input(17))
    c.run()


def b():
    c = Computer()
    c.load_program(get_input(17))
    p_len = len(c.program)
    nr = "0" * p_len
    possible_starts = [""]
    for i in range(p_len):
        new_possible_starts = []
        for s in possible_starts:
            for j in range(8):
                test_nr = int(f"{s}{j}{nr[i+1:]}", 8)
                c.reset()
                c.A = test_nr
                res = c.run(silent=True)
                try:
                    if res[::-1][i] == c.program[::-1][i]:
                        new_possible_starts.append(f"{s}{j}")
                except IndexError:
                    pass
        possible_starts = new_possible_starts
    print(sorted([int(x, 8) for x in possible_starts])[0])




if __name__ == '__main__':
    a()
    b()
