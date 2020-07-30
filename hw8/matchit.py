# ----------------------------------------------------------------------
# Name:        matchit
# Purpose:     Implement a single player matching game
#
# Author(s):   Haitao Huang, Duong Cao
# ----------------------------------------------------------------------
"""
A single player matching game.

usage: matchit.py [-h] [-f] {blue,green,magenta} image_folder
positional arguments:
  {blue,green,magenta}  What color would you like for the player?
  image_folder          What folder contains the game images?

optional arguments:
  -h, --help            show this help message and exit
  -f, --fast            Fast or slow game?
"""
import tkinter
import os
import random
import argparse


class MatchGame(object):

    """
    GUI Game class for a matching game.

    Arguments:
    parent: the root window object
    player_color (string): the color to be used for the matched tiles
    folder (string) the folder containing the images for the game
    delay (integer) how many milliseconds to wait before flipping a tile

    Attributes:
    image_names (list): a list of 16 matching images
    images_dict (dict): maps each image name to a tkinter.PhotoImage
    player_color (str): the color to be used for the matched tiles
    delay (int): how many milliseconds to wait before flipping a tile
    canvas (tkinter.Canvas): canvas of the 4x4 grid
    score_label (tkinter.Label): label to show the score
    game_over_message (tkinter.Label): label to show the game over msg
    num_of_tries_label (tkinter.Label): label to show the num of tries
    score (int): game score
    num_of_tries (int): number of tries
    num_of_revealed_tiles (int): num of revealed tile currently
    revealed_tiles (list): a list of squares corresponding to the
                           revealed tiles
    matched_pairs (int): num of pairs that have matched during the game
    """

    # Add your class variables if needed here - square size, etc...)
    square_size = 120
    square_color = 'yellow'

    def __init__(self, parent, player_color, folder, delay):
        parent.title('Match it!')
        # Get all the gif files in the given folder
        folder_images = [fn for fn in os.listdir(folder) if
                         fn.endswith(".gif")]
        # Check if the folder has at least 8 gif files
        if len(folder_images) < 8:
            raise argparse.ArgumentTypeError(
                folder + ' must contain at least 8 gif images')
        # Create a list of all matching images and shuffle them
        self.image_names = 2 * folder_images
        random.shuffle(self.image_names)
        # Create a dict that map each image name to a tkinter.PhotoImage
        self.images_dict = {fn: tkinter.PhotoImage(file=folder+'/'+fn)
                       for fn in folder_images}
        self.player_color = player_color
        self.delay = delay
        # Create the restart button widget
        restart_button = tkinter.Button(parent, text='RESTART', width=20,
                                        command=self.restart)
        # Create a canvas widget
        self.canvas = tkinter.Canvas(parent, width=self.square_size * 4,
                                     height=self.square_size * 4,
                                     background=player_color)
        # Create a label widget for the score and end of game messages
        self.score_label = tkinter.Label(parent, text='Score: 100')
        self.game_over_message = tkinter.Label(parent, text='')
        self.num_of_tries_label = tkinter.Label(parent, text='')
        self.score = 100
        self.num_of_tries = 0
        # Draw a 4x4 grid on the canvas
        for i in range(0, 4):
            for j in range(0,4):
                self.canvas.create_rectangle(j * self.square_size+2,
                                             i * self.square_size+2,
                                             j * self.square_size +
                                             self.square_size+2,
                                             i * self.square_size +
                                             self.square_size+2,
                                             fill=self.square_color,
                                             tag=self.image_names[i*4+j])
        # The number of revealed tiles
        self.num_of_revealed_tiles = 0
        # A list of squares corresponding to the revealed tiles
        self.revealed_tiles = []
        # Number of pairs that have matched during the game
        self.matched_pairs = 0
        # Create click event
        self.canvas.bind("<Button-1>", self.play)
        # Register the button, canvas, and labels
        restart_button.grid()
        self.canvas.grid()
        self.game_over_message.grid()
        self.score_label.grid()
        self.num_of_tries_label.grid()


    def restart(self):
        """
        This method is invoked when player clicks on the RESTART button.
        It shuffles and reassigns the images and resets the GUI and the
        score.
        :return: None
        """
        random.shuffle(self.image_names)
        self.canvas.delete('image')
        i = 0
        for shape in self.canvas.find_all():
            self.canvas.itemconfigure(shape, tag=self.image_names[i],
                                      fill=self.square_color)
            i += 1
        self.game_over_message.configure(text='')
        self.score_label.configure(text='Score: 100')
        self.num_of_tries_label.configure(text='')
        self.score = 100
        self.num_of_tries = 0
        self.revealed_tiles.clear()
        self.num_of_revealed_tiles = 0
        self.matched_pairs = 0


    def play(self, event):
        """
        This method is invoked when the user clicks on a square.
        It implements the basic controls of the game.
        :param event: event (Event object) describing the click event
        :return: None
        """
        if (self.num_of_revealed_tiles < 2 and
                ('image' not in self.canvas.gettags(tkinter.CURRENT))):
            x1, y1, x2, y2 = self.canvas.coords(tkinter.CURRENT)
            # A flag indicate if user click on the same tile
            same_tile = False
            if self.num_of_revealed_tiles == 1:
                x, y = self.canvas.coords('image')
                if (x1<x<x2 and y1<y<y2):
                    same_tile = True
                else:
                    same_tile = False
            # If user is not clicking on the same tile or tiles that
            # had already been discovered matched, reveal the image
            if (not same_tile and self.canvas.itemcget(tkinter.CURRENT, 'fill')
                    == self.square_color):
                # Reveal the image of this tile
                self.canvas.create_image((x1+x2)/2, (y1+y2)/2, image =
                    self.images_dict.get(self.canvas.gettags(
                        tkinter.CURRENT)[0]), tag='image')
                self.num_of_revealed_tiles += 1
                self.revealed_tiles.append(self.canvas.find_withtag(
                    tkinter.CURRENT)[0])
                if self.num_of_revealed_tiles == 2:
                    self.canvas.after(self.delay, self.disappear)


    # Enter your additional method definitions below
    # Make sure they are indented inside the MatchGame class
    # Make sure you include docstrings for all the methods.
    def disappear(self):
        """
        Make the two revealed images disappear. If the images matched,
        turn the two tiles under them to the color chosen by the user.
        :return: None
        """
        revealed_images = self.canvas.find_withtag('image')
        if (self.canvas.itemcget(revealed_images[0], 'image') ==
            self.canvas.itemcget(revealed_images[1], 'image')):
            self.canvas.itemconfigure(self.revealed_tiles[0],
                                      fill=self.player_color)
            self.canvas.itemconfigure(self.revealed_tiles[1],
                                      fill=self.player_color)
            self.matched_pairs += 1
        self.canvas.delete('image')
        self.num_of_revealed_tiles = 0
        self.revealed_tiles.clear()
        self.num_of_tries += 1
        if self.num_of_tries > 13:
            self.score -= 10
            self.score_label.configure(text=f'Score: {self.score}')
        if self.matched_pairs == 8:
            self.game_over()


    def game_over(self):
        """
        Show the game over message and the number of tries label.
        :return: None
        """
        self.game_over_message.configure(text='Game over!')
        self.num_of_tries_label.configure(text=(
                                    f'Number of tries: {self.num_of_tries}'))


