string = input()
char = string[0]
word_list = string[1:].split('V')
nums = 0
for move in word_list:
    if move and move[0] == '<':
        nums -= len(move)
    print(' '*nums + char*(1+len(move)))
    if move and move[0] == '>':
        nums += len(move)