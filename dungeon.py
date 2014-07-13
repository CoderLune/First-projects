#!/usr/bin/env python3
gobblin_attack = 40
gobblin1_alive = True
gobblin2_alive = True
gobblins_alive = 2
gobblin1_stunned = False
gobblin2_stunned = False
gobblin1_health = 30
gobblin2_health = 30
rat_alive = True
rat_health = 15
fists = True
sword = False
shield = False
armor = False
end = False
room = 1
defense = 0 
health = 50
weapon = 10
emerald = False
emerald_bribe = False
rope_cut = False

print("Welcome to the Poorly-Coded-Dungeon!")
print("What is your name, player?")
player = input("> ")
print("Well,", player, "you start...IN A DUNGEON!! (big surprise)")
while not end:
#starting room
  if room == 1:
    print("What do you want to do?")
    action = input("> ")
    if action == "look around":
      if sword:
        print("Looking around, there is nothing else of interest; just a way in either direction.")
      else:
        print("Looking around, you spot a sword. There are also ways out going in any direction.")
    elif action == "grab sword":
        print("You grab the sword and equip it.")
        sword = True
        weapon += 5
    elif action == "take sword":
        print("You take and equip the sword.")
        sword = True
        weapon += 5
    elif action == "help":
        print("Your commands are 'look around', 'move forward', 'move left', 'move right', 'move back', 'stats', 'take *item*', 'inspect *item and/or monster*,  and 'attack *monster name*'")
    elif action == "stats":
        print("Health:", health, "Attack:", weapon, "Defense:", defense)
    elif action == "move forward":
        print("You move forward.")
        print("This room is empty. There is only a way forwards and the way you came.")
        print("The way forwards leads outside!")
        print("You hear some chattering in the distance.")
        room = 2
    elif action == "move back":
        print("You move back.")
        print("This room is filled with a lot of discarded items.")
        room = 3
    elif action == "move left":
        print("You move to the left.")
        print("You spring a trap!")
        health -= 5
        print("Don't you know anything about scrolling videogames?")
        print("Always go to the RIGHT!")
        print("Also, you're not alone in here.")
        room = 4
    elif action == "move right":
        print("You move to the right.")
        room = 5
        if emerald == False:
          if rope_cut == True:
            print("This room is mostly empty, save for an emerald that you left in the dead-center of the room")
            print("You could easily grab this emerald now.")
          else:
            print("This room is mostly empty, save for an emerald in the dead-center of the room.")
        else:
          print("This room is completely empty now. Nothing left of interest.")
    else:
      print("Sorry, try a different command.")

#Room 2
  if room == 2:
    print("What do you want to do?")
    action = input("> ")
    if action == "move back":
      print("You move back to the starting room")
      room = 1
    elif action == "move forward":
      print("You move forwards, outside of the dungeon! It's dark outside.")
      room = 6
      if gobblins_alive == 2:
        if emerald == True:
          print("It seems the chattering you heard was two gobblins! They spot you and wield their weapons!")
          print("They are about to step forward to attack, but suddenly stop, noticing your shiny emerald.")
        else:
          print("It seems the chattering you heard was two gobblins! They spot you and wield their weapons!")
      else:
        print("There is nothing left in this room.")
    else:
      print("Sorry, try a different command.")

#Room 3
  if room == 3:
    print("What do you want to do?")
    action = input("> ")
    if action == "search items":
      print("Searching through the rabble, you find a shield!")
      print("Take shield with you?")
      action = input("(yes/no) ")
      if action == "yes":
        print("You take the shield and put it on")
        defense += 10
        shield = True
      else:
        print("You leave the shield as it is.") 
    elif action == "inspect items":
      print("Searching through the rabble, you find a shield!")
      print("Take shield with you?")
      action = input("> ")
      if action == "yes":
        print("You take the shield and put it on")
        defense += 10
        shield = True
      else:
        print("You leave the shield as it is.") 
    elif action == "move forward":
      print("You go back to the starting room.")
      room = 1
    elif action == "look around":
      print("Several unuseable items are thrown about all over the place.")
      print("Who knows why for.")
      print("There may be a chance some of it may be useable, but you'd have to get your hands dirty and search.") 
    else:
      print("I'm sorry, please try a different command.")

