from stack_array import StackArray


def reverse_file(filename):
    S = StackArray()
    with open(filename) as infile:
        for line in infile:
            S.push(line.strip('\n'))
    with open(filename, 'w') as outfile:
        while not S.is_empty():
            outfile.write(S.pop()+'\n')

reverse_file('hello.txt')
