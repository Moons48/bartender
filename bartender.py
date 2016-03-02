"""
    I got a bit out of hand with the prompt and made a whole bar scene.
        I am having problems with the drinkMaker and customMenu functions"""
    
recipes = {
        "Rusty Nail": ["scotch","drambuie"],
        "Tom Collins":["gin", "lemon", "lemon juice", "simple Syrup", "club soda", "orange", "cherry"],
        "Greyhound": ["vodka", "grapefruit juice"],
        "Bloody Mary": ["vodka", "tomato juice", "worcestershire sauce", "tabasco", "salt", "pepper"],
        "Cosmopolitan":["vodka", "cointreau", "lime", "cranberry"],
            }
 
cost = {
    "Cocktails":{
        "Rusty Nail":6,
        "Tom Collins":8,
        "Greyhound": 5,
         "Bloody Mary": 5,
         },
     "Beer":{
        "Yuengling": 4,
        "Bud Light": 3,
        "Bud Heavy": 4,
        },
    "Wine":{
        "Merlot": 6,
        "Pinot Noir":6,
        "Mad Dog 20/20": 2,
    }}

userMenu = {} #This is the custom list created based on the users drink preferences
regularsDrinks = {} #These are the drinks drank by regulars
customertab={} #This is each customers running tab
name = "" #global name variable
   
def drinkRequest():
    """Greets patron. If recurring patron, asks if they want what they got last time"""
    print "Hey there, pal. What's your name?"
    global name
    name = raw_input()
    if name not in regularsDrinks:
        print "Alrighty then %s" %name
        menu()
    elif name in regularsDrinks:
        print "Hello again, "+ name +"\nIn the mood for another "+ regularsDrinks[name]+ " today?"
        order = raw_input()
        if order.lower() == "yes":
            print "Another %s coming right at you!" %(regularsDrinks[name])
            costCalc(regularsDrinks[name])
        else:
            print "Alrighty then"
            menu()

def menu():
    """prints menu items"""
    global name
    menuPrint = raw_input("Would you like to see our menu? ")
    if menuPrint.lower() == "yes":
        for k, v in cost.items():
            print "\n"+k+":"
            for k,v in v.items():
                print "\t" + k + "\t" + "$" + str(v)
        selector()
    elif menuPrint == "no":
        print "Ok"
        selector()
    else:
        for k, v in cost.items():
            print "\n"+k+":"
            for k,v in v.items():
                print "\t" + k + "\t" + "$" + str(v)
        selector()

        
def selector():
    """Lets patron choose drink or create custom drink
        This is where I am having trouble. Had it working at one pt, didnt commit it and messed it up"""
    choice = raw_input("Do you know what you want? If not, type 'custom' to make a drink tailored to your tastes\n")
    if choice.lower() == "yes":
        order = raw_input("Lay it on me\n")
        for k, v in cost.items():
            for d, p in v.items():
                if order in v:
                    costCalc(order)
    elif choice.lower() == "custom":
        drinkMaker()
    else:
        for k, v in cost.items():
            for d, p in v.items():
                if choice in v:
                    costCalc(choice)

            
def drinkMaker():
    """Matches patron's input with ingredients found in recipe dict
        and returns cocktails with common ingredients"""
    print "Anything particular you want in your drink?"
    customDrink = set(raw_input().split(" ")) #ingredients in custom drink
    print customDrink
    print "Let's take a look at the menu..."
    for drink, ingred in recipes.items():
        setIngr = set(recipes[drink])
        setIngr.intersection_update(customDrink) #returns only common ingredients in userinput and recipesDict
    if len(setIngr) >= 1:
        userMenu.setdefault(setIngr, recipes[drink]) #Custom list that contains drink preferences
        customMenu()
    elif len(setIngr) == 0: 
        print "Hmmm you've got interesting tastes...\nWe actually don't have any drinks with those ingredients"
        print "Let's start over"
        selector()
        
   
def customMenu():
    """Prints out items that match patron's taste"""
    global name
    print "Great! Looks like we found a few cocktails for you:\n"
    for k, v in userMenu.items():
        print k
    selection = raw_input("So which one would you like?\n")
    try: 
        for k, v in cost.items():
            for d, p in v.items():
                if selection in v:
                    costCalc(selection)
    except KeyError:
        print "I don't see that on the menu..."
        selector()
    
def costCalc(drink):
    """User pays cash or credit.
        If user has tab, bill added to tab. If not, tab is created for user and bill is added"""
    global name
    regularsDrinks.setdefault(name, drink)
    for k, v in cost.items():
        if drink in v:
            drinkCost = v[drink]
    print "That'll be %s" %drinkCost
    cashCred = raw_input("Do you want to pay with cash or credit?")
    
    if cashCred.lower() == "cash":
        print "Great. Thanks! Have a great night!"
        print "Who's next?"
        drinkRequest()
    
    elif cashCred.lower() == "credit":
        tab = raw_input("Do you have a tab open?")
        if tab.lower() == "no":
            tabname = raw_input("Whats your name again?")
            customertab.setdefault(tabname.lower(), {drink:drinkCost})
            print "Alright. I'll add %s dollars to the %s tab" %(drinkCost, tabname)
            print "Who's next?"
            drinkRequest()
        elif tab.lower() == "yes":
            tabname = raw_input("Whats the name?")
            if tabname in customertab:
                customertab[tabname] += {drink:drinkCost} #how do I add dictionary items to a dict of dicts
                print "Alright. I'll add %s dollars to the %s tab" %(drinkCost, tabname)
                print "Who's next?"
                drinkRequest()
            elif tabname not in customertab:
                print "I don't see that tab, but I'll add %s dollars to the newly opened %s tab" %(drinkCost, name)
                customertab.setdefault(name, {drink:drinkCost})
                print "Who's next?"
                drinkRequest()
                
        else:
            print "I don't see that tab, I'll add %s dollars to the %s tab" %(drinkCost, name)
            customertab.setdefault(name, {drink:drinkCost})
            print "Who's next?"
            drinkRequest()
        

drinkRequest()