# Room 4
  if room == 4:
    print("What do you want to do?")
    action = input("> ")
    if action == "look around":
      if rat_alive == True:
        print("You spot a giant rat!")
        print("Or rather, he spots you!")
        print("Why, oh WHY does EVERY MMORPG start you off killing rats for experience!?")
        print("This rat has", rat_health, "health")
      else:
        print("With the rat dead, you see he was guarding something shiny")
        print("Inspect shiny?")
        action = input("> ")
        if action == "yes":
          print("It's a plate of armor!")
          print("Take with you?")
          action = input("> ")
          if action == "yes":
            print("You take the armor with you!")
            armor = True
            defense += 20
          else:
            print("You leave the armor be")
        else:
          print("You leave shiny be. Could have been something heavy anyway.")
    elif action == "attack rat":
      print("You strike at the rat!")
      if sword == True:
        print("In one mighty blow, you take off it's head!")
        rat_alive = False
        rat_health = 0
        print("You get the sense that the rat was guarding something.")
      else:
        print("You hit the rat with your fist! The rat takes damage!")
        rat_health -= 5
        if rat_health == 0:
          print("The rat is dead!")
          rat_alive = False
          print("You get the sense that the rat was guarding something.")
        else:
          print("The rat fights back! Gnawing at your injured foot!")
          health -= 5
          if health <= 0:
            print("You have died!")
            print("---GAME OVER---")
            end = True
    elif action == "inspect rat":
       print("The rat's health is", rat_health)
    elif action == "stats":
      print("Health:", health, "Attack:", weapon, "Defense:", defense)
    elif action == "move back":
      if rat_alive == True:
        print("You start to move back, but the rat prevents escape and attacks!")
        health -=10
        if health <= 0:
          print("You have died!")
          print("---GAME OVER---")
          end = True
      else:
        print("You move back.")
        room = 1
    else:
      print("Sorry, please try a different command.")

#Room 5
  if room == 5:
    print("What would you like to do?")
    action = input("> ")
    if action == "take emerald":
      if emerald == True:
        print("There is no emerald, you took it already.")
        print("Greedy.")
      else:
        if rope_cut == True:
          print("You easily take the emerald you left here earlier")
          emerald = True
        else:
          print("You attempt to take the emerald, but find that it pulls a rope in the ground.")
          print("The floor gives way and you fall down an endless pit")
          print("Congratulations, you now have eternity to think on how your greed was the end of you!")
          print("---GAME OVER---")
          end = True
    elif action == "inspect emerald":
      if emerald == True:
        print("There is no emerald, you took it already.")
        print("You're just full of greed, aren't ya?")
      else:
        if rope_cut == True:
          print("What's there to inspect? It's just the emerald you left here earlier.")
        else:
          print("Upon inspection, you see that there is a rope attatched to the bottom of the emerald.")
          print("Try to cut rope?")
          answer = input("(yes/no)  ")
          if answer == "yes":
            if sword == True:
              print("You take your sword and Cut the Rope! The emerald is free!")
              rope_cut = True
              print("Take emerald?")
              choice = input("(yes/no)  ")
              if choice == "no":
                print("Well, that seemed rather pointless then.")
              elif choice == "yes":
                print("You take the emerald with you.")
                emerald = True
              else:
                print("How difficult is it to type in 'yes' or 'no'?")
            else:
              print("You try with all your might, but you can't Cut the Rope!")
          elif answer == "no":
            print("Alright....you leave it as it is.")
          else:
            print("Your options are 'yes' and 'no'. No more have been coded in")
    elif action == "move back":
      print("You move back")
      room = 1
    elif action== "stats":
      print("Health:", health, "Attack", attack, "Defense", defense)
    else:
      print("Sorry, try another command.")


