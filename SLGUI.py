#still thinking how should I import the machine learning to the gui
#This version is use multiple windows since the questions cannot fit into one window, got one more version below (section version)
import PySimpleGUI as sg

def window1():
    layout_1 = [[sg.Image(r'C:\Users\issac\OneDrive\Pictures\Pictures\love-yourself-j.png')],#can just cut this line since i just randomly get an image from google
                [sg.Text("This is a Self-Love App"), sg.Text(size=(15, 1), key='-OUT1-')],
                [sg.Text("Please click Start to continue."), sg.Text(size=(20, 1), key='-OUT2-')],
                [sg.Button('Start'), sg.Button('Exit')]]

    window_1 = sg.Window(title="Self-Love App", layout=layout_1, no_titlebar=True, alpha_channel=1, grab_anywhere=True)

    while True:
        event1, values1 = window_1.read()
        if event1 == 'Exit' or event1 == sg.WIN_CLOSED:
            break
        if event1 == 'Start':
            window2()

    window_1.close()


def window2():
    occupation = ('University Student', 'Employed', 'Unemployed', 'Retired')

    layout_2 = [[sg.Text('Please enter your name:')],
                [sg.InputText(key='-NAME-')],
                [sg.Text('Please enter your gender (Male/Female):')],
                [sg.InputText(key='-GENDER-')],
                [sg.Text('What is your current occupation?:')],
                [sg.Listbox(occupation, size=(18, len(occupation)), key='-OCCUPATION-')],
                [sg.Button('Next')]]

    window_2 = sg.Window(title='Questionnaires', layout=layout_2, no_titlebar=True, alpha_channel=1, grab_anywhere=True)

    while True:
        event2, values2 = window_2.read()
        if event2 == sg.WIN_CLOSED:
            break
        if event2 == 'Next':
            window_2.hide()
            window3()


def window3():
    multiple_choices1 = ('When you accomplish a project', 'When someone acknowledges you', 'By earning a lot of money',
                         'By leading others to success', 'Owning famous brands',
                         'Get the most/ special attention among the members')
    multiple_choices2 = (
        'Food', 'The latest technology', 'The latest fashion', 'Activities with friends', 'Home Improvements')
    multiple_choices3 = ('I make a chart or graph', 'Jotting it down on a scrap of paper', 'I talk to myself out loud',
                         'I write it down in my calendar', 'Any combination of these')
    multiple_choices4 = (
        'Dog', 'Cat', 'Fish', 'Bird', 'Snake', 'Hamster', 'Rabbit', 'Insects', 'Arachnids', 'Tortoise', 'Horse',
        'I am not a pet person')
    multiple_choices5 = ('Morning', 'Afternoon', 'Evening', 'Night')

    layout_3 = [[sg.Text('What boosts your confidence ? ')],
                [sg.Listbox(multiple_choices1, size=(45, len(multiple_choices1)), key='-MULTIPLE_CHOICES1-')],
                [sg.Text('I prefer to spend my money on.... ')],
                [sg.Listbox(multiple_choices2, size=(23, len(multiple_choices2)), key='-MULTIPLE_CHOICES2-')],
                [sg.Text('How do you organize your thoughts? Please pick whichever is closest. ')],
                [sg.Listbox(multiple_choices3, size=(35, len(multiple_choices3)), key='-MULTIPLE_CHOICES3-')],
                [sg.Text('Choose a pet which you prefer to keep. ')],
                [sg.Listbox(multiple_choices4, size=(18, len(multiple_choices4)), key='-MULTIPLE_CHOICES4-')],
                [sg.Text('What is your favorite time of the day? ')],
                [sg.Listbox(multiple_choices5, size=(15, len(multiple_choices5)), key='-MULTIPLE_CHOICES5-')],
                [sg.Button('Next')]]

    window_3 = sg.Window(title='Questionnaires', layout=layout_3, no_titlebar=True, alpha_channel=1, grab_anywhere=True)

    while True:
        event3, values3 = window_3.read()
        if event3 == sg.WIN_CLOSED:
            break
        if event3 == 'Next':
            window_3.hide()
            window4()


