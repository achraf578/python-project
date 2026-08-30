anime_number=int(input("how many anime do you want to add? "))

anime=[]
for i in range(anime_number):
    anime_name=input("Write the anime name: ").lower()
    anime.append(anime_name)

print("anime list:")
for name in anime:
    print(f"-{name}")

anime_search=input("search for an anime: ")
if anime_search.lower() in anime:
    print("anime found!")
else:
    print("anime not found!")