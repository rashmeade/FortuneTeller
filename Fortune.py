'''
Created on Mar 1, 2021

@author: rashmeade22
'''

one = 'Pick a number. 1, 4, 5, or 8: '
two = 'Pick a number. 2, 3, 7, or 9: '

def SecondNumber(first_number, color):  # main code
    first_number = int(first_number)
    color = int(color)
    
    if (color % 2) == 0 and (first_number % 2) == 0: 
        while True:
            second_number = input(one)
            if second_number != '1' and second_number != '4' and second_number != '5' and second_number != '8':
                continue
            else:
                break 
    elif (color % 2) == 0 and (first_number % 2) != 0:
        while True:
            second_number = input(two)
            if second_number != '2' and second_number != '3' and second_number != '7' and second_number != '9':
                continue
            else:
                break
    elif (color % 2) != 0 and (first_number % 2) == 0:
        while True:
            second_number = input(two)
            if second_number != '2' and second_number != '3' and second_number != '7' and second_number != '9':
                continue
            else:
                break
    elif (color % 2) != 0 and (first_number % 2) != 0:
        while True:
            second_number = input(one)
            if second_number != '1' and second_number != '4' and second_number != '5' and second_number != '8':
                continue
            else:
                break
        
    return int(second_number)

def Outcome(second_number):
    if second_number == 1:
        outcome = ('')
    elif second_number == 2:
        outcome = ('')
    elif second_number == 3:
        outcome = ('')
    elif second_number == 4:
        outcome = ('')
    elif second_number == 5:
        outcome = ('')
    elif second_number == 9:
        outcome = ('')
    elif second_number == 7:
        outcome = ('')
    elif second_number == 8:
        outcome = ('')
        
    return outcome
def main():
    fortune = True
    while fortune:
        color = input("Pick a color. 1) for red; 2) for blue; 3) for green; 4) for yellow: ")
        if color == '1' or color == '3':
            while True:
                first_number = input(two)
                if first_number != '2' and first_number != '3' and first_number != '7' and first_number != '9':
                    continue
                else:
                    second_number = SecondNumber(first_number, color)
                    print(Outcome(second_number))
                    fortune = False
                    break
        elif color == '2' or color == '4':
            while True:
                first_number = input(one)
                if first_number != '1' and first_number != '4' and first_number != '5' and first_number != '8':
                    continue
                else:
                    second_number = SecondNumber(first_number, color)
                    print(Outcome(second_number))
                    fortune = False
                    break
      

if __name__ == '__main__':
    main()