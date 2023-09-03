import kivy #using for GUI
kivy.require('2.2.1')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
#from kivy.uix.image import Image
from kivy.uix.spinner import Spinner
from kivy.uix.floatlayout import FloatLayout
#from kivy.graphics import Color, Rectangle

class Chessboard(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 8  # Number of columns
        self.rows = 8  # Number of rows
        self.spacing = [0, 0]

        # Initialize the chessboard grid
        self.init_chessboard()

    def init_chessboard(self):
        for row in range(self.rows):
            for col in range(self.cols):
                # Determine the background color of the square
                if (row + col) % 2 == 0:
                    square_color = [0.9, 0.9, 0.9, 1]  # Light color
                else:
                    square_color = [0.1, 0.1, 0.1, 1]  # Dark color

                # Create a Button widget representing a square
                square = Button(
                    background_color=square_color,
                    background_normal='',
                    background_down='',
                )

                # Add the square to the chessboard
                self.add_widget(square)

class ChessApp(App):
    def build(self):
   # Create the main layout for the chessboard
        layout = BoxLayout(orientation='horizontal', spacing=10)

        # Create the chessboard grid
        chessboard = Chessboard()

        # Create the extended section on the right using a FloatLayout
        extended_section = FloatLayout(size_hint=(None, 1), width=100)  # Adjust the width as needed

        # Add a "New Game" button
        new_game_button = Button(text='New Game', size_hint=(None, None), width=100, height=30, pos_hint={'center_x': 0.5, 'top': 1})
        extended_section.add_widget(new_game_button)
        
         # Add an "Undo Move" button
        undo_button = Button(text='Undo Move', size_hint=(None, None), width=100, height=60, pos_hint={'center_x': 0.5, 'top': 0.8})
        extended_section.add_widget(undo_button)

        # Add an "Redo Move" button
        redo_button = Button(text='Redo Move', size_hint=(None, None), width=100, height=60, pos_hint={'center_x': 0.5, 'top': 0.7})
        extended_section.add_widget(redo_button)

        # Add a label for difficulty selection
        difficulty_label = Label(text='Difficulty:', size_hint=(None, None), width=100, height=30, pos_hint={'center_x': 0.5, 'top': 0.5})    
        extended_section.add_widget(difficulty_label)

        # Create a Spinner for difficulty selection
        difficulty_spinner = Spinner(
            text='Easy',
            values=('Easy', 'Medium', 'Hard'),  # Difficulty levels corresponding to Stockfish settings
            size_hint=(None, None),
            width=100,
            height=120,
            pos_hint={'center_x': 0.5, 'top': 0.4}
        )
        extended_section.add_widget(difficulty_spinner)

        # Add the chessboard and extended section to the main layout
        layout.add_widget(chessboard)
        layout.add_widget(extended_section)


        return layout

if __name__ == '__main__':
    ChessApp().run()