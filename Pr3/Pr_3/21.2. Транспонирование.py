def transpose(matrix):
    matrix[:] = [list(i) for i in zip(*matrix)]

def main():
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    transpose(matrix)
    print(matrix)
