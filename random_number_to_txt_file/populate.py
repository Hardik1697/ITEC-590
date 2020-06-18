import random


def pop(lst, ran, numbers):
    lst = random.sample(range(ran), numbers)
    return lst


def write_to_file(name, lst):
    f = open(name, 'w')
    f.writelines("%s\n" % i for i in lst)
    f.close()


def main():
    lst = []
    name = input("Enter the name of the new file you want to create, without extension (E.g., fileName): ")
    name += ".txt"
    ran = int(input("Enter the range of the numbers. E.g., if you want a range of numbers between 0 and 100 (0 is "
                    "included and 100 is not), enter 100: "))
    numbers = int(input("Enter the number of integers you want to populate the text file with: "))
    lst = pop(lst, ran, numbers)
    print(lst)
    write_to_file(name, lst)


if __name__ == '__main__':
    main()
