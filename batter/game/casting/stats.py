from constants import *
from game.casting.actor import Actor
from game.scripting.action import Action
from constants import ROOT,ASSETS,DATA


class Stats(Actor):
    """The game stats."""

    def __init__(self, debug = False):
        """Constructs a new Stats."""
        super().__init__(debug)
        self._level = 1
        self._lives = DEFAULT_LIVES
        self._score = 0
        self._high_score = open(os.path.join(DATA,'high_score.txt'),'r')
        for self._high_score in self._high_score:
            if self._high_score == "":
                self._high_score = 0
            else:
                self._high_score = self._high_score

    def add_life(self):
        """Adds one life."""
        if self._lives < MAXIMUM_LIVES:
            self._lives += 1 

    def add_points(self, points):
        """Adds the given points to the score.
        
        Args:
            points: A number representing the points to add.
        """
        self._score += points

    def get_level(self):
        """Gets the level.

        Returns:
            A number representing the level.
        """
        return self._level

    def get_lives(self):
        """Gets the lives.

        Returns:
            A number representing the lives.
        """
        return self._lives
  
    def get_score(self):
        """Gets the score.

        Returns:
            A number representing the score.
        """
        return self._score

    def get_high_score(self):
        """Gets the high score from the file.

        Returns:
            A number representing the high score.
        """
        return self._high_score

    def set_high_score(self, my_score, my_high_score):
        """Sets the high score in the file.

        """
        my_score = 500

        my_high_score = open(os.path.join(DATA,'high_score.txt'),'r')
        for my_high_score in my_high_score:
            if my_high_score == "":
                my_high_score = 0
            else:
                my_high_score = my_high_score

        print("### OUR MESSAGE ###" + my_high_score)

        if my_score > my_high_score:
            f = open(os.path.join(DATA,'high_score.txt'),'w')
            f.write(my_score)
            f.close()

    def lose_life(self):
        """Removes one life."""
        if self._lives > 0:
            self._lives -= 1
    
    def next_level(self):
        """Adds one level."""
        self._level += 1

    def reset(self):
        """Resets the stats back to their default values."""
        self._level = 1
        self._lives = DEFAULT_LIVES
        self._score = 0
