#-----Imports-----
import turtle as trtl
from PIL import ImageGrab


#-----Functions-----
#This function's purpose is to change a button turtle's shape to its corresponding picture.
def draw_button(button):
    global index
    for turtle in allbuttonturtles_list:
        if button == turtle:
            index = allbuttonturtles_list.index(button)
            button.shape(allbuttonimages_list[index])
    button.showturtle()


#This function's purpose is to change a nonbutton turtle's shape to its corresponding picture.
def draw_nonbutton(nonbutton):
    global index
    for images in allnonbuttonturtles_list:
        if nonbutton == images:
            index = allnonbuttonturtles_list.index(nonbutton)
            nonbutton.shape(allnonbuttonimages_list[index])
    nonbutton.hideturtle()


#This function shows the sprinkles and hides all the other sweets from view.
def selection_sprinkles(x, y):
    global yogurt_flavor_picked
    if yogurt_flavor_picked == True:
        sprinkles_sweet.showturtle()
        wn.update()
        mochi_sweet.hideturtle()
        gummy_sweet.hideturtle()
        chocolate_sweet.hideturtle()
        get_currenttopping(sprinkles_sweet)


#This function shows the gummy and hides all the other sweets from view.
def selection_gummy(x, y):
    global yogurt_flavor_picked
    if yogurt_flavor_picked == True:
        gummy_sweet.showturtle()
        wn.update()
        mochi_sweet.hideturtle()
        chocolate_sweet.hideturtle()
        sprinkles_sweet.hideturtle()
        get_currenttopping(gummy_sweet)


#This function shows the mochi and hides all the other sweets from view.
def selection_mochi(x, y):
    global yogurt_flavor_picked
    if yogurt_flavor_picked == True:
        mochi_sweet.showturtle()
        wn.update()
        chocolate_sweet.hideturtle()
        gummy_sweet.hideturtle()
        sprinkles_sweet.hideturtle()
        get_currenttopping(mochi_sweet)


#This function shows the chocolate and hides all the other sweets from view.
def selection_chocolate(x, y):
    global yogurt_flavor_picked
    if yogurt_flavor_picked == True:
        chocolate_sweet.showturtle()
        wn.update()
        mochi_sweet.hideturtle()
        gummy_sweet.hideturtle()
        sprinkles_sweet.hideturtle()
        get_currenttopping(chocolate_sweet)


#This function shows the kiwi and hides all the other fruits from view.
def selection_kiwi(x, y):
    global yogurt_flavor_picked
    if yogurt_flavor_picked == True:
        kiwi_fruit.showturtle()
        wn.update()
        strawberry_fruit.hideturtle()
        blueberry_fruit.hideturtle()
        cherry_fruit.hideturtle()
        get_currentfruit(kiwi_fruit)


#This function shows the blueberry and hides all the other fruits from view.
def selection_blueberry(x, y):
    global yogurt_flavor_picked
    if yogurt_flavor_picked == True:
        blueberry_fruit.showturtle()
        wn.update()
        strawberry_fruit.hideturtle()
        cherry_fruit.hideturtle()
        kiwi_fruit.hideturtle()
        get_currentfruit(blueberry_fruit)


#This function shows the strawberry and hides all the other fruits from view.
def selection_strawberry(x, y):
    global yogurt_flavor_picked
    if yogurt_flavor_picked == True:
        strawberry_fruit.showturtle()
        wn.update()
        cherry_fruit.hideturtle()
        blueberry_fruit.hideturtle()
        kiwi_fruit.hideturtle()
        get_currentfruit(strawberry_fruit)


#This function shows the cherry and hides all the other fruits from view.
def selection_cherry(x, y):
    global yogurt_flavor_picked
    if yogurt_flavor_picked == True:
        cherry_fruit.showturtle()
        wn.update()
        strawberry_fruit.hideturtle()
        blueberry_fruit.hideturtle()
        kiwi_fruit.hideturtle()
        get_currentfruit(cherry_fruit)


