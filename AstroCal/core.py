import model
import control
import view

def run():
    hello()
    # print("Sun Rise and Set for Sept, 22")
    # print(control.getRiseSet(2022, 9, 22, 'SUN', 'RISE'))
    # print(control.getRiseSet(2022, 9, 22, 'SUN', 'SET'))

    # print("Moon Rise and Set for Sept, 22")
    # print(control.getRiseSet(2022, 9, 22, 'MOON', 'RISE'))
    # print(control.getRiseSet(2022, 9, 22, 'MOON', 'SET'))
    app = view.tkGUI_Launch
    app.mainloop()
    #view.createMenu()
    #runs everything
    #app = view.mainApp()
    #app.mainloop()

def hello():
    print("Hello, moon!")
