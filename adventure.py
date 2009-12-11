def scenario1():
    print "You wake up at night confused in a unknown dark room. You have no idea how you ended up in there. You are laying down in the foor with your hards tied behind your back."
    print "1) try to break loose"
    print "2) scream"
    print "3) look around for something to use"
    answer=input()
    if answer == 1:
        print "The rope is tied too tight."
        scenario1()
    elif answer == 2:
        print "A man with a hammer walks in and smashes your head. THE END!"
    elif answer == 3:
        print "You find broken glass in the floor and used it to cut the rope. You stand up and found the lights. You turned it on."
        scenario2()
    else:
        print "Answer using numbers: 1, 2, or 3"
        scenario1()

def scenario2(): 
    print "The room is bright you see everything clearly."
    print "1) escape"
    print "2) look for weapons"
    answer=input()
    if answer == 1:
        print "All the windows are barricaded and the door is lock."
        scenario2()
    elif answer == 2:
        scenario3()

def scenario3():
    print "You see a bunch of stuff in a table."
    print "1) take the flash light"
    print "2) take the knife"
    print "3) take the hammer"
    print "4) take the rock"
    print "5) take all"
    print "6) read the piece of paper"
    answer = input()
    if answer in [1,2,3,4]:
        scenario4()
    elif answer == 5:
        scenario5()
    elif answer == 6:
        print 'The piece of paper says: "RUN FOR IT!"'
        scenario3()
        
def scenario4():
    print "You hear the door open. A man comes in. It turns out it was Enrique. He has blood all over his muscular body. Your heart is beating and you start to sweat."
    print "1) Kill Enrique"
    print "2) Run for it"
    print "3) Confront him"
    answer=input() 
    if answer == 1:
        print "It turns out that Enrique is a zombie and he can't die."
    elif answer == 2:
        scenario6()
    elif answer == 3:
        print "It turns out that Enrique is a zombie. He bites you in the head and starts eating your intestines with his clean white teeth."

def scenario5():
    print "1) Kill Enrique"
    print "2) Run for it"
    answer=input()
    if answer == 1:
        print "It turns out that Enrique is a zombie and he can't die. He bites you in the head and starts eating your intestines with his clean white teeth. THE END!"
    elif answer == 2:
        print "You try to run but the weapons slowed you down and Enrique bites you in the head and starts eating your intestines with his clean white teeth. THE END!"

def scenario6():
    print "You run into a hallway and there are two doors, one in the right and one in the left."
    print "1) go to the door in the right"
    print "2) go to the door in the left"
    answer=input()
    if answer == 1:
        scenario7a()
    if answer == 2:
        scenario7b()
        
def scenario7a():
    print "In that room, Mark is laying in floor. He is tied up.
    
def scenario7b():
        
scenario1()