#This function shows the original flavor and hides all the other flavors from view.
def selection_mangoflavor(x, y):
    global yogurt_flavor_picked
    if cup_picked == True:
        mango_flavor.showturtle()
        wn.update()
        strawberry_flavor.hideturtle()
        blueberry_flavor.hideturtle()
        original_flavor.hideturtle()
        get_currentflavor(mango_flavor)
        yogurt_flavor_picked = True


#This function shows the original flavor and hides all the other flavors from view.
def selection_blueberryflavor(x, y):
    global yogurt_flavor_picked
    if cup_picked == True:
        blueberry_flavor.showturtle()
        wn.update()
        strawberry_flavor.hideturtle()
        original_flavor.hideturtle()
        mango_flavor.hideturtle()
        get_currentflavor(blueberry_flavor)
        yogurt_flavor_picked = True

#This function shows the original flavor and hides all the other flavors from view.
def selection_strawberryflavor(x, y):
    global yogurt_flavor_picked
    if cup_picked == True:
        strawberry_flavor.showturtle()
        wn.update()
        original_flavor.hideturtle()
        blueberry_flavor.hideturtle()
        mango_flavor.hideturtle()
        get_currentflavor(strawberry_flavor)
        yogurt_flavor_picked = True

#This function shows the original flavor and hides all the other flavors from view.
def selection_originalflavor(x, y):
    global yogurt_flavor_picked
    if cup_picked == True:
        original_flavor.showturtle()
        wn.update()
        strawberry_flavor.hideturtle()
        blueberry_flavor.hideturtle()
        mango_flavor.hideturtle()
        get_currentflavor(original_flavor)
        yogurt_flavor_picked = True

#This function shows the leaf cup and hides all the other cups from view.
def selection_leafcup(x, y):
    global cup_picked
    leaf_cup.showturtle()
    wn.update()
    heart_cup.hideturtle()
    bubble_cup.hideturtle()
    star_cup.hideturtle()
    get_currentcup(leaf_cup)
    cup_picked = True

#This function shows the bubble cup and hides all the other cups from view.
def selection_bubblecup(x, y):
    global cup_picked
    bubble_cup.showturtle()
    wn.update()
    heart_cup.hideturtle()
    star_cup.hideturtle()
    leaf_cup.hideturtle()
    get_currentcup(bubble_cup)
    cup_picked = True

#This function shows the heart cup and hides all the other cups from view.
def selection_heartcup(x, y):
    global cup_picked
    heart_cup.showturtle()
    wn.update()
    star_cup.hideturtle()
    bubble_cup.hideturtle()
    leaf_cup.hideturtle()
    get_currentcup(heart_cup)
    cup_picked = True

#This function shows the star cup and hides all the other cups from view.
def selection_starcup(x, y):
    global cup_picked
    star_cup.showturtle()
    wn.update()
    heart_cup.hideturtle()
    bubble_cup.hideturtle()
    leaf_cup.hideturtle()
    get_currentcup(star_cup)
    cup_picked = True

#This function changes the current cup that the user picked.
def get_currentcup(cup):
    current_froyo.insert(1, cup)
    current_froyo.pop(0)

#This function changes the current flavor that the user picked.
def get_currentflavor(flavor):
    current_froyo.insert(2,flavor)
    current_froyo.pop(1)

#This function changes the current fruit that the user picked.
def get_currentfruit(fruit):
    current_froyo.insert(3,fruit)
    current_froyo.pop(2)

#This function changes the current topping that the user picked.
def get_currenttopping(topping):
    current_froyo.append(topping)
    current_froyo.pop(3)

