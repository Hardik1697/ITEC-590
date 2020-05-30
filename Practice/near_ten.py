def near_ten(num):
    a = num % 10        
    #print(a)
    b = abs(a - 2)
    #print(b)
    if a > 2:
        print("F")  
    else:
        print("T")

def main():
    near_ten(12)
    near_ten(17)
    near_ten(19)
    near_ten(31)
    near_ten(6)
    near_ten(10)
    near_ten(11)
    near_ten(21)
    near_ten(22)
    near_ten(23)
    near_ten(54)
    near_ten(155)
    near_ten(158)
    near_ten(13)
    near_ten(1)

if __name__ == "__main__":
    main()
