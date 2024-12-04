def get_input(day, test=False, test_nr=1):
    if test:
        return open(f'input/{str(day).zfill(2)}_test_{test_nr}.txt').read()
    return open(f'input/{str(day).zfill(2)}.txt').read()