#This function allows the sub buttons on the game to be clickable.
def click_sub_buttons():
    starcup_button.onclick(selection_starcup)
    heartcup_button.onclick(selection_heartcup)
    bubblecup_button.onclick(selection_bubblecup)
    leafcup_button.onclick(selection_leafcup)
    originalflavor_button.onclick(selection_originalflavor)
    blueberryflavor_button.onclick(selection_blueberryflavor)
    strawberryflavor_button.onclick(selection_strawberryflavor)
    mangoflavor_button.onclick(selection_mangoflavor)
    cherry_button.onclick(selection_cherry)
    blueberry_button.onclick(selection_blueberry)
    strawberry_button.onclick(selection_strawberry)
    kiwi_button.onclick(selection_kiwi)
    chocolate_button.onclick(selection_chocolate)
    mochi_button.onclick(selection_mochi)
    sprinkles_button.onclick(selection_sprinkles)
    gummy_button.onclick(selection_gummy)

#This function hides all of the cup buttons.
def hide_all_cup_buttons():
    starcup_button.hideturtle()
    heartcup_button.hideturtle()
    leafcup_button.hideturtle()
    bubblecup_button.hideturtle()

#This function hides all of the fruit buttons.
def hide_all_fruit_buttons():
    kiwi_button.hideturtle()
    strawberry_button.hideturtle()
    blueberry_button.hideturtle()
    cherry_button.hideturtle()

#This function hides all of the flavor buttons.
def hide_all_flavor_buttons():
    originalflavor_button.hideturtle()
    blueberryflavor_button.hideturtle()
    strawberryflavor_button.hideturtle()
    mangoflavor_button.hideturtle()

#This function hides all of the topping buttons.
def hide_all_topping_buttons():
    chocolate_button.hideturtle()
    mochi_button.hideturtle()
    sprinkles_button.hideturtle()
    gummy_button.hideturtle()

#This function shows the subselection buttons of the cups by drawing them and hiding all the other subselection buttons.
def selection_cup(x, y):
    for button in cupbutton_list:
        draw_button(button)
    wn.update()
    hide_all_fruit_buttons()
    hide_all_flavor_buttons()
    hide_all_topping_buttons()
    click_sub_buttons()

#This function shows the subselection buttons of the flavors by drawing them and hiding all the other subselection buttons.
def selection_flavor(x, y):
    for button in flavorbutton_list:
        draw_button(button)
    wn.update()
    hide_all_cup_buttons()
    hide_all_fruit_buttons()
    hide_all_topping_buttons()
    click_sub_buttons()

#This function shows the subselection buttons of the fruits by drawing them and hiding all the other subselection buttons.
def selection_fruit(x, y):
    for button in fruitbutton_list:
        draw_button(button)
    wn.update()
    hide_all_cup_buttons()
    hide_all_flavor_buttons()
    hide_all_topping_buttons()
    click_sub_buttons()

#This function shows the subselection buttons of the toppings by drawing them and hiding all the other subselection buttons.
def selection_topping(x, y):
    for button in toppingbutton_list:
        draw_button(button)
    wn.update()
    hide_all_cup_buttons()
    hide_all_fruit_buttons()
    hide_all_flavor_buttons()
    click_sub_buttons()

#This function exits the game and resets all progress.
def selection_x(x, y):
    wn.clear()
    set_game()

#This function takes a screenshot of the user's finished froyo.
def take_screenshot(x,y):
    for wallpaper_button in wallpaper_list:
        wallpaper_button.hideturtle()
    white_bar.hideturtle()
    save_button.hideturtle()
    x_button.hideturtle()
    #Screenshot code retrieved from medium.com
    #left,top,right,bottom
    screenshot = ImageGrab.grab(bbox=(350,50,1620,1030))
    screenshot.save("froyo.gif")
    screenshot.close()
    for wallpaper_button in wallpaper_list:
        wallpaper_button.showturtle()
    white_bar.showturtle()
    save_button.showturtle()
    x_button.showturtle()


#This function changes the wallpaper to blue.
def selection_blue(x, y):
    wn.bgpic("wallpaper_blue.gif")


#This function changes the wallpaper to yellow.
def selection_yellow(x, y):
    wn.bgpic("wallpaper_yellow.gif")

#This function changes the wallpaper to white.
def selection_white(x, y):
    wn.bgpic("wallpaper_white.gif")


