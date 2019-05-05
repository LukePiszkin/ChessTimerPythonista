import ui, time

view = ui.View()
view.size_to_fit()
view.background_color = 'white'
view.flex = 'WH'

player1button = ui.Button()
player1button.title = time1
player1button.action  = tap 

def tap(sender):
    pass

def timer1(sender):
    if time1 < 0:
        time1 -= 1
        player1button.title = time1
        ui.delay(timer1, 1)


view.add_subview(player1button)
view.present()

