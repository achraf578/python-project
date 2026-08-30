while True:
    user_choice = int(input("1-add anime\n2-remove anime\n3-search anime\n4-show anime list\n5-save&exit\nPlease choose the number of the action you want: "))

    if user_choice == 1:
        anime_number=int(input("How many anime do you want to add? "))
        for i in range(anime_number):
            anime_add=input("enter anime name: ").lower()
            with open("anime.txt", "r") as file:
                line=file.readlines()
                line=[word.strip() for word in line]
            if anime_add in line:
                    print("Anime already exist!")
            else:
                    with open("anime.txt", "a") as file:
                        file.write(f"{anime_add}\n")
        print("Done!")

    elif user_choice == 2:
        anime_number=int(input("How many anime do you want to remove? "))  
        for i in range(anime_number):      
            anime_remove = input("enter anime name: ").lower()
            with open("anime.txt", "r") as file:
                line=file.readlines()
                line=[word.strip() for word in line]
            if anime_remove in line:
                line.remove(anime_remove)
                with open("anime.txt", "w") as file:
                    text="\n".join(line)
                    file.write(text+"\n")
                    print("Done!")
            else:
                print("anime not found!")

    elif user_choice == 3:
        anime_search=input("search: ").lower()
        with open("anime.txt", "r") as file:
            line=file.readlines()
            line=[word.strip() for word in line]
        if anime_search in line:
            print("anime found!")
        else:
            print("anime not found!")

    elif user_choice == 4:
        with open("anime.txt", "r") as file:
            anime_list=file.readlines()
            anime_list2=[name.strip().title() for name in anime_list]
            for x, name in enumerate(anime_list2, start=1):
                print(f"{x}-{name}\n")

    elif user_choice == 5:
        print("Goodbye!")
        break