def window4():
    multiple_choices6 = ('The future', 'The past', 'Neither. I prefer the present')
    multiple_choices7 = (
        'Your future', 'Your family and friends', 'The state of the world', 'Money', 'How others see me')
    multiple_choices8 = (
        'Exactly where I live now', 'Overseas', 'In a small town', 'In a hectic big city', 'Cabin in the woods',
        'Traveling the world')
    multiple_choices9 = ('Green', 'Blue', 'Red', 'Yellow', 'Purple', 'White', 'Black')
    multiple_choices10 = (
        'By attending online courses', 'By attending lectures', 'By reading an e-Book', 'By reading a physical book',
        'By doing tutorial/lab questions', 'By doing assignments')

    layout_4 = [[sg.Text('Would you rather visit the future or the past? ')],
                [sg.Listbox(multiple_choices6, size=(20, len(multiple_choices6)), key='-MULTIPLE_CHOICES6-')],
                [sg.Text('What do you worry more about the most? ')],
                [sg.Listbox(multiple_choices7, size=(25, len(multiple_choices7)), key='-MULTIPLE_CHOICES7-')],
                [sg.Text('When you retire, you would like to live... ')],
                [sg.Listbox(multiple_choices8, size=(35, len(multiple_choices8)), key='-MULTIPLE_CHOICES8-')],
                [sg.Text('What is your favorite color? ')],
                [sg.Listbox(multiple_choices9, size=(15, len(multiple_choices9)), key='-MULTIPLE_CHOICES9-')],
                [sg.Text('What is your learning style? (Pick one that benefit you the most) ')],
                [sg.Listbox(multiple_choices10, size=(35, len(multiple_choices10)), key='-MULTIPLE_CHOICES10-')],
                [sg.Button('Next')]]

    window_4 = sg.Window(title='Questionnaires', layout=layout_4, no_titlebar=True, alpha_channel=1, grab_anywhere=True)

    while True:
        event4, values4 = window_4.read()
        if event4 == sg.WIN_CLOSED:
            break
        if event4 == 'Next':
            window_4.hide()
            window5()


