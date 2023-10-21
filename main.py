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


def f4():
    file = open('sequence.txt', 'r')
    sum1 = 0
    count = 0
    sum2 = 0
    for number in file:
        if count < 150:
            sum1 += float(number)
        else:
            sum2 += float(number)
        count += 1
    file.close()
    print(sum1, sum2)

if __name__ == "__main__":
    print("task 1")
    f1()
    print("------------------------")
    print("task 2")
    f2()
    print("------------------------")
    print("task 3")
    f3()
    print("------------------------")
    print("task 4")
    f4()