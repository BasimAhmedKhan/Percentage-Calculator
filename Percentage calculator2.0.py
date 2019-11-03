print("Select Operation")
print("1.S.S.C Part:1")
print("2.S.S.C Part:2")
print("3.H.S.C Part:1")
print("4.H.S.C Part:2")

choice = int(input("Enter Choice(1/2/3/4): "))

if choice == 1:
    print('"S.S.C Part 1"')
    sub1 = int(input("Sindhi Salees: "))
    sub2 = int(input("English: "))
    sub3 = int(input("Pakistan Studies: "))
    sub4 = int(input("Biology|Computer Science: "))
    sub5 = int(input("Chemistry: "))
    percentage = ((sub1 + sub2 + sub3 + sub4 + sub5)/425) * 100
    print(((sub1 + sub2 + sub3 + sub4 + sub5)/425) * 100)
    if percentage >= 80: 
        print('"A+ Grade"')
    elif percentage >= 70:
        print('"A Grade"')
    elif percentage >= 60:
        print('"B Grade"')
    elif percentage >= 50:
        print('"C Grade"')
    elif percentage >= 40:
        print('"D Grade"')
    else: 
        print('"Failed"')    

elif choice == 2:
    print('"S.S.C Part 2"')
    subj1 = int(input("Sindhi|Urdu Normal: "))
    subj2 = int(input("English Papper1|English Papper2: "))
    subj3 = int(input("Pakistan Studies: "))
    subj4 = int(input("Biology|Computer Science: "))
    subj5 = int(input("Chemistry: "))
    subj6 = int(input("Islamiat: "))
    subj7 = int(input("Mathematics: "))
    subj8 = int(input("Physics: "))
    prct = ((subj1 + subj2 + subj3 + subj4 + subj5 + subj6 + subj7 + subj8)/835) * 100
    print(((subj1 + subj2 + subj3 + subj4 + subj5 + subj6 + subj7 + subj8)/835) * 100)
    if prct >= 80: 
        print('"A+ Grade"')
    elif prct >= 70:
        print('"A Grade"')
    elif prct >= 60:
        print('"B Grade"')
    elif prct >= 50:
        print('"C Grade"')
    elif prct >= 40:
        print('"D Grade"')
    else: 
        print('"Failed"')

elif choice == 3:
    print('"H.S.C Part 1"')
    pap1 = int(input("Mathematics: "))
    pap2 = int(input("Chemistry: "))
    pap3 = int(input("Physics: "))
    pap4 = int(input("English: "))
    pap5 = int(input("Urdu Normal: "))
    pap6 = int(input("Islamiat: "))
    prc = ((pap1 + pap2 + pap3 + pap4 + pap5 + pap6)/550) * 100
    print(((pap1 + pap2 + pap3 + pap4 + pap5 + pap6)/550) * 100)
    if prc >= 80: 
        print('"A+ Grade"')
    elif prc >= 70:
        print('"A Grade"')
    elif prc >= 60:
        print('"B Grade"')
    elif prc >= 50:
        print('"C Grade"')
    elif prc >= 40:
        print('"D Grade"')
    else: 
        print('"Failed"')

elif choice == 4:
    print('"H.S.C Part 2"')
    pape1 = int(input("Mathematics: "))
    pape2 = int(input("Chemistry: "))
    pape3 = int(input("Physics: "))
    pape4 = int(input("English: "))
    pape5 = int(input("Urdu Normal: "))
    pape6 = int(input("Pakistan Studies: "))
    pr = ((pape1 + pape2 + pape3 + pape4 + pape5 + pape6)/550) * 100
    print(((pape1 + pape2 + pape3 + pape4 + pape5 + pape6)/550) * 100)
    if pr >= 80: 
        print('"A+ Grade"')
    elif pr >= 70:
        print('"A Grade"')
    elif pr >= 60:
        print('"B Grade"')
    elif pr >= 50:
        print('"C Grade"')
    elif pr >= 40:
        print('"D Grade"')
    else: 
        print('"Failed"')

else:
    print("Invalid input")

