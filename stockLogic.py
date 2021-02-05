
def begin():
    print("1 - change mod percent (default 3% down, 5% up)\n2 - change values\n3 - Start")
    start = int(input("-->"))

    upPerc = .05
    downPerc = .03
    if start == 1:
        print("set percent to increase when bought (default 5%)\n*ENTER AS DEC 5% == .05*\n")
        upPerc = input("-->")
        print("set percent to decrease when bought (default 3%)\n*ENTER AS DEC 5% == .05*\n")
        downPerc = input("-->")
        begin()
    elif start == 2:
        pr1 = int(input("Set fist price (lowest)\n-->"))
        pr2 = int(input("Set second price\n-->"))
        pr3 = int(input("Set third price\n-->"))
        pr4 = int(input("Set fourth price\n-->"))
        pr5 = int(input("Set fifth price\n-->"))
        pr6 = int(input("Set sixth price\n-->"))
        pr7 = int(input("Set seventh price (highest) \n-->"))
        
        setPrices(pr1, pr2, pr3, pr4, pr5, pr6, pr7)
        begin()
    elif start == 3:
        main(upPerc, downPerc)


def logic(buy, up, down):

    if buy == 9999:
        reset()
        return 0
    
    f1 = open("1.txt", "r+")
    f2 = open("2.txt", "r+")
    f3 = open("3.txt", "r+")
    f4 = open("4.txt", "r+")
    f5 = open("5.txt", "r+")
    f6 = open("6.txt", "r+")
    f7 = open("7.txt", "r+")


    #get all numbers in file

    p1 = float(f1.read())

    p2 = float(f2.read())

    p3 = float(f3.read())

    p4 = float(f4.read())

    p5 = float(f5.read())

    p6 = float(f6.read())

    p7 = float(f7.read())

    #find whats been bought
    #change prices +1 for bought -.1 for not bought
    buy = int(buy)

    ch1 = float(p1 * down)
    ch2 = float(p2 * down)
    ch3 = float(p3 * down)
    ch4 = float(p4 * down)
    ch5 = float(p5 * down)
    ch6 = float(p6 * down)
    ch7 = float(p7 * down)


    p1 = p1 - ch1
    p2 = p2 - ch2
    p3 = p3 - ch3
    p4 = p4 - ch4
    p5 = p5 - ch5
    p6 = p6 - ch6
    p7 = p7 - ch7
    
    if buy == 1:
        p1 = p1 + ch1
        p1 = float(p1 * (1.00 + up))
    elif buy == 2:
        p2 = p2 + ch2
        p2 = float(p2 * (1.00 + up))
    elif buy == 3:
        p3 = p3 + ch3
        p3 = float(p3 * (1.00 + up))
    elif buy == 4:
        p4 = p4 + ch4
        p4 = float(p4 * (1.00 + up))
    elif buy == 5:
        p5 = p5 + ch5
        p5 = float(p5 * (1.00 + up))
    elif buy == 6:
        p6 = p6 + ch6
        p6 = float(p6 * (1.00 + up))
    elif buy == 7:
        p7 = p7 + ch7
        p7 = float(p7 * (1.00 + up))
        
    #change text in file
    f1.close()
    f2.close()
    f3.close()
    f4.close()
    f5.close()
    f6.close()
    f7.close()

    setPrices(p1, p2, p3, p4, p5, p6, p7)
    

def setPrices(p1, p2, p3, p4, p5, p6, p7):
    f1 = open("1.txt", "w")
    f2 = open("2.txt", "w")
    f3 = open("3.txt", "w")
    f4 = open("4.txt", "w")
    f5 = open("5.txt", "w")
    f6 = open("6.txt", "w")
    f7 = open("7.txt", "w")

    f1.write("%.2f"%p1)
    f2.write("%.2f"%p2)
    f3.write("%.2f"%p3)
    f4.write("%.2f"%p4)
    f5.write("%.2f"%p5)
    f6.write("%.2f"%p6)
    f7.write("%.2f"%p7)

    printPrice(p1, p2, p3, p4, p5, p6, p7)

def reset():
    setPrices(1.00, 2.00, 5.00, 13.00, 18.00, 20.00, 30.00)

def main(up, down):
    while(True):
        choice = int(input("Which was bought\n -->\t"))
        logic(choice, up, down)

def printPrice(p1, p2, p3, p4, p5, p6, p7):
    f1 = open("1.txt", "w")
    f2 = open("2.txt", "w")
    f3 = open("3.txt", "w")
    f4 = open("4.txt", "w")
    f5 = open("5.txt", "w")
    f6 = open("6.txt", "w")
    f7 = open("7.txt", "w")

    print("%.2f"%p1)
    print("%.2f"%p2)
    print("%.2f"%p3)
    print("%.2f"%p4)
    print("%.2f"%p5)
    print("%.2f"%p6)
    print("%.2f"%p7)

#reset()
begin()

    
