name = input("what is your name,[mr/mst]:")

answer = input("Do you went to play this game? [yes/no]:")

if answer == "yes":
    print(name,"wellcame to the interesting game")
    answer = input("do you want to go jungle or hill? [jungle/hill]:")
    if answer == "jungle":
        print("jungle is too riskey you will go there? yes/no ")
        answer = input("[yes/no]:")
        if answer == "yes":
            print("you see the hungry triger run or stray hear don't run/ run")
            answer = input("[don't run/ run]:")
            if answer == "run":
                print("you are still alive.you are so tried you need some food and water")
                answer = input("[yes/no]:")
                if answer == "yes":
                    print("do you eat apple or piza")
                    answer = input("[apple/piza]:")
                    if answer == "apple":
                        print("congatulation you life is incriese")
                        answer = input("do you go some safe place.[yes/no]:")
                        if answer == "yes":
                            print("what do you want to go now")
                            answer = input("[home/fight tiger]:")
                            if answer == "home":
                                print("now how viarical you use to go home")
                                answer = input("[car/brike]:")
                                if answer == "car":
                                    print("congatulation you are safely go home")
                                elif answer == "brike":
                                    print("bike is not safe in this forest.do you go in this bike")
                                    answer = input("[yes/no]:")
                                    if answer == "yes":
                                        print("animal has came and kill you.[game over]")
                                    elif answer == "no":
                                        print("you do go animal are kill you.[game over]")
                            elif answer == "fight tiger":
                                print("tiger was vary stong.tiger was killed you.[game over]")
                        elif answer == "no":
                            print("tiger has come on you side.tiger has been atake any time")
                    elif answer == "piza":
                        print("now this food is not good for your health")
                elif answer == "no":
                    print("your sicuation is vary hard.you will die any time ")
            elif answer == "don't run":
                print("tiger was kill you.")
        elif answer == "no":
            print("you are still alive. [congaculation you win]")
    elif answer == "hill":
        print("hill is so riskey, went you go there [yes/no] ")
        answer = input("[yes/no]:")
        if answer == "yes":
            print("you accident in the hill and die.[game over] ")
        elif answer == "no":
            print("you are alive [congaculation you win] ")
else:
    print("[game over]")
























    