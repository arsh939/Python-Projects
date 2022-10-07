# 90's kid game F.L.A.M.E.S. ~ check what's your relation with your crush

def flames_game():
    print("FLAMES GAME")

    name1 = input("Enter your name: ")
    name2 = input("Enter your crush's name: ")
    name1 = name1.lower()
    name2 = name2.lower()
    name1 = name1.replace(" ", "")
    name2 = name2.replace(" ", "")
    name1 = list(name1)
    name2 = list(name2)
    for i in name1:
        if i in name2:
            name1.remove(i)
            name2.remove(i)
    count = len(name1) + len(name2)
    flames = ["FRIENDS", "LOVE", "AFFECTION", "MARRIAGE", "ENEMY", "SISTER"]
    while len(flames) > 1:
        index = count % len(flames)
        if index == 0:
            flames.pop()
        else:
            flames = flames[index:] + flames[:index-1]
    print("Your relation with your crush is: ", flames[0])

if __name__ == "__main__":
    flames_game()