#This function changes the wallpaper to pink.
def selection_pink(x, y):
    wn.bgpic("wallpaper_pink.gif")


#This function moves onto the next part of game (Where the user takes a picture of their froyo with a background of choice).
def selection_done(x, y):
    global current_froyo
    if (cup_picked == True) and (yogurt_flavor_picked == True):
        for each in allbuttonturtles_list:
            each.hideturtle()
        wn.bgpic("nopic")
        for each in current_froyo:
            each.speed(0)
            if each in cup_list:
                each.goto(0,-210)
            elif each in yogurt_list:
                each.goto(0,250)
            elif each in fruit_list:  
                if each == cherry_fruit:
                    each.goto(0,350)
                else:    
                    each.goto(0,200)
            else:
                each.goto(0,220)
        draw_nonbutton(white_bar)
        draw_button(save_button)
        for wallpaper_button in wallpaper_list:
            draw_button(wallpaper_button)
        x_button.showturtle()
        white_bar.showturtle()
        save_button.showturtle()
        white_bar.speed(0)
        blue_button.onclick(selection_blue)
        yellow_button.onclick(selection_yellow)
        white_button.onclick(selection_white)
        pink_button.onclick(selection_pink)
        save_button.onclick(take_screenshot)


#This function allows the main buttons on the game to be clickable and then calls the next function to make the sub buttons clickable.
def click_main_buttons():
    for cup in cup_list:
        draw_nonbutton(cup)
    for yogurt in yogurt_list:
        draw_nonbutton(yogurt)
    for fruit in fruit_list:
        draw_nonbutton(fruit)
    for topping in topping_list:
        draw_nonbutton(topping)
    wn.update()
    cup_button.onclick(selection_cup)
    flavor_button.onclick(selection_flavor)
    fruit_button.onclick(selection_fruit)
    topping_button.onclick(selection_topping)
    x_button.onclick(selection_x)
    done_button.onclick(selection_done)


#Sets the main selection buttons by making the new background screen and drawing the buttons on the screen, then it calls the next function to make them clickable.
def set_mainselection():
    global mainselectionbutton_list
    wn.bgpic("screen_subselection.gif")
    for button in mainselectionbutton_list:
        draw_button(button)
    wn.update()
    click_main_buttons()


#When the play button is clicked, this function runs, which clears the main menu screen and calls the next function to set the main selection buttons.
def gameplay(x,y):
    wn.clear()
    set_mainselection()