#Room 6
  if room == 6:
    print("What do you want to do?")
    action = input("> ")
    if action == "attack gobblin":
      if gobblin1_alive == False:
        if gobblin2_alive == False:
          print("There are no more gobblins alive.")
          print("You killed them both.")
          gobblins_alive = 0
          room = 7
        else:
          print("You attack the second gobblin!")
          room = 9
      elif gobblin2_alive == False:
        if gobblin1_alive == False:
          print("There are no more gobblins alive.")
          print("You killed them both.")
          gobblins_alive = 0
          room = 7
        else:
          print("You attack the first gobblin!")
          room = 10
      else:
        print("Which Gobblin?")
        choice = input("1/2: ")
        if choice == "1":
          print("Attack Gobblin", choice, "with what?")
          choice2 = input("shield/weapon: ")
          if choice2 == "shield":
            if shield == True:
              print("You bash the first gobblin with your shield!")
              print("Gobblin", choice, "takes 1 damage!")
              gobblin1_health -=1
              print("Gobblin", choice, "is stunned!")
              gobblin1_stunned = True
              if gobblin2_alive == True:
                if gobblin2_stunned == True:
                  print("The second gobblin skips out on attacking and regains control!")
                  print("The second gobblin is no longer stunned!")
                  gobblin2_stunned = False
                else:
                  print("The second gobblin attacks!")
                  if defense == 30:
                    print("The gobblin hits you for 10 damage!")
                    health -=10
                    if health <= 0:
                      print("The gobblin killed you!")
                      print("You have died!")
                      print("---GAME OVER---")
                      end = True
                  elif defense == 20:
                    print("The gobblin hits you for 20 damage!")
                    health -= 20
                    if health <= 0:
                      print("The gobblin killed you!")
                      print("You have died!")
                      print("---GAME OVER---")
                      end = True
                  elif defense == 10:
                    print("The gobblin hits you for 30 damage!")
                    health -= 30
                    if health <= 0:
                      print("The gobblin killed you!")
                      print("You have died!")
                      print("---GAME OVER---")
                      end = True
                  else:
                    print("The gobblin hits you full force!")
                    health -= 40
                    if health <= 0:
                      print("The gobblin killed you!")
                      print("You have died!")
                      print("---GAME OVER---")
                      end = True                        
              else:
                print("Get ready for the next round!")
            else:
              print("You don't have the shield!")
          elif choice2 == "weapon":
            print("You take your weapon and strike at the first gobblin!")
            gobblin1_health -= weapon
            if gobblin1_health <= 0:
              print("The first gobblin died!")
              gobblin1_alive = False
              if gobblin2_alive == False:
                print("You've killed both gobblins!")
                gobblins_alive = 0
                room = 7
              else:
                gobblins_alive = 1
            elif gobblin1_stunned == False:
              print("The gobblin fights back!")
              if defense == 30:
                print("The gobblin hits you for 10 damage!")
                health -=10
                if health <= 0:
                  print("The gobblin killed you!")
                  print("You have died!")
                  print("---GAME OVER---")
                  end = True
                elif gobblin2_alive == False:
                  print("Get ready for the next round!")
                else:
                  if gobblin2_stunned == True:
                    print("The second gobblin skips out on attacking and regains control!")
                    print("The second gobblin is no longer stunned!")
                  else:
                    print("The second gobblin attacks!")
                    if defense == 30:
                      print("The gobblin hits you for 10 damage!")
                      health -=10
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True
                    elif defense == 20:
                      print("The gobblin hits you for 20 damage!")
                      health -= 20
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True
                    elif defense == 10:
                      print("The gobblin hits you for 30 damage!")
                      health -= 30
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True
                    else:
                      print("The gobblin hits you full force!")
                      health -= 40
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True                        
              elif defense == 20:
                print("The gobblin hits you for 20 damage!")
                health -= 20
                if health <= 0:
                  print("The gobblin killed you!")
                  print("You have died!")
                  print("---GAME OVER---")
                  end = True
                elif gobblin2_alive == False:
                  print("Get ready for the next round!")
                else:
                  if gobblin2_stunned == True:
                    print("The second gobblin skips out on attacking and regains control!")
                    print("The second gobblin is no longer stunned!")
                  else:
                    print("The second gobblin attacks!")
                    if defense == 30:
                      print("The gobblin hits you for 10 damage!")
                      health -=10
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True
                    elif defense == 20:
                      print("The gobblin hits you for 20 damage!")
                      health -= 20
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True
                    elif defense == 10:
                      print("The gobblin hits you for 30 damage!")
                      health -= 30
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True
                    else:
                      print("The gobblin hits you full force!")
                      health -= 40
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True                        
              elif defense == 10:
                print("The gobblin hits you for 30 damage!")
                health -= 30
                if health <= 0:
                  print("The gobblin killed you!")
                  print("You have died!")
                  print("---GAME OVER---")
                  end = True
                elif gobblin2_alive == False:
                  print("Get ready for the next round!")
                else:
                  if gobblin2_stunned == True:
                    print("The second gobblin skips out on attacking and regains control!")
                    print("The second gobblin is no longer stunned!")
                  else:
                    print("The second gobblin attacks!")
                    if defense == 30:
                      print("The gobblin hits you for 10 damage!")
                      health -=10
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True
                    elif defense == 20:
                      print("The gobblin hits you for 20 damage!")
                      health -= 20
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True
                    elif defense == 10:
                      print("The gobblin hits you for 30 damage!")
                      health -= 30
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True
                    else:
                      print("The gobblin hits you full force!")
                      health -= 40
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True                        
              else:
                print("The gobblin hits you full force!")
                health -= 40
                if health <= 0:
                  print("The gobblin killed you!")
                  print("You have died!")
                  print("---GAME OVER---")
                  end = True          
                elif gobblin2_alive == False:
                  print("Get ready for the next round!")
                else:
                  if gobblin2_stunned == True:
                    print("The second gobblin skips out on attacking and regains control!")
                    print("The second gobblin is no longer stunned!")
                  else:
                    print("The second gobblin attacks!")
                    if defense == 30:
                      print("The gobblin hits you for 10 damage!")
                      health -=10
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True
                    elif defense == 20:
                      print("The gobblin hits you for 20 damage!")
                      health -= 20
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True
                    elif defense == 10:
                      print("The gobblin hits you for 30 damage!")
                      health -= 30
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True
                    else:
                      print("The gobblin hits you full force!")
                      health -= 40
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True                        
            else:
              print("The first gobblin skips out on attacking and regains control!")
              print("The first gobblin is no longer stunned!")
              gobblin1_stunned = False
              if gobblin2_alive == False:
                print("Get ready for the next round!")
              else:
                if gobblin2_stunned == True:
                  print("The second gobblin skips out on attacking and regains control!")
                  print("The second gobblin is no longer stunned!")
                else:
                  print("The second gobblin attacks!")
                  if defense == 30:
                    print("The gobblin hits you for 10 damage!")
                    health -=10
                    if health <= 0:
                      print("The gobblin killed you!")
                      print("You have died!")
                      print("---GAME OVER---")
                      end = True
                    elif defense == 20:
                      print("The gobblin hits you for 20 damage!")
                      health -= 20
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True
                    elif defense == 10:
                      print("The gobblin hits you for 30 damage!")
                      health -= 30
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True
                    else:
                      print("The gobblin hits you full force!")
                      health -= 40
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True                                  
        elif choice == "2":
          print("Attack Gobblin", choice, "with what?")
          choice2 = input("shield/weapon: ")
          if choice2 == "shield":
            if shield == True:
              print("You bash the second gobblin with your shield!")
              print("Gobblin", choice, "takes 1 damage!")
              gobblin2_health -=1
              print("Gobblin", choice, "is stunned!")
              gobblin2_stunned = True
              if gobblin1_alive == True:
                if gobblin1_stunned == True:
                  print("The first gobblin skips out on attacking and regains control!")
                  print("The first gobblin is no longer stunned!")
                  gobblin1_stunned = False
                else:
                  print("The first gobblin attacks!")
                  if defense == 30:
                    print("The gobblin hits you for 10 damage!")
                    health -=10
                    if health <= 0:
                      print("The gobblin killed you!")
                      print("You have died!")
                      print("---GAME OVER---")
                      end = True
                  elif defense == 20:
                    print("The gobblin hits you for 20 damage!")
                    health -= 20
                    if health <= 0:
                      print("The gobblin killed you!")
                      print("You have died!")
                      print("---GAME OVER---")
                      end = True
                  elif defense == 10:
                    print("The gobblin hits you for 30 damage!")
                    health -= 30
                    if health <= 0:
                      print("The gobblin killed you!")
                      print("You have died!")
                      print("---GAME OVER---")
                      end = True
                  else:
                    print("The gobblin hits you full force!")
                    health -= 40
                    if health <= 0:
                      print("The gobblin killed you!")
                      print("You have died!")
                      print("---GAME OVER---")
                      end = True                        
              else:
                print("Get ready for the next round!")
            else:
              print("You don't have the shield!")
          elif choice2 == "weapon":
            print("You take your weapon and strike at the second gobblin!")
            gobblin2_health -= weapon
            if gobblin2_health <= 0:
              print("The second gobblin died!")
              gobblin2_alive = False
              if gobblin1_alive == False:
                print("You've killed both gobblins!")
                gobblins_alive = 0
                room = 7
              else:
                gobblins_alive = 1
            elif gobblin2_stunned == False:
              print("The gobblin fights back!")
              if defense == 30:
                print("The gobblin hits you for 10 damage!")
                health -=10
                if health <= 0:
                  print("The gobblin killed you!")
                  print("You have died!")
                  print("---GAME OVER---")
                  end = True
                elif gobblin1_alive == False:
                  print("Get ready for the next round!")
                else:
                  if gobblin1_stunned == True:
                    print("The first gobblin skips out on attacking and regains control!")
                    print("The first gobblin is no longer stunned!")
                  else:
                    print("The first gobblin attacks!")
                    if defense == 30:
                      print("The gobblin hits you for 10 damage!")
                      health -=10
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True
                    elif defense == 20:
                      print("The gobblin hits you for 20 damage!")
                      health -= 20
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True
                    elif defense == 10:
                      print("The gobblin hits you for 30 damage!")
                      health -= 30
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True
                    else:
                      print("The gobblin hits you full force!")
                      health -= 40
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True                        
              elif defense == 20:
                print("The gobblin hits you for 20 damage!")
                health -= 20
                if health <= 0:
                  print("The gobblin killed you!")
                  print("You have died!")
                  print("---GAME OVER---")
                  end = True
                elif gobblin1_alive == False:
                  print("Get ready for the next round!")
                else:
                  if gobblin1_stunned == True:
                    print("The first gobblin skips out on attacking and regains control!")
                    print("The first gobblin is no longer stunned!")
                  else:
                    print("The first gobblin attacks!")
                    if defense == 30:
                      print("The gobblin hits you for 10 damage!")
                      health -=10
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True
                    elif defense == 20:
                      print("The gobblin hits you for 20 damage!")
                      health -= 20
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True
                    elif defense == 10:
                      print("The gobblin hits you for 30 damage!")
                      health -= 30
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True
                    else:
                      print("The gobblin hits you full force!")
                      health -= 40
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True                        
              elif defense == 10:
                print("The gobblin hits you for 30 damage!")
                health -= 30
                if health <= 0:
                  print("The gobblin killed you!")
                  print("You have died!")
                  print("---GAME OVER---")
                  end = True
                elif gobblin1_alive == False:
                  print("Get ready for the next round!")
                else:
                  if gobblin1_stunned == True:
                    print("The first gobblin skips out on attacking and regains control!")
                    print("The first gobblin is no longer stunned!")
                  else:
                    print("The first gobblin attacks!")
                    if defense == 30:
                      print("The gobblin hits you for 10 damage!")
                      health -=10
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True
                    elif defense == 20:
                      print("The gobblin hits you for 20 damage!")
                      health -= 20
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True
                    elif defense == 10:
                      print("The gobblin hits you for 30 damage!")
                      health -= 30
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True
                    else:
                      print("The gobblin hits you full force!")
                      health -= 40
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True                        
              else:
                print("The gobblin hits you full force!")
                health -= 40
                if health <= 0:
                  print("The gobblin killed you!")
                  print("You have died!")
                  print("---GAME OVER---")
                  end = True          
                elif gobblin1_alive == False:
                  print("Get ready for the next round!")
                else:
                  if gobblin1_stunned == True:
                    print("The first gobblin skips out on attacking and regains control!")
                    print("The first gobblin is no longer stunned!")
                  else:
                    print("The first gobblin attacks!")
                    if defense == 30:
                      print("The gobblin hits you for 10 damage!")
                      health -=10
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True
                    elif defense == 20:
                      print("The gobblin hits you for 20 damage!")
                      health -= 20
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True
                    elif defense == 10:
                      print("The gobblin hits you for 30 damage!")
                      health -= 30
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True
                    else:
                      print("The gobblin hits you full force!")
                      health -= 40
                      if health <= 0:
                        print("The gobblin killed you!")
                        print("You have died!")
                        print("---GAME OVER---")
                        end = True                        
            else:
              print("The second gobblin skips out on attacking and regains control!")
              print("The second gobblin is no longer stunned!")
              gobblin2_stunned = False
              if gobblin1_alive == False:
                print("Get ready for the next round!")
              else:
                if gobblin1_stunned == True:
                  print("The first gobblin skips out on attacking and regains control!")
                  print("The first gobblin is no longer stunned!")
                else:
                  print("The first gobblin attacks!")
                  if defense == 30:
                    print("The gobblin hits you for 10 damage!")
                    health -=10
                    if health <= 0:
                      print("The gobblin killed you!")
                      print("You have died!")
                      print("---GAME OVER---")
                      end = True
                  elif defense == 20:
                    print("The gobblin hits you for 20 damage!")
                    health -= 20
                    if health <= 0:
                      print("The gobblin killed you!")
                      print("You have died!")
                      print("---GAME OVER---")
                      end = True
                  elif defense == 10:
                    print("The gobblin hits you for 30 damage!")
                    health -= 30
                    if health <= 0:
                      print("The gobblin killed you!")
                      print("You have died!")
                      print("---GAME OVER---")
                      end = True
                  else:
                    print("The gobblin hits you full force!")
                    health -= 40
                    if health <= 0:
                      print("The gobblin killed you!")
                      print("You have died!")
                      print("---GAME OVER---")
                      end = True                        
          else:
            print("Sorry, please type 'weapon' or 'shield'")
        else:
          print("Sorry, please type '1' or '2'")
    elif action == "inspect gobblin":
      print("Which gobblin?")
      choice = input("1/2  ")
      if choice == "1":
        print("The first gobblin's health is:", gobblin1_health)
      elif choice == "2":
        print("The second gobblin's health is:", gobblin2_health)
      else:
        print("Sorry, please choose '1' or '2'")
    elif action == "stats":
      print("Health:", health, "Attack:", weapon, "Defense:", defense)
    elif action == "inspect gobblin 1":
      print("The first gobblin's health is:", gobblin1_health)
    elif action == "inspect gobblin 2":
      print("The second gobblin's health is:", gobblin2_health)
    elif action == "bribe gobblins":
      if emerald == True:
        print("You wave your pretty emerald in front of their greedy little faces, they are entranced by it's beauty.")
        print("Throw emerald at them?")
        action2 = input("(yes/no) ")
        if action2 == "yes":
          print("You throw the emerald at them and they immediately jump for it!")
          print("One of them grabs it and the other starts fighting for it.")
          print("It seems whoever has the emerald tries running from the other.")
          print("Soon enough, both gobblins are gone, and the fighting continues elsewhere.")
          print("You are safe, and both gobblins are gone!")
          gobblins_alive = 0
          gobblin1_alive = False
          gobblin2_alive = False
          emerald = False
          emerald_bribe = True
          room = 7
        elif action2 == "no":
          print("Turns out, flashing the emerald at them wasn't such a good idea.")
          print("They jump for it, scratching, clawing, biting, and slicing at you until it's in their grasp.")
          print("Through their determination, speed, and the fact that they are both on you, you are unable to attack or push them back.")
          print("They soon realize that you are the one holding the emerald up and slice your throat.")
          print("With you dead, the gobblins take the emerald and fight over it themselves, running from one another when it is in their grasp.")
          print("The gobblins have killed you!")
          print("You have died!")
          print("---GAME OVER---")
          end = True
        else:
          print("I don't know what you typed in...the coder didn't put any other options, sooo...")
      else:
        print("You don't have anything they want!")
    elif action == "look around":
      print("What do you want? There are gobblins in front of you! Nothing to aid your combat either!")
    elif action == "move back":
      print("You can't escape!")
    else:
      print("You don't have any other options, just follow the script.")
