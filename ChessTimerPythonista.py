import ui, time, notification, sound

view = ui.View()
view.size_to_fit()
view.background_color = 'white'
view.flex = 'WH'

time1 = 5
time2 = 0
time3 = 0


player1button = ui.Button()
player1button.border_color = '#198054#'
player1button.border_width = 5
player1button.title = str(time1) + ':' + str(time2) + str(time3)



def timer1(sender):
    global time1
    global time2
    global time3
    if time3 == 0:
        time3  = 9
        if time2 == 0:
            time2 = 5
             player1button.title = str(time1) + ':' + str(time2) + str(time3)
             timer1(sender)
        if time2 != 0:
            time2 -=1 
             player1button.title = str(time1) + ':' + str(time2) + str(time3)
        timer1(sender)
        time.sleep(1)
        player1button.title = str(time1) + ':' + str(time2) + str(time3)
        timer1(sender)
    if time2 == 0:
        time1 -=1
         player1button.title = str(time1) + ':' + str(time2) + str(time3)
        timer1(sender)
    if time3 > 0:
        time3 -= 1
        time.sleep(1)
        player1button.title = str(time1) + ':' + str(time2) + str(time3)
        timer1(sender)
    if time1 == 0:
        notification.schedule(Flag Down! Player 2 wins!)



    
        

player1button.action = timer1

view.add_subview(player1button)
view.present()