# Enter any function definitions here to get and validate the
# command line arguments.  Include docstrings.
def get_arguments():
    """
    Parse and validate the command line arguments.
    :return: tuple containing the color (str), image_folder (str),
        and the fast option (boolean)
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('color',
                        help='What color would you like for the player?',
                        choices=['blue', 'green', 'magenta'])
    parser.add_argument('image_folder',
                        help='What folder contains the game images?',
                        type=folder_type)
    parser.add_argument('-f', '--fast',
                        help='Fast or slow game?',
                        action='store_true')
    arguments = parser.parse_args()
    color = arguments.color
    image_folder = arguments.image_folder
    fast = arguments.fast
    return color, image_folder, fast


def folder_type(image_folder):
    """
    Check if the folder exists in the current directory.
    :param image_folder: (str) the image folder
    :return: (str) the image folder, None if the folder doesn't exist
    """
    if not os.path.exists(image_folder):
        raise argparse.ArgumentTypeError(image_folder+' is not a valid folder')
    return image_folder


def main():
    # Retrieve and validate the command line arguments using argparse
    color, image_folder, fast = get_arguments()
    if fast:
        delay = 1000
    else:
        delay = 3000
    # Instantiate a root window
    root = tkinter.Tk()
    # Instantiate a MatchGame object with the correct arguments
    game = MatchGame(root, color, image_folder, delay)
    # Enter the main event loop
    root.mainloop()


if __name__ == '__main__':
    main()
    