#Room 7
  if room == 7:
    if emerald_bribe == True:
      print("Well, you survived the cave, got a cool sword, bribed the gobblins, and are here alive!")
      print("But is that really all there is to this game? Is there any more? What happens next?")
      print("Just as you ask yourself these questions, you hear leaves rustling in the distance.")
      print("Investigate?")
      action = input("(yes/no) ")
      if action == "yes":
        print("You move forward to investigate...")
        room = 8
      elif action == "no":
        print("Okay....there's nothing left to do here...soo.....The end I guess?")
        print("You decide to stand around for eternity!")
        print("Turns out that you need things like food, water, movement, etc. to live!")
        print("You have died!")
        print("---GAME OVER---")
        end = True
    elif emerald == True:
      print("Well, you survived the cave, got a shiny emerald, defeated two gobblins, and are here alive!")
      print("But is that really all there is to this game? Is there any more? What happens next?")
      print("Just as you ask yourself these questions, you hear leaves rustling in the distance.")
      print("Investigate?")
      action = input("(yes/no) ")
      if action == "yes":
        print("You move forward to investigate...")
        room = 8
      elif action == "no":
        print("Okay....there's nothing left to do here...soo.....The end I guess?")
        print("You decide to stand around for eternity!")
        print("Turns out that you need things like food, water, movement, etc. to live!")
        print("You have died!")
        print("---GAME OVER---")
        end = True
    else:
      print("Well, you survived the cave, defeated two gobblins, and are here alive!")
      print("But is that really all there is to this game? Is there any more? What happens next?")
      print("Just as you ask yourself these questions, you hear leaves rustling in the distance.")
      print("Investigate?")
      action = input("(yes/no) ")
      if action == "yes":
        print("You move forward to investigate...")
        room = 8
      elif action == "no":
        print("Okay....there's nothing left to do here...soo.....The end I guess?")
        print("You decide to stand around for eternity!")
        print("Turns out that you need things like food, water, movement, etc. to live!")
        print("You have died!")
        print("---GAME OVER---")
        end = True