#Sets all the buttons and images to the correct coordinates, draws the play button, and makes the play button clickable.
def set_game():
    global wallpaper_img_list, wallpaper_list, blue_button, pink_button, yellow_button, white_button, save_button_img, save_button, white_bar, whitebar_img, button_blue_img, button_pink_img, button_white_img, button_yellow_img, wn, playbutton_img, xbutton_img, donebutton_img, cupbutton_img, flavorbutton_img, toppingbutton_img, fruitbutton_img, blueberrybutton_img, kiwibutton_img, cherrybutton_img, strawberrybutton_img, chocolatebutton_img, gummybutton_img, sprinklesbutton_img, mochibutton_img, bubblecupbutton_img, starcupbutton_img, leafcupbutton_img, heartcupbutton_img, mangoflavor_button_img, strawberryflavor_button_img, originalflavor_button_img, blueberryflavor_button_img, blueberry_fruit_img, kiwi_fruit_img, strawberry_fruit_img, cherry_fruit_img, chocolate_sweet_img, gummy_sweet_img, sprinkles_sweet_img, mochi_sweet_img, star_cup_img, bubble_cup_img, heart_cup_img, leaf_cup_img, mango_flavor_img, strawberry_flavor_img, blueberry_flavor_img, original_flavor_img, play_button, done_button, x_button, cup_button, flavor_button, topping_button, fruit_button, blueberry_button, strawberry_button, kiwi_button, cherry_button, mochi_button, gummy_button, sprinkles_button, chocolate_button, starcup_button, bubblecup_button, heartcup_button, leafcup_button, originalflavor_button, strawberryflavor_button, blueberryflavor_button, mangoflavor_button, blueberry_fruit, strawberry_fruit, kiwi_fruit, cherry_fruit, mochi_sweet, gummy_sweet, sprinkles_sweet, chocolate_sweet, star_cup, bubble_cup, heart_cup, leaf_cup, original_flavor, strawberry_flavor, blueberry_flavor, mango_flavor, empty, cup_picked, yogurt_flavor_picked, current_froyo, mainselectionbutton_list, cup_list, yogurt_list, fruit_list, topping_list, cupbutton_list, flavorbutton_list, fruitbutton_list, toppingbutton_list, allbuttonimages_list, allbuttonturtles_list, allnonbuttonimages_list, allnonbuttonturtles_list
    #-----Screen-----
    wn = trtl.Screen()
    wn.setup(width = 1920, height = 1080)
    wn.tracer(0)
    #-----Image Setup-----
    #-----Main buttons-----
    playbutton_img = "button_play.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(playbutton_img)
    xbutton_img = "button_exit.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(xbutton_img)
    donebutton_img = "button_done.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(donebutton_img)
    cupbutton_img = "button_cup.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(cupbutton_img)
    flavorbutton_img = "button_yogurt.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(flavorbutton_img)
    toppingbutton_img = "button_sweet.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(toppingbutton_img)
    fruitbutton_img = "button_fruit.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(fruitbutton_img)
    #-----Sub Buttons-----
    #---Fruits---
    blueberrybutton_img = "button_blueberry.gif"
    wn.setup(width=1.0, height=1.0)  
    wn.addshape(blueberrybutton_img)
    kiwibutton_img = "button_kiwi.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(kiwibutton_img)
    cherrybutton_img = "button_cherry.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(cherrybutton_img)
    strawberrybutton_img = "button_strawberry.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(strawberrybutton_img)
    #----Sweets----
    chocolatebutton_img = "button_chocolate.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(chocolatebutton_img)
    gummybutton_img = "button_gummy.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(gummybutton_img)
    sprinklesbutton_img = "button_sprinkles.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(sprinklesbutton_img)
    mochibutton_img = "button_mochi.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(mochibutton_img)
    #---Cups---
    bubblecupbutton_img = "button_cup_bubble.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(bubblecupbutton_img)
    starcupbutton_img = "button_cup_star.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(starcupbutton_img)
    leafcupbutton_img = "button_cup_leaf.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(leafcupbutton_img)
    heartcupbutton_img = "button_cup_heart.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(heartcupbutton_img)
    #---Flavors---
    mangoflavor_button_img = "button_flavor_mango.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(mangoflavor_button_img)
    strawberryflavor_button_img = "button_flavor_strawberry.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(strawberryflavor_button_img)
    originalflavor_button_img = "button_flavor_original.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(originalflavor_button_img)
    blueberryflavor_button_img = "button_flavor_blueberry.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(blueberryflavor_button_img)
    #----Wallpaper----
    button_blue_img = "button_blue.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(button_blue_img)
    button_pink_img = "button_pink.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(button_pink_img)
    button_yellow_img = "button_yellow.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(button_yellow_img)
    button_white_img = "button_white.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(button_white_img)
    #-----Non Buttons-----
    #---Fruits---
    blueberry_fruit_img = "fruit_blueberry.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(blueberry_fruit_img)
    kiwi_fruit_img = "fruit_kiwi.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(kiwi_fruit_img)
    strawberry_fruit_img = "fruit_strawberry.gif"
    wn.setup(width=2.0, height=2.0)
    wn.addshape(strawberry_fruit_img)
    cherry_fruit_img = "fruit_cherry.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(cherry_fruit_img)
    #----Sweets----
    chocolate_sweet_img = "sweet_chocolate.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(chocolate_sweet_img)
    gummy_sweet_img = "sweet_gummy.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(gummy_sweet_img)
    sprinkles_sweet_img = "sweet_sprinkles.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(sprinkles_sweet_img)
    mochi_sweet_img = "sweet_mochi.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(mochi_sweet_img)
    #---Cups---
    star_cup_img = "cup_star.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(star_cup_img)
    bubble_cup_img = "cup_bubble.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(bubble_cup_img)
    heart_cup_img = "cup_heart.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(heart_cup_img)
    leaf_cup_img = "cup_leaf.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(leaf_cup_img)
    #---Flavors---
    mango_flavor_img = "flavor_mango.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(mango_flavor_img)
    strawberry_flavor_img = "flavor_strawberry.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(strawberry_flavor_img)
    blueberry_flavor_img = "flavor_blueberry.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(blueberry_flavor_img)
    original_flavor_img = "flavor_original.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(original_flavor_img)
    #-----Additionals-----
    whitebar_img = "white_bar.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(whitebar_img)
    save_button_img = "button_save.gif"
    wn.setup(width=1.0, height=1.0)
    wn.addshape(save_button_img)
    #-----Turtle Setup-----
    #-----Buttons-----
    play_button = trtl.Turtle()
    play_button.penup()
    play_button.hideturtle()
    done_button = trtl.Turtle()
    done_button.penup()
    done_button.hideturtle()
    x_button = trtl.Turtle()
    x_button.penup()
    x_button.hideturtle()
    save_button = trtl.Turtle()
    save_button.penup()
    save_button.hideturtle()
    cup_button = trtl.Turtle()
    cup_button.penup()
    cup_button.hideturtle()
    flavor_button = trtl.Turtle()
    flavor_button.penup()
    flavor_button.hideturtle()
    fruit_button = trtl.Turtle()
    fruit_button.penup()
    fruit_button.hideturtle()
    topping_button = trtl. Turtle()
    topping_button.penup()
    topping_button.hideturtle()
    blue_button = trtl.Turtle()
    blue_button.penup()
    blue_button.hideturtle()
    yellow_button = trtl.Turtle()
    yellow_button.penup()
    yellow_button.hideturtle()
    pink_button = trtl.Turtle()
    pink_button.penup()
    pink_button.hideturtle()
    white_button = trtl.Turtle()
    white_button.penup()
    white_button.hideturtle()
    #-----Sub Buttons-----
    #---Fruits---
    blueberry_button = trtl.Turtle()
    blueberry_button.penup()
    blueberry_button.hideturtle()
    strawberry_button = trtl.Turtle()
    strawberry_button.penup()
    strawberry_button.hideturtle()
    kiwi_button = trtl.Turtle()
    kiwi_button.penup()
    kiwi_button.hideturtle()
    cherry_button = trtl.Turtle()
    cherry_button.penup()
    cherry_button.hideturtle()
    #----Sweets----
    mochi_button = trtl.Turtle()
    mochi_button.penup()
    mochi_button.hideturtle()
    gummy_button = trtl.Turtle()
    gummy_button.penup()
    gummy_button.hideturtle()
    sprinkles_button = trtl.Turtle()
    sprinkles_button.penup()
    sprinkles_button.hideturtle()
    chocolate_button = trtl.Turtle()
    chocolate_button.penup()
    chocolate_button.hideturtle()  
    #---Cups---
    starcup_button = trtl.Turtle()
    starcup_button.penup()
    starcup_button.hideturtle()
    bubblecup_button = trtl.Turtle()
    bubblecup_button.penup()
    bubblecup_button.hideturtle()
    heartcup_button = trtl.Turtle()
    heartcup_button.penup()
    heartcup_button.hideturtle()
    leafcup_button = trtl.Turtle()
    leafcup_button.penup()
    leafcup_button.hideturtle()
    #---Flavors---
    originalflavor_button = trtl.Turtle()
    originalflavor_button.penup()
    originalflavor_button.hideturtle()
    strawberryflavor_button = trtl.Turtle()
    strawberryflavor_button.penup()
    strawberryflavor_button.hideturtle()
    blueberryflavor_button = trtl.Turtle()
    blueberryflavor_button.penup()
    blueberryflavor_button.hideturtle()
    mangoflavor_button = trtl.Turtle()
    mangoflavor_button.penup()
    mangoflavor_button.hideturtle()
    #-----Non Buttons-----
    #---Fruits---
    blueberry_fruit = trtl.Turtle()
    blueberry_fruit.penup()
    blueberry_fruit.hideturtle()
    strawberry_fruit = trtl.Turtle()
    strawberry_fruit.penup()
    strawberry_fruit.hideturtle()
    kiwi_fruit = trtl.Turtle()
    kiwi_fruit.penup()
    kiwi_fruit.hideturtle()
    cherry_fruit = trtl.Turtle()
    cherry_fruit.penup()
    cherry_fruit.hideturtle()
    #----Sweets----
    mochi_sweet = trtl.Turtle()
    mochi_sweet.penup()
    mochi_sweet.hideturtle()
    gummy_sweet = trtl.Turtle()
    gummy_sweet.penup()
    gummy_sweet.hideturtle()
    sprinkles_sweet = trtl.Turtle()
    sprinkles_sweet.penup()
    sprinkles_sweet.hideturtle()
    chocolate_sweet = trtl.Turtle()
    chocolate_sweet.penup()
    chocolate_sweet.hideturtle()
    #---Cups---
    star_cup = trtl.Turtle()
    star_cup.penup()
    star_cup.hideturtle()
    bubble_cup = trtl.Turtle()
    bubble_cup.penup()
    bubble_cup.hideturtle()
    heart_cup = trtl.Turtle()
    heart_cup.penup()
    heart_cup.hideturtle()
    leaf_cup = trtl.Turtle()
    leaf_cup.penup()
    leaf_cup.hideturtle()
    #---Flavors---
    original_flavor = trtl.Turtle()
    original_flavor.penup()
    original_flavor.hideturtle()
    strawberry_flavor = trtl.Turtle()
    strawberry_flavor.penup()
    strawberry_flavor.hideturtle()
    blueberry_flavor = trtl.Turtle()
    blueberry_flavor.penup()
    blueberry_flavor.hideturtle()
    mango_flavor = trtl.Turtle()
    mango_flavor.penup()
    mango_flavor.hideturtle()
    #---Empty---
    empty = trtl.Turtle()
    empty.penup()
    empty.hideturtle()
    white_bar = trtl.Turtle()
    white_bar.penup()
    white_bar.hideturtle()
    #----Placement----
    chocolate_sweet.goto(110,220)
    mochi_sweet.goto(110,220)
    sprinkles_sweet.goto(110,220)
    gummy_sweet.goto(110,220)
    cherry_fruit.goto(125,350)
    strawberry_fruit.goto(125,200)
    blueberry_fruit.goto(125,200)
    kiwi_fruit.goto(125,200)
    original_flavor.goto(100,250)
    strawberry_flavor.goto(100,250)
    blueberry_flavor.goto(100,250)
    mango_flavor.goto(100,250)
    star_cup.goto(100,-210)
    heart_cup.goto(100,-210)
    bubble_cup.goto(100,-210)
    leaf_cup.goto(100,-210)
    cup_button.goto(-800,375)
    flavor_button.goto(-800,127)
    fruit_button.goto(-800,-127)
    topping_button.goto(-800,-375)
    done_button.goto(700,-400)
    save_button.goto(700,-400)
    x_button.goto(850,425)
    starcup_button.goto(-490,375)
    leafcup_button.goto(-490,125)
    heartcup_button.goto(-490,-125)
    bubblecup_button.goto(-490,-375)
    originalflavor_button.goto(-490,375)
    strawberryflavor_button.goto(-490,125)
    blueberryflavor_button.goto(-490,-125)
    mangoflavor_button.goto(-490,-375)
    cherry_button.goto(-490,375)
    strawberry_button.goto(-490,123)
    blueberry_button.goto(-490,-125)
    kiwi_button.goto(-490,-375)
    chocolate_button.goto(-490,375)
    mochi_button.goto(-490,125)
    sprinkles_button.goto(-490,-125)
    gummy_button.goto(-490,-375)
    play_button.goto(-365,-300)
    white_bar.goto(-800,0)
    blue_button.goto(-800, 375)
    yellow_button.goto(-800, 127)
    pink_button.goto(-800,-127)
    white_button.goto(-800,-375)
    #-----Variables-----
    cup_picked = False
    yogurt_flavor_picked = False
    current_froyo = [empty, empty, empty, empty]
    wallpaper_list = [blue_button,yellow_button,pink_button,white_button]
    mainselectionbutton_list = [cup_button, flavor_button, fruit_button, topping_button,done_button,x_button]
    wallpaper_img_list = [button_blue_img, button_yellow_img,button_pink_img,button_white_img]
    cup_list = [star_cup, bubble_cup, heart_cup, leaf_cup]
    yogurt_list = [original_flavor, blueberry_flavor, strawberry_flavor, mango_flavor]
    fruit_list = [strawberry_fruit, cherry_fruit, blueberry_fruit, kiwi_fruit]
    topping_list = [mochi_sweet, chocolate_sweet, gummy_sweet, sprinkles_sweet]
    cupbutton_list = [starcup_button, bubblecup_button, heartcup_button, leafcup_button]
    flavorbutton_list = [originalflavor_button, strawberryflavor_button, blueberryflavor_button, mangoflavor_button]
    fruitbutton_list = [blueberry_button, strawberry_button, cherry_button, kiwi_button]
    toppingbutton_list = [gummy_button, sprinkles_button, mochi_button, chocolate_button]
    allbuttonimages_list = [save_button_img, button_blue_img, button_yellow_img,button_pink_img,button_white_img, playbutton_img, xbutton_img, donebutton_img, cupbutton_img, flavorbutton_img, toppingbutton_img, fruitbutton_img, blueberrybutton_img, kiwibutton_img, cherrybutton_img, strawberrybutton_img, chocolatebutton_img, gummybutton_img, sprinklesbutton_img, mochibutton_img, bubblecupbutton_img, starcupbutton_img, leafcupbutton_img, heartcupbutton_img, mangoflavor_button_img, strawberryflavor_button_img, originalflavor_button_img, blueberryflavor_button_img]
    allbuttonturtles_list = [save_button, blue_button,yellow_button,pink_button,white_button, play_button, x_button, done_button, cup_button, flavor_button, topping_button, fruit_button, blueberry_button, kiwi_button, cherry_button, strawberry_button, chocolate_button, gummy_button, sprinkles_button, mochi_button, bubblecup_button, starcup_button, leafcup_button, heartcup_button, mangoflavor_button, strawberryflavor_button, originalflavor_button, blueberryflavor_button]
    allnonbuttonimages_list = [star_cup_img,heart_cup_img,leaf_cup_img,bubble_cup_img,strawberry_flavor_img, blueberry_flavor_img,mango_flavor_img,original_flavor_img,kiwi_fruit_img,strawberry_fruit_img,blueberry_fruit_img,cherry_fruit_img,chocolate_sweet_img,mochi_sweet_img,sprinkles_sweet_img,gummy_sweet_img, whitebar_img]
    allnonbuttonturtles_list = [star_cup,heart_cup,leaf_cup,bubble_cup,strawberry_flavor,blueberry_flavor,mango_flavor,original_flavor,kiwi_fruit,strawberry_fruit,blueberry_fruit,cherry_fruit,chocolate_sweet,mochi_sweet,sprinkles_sweet,gummy_sweet, white_bar]
    wn.bgpic("screen_menu.gif")
    draw_button(play_button)
    play_button.showturtle()
    wn.update()
    play_button.onclick(gameplay)


#-----Function Calls-----
set_game()
wn.mainloop()