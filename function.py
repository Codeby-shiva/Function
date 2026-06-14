def percentage(x):
    pct = x/600*100
    print(f"Your Percentage is : {pct:.0f}%")              
    # .0f  means f stand for howmuch floating numbers will be display after decimal , here  0, so no floating number will be display 
    

while True:
    print(" ---||  PUT YOUR MARK DOWN AND SEE YOUR PERCENTAGE OUT OF 100%  ||--- ")
    student_mark = int(input("Enter your mark out of total '600' : "))
    if student_mark > 600  or student_mark < 0:
        print("Given input is out of range !")
        break
    percentage(student_mark)

    