#Room 8 Final room
  if room == 8:
    print("The path goes on and it gets brighter and brighter. Before long, you have to shield your eyes.")
    print("By the time the path stops you can barely see anything. Suddenly, all the lights turn dim enough for you to be able to see.")
    print("It takes a few moments, of course, for your eyes to adjust. When they do, you finally see that...")
    print("before you stands a creature of Light! It is completely white, save for it's golden-yellow eyes!")
    print("It takes you a few moments more to realize that this creature looks exactly like you!")
    print("Save for the fact that it's made out of Light, of course.")
    print("It simply stares menacingly at you. Almost as if expecting you to do something.")
    print("Provoke the creature?")
    answer = input("(yes/no) ")
    if answer == "yes":
      print("Immediately, you are lifted in the air; your Light doppleganger simply stares at you as you flail around.")
      print("Suddenly, everything ends. The last thing you hear is a deep male voice coming from behind you, saying only...")
      print("'You shouldn't have done that.'")
      print("---GAME OVER---")
      end = True
    elif answer == "no":
      print("You decide against attacking the Light creature; it /is/ quite the good looking person, if you do say so yourself.")
      print("A deep male voice speaks from behind you; saying 'You are very wise,", player,"'")
      print("Turning around, you see a tall, pale man dressed in a formal, victorian era, suit, wearing his overcoat like a cape.")
      print("The man speaks: 'The final battle with the gobblins already got this poorly-coded game past 1000 lines of code.'")
      print("'If The Creator had simply known what he was doing, we may have had a good run, this game.'")
      print("'But there is still a chance that The Creator will make another, more decently coded, game...'")
      print("'Should that occur, we may meet again. Until then...consider this game 'won' '")
      print("The man lifts his arm, saying: 'Congratulations,", player,"'")
      print("The man snaps his fingers. Both him and your doppleganger vanish!")
      print("Congratulations! You have beaten the game!!")
      print("---GAME OVER---")
      end = True
    else:
      print("A deep male voice comes from behind you, saying 'I will take none of your nonsense!'")
      print("Suddenly, everything stops.")
      print("The last thing you hear is that voice, saying 'You shouldn't have done that!'")
      print("You have died!")
      print("---GAME OVER---")
      end = True
