point = 0

def hardware(point):
    q1_ans = input("\nName the moving hardware on your computer: ").lower()
    if q1_ans == 'mouse':
        point += 10
        print("Correct Answer")
    else:
        print("Answer is wrong, correct answer is 'Mouse'")

    print(f"Thank you\n Your point is {point}") 

def software(point):
    q1_ans = input("\nName a famous photo-editing software?: ").lower()
    if q1_ans == 'photoshop':
        point += 10
        print("Correct Answer")
    else:
        print("Answer is wrong, correct answer is 'Photoshop'")

    print(f"Thank you\nYour point is {point}")

def comp_game(point):
    inp = int(input("\n1: Hardware\n2: Software\nYour choice: "))
    if inp == 1:
        hardware(point)
    elif inp == 2:
        software(point)
    else:
        print("Wrong Input.")

def phy(point):
    q1_ans = input("\nWho proposed the theory of relativity?: ").lower()
    if q1_ans == 'albert einstein':
        point += 10
        print("Correct Answer")
    else:
        print("Answer is wrong, correct answer is 'Albert Einstein'")

    print(f"Thank you\n Your point is {point}") 

def chem(point):
    q1_ans = input("\nWhat is the fourth state of matter called?: ").lower()
    if q1_ans == 'plasma':
        point += 10
        print("Correct Answer")
    else:
        print("Answer is wrong, correct answer is 'Plasma'")

    print(f"Thank you\n Your point is {point}")    
    

def sci_game(point):
    inp = int(input("\n1: Physics\n2: Chemistry\nYour choice: "))
    if inp == 1:
        phy(point)
    elif inp == 2:
        chem(point)
    else:
        print("Wrong Input.")        

    
def game1(point):
    inp = int(input("\n1: Sciene\n2: Computer\nYour choice: "))
    if inp == 1:
        sci_game(point)
    elif inp == 2:
        comp_game(point)
    else:
        print("Wrong Input.")    

def main(point):
    name = input("Enter your name: ")
    psw  = int(input("Enter password (12): "))

    if psw == 12:
        game1(point)
    else:
        print("Wrong password.\n")    

if __name__ == "__main__":
    main(point)    