
# Style sheet for the Pomodoro Timer GUI

style_sheet = """
QWidget {
    background-color: #D8D3D3;
}

QTabWidget:pane {
    border-top: 0px;
}

QTabBar:tab {
    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                        stop:0 #E1E1E1, stop:0.4 #DDDDDD,
                        stop:0.5 #D8D8D8, stop:1.0 #D3D3D3);
    border: 2px solid #C4C4C3;
    border-bottom-color: #C2C7CB;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    min-width: 8ex;
    padding: 2px;
}

QTabBar:tab:selected, QTabBar:hover {
    background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,
                        stop: 0 #FAFAFA, stop: 0.4 #F4F4F4,
                        stop: 0.5 #E7E7E7, stop: 1.0 #FAFAFA);
}

QTabBar:tab:selected {
    border-color: #9B9B9B;
    border-bottom-color: #C2C7CB;
}

QTabBar:tab:!selected {
    margin-top: 2px;  /* Make non-selected tabs look smaller when not
    selected */
}

QWidget#Pomodoro {
    background-color: #EF635C;
    border: 1px solid #EF635C;
    border-radius: 4px;
}

QWidget#ShortBreak {
    background-color: #398AB5;
    border: 1px solid #398AB5;
    border-radius: 4px;
}

QWidget#LongBreak{ /* Long break tab container widget */
    background-color: #55A992;
    border: 1px solid #55A992;
    border-radius: 4px;
}

QLCDNumber#PomodoroLCD {
    background-color: #F48B86;
    color: #FFFFFF;
    border: 2px solid #F48B86;
    border-radius: 4px;
}

QLCDNumber#ShortLCD {
    background-color: #5CAFDC;
    color: #FFFFFF;
    border: 2px solid #5CAFDC;
    border-radius: 4px;
}

QLCDNumber#LongLCD {
    background-color: #6DD4B7;
    color: #FFFFFF;
    border: 2px solid #6DD4B7;
    border-radius: 4px;
}

QPushButton { /* General look of QPushButtons */
    background-color: #E1E1E1;
    border: 2px solid #C4C4C3;
    border-radius: 4px;
    padding: 5px 0;
}

QPushButton:hover {
    background-color: #F8F4F4
}

QPushButton:pressed {
    background-color: #E9E9E9;
    border: 2px solid #C4C4C3;
    border-radius: 4px;
}

QPushButton:disabled {
    background-color: #D8D3D3;
    border: 2px solid #C4C4C3;
    border-radius: 4px;
}

QGroupBox { /* Style for Pomodoro task bar */
    background-color: #EF635C;
    border: 2px solid #EF635C;
    border-radius: 4px;
    margin-top: 3ex
}

QGroupBox:title {
    subcontrol-origin: margin;
    padding: 2px;
}

QLineEdit {
    background-color: #FFFFFF;
    height: 30px;
    padding: 0 5px;
    font: 16pt Tahoma;
}

QLabel {
    background-color: #EF635C;
    color: #FFFFFF;
}
"""
