import ui, time

class Main(ui.view):
    def.decrement(self): 
        if self.time > 0
        self.time -= 1
        self.lbl.text = str(self.time)
        ui.delay(self.decrement, 1)

    self.view_main  = ui.load_view()
    self.lbl = self.view_main("time1")
    self.view_main.present("sheet")
    self.time = 5
    self.view_main["btn_start"].action = self.change_label_time  


  def change_label_time(self, sender):
        ui.delay(self.decrement, 1)

Main()