def window5():
    layout_5 = [[sg.Text('Do you enjoy socializing with large groups of people?')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER1')],
                [sg.Text('I prefer to be alone             I yearn for human interaction')],
                [sg.Text('Do you enjoy challenges?')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER2')],
                [sg.Text('No, I like to take it easy             Yes, pain please!')],
                [sg.Text('How creative of a person do you think you are? ')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER3')],
                [sg.Text('Not creative at all                Leonardo Da Vinci')],
                [sg.Text('How logical of a person do you think you are? ')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER4')],
                [sg.Text('Not logic at all                     Albert Einstein')],
                [sg.Text('Would you prefer to engage your brain more than your body? ')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER5')],
                [sg.Text('I am more sporty                 I am more intellectual')],
                [sg.Text('Are you a curious person?')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER6')],
                [sg.Text('Not curious at all                 Extremely curious')],
                [sg.Text('Are you a perfectionist?')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER7')],
                [sg.Text('Everybody makes mistakes      Everything must be perfect')],
                [sg.Button('Next')]]

    window_5 = sg.Window(title='Questionnaires', layout=layout_5, no_titlebar=True, alpha_channel=1, grab_anywhere=True)

    while True:
        event5, values5 = window_5.read()
        if event5 == sg.WIN_CLOSED:
            break
        if event5 == 'Next':
            window_5.hide()
            window6()


def window6():
    layout_6 = [[sg.Text('Are you a trusting person?')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER8')],
                [sg.Text('I trust nobody                     I trust everyone!')],
                [sg.Text('Do you have lot of patience?')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER9')],
                [sg.Text('No patience at all                Extremely patient')],
                [sg.Text('Do you organize your schedule well? ')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER10')],
                [sg.Text('What schedule?            My schedule is very organized')],
                [sg.Text('Do you like to sit in front of a computer for long hours? ')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER11')],
                [sg.Text('    I hate it                                    I love it')],
                [sg.Text('Do you enjoy making others happy?')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER12')],
                [sg.Text('Others reactions               I am happy when ')],
                [sg.Text('do not affect me               everyone is happy!')],
                [sg.Text('Can you understand others perspectives and feelings?')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER13')],
                [sg.Text('Too complex to understand        I can read minds')],
                [sg.Text('How confident are you in your own abilities? ')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER14')],
                [sg.Text('Not confident at all           Extremely confident')],
                [sg.Button('Done')]]

    window_6 = sg.Window(title='Questionnaires', layout=layout_6, no_titlebar=True, alpha_channel=1, grab_anywhere=True)

    while True:
        event6, values6= window_6.read()
        if event6 == sg.WIN_CLOSED:
            break
        if event6 == 'Done':
            window_6.hide()
            output_element()


def output_element():#just ignore this one for now I'm already has idea how to get the output
    '''layout_output = [[sg.Text('This is the output of your choices')],
                     [sg.Output(size=(45, 50), key='-OUTPUT-')],
                     [sg.Button('Check Your Result')]]

    window_output = sg.Window(title='Output', layout=layout_output, no_titlebar=True, alpha_channel=1,
                              grab_anywhere=True)'''

    while True:
        event7, values7 = window_output.read()
        if event7 == sg.WIN_CLOSED:
            break
        #window_output['-OUTPUT-'].update(values=window2().values['-NAME-'])
        if event7 == 'Check Your Result':
            window_output.close()
            '''Todo'''


def main():
    sg.theme('SystemDefault')
    window1()


if __name__ == '__main__':
    main()

#https://pysimplegui.readthedocs.io/en/latest/#pattern-1-a-one-shot-window-read-a-window-one-time-then-close-it
#https://pysimplegui.readthedocs.io/en/latest/cookbook/#recipe-printing
#https://pysimplegui.readthedocs.io/en/latest/call%20reference/#the-main-program-test-harness-global-settings-debug-information-upgrade-from-github
#https://github.com/PySimpleGUI/PySimpleGUI/issues/1633

#Below here is another version of the GUI. It uses sections in one window
#It works when I test it (without def) but then when i def it, then the window will disappear when go to next section (unknown issue) 

'''import PySimpleGUI as sg

def window1():
    layout_1 = [[sg.Image(r'C:\Users\issac\OneDrive\Pictures\Pictures\love-yourself-j.png')], #can just cut this line since i just randomly get an image from google
                [sg.Text("This is a Self-Love App"), sg.Text(size=(15, 1), key='-OUT1-')],
                [sg.Text("Please click Start to continue."), sg.Text(size=(20, 1), key='-OUT2-')],
                [sg.Button('Start'), sg.Button('Exit')]]

    window_1 = sg.Window(title="Self-Love App", layout=layout_1, no_titlebar=True, alpha_channel=1, grab_anywhere=True)

    while True:
        event1, values1 = window_1.read()
        if event1 == 'Exit' or event1 == sg.WIN_CLOSED:
            break
        if event1 == 'Start':
            window2()
            window_1.hide()

    window_1.close()


SYMBOL_UP = '▲'
SYMBOL_DOWN = '▼'


def collapse(layout, key, visible):
    return sg.pin(sg.Column(layout, key=key, visible=visible))


def window2():
    occupation = ('University Student', 'Employed', 'Unemployed', 'Retired')

    section1 = [[sg.Text('Please enter your name:')],
                [sg.InputText(key='-NAME-')],
                [sg.Text('Please enter your gender (Male/Female):')],
                [sg.InputText(key='-GENDER-')],
                [sg.Text('What is your current occupation?:')],
                [sg.Listbox(occupation, size=(18, len(occupation)), key='-OCCUPATION-')], ]

    multiple_choices1 = ('When you accomplish a project', 'When someone acknowledges you', 'By earning a lot of money',
                         'By leading others to success', 'Owning famous brands',
                         'Get the most/ special attention among the members')
    multiple_choices2 = (
        'Food', 'The latest technology', 'The latest fashion', 'Activities with friends', 'Home Improvements')
    multiple_choices3 = ('I make a chart or graph', 'Jotting it down on a scrap of paper', 'I talk to myself out loud',
                         'I write it down in my calendar', 'Any combination of these')
    multiple_choices4 = (
        'Dog', 'Cat', 'Fish', 'Bird', 'Snake', 'Hamster', 'Rabbit', 'Insects', 'Arachnids', 'Tortoise', 'Horse',
        'I am not a pet person')
    multiple_choices5 = ('Morning', 'Afternoon', 'Evening', 'Night')

    section2 = [[sg.Text('What boosts your confidence ? ')],
                [sg.Listbox(multiple_choices1, size=(45, 5), key='-MULTIPLE_CHOICES1-')],
                [sg.Text('I prefer to spend my money on.... ')],
                [sg.Listbox(multiple_choices2, size=(23, len(multiple_choices2)), key='-MULTIPLE_CHOICES2-')],
                [sg.Text('How do you organize your thoughts? Please pick whichever is closest. ')],
                [sg.Listbox(multiple_choices3, size=(35, len(multiple_choices3)), key='-MULTIPLE_CHOICES3-')],
                [sg.Text('Choose a pet which you prefer to keep. ')],
                [sg.Listbox(multiple_choices4, size=(18, 5), key='-MULTIPLE_CHOICES4-')],
                [sg.Text('What is your favorite time of the day? ')],
                [sg.Listbox(multiple_choices5, size=(15, len(multiple_choices5)), key='-MULTIPLE_CHOICES5-')]]

    multiple_choices6 = ('The future', 'The past', 'Neither. I prefer the present')
    multiple_choices7 = (
        'Your future', 'Your family and friends', 'The state of the world', 'Money', 'How others see me')
    multiple_choices8 = (
        'Exactly where I live now', 'Overseas', 'In a small town', 'In a hectic big city', 'Cabin in the woods',
        'Traveling the world')
    multiple_choices9 = ('Green', 'Blue', 'Red', 'Yellow', 'Purple', 'White', 'Black')
    multiple_choices10 = (
        'By attending online courses', 'By attending lectures', 'By reading an e-Book', 'By reading a physical book',
        'By doing tutorial/lab questions', 'By doing assignments')

    section3 = [[sg.Text('Would you rather visit the future or the past? ')],
                [sg.Listbox(multiple_choices6, size=(20, len(multiple_choices6)), key='-MULTIPLE_CHOICES6-')],
                [sg.Text('What do you worry more about the most? ')],
                [sg.Listbox(multiple_choices7, size=(25, len(multiple_choices7)), key='-MULTIPLE_CHOICES7-')],
                [sg.Text('When you retire, you would like to live... ')],
                [sg.Listbox(multiple_choices8, size=(35, 5), key='-MULTIPLE_CHOICES8-')],
                [sg.Text('What is your favorite color? ')],
                [sg.Listbox(multiple_choices9, size=(15, 5), key='-MULTIPLE_CHOICES9-')],
                [sg.Text('What is your learning style? (Pick one that benefit you the most) ')],
                [sg.Listbox(multiple_choices10, size=(35, 5), key='-MULTIPLE_CHOICES10-')]]

    section4 = [[sg.Text('Do you enjoy socializing with large groups of people?')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER1')],
                [sg.Text('I prefer to be alone    I yearn for human interaction', font='Courier 8')],
                [sg.Text('Do you enjoy challenges?')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER2')],
                [sg.Text('No, I like to take it easy    Yes, pain please!', font='Courier 8')],
                [sg.Text('How creative of a person do you think you are? ')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER3')],
                [sg.Text('Not creative at all      Leonardo Da Vinci', font='Courier 8')],
                [sg.Text('How logical of a person do you think you are? ')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER4')],
                [sg.Text('Not logic at all         Albert Einstein', font='Courier 8')],
                [sg.Text('Would you prefer to engage your brain more than your body? ')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER5')],
                [sg.Text('I am more sporty      I am more intellectual', font='Courier 8')],
                [sg.Text('Are you a curious person?')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER6')],
                [sg.Text('Not curious at all       Extremely curious', font='Courier 8')],
                [sg.Text('Are you a perfectionist?')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER7')],
                [sg.Text('Everybody makes mistakes  Everything must be perfect', font='Courier 8')]]

    section5 = [[sg.Text('Are you a trusting person?')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER8')],
                [sg.Text('I trust nobody         I trust everyone!', font='Courier 8')],
                [sg.Text('Do you have lot of patience?')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER9')],
                [sg.Text('No patience at all        Extremely patient', font='Courier 8')],
                [sg.Text('Do you organize your schedule well? ')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER10')],
                [sg.Text('What schedule?      My schedule is very organized', font='Courier 8')],
                [sg.Text('Do you like to sit in front of a computer for long hours? ')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER11')],
                [sg.Text(' I hate it                I love it', font='Courier 8')],
                [sg.Text('Do you enjoy making others happy?')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER12')],
                [sg.Text('Others reactions           I am happy when ', font='Courier 8')],
                [sg.Text('do not affect me           everyone is happy!', font='Courier 8')],
                [sg.Text('Can you understand others perspectives and feelings?')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER13')],
                [sg.Text('Too complex to understand   I can read minds', font='Courier 8')],
                [sg.Text('How confident are you in your own abilities? ')],
                [sg.Slider(range=(1, 5), default_value=3, pad=(50, 0), orientation='horizontal', key='SLIDER14')],
                [sg.Text('Not confident at all      Extremely confident', font='Courier 8')]]

    layout = [[sg.Text('Please answer the following questions.')],
              [sg.T(SYMBOL_DOWN, enable_events=True, k='-OPEN SEC1-', text_color='yellow'),
               sg.T('Section 1', enable_events=True, text_color='yellow', k='-OPEN SEC1-TEXT')],
              [collapse(section1, '-SEC1-', True)],
              [sg.T(SYMBOL_UP, enable_events=True, k='-OPEN SEC2-', text_color='purple'),
               sg.T('Section 2', enable_events=True, text_color='purple', k='-OPEN SEC2-TEXT')],
              [collapse(section2, '-SEC2-', False)],
              [sg.T(SYMBOL_UP, enable_events=True, k='-OPEN SEC3-', text_color='red'),
               sg.T('Section 3', enable_events=True, text_color='red', k='-OPEN SEC3-TEXT')],
              [collapse(section3, '-SEC3-', False)],
              [sg.T(SYMBOL_UP, enable_events=True, k='-OPEN SEC4-', text_color='green'),
               sg.T('Section 4', enable_events=True, text_color='green', k='-OPEN SEC4-TEXT')],
              [collapse(section4, '-SEC4-', False)],
              [sg.T(SYMBOL_UP, enable_events=True, k='-OPEN SEC5-', text_color='blue'),
               sg.T('Section 5', enable_events=True, text_color='blue', k='-OPEN SEC5-TEXT')],
              [collapse(section5, '-SEC5-', False)],
              [sg.Button('Done'), sg.Button('Exit')]]

    window = sg.Window('Questionnaire', layout, no_titlebar=True, alpha_channel=1, grab_anywhere=True)

    opened1, opened2, opened3, opened4, opened5 = True, False, False, False, False

    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED or event == 'Exit':
            break

        opened1 = not opened1
        opened2 = not opened2
        opened3 = not opened3
        opened4 = not opened4
        opened5 = not opened5

        if event.startswith('-OPEN SEC1-'):
            window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened1 else SYMBOL_UP)
            window['-SEC1-'].update(visible=opened1)
            if opened1 == True:
                window['-OPEN SEC2-'].update(SYMBOL_DOWN if not opened2 else SYMBOL_UP)
                window['-SEC2-'].update(visible=not opened2)
                window['-OPEN SEC3-'].update(SYMBOL_DOWN if not opened3 else SYMBOL_UP)
                window['-SEC3-'].update(visible=not opened3)
                window['-OPEN SEC4-'].update(SYMBOL_DOWN if not opened4 else SYMBOL_UP)
                window['-SEC4-'].update(visible=not opened4)
                window['-OPEN SEC5-'].update(SYMBOL_DOWN if not opened5 else SYMBOL_UP)
                window['-SEC5-'].update(visible=not opened5)

            if opened2 == False and opened3 == False and opened4 == False and opened5 == False:
                window['-OPEN SEC2-'].update(SYMBOL_DOWN if opened2 else SYMBOL_UP)
                window['-SEC2-'].update(visible=opened2)
                window['-OPEN SEC3-'].update(SYMBOL_DOWN if opened3 else SYMBOL_UP)
                window['-SEC3-'].update(visible=opened3)
                window['-OPEN SEC4-'].update(SYMBOL_DOWN if opened4 else SYMBOL_UP)
                window['-SEC4-'].update(visible=opened4)
                window['-OPEN SEC5-'].update(SYMBOL_DOWN if opened5 else SYMBOL_UP)
                window['-SEC5-'].update(visible=opened5)

        if event.startswith('-OPEN SEC2-'):
            window['-OPEN SEC2-'].update(SYMBOL_DOWN if opened2 else SYMBOL_UP)
            window['-SEC2-'].update(visible=opened2)
            if opened2 == True:
                window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened1 else SYMBOL_UP)
                window['-SEC1-'].update(visible=opened1)
                window['-OPEN SEC3-'].update(SYMBOL_DOWN if not opened3 else SYMBOL_UP)
                window['-SEC3-'].update(visible=not opened3)
                window['-OPEN SEC4-'].update(SYMBOL_DOWN if not opened4 else SYMBOL_UP)
                window['-SEC4-'].update(visible=not opened4)
                window['-OPEN SEC5-'].update(SYMBOL_DOWN if not opened5 else SYMBOL_UP)
                window['-SEC5-'].update(visible=not opened5)

            if opened1 == False and opened3 == False and opened4 == False and opened5 == False:
                window['-OPEN SEC1-'].update(SYMBOL_DOWN if not opened1 else SYMBOL_UP)
                window['-SEC1-'].update(visible=not opened1)
                window['-OPEN SEC3-'].update(SYMBOL_DOWN if not opened3 else SYMBOL_UP)
                window['-SEC3-'].update(visible=opened3)
                window['-OPEN SEC4-'].update(SYMBOL_DOWN if opened4 else SYMBOL_UP)
                window['-SEC4-'].update(visible=opened4)
                window['-OPEN SEC5-'].update(SYMBOL_DOWN if opened5 else SYMBOL_UP)
                window['-SEC5-'].update(visible=opened5)

        if event.startswith('-OPEN SEC3-'):
            window['-OPEN SEC3-'].update(SYMBOL_DOWN if opened3 else SYMBOL_UP)
            window['-SEC3-'].update(visible=opened3)
            if opened3 == True:
                window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened1 else SYMBOL_UP)
                window['-SEC1-'].update(visible=opened1)
                window['-OPEN SEC2-'].update(SYMBOL_DOWN if not opened2 else SYMBOL_UP)
                window['-SEC2-'].update(visible=not opened2)
                window['-OPEN SEC4-'].update(SYMBOL_DOWN if not opened4 else SYMBOL_UP)
                window['-SEC4-'].update(visible=not opened4)
                window['-OPEN SEC5-'].update(SYMBOL_DOWN if not opened5 else SYMBOL_UP)
                window['-SEC5-'].update(visible=not opened5)

            if opened1 == False and opened2 == False and opened4 == False and opened5 == False:
                window['-OPEN SEC1-'].update(SYMBOL_DOWN if not opened1 else SYMBOL_UP)
                window['-SEC1-'].update(visible=not opened1)
                window['-OPEN SEC2-'].update(SYMBOL_DOWN if opened2 else SYMBOL_UP)
                window['-SEC2-'].update(visible=opened2)
                window['-OPEN SEC4-'].update(SYMBOL_DOWN if opened4 else SYMBOL_UP)
                window['-SEC4-'].update(visible=opened4)
                window['-OPEN SEC5-'].update(SYMBOL_DOWN if opened5 else SYMBOL_UP)
                window['-SEC5-'].update(visible=opened5)

        if event.startswith('-OPEN SEC4-'):
            window['-OPEN SEC4-'].update(SYMBOL_DOWN if opened4 else SYMBOL_UP)
            window['-SEC4-'].update(visible=opened4)
            if opened4 == True:
                window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened1 else SYMBOL_UP)
                window['-SEC1-'].update(visible=opened1)
                window['-OPEN SEC2-'].update(SYMBOL_DOWN if not opened2 else SYMBOL_UP)
                window['-SEC2-'].update(visible=not opened2)
                window['-OPEN SEC3-'].update(SYMBOL_DOWN if not opened3 else SYMBOL_UP)
                window['-SEC3-'].update(visible=not opened3)
                window['-OPEN SEC5-'].update(SYMBOL_DOWN if not opened5 else SYMBOL_UP)
                window['-SEC5-'].update(visible=not opened5)

            if opened1 == False and opened2 == False and opened3 == False and opened5 == False:
                window['-OPEN SEC1-'].update(SYMBOL_DOWN if not opened1 else SYMBOL_UP)
                window['-SEC1-'].update(visible=not opened1)
                window['-OPEN SEC2-'].update(SYMBOL_DOWN if opened2 else SYMBOL_UP)
                window['-SEC2-'].update(visible=opened2)
                window['-OPEN SEC3-'].update(SYMBOL_DOWN if opened3 else SYMBOL_UP)
                window['-SEC3-'].update(visible=opened3)
                window['-OPEN SEC5-'].update(SYMBOL_DOWN if opened5 else SYMBOL_UP)
                window['-SEC5-'].update(visible=opened5)

        if event.startswith('-OPEN SEC5-'):
            window['-OPEN SEC5-'].update(SYMBOL_DOWN if opened5 else SYMBOL_UP)
            window['-SEC5-'].update(visible=opened5)
            if opened5 == True:
                window['-OPEN SEC1-'].update(SYMBOL_DOWN if opened1 else SYMBOL_UP)
                window['-SEC1-'].update(visible=opened1)
                window['-OPEN SEC2-'].update(SYMBOL_DOWN if not opened2 else SYMBOL_UP)
                window['-SEC2-'].update(visible=not opened2)
                window['-OPEN SEC4-'].update(SYMBOL_DOWN if not opened4 else SYMBOL_UP)
                window['-SEC4-'].update(visible=not opened4)
                window['-OPEN SEC3-'].update(SYMBOL_DOWN if not opened3 else SYMBOL_UP)
                window['-SEC3-'].update(visible=not opened3)

            if opened1 == False and opened2 == False and opened3 == False and opened5 == False:
                window['-OPEN SEC1-'].update(SYMBOL_DOWN if not opened1 else SYMBOL_UP)
                window['-SEC1-'].update(visible=not opened1)
                window['-OPEN SEC2-'].update(SYMBOL_DOWN if opened2 else SYMBOL_UP)
                window['-SEC2-'].update(visible=opened2)
                window['-OPEN SEC4-'].update(SYMBOL_DOWN if opened4 else SYMBOL_UP)
                window['-SEC4-'].update(visible=opened4)
                window['-OPEN SEC3-'].update(SYMBOL_DOWN if opened3 else SYMBOL_UP)
                window['-SEC3-'].update(visible=opened3)

        window.close()

def main():
    sg.theme('SystemDefault')
    window1()


if __name__ == '__main__':
    main()'''
