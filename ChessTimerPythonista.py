import ui, time, notification, sound, sys

view = ui.View()
view.size_to_fit()
view.background_color = 'white'
view.flex = 'WH'

time1 = 0
time2 = 1
time3 = 0
time4 = 0
time5 = 1
time6 = 0
tap1 == False
tap2 == False
player1button = ui.Button()
player1button.border_color = '#198054#'
player1button.border_width = 5
player1button.frame = (90,30,200,75)
player1button.title = str(time1) + ':' + str(time2) + str(time3)

player2button = ui.Button()
player2button.border_color = '#198054#'
player2button.border_width = 5
player2button.frame = (90,530,200,75)
player2button.title = str(time1) + ':' + str(time2) + str(time3)



@ui.in_background
def timer1(sender):
    global time1
    global time2
    global time3
    global tap2
    global tap1
    tap1 = False
    tap2 = True
    if tap1 == True:
        timer2()
    if time3 == 0 & (time2 > 0 | time1 > 0):
        time3  = 9
        if time2 == 0:
            time1 -= 1
            time2 = 5
        else:
            time2 -=1 
    else:
        time3 -= 1
    time.sleep(1)
    player1button.title = str(time1) + ':' + str(time2) + str(time3)
    timer1(sender)
    if time1 == time2 == time3 == 0:
        notification.schedule('Flag Down! Player 2 Wins!')
        view.remove_subview(player1button)
        view.remove_subview(player2button)


@ui.in_background
def timer2(sender):
    global time4
    global time5
    global time6
    global tap1
    global tap2
    tap1 == True 
    tap2 == False
    if tap2 == True:
        timer1()
    if time6 == 0 & (time5 > 0 | time4 > 0):
        time6  = 9
        if time5 == 0:
            time4 -= 1
            time5 = 5
        else:
            time5 -=1
    else:
        time6 -= 1
    time.sleep(1)
    player1button.title = str(time4) + ':' + str(time5) + str(time6)
    timer2(sender)
    if time4 == time5 == time6 == 0:
        notification.schedule('Flag Down! Player 1 Wins!')
        view.remove_subview(player1button)
        view.remove_subview(player2button)




player1button.action = timer2
player2button.action = timer1


view.add_subview(quitbutton)
view.add_subview(player1button)
view.present()
