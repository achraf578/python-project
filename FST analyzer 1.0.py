fsts = []

number_of_fst=int(input("How many FST do you want to add? "))

for i in range(number_of_fst):
    fst = {
        "City" : input("enter the City: "),
        "Branch" : input("enter the branch: "),
        "Applicants" : int(input("enter the number of applicants: ")),
        "Seats" : int(input("enter the number of seats available: "))
    }
    ratio=fst["Applicants"]/fst["Seats"]
    fsts.append(fst)
    print(f"FST {fst['City']}:\nBranch: {fst['Branch']}\nRatio: {ratio:.2f}")