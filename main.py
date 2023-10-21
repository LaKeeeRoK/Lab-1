#com2
BLACK = '\u001b[48;5;16m'
RED = '\u001b[41m'
GREEN = '\u001b[48;5;22m'
WHITE = '\u001b[47m'
END = '\u001b[0m'
sl = {0:3, 1:6, 2:8, 3:9, 4:10}
def f1():
    for _ in range(2):
        print(f'{GREEN}{" "*40}{END}')
    for i in range(4):
        print(f'{GREEN}{" "*(17-sl[i])}{RED}{" "* sl[i]*2}{GREEN}{" "*(23 - sl[i])}{END}')
    for i in range(4, -1, -1):
        print(f'{GREEN}{" "*(17-sl[i])}{RED}{" "* sl[i]*2}{GREEN}{" "*(23 - sl[i])}{END}')
    for _ in range(2):
        print(f'{GREEN}{" "*40}{END}')


# task2
def f2():
    stroki = {
        0 : f'{BLACK}{" "* 20}{END}{" "*10}',
        1  : f'{BLACK}{" "* 20}{END}{" "*10}',
        2  : f'{BLACK}{" "* 4}{END}{" "*12}{BLACK}{" "* 4}{END}{" "* 10}',
        3  : f'{BLACK}{" "* 4}{END}{" "*12}{BLACK}{" "* 4}{END}{" "* 10}',
        4  : f'{BLACK}{" "* 4}{END}{" "*12}{BLACK}{" "* 4}{END}{" "* 10}',
        5 :  f'{BLACK}{" "* 4}{END}{" "*6}{BLACK}{" "* 10}{END}{" "* 10}',
        6 : f'{BLACK}{" "* 4}{END}{" "*6}{BLACK}{" "* 10}{END}{" "* 10}',
        7 :  f'{BLACK}{" "* 4}{END}{" "*6}{BLACK}{" "* 4}{END}{" "* 16}',
        8  : f'{BLACK}{" "* 4}{END}{" "*6}{BLACK}{" "* 4}{END}{" "* 16}',
        9 :  f'{BLACK}{" "* 4}{END}{" "*6}{BLACK}{" "* 4}{END}{" "* 16}',
        10 :  f'{BLACK}{" "* 4}{END}{" "*6}{BLACK}{" "* 20}{END}',
    }
    numbers = int(input("Сколько раз вывести орнамент? "))
    for j in range(len(stroki)):
        for i in range(numbers):
            print(stroki[j], end="")
        print("")

        

#task3 y=2x+3
def f3():
    for y in range(-30, 31):
        for x in range(-50, 51):
            if (x == 0 or y == 0 or (x == -1 and y == -29) or
                    (x == 1 and y == -29) or (x == -2 and y == -28) or (x == 2 and y == -28)
                    or (x == 48 and y == -2) or (x == 49 and y == -1) or (x == 49 and y == 1) or
                    (x == 48 and y == 2)):
                print(f'{BLACK}{" "*2}{END}',end="")
            elif y == 2*x + 3:
                 print(f'{RED}{" "*2}{END}',end="")
            else:
                print(" "*2, end="")
        print("")

# for i in range(10):
#     for j in range(10):
#         if j == 0:
#             plot_list[i][j] = step * (8-i) + step

# for i in range(9):
#     for j in range(10):
#         if abs(plot_list[i][0] - result[9 - j]) < step:
#             for k in range(9):
#                 if 8 - k == j:
#                     plot_list[i][k+1] = 1

# for i in range(9):
#     line = ''
#     for j in range(10):
#         if j == 0:
#             line += '\t' + str(int(plot_list[i][j])) + '\t'
#         if plot_list[i][j] == 0:
#             line += '--'
#         if plot_list[i][j] == 1:
#             line += '!!'
#     print(line)
# print('\t0\t1 2 3 4 5 6 7 8 9')

# for i in range(10):
#     #print(plot_list[i])
#     pass

# file = open('sequence.txt', 'r')
# list = []
# for number in file:
#     list.append(float(number))
# file.close()
# print(list)

if __name__ == "__main__":
    f3()