#Room 9 (gobblin 2 attack)
  if room == 9:
    print("Attack the second gobblin with what?")
    choice2 = input("shield/weapon: ")
    if choice2 == "shield":
      if shield == True:
        print("You bash the second gobblin with your shield!")
        print("Gobblin 2 takes 1 damage!")
        gobblin2_health -=1
        print("Gobblin 2 is stunned!")
        gobblin2_stunned = True
      else:
        print("You don't have the shield!")
    elif choice2 == "weapon":
      print("You take your weapon and strike at the second gobblin!")
      gobblin2_health -= weapon
      if gobblin2_health <= 0:
        print("The second gobblin died!")
        gobblin2_alive = False
        if gobblin1_alive == False:
          print("You've killed both gobblins!")
          gobblins_alive = 0
          room = 7
        else:
          gobblins_alive = 1
      elif gobblin2_stunned == False:
        print("The gobblin fights back!")
        if defense == 30:
          print("The gobblin hits you for 10 damage!")
          health -=10
          if health <= 0:
            print("The gobblin killed you!")
            print("You have died!")
            print("---GAME OVER---")
            end = True
        elif defense == 20:
          print("The gobblin hits you for 20 damage!")
          health -= 20
          if health <= 0:
            print("The gobblin killed you!")
            print("You have died!")
            print("---GAME OVER---")
            end = True
        elif defense == 10:
          print("The gobblin hits you for 30 damage!")
          health -= 30
          if health <= 0:
            print("The gobblin killed you!")
            print("You have died!")
            print("---GAME OVER---")
            end = True
        else:
          print("The gobblin hits you full force!")
          health -= 40
          if health <= 0:
            print("The gobblin killed you!")
            print("You have died!")
            print("---GAME OVER---")
            end = True                        
      elif gobblin2_stunned == True:
        print("The gobblin skips out on attacking and regains control!")
        print("The gobblin is no longer stunned!")
        gobblin2_stunned = False
      else:
        print("Sorry, please type 'weapon' or 'shield'")


