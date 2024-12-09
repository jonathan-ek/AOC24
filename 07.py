from utils import get_input


def a():
    inp = get_input(7).strip().split('\n')
    operators = ['+', '*']
    total = 0
    for d in inp:
        res, nums = d.split(': ')
        res = int(res)
        nums = [int(x) for x in nums.split(' ')]
        num_operators = len(nums) - 1
        for i in range(2 ** num_operators):
            it_nums = nums.copy()
            binary = bin(i)[2:].zfill(num_operators)
            for idx, operator_index in enumerate(binary):
                operator = operators[int(operator_index)]
                if operator == '+':
                    it_nums[0] += it_nums[idx + 1]
                elif operator == '*':
                    it_nums[0] *= it_nums[idx + 1]
            if it_nums[0] == res:
                total += res
                break
    print(total)


def to_base(n, base):
    if n == 0:
        return '0'
    nums = []
    while n:
        n, r = divmod(n, base)
        nums.append(str(r))
    return ''.join(reversed(nums))

def b():
    inp = get_input(7).strip().split('\n')
    operators = ['+', '*', '||']
    total = 0
    for d in inp:
        res, nums = d.split(': ')
        res = int(res)
        nums = [int(x) for x in nums.split(' ')]
        num_operators = len(nums) - 1
        for i in range(len(operators) ** num_operators):
            it_nums = nums.copy()
            binary = to_base(i, len(operators)).zfill(num_operators)
            for idx, operator_index in enumerate(binary):
                operator = operators[int(operator_index)]
                if operator == '+':
                    it_nums[0] += it_nums[idx + 1]
                elif operator == '*':
                    it_nums[0] *= it_nums[idx + 1]
                elif operator == '||':
                    it_nums[0] = int(f"{it_nums[0]}{it_nums[idx + 1]}")
            if it_nums[0] == res:
                total += res
                break
    print(total)


if __name__ == '__main__':
    a()
    b()