#Room 10 (gobblin 1 attack)
  if room == 10:
    print("Attack the first gobblin with what?")
    choice2 = input("shield/weapon: ")
    if choice2 == "shield":
      if shield == True:
        print("You bash the first gobblin with your shield!")
        print("Gobblin 1 takes 1 damage!")
        gobblin1_health -=1
        print("Gobblin 1 is stunned!")
        gobblin1_stunned = True
      else:
        print("You don't have the shield!")
    elif choice2 == "weapon":
      print("You take your weapon and strike at the first gobblin!")
      gobblin1_health -= weapon
      if gobblin1_health <= 0:
        print("The first gobblin died!")
        gobblin1_alive = False
        if gobblin2_alive == False:
          print("You've killed both gobblins!")
          gobblins_alive = 0
          room = 7
        else:
          gobblins_alive = 1
      elif gobblin1_stunned == False:
        print("The gobblin fights back!")
        if defense == 30:
          print("The gobblin hits you for 10 damage!")
          health -=10
          if health <= 0:
            print("The gobblin killed you!")
            print("You have died!")
            print("---GAME OVER---")
            end = True
        elif defense == 20:
          print("The gobblin hits you for 20 damage!")
          health -= 20
          if health <= 0:
            print("The gobblin killed you!")
            print("You have died!")
            print("---GAME OVER---")
            end = True
        elif defense == 10:
          print("The gobblin hits you for 30 damage!")
          health -= 30
          if health <= 0:
            print("The gobblin killed you!")
            print("You have died!")
            print("---GAME OVER---")
            end = True
        else:
          print("The gobblin hits you full force!")
          health -= 40
          if health <= 0:
            print("The gobblin killed you!")
            print("You have died!")
            print("---GAME OVER---")
            end = True                        
      elif gobblin1_stunned == True:
        print("The gobblin skips out on attacking and regains control!")
        print("The gobblin is no longer stunned!")
        gobblin1_stunned = False
      else:
        print("Sorry, please type 'weapon' or 'shield'")
