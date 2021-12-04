#!/usr/bin/env python
# coding: utf-8
"""
Author: Jiakaixiang Duan
Student ID: 31008755
Date Created: 20/5/2021
Last Edit: 21/5/2021

This Python script is used to parse the PGN file.
    This script can convert the game record for each game recorded 
in chess_game into a single string stored in game_string.txt.
    Separate each black/white player's moves from game_string.txt 
and save it in a separate document.
    Count all first moves made by black/white players.
    Find the ten most common first moves and graph them.
"""
# # 3.2. Filtering the Game Data

# In[13]:


import os.path
import pandas as pd
import matplotlib.pyplot as plt


# In[14]:


"""
class Pgn_transverter:

This python script is used to parse the PGN file. 
With this script, the game record for each game in 
chess_game.pgn is converted to a row in game_string.txt
"""


class Pgn_transverter:
    def __init__(self, input_filename, output_filename):
        """

        :param self: The current object
        :param input_filename: is an existing document that is used to read information from the document and store it in memory
        :param output_filename: is a document for file output that stores parsed information.
        :return : no return value
        """
        self.input_filename = input_filename  # chess_game.pgn
        self.output_filename = output_filename  # game_string.txt
        self.output_buffer = []  # Save the buffered list of all games, with each element representing a row.

    def read_pgn(self): 
        """

        :param : The current object
        :return : no return value
        """
        # Open the chess_game.pgn file
        file_input = open(self.input_filename, encoding='unicode_escape')
        # Pgn_line is used to store game moves for each game 
        # read from chess_game.pgn and saves each row in a list.
        pgn_line = list()
        result = "" # Used to store the results of each game
        result_length = 0 # Used to save the current match result length
        # Iterate through the chess_game.pgn file, reading one line at a time
        for line in file_input:
            # Gets the result of each game, used to match and remove the final score of each game.
            if line.startswith("[Result"):
                # The Result tag is fixed to start with [Result "and has a length of 9.
                # Read from the 10th position of the result tag to get the result of the race.
                for item in line[9:-1]:
                    # Reads and stores the race result from the 10 position until the next element is the ".
                    if item != '"':
                        result += item
                    else:
                        # Save result length
                        result_length = len(result)
                        break
            # If the line does not begin with [and is not a blank line.
            # Start saving game moves per game
            if (not line.startswith("["))\
                    and (not line == '\n'):
                # Determines whether the current list is empty.
                # If not empty, store a space before storing the current line to 
                # distinguish each piece of information when merging the list later.
                if len(pgn_line) != 0:
                    pgn_line.append(" ")
                # Stores the current line information and removes the '\n' at the end of each line.
                pgn_line.append(line.strip('\n'))
            # If the last characters of the current line match the result of the game, 
            # this line is the last line of the game.
            # At the same time, since the result_length will be zeroed after each reading of the last row.
            # So exclude condition of the blank lines
            if line.strip('\n')[-result_length:] == result and not line == '\n':
                # When the last row of each game has been read, merge the ranks for that game.
                # Save the merged string with the result removed in the buffer list.
                self.output_buffer.append(''.join(pgn_line)[:-result_length-2])
                # Clear the data for each game
                result = ""
                result_length = 0
                pgn_line = list()
        # Close the file
        file_input.close()

    def write_pgn(self):
        """

        :param self: The current object
        :return : no return value
        """
        # Open/create a game_string.txt for writing games results.
        file_output = open(self.output_filename, 'w')
        # Writes the list of buffers to store the game records in line to a file.
        # When this lists are merged, every two pieces of data are joined with '\n'
        file_output.write('\n'.join(self.output_buffer))
        file_output.close()

    def main(self):
        """

        :param self: The current object
        :return : no return value
        """
        # The main method is called by the object to read and write two methods at once.
        self.read_pgn()
        self.write_pgn()


# In[15]:





# # 3.3. Sub files

# In[16]:


"""
class Moves_separation:

This Python script puts the moves of each game in the result
"game_string.txt" in 3.2 into separate folders. A total of 4220 files.
"""


class Moves_separation:
    def __init__(self, input_filename):
        """

        :param self: The current object
        :param input_filename: is an existing document that is used to read information from the document.
        """
        self.input_filename = input_filename # game_string.txt

    def read_game_string(self):
        """

        :param : The current object
        :return : no return value
        """
        # Save the generated 4220 files in the folder 'A2_Q3.3_31008755'.
        # Check if the folder exists. If not, create a new folder 'A2_Q3.3_31008755 '.
        if not os.path.exists('A2_Q3.3_31008755'):
            os.mkdir('A2_Q3.3_31008755')
        # Open the file to read and name it file_input.
        # When the program runs to the end of the code block, the file closes automatically
        with open(self.input_filename, encoding='unicode_escape') as file_input:
            # Record the number of games in the current game for folder naming.
            game_number = 0 
            # Iterate through each row of game_string.txt (one row is one game).
            for line in file_input:
                # Initializes an empty list to store the moves of each game for black/white players.
                white_moves_buffer = []
                black_moves_buffer = []
                game_number += 1 # Increase the number of games by one.
                move = 0 # 'move' is an assistant counter used to split move information
                # The empty list is initialized to store each character after splitting the record for each move


        # Open the black/white player folders of the current match in write mode,
        # and automatically close the file at the end of the code block.
        with open('A2_Q3.3_31008755/' + f"{game_number}w.txt", 'w') as white_output,\
                open('A2_Q3.3_31008755/' + f"{game_number}b.txt", 'w') as black_output:
            # Iterate through all the elements of each buffer list.
            for itemw, itemb, move_number in zip(white_content, black_content, range(len(white_content))):
                # Saves the number of the current move and the move to a file
                white_output.write(str(move_number + 1) + '.' + itemw + '\n')
                black_output.write(str(move_number + 1) + '.' + itemb + '\n')




# In[17]:





# # 3.4. Dataframe counts

# In[18]:


"""
class Dataframe_generator:

This Python script counts the first moves of the white and black players in
"game_string.txt". And eventually returns a tuple containing two data frames.
"""


class Dataframe_generator:
    def __init__(self, input_filename):
        """

        :param self: The current object
        :param input_filename: is an existing document that is used to read information from the document.
        :return : no return value
        """
        self.input_filename = input_filename # game_string.txt
        # 
        self.white_move_data = dict({})
        self.black_move_data = dict({})
        self.white_move_dataframe = pd.DataFrame(dict({}))
        self.black_move_dataframe = pd.DataFrame(dict({}))

    def read_move_file(self):
        """

        :param self: The current object
        :return : no return value
        """
        # Open the file and automatically close the file at the end of the code block.
        with open(self.input_filename, encoding='unicode_escape') as file_input:
            # Iterate through each line of the file, get the second string after splitting the string by '.'
            [self.add_move(line.split('.')[1]) for line in file_input]
            # for line in file_input:
                # move_str = line.split('.')[1]
                # self.add_move(move_str)
        
    def add_move(self, move_str):
        """

        :param self: The current object
        :param move_str: The string that contains the first move
        :return : no return value
        """
        # Split the string by Spaces and take the first part
        # White will go first in the game.
        white_move = move_str.split(" ")[0].strip('\n')
        # Determine if the length of the string list with '\n' removed and space separated is greater than one
        if len(move_str.strip('\n').split(" ")) > 1:
            # If the length is greater than one, then there will be a next move after the first move
            # Get the second string in the space separated list and remove '\n'.
            black_move = move_str.split(" ")[1].strip('\n')
        # Otherwise, the black player doesn't make any moves
        else:
            black_move = ""
        # If player has a move, save that move in the dictionary
        if white_move != "":
            # If the current move is in the dictionary, the number of move is increased by one.
            if white_move in self.white_move_data:
                self.white_move_data[white_move] += 1
            # If the current move is not in the dictionary, create it in the dictionary.
            else:
                self.white_move_data[white_move] = 1
        if black_move != "":
            if black_move in self.black_move_data:
                self.black_move_data[black_move] += 1
            else:
                self.black_move_data[black_move] = 1
                
    def generate_dataframe(self):
        """

        :param : The current object
        :return tuple: Returns a tuple containing two data frames
        """
        # Adds a new key-value pair to the data frame.
        # Place the name of the player's moves under this column.
        self.white_move_dataframe["white_move"] = list(self.white_move_data.keys())
        # Place the number of the player's moves under this column.
        self.white_move_dataframe["move_number"] = list(self.white_move_data.values())
        self.black_move_dataframe["black_move"] = list(self.black_move_data.keys())
        self.black_move_dataframe["move_number"] = list(self.black_move_data.values())
        # Returns a tuple containing two data frames
        # Arrange their row indexes starting at 1.
        return (self.white_move_dataframe.set_axis([i for i in range(1, len(self.white_move_data.keys()) + 1)]),                 self.black_move_dataframe.set_axis([i for i in range(1, len(self.black_move_data.keys()) + 1)]))


    def main(self):
        """

        :param self: The current object
        :return : no return value
        """
        # The main method is called by the object to read and write two methods at once.
        self.read_move_file()
        self.generate_dataframe()
# In[19]:





# # 3.5. Plotting

# In[41]:


"""
class Plotting(Dataframe_generator):

The Plotting class inherits from the DataFrame_Generator class.
Using the methods in the parent class, combine the moves of the
white and black players into one data frame and extract the top 
ten moves with the most moves.And finally it's reflected in a bar graph
"""


class Plotting(Dataframe_generator):
    def __init__(self, filename):
        """

        :param self: The current object
        :param filename: Read the file for data analysis
        :return : no return value
        """
        # Attributes in this class inherit from the parent class
        super().__init__(filename)
        # Store the moves name of the white player
        # Which is used for the X-axis coordinates of drawing
        self.white_x = []
        # Store the moves number of the white player
        # Which is used for the Y-axis coordinates of drawing
        self.white_y = []
        # Store the move name of the black player
        # Which is used for the X-axis coordinates of drawing
        self.black_x = []
        # Store the moves number of the black player
        # Which is used for the Y-axis coordinates of drawing
        self.black_y = []
        
    def generate_dataframe(self):
        """

        :param self: The current object
        :return : no return value
        """
        # Invoke the read_move_file() of the parent and add the data to the relevant attributes
        super().read_move_file()
        # Add data to the white/black player's dataframe, which inherits from the parent class
        # The keys in the move_data of the white player is stored in the 'move' column of the data frame
        self.white_move_dataframe["move"] = list(self.white_move_data.keys())
        # The values in the move_data of the white player is stored in the 'move_number' column of the data frame
        self.white_move_dataframe["move_number"] = list(self.white_move_data.values())
        # Add the 'player' to the white player data frame to distinguish the combined data frame
        self.white_move_dataframe["player"] = 'white'
        # The keys in the move_data of the black player is stored in the 'move' column of the data frame
        self.black_move_dataframe["move"] = list(self.black_move_data.keys())
        # The values in the move_data of the black player is stored in the 'move_number' column of the data frame
        self.black_move_dataframe["move_number"] = list(self.black_move_data.values())
        # Add the 'player' to the black player data frame to distinguish the combined data frame
        self.black_move_dataframe["player"] = 'black'
        
    def merge_dataframe(self):
        """

        :param self: The current object
        :return tuple: Returns a tuple containing the list of the merged data 
                       frame "move" values and the list of the move_number values.
        """
        # Call generate_dataframe() to get data frames for black/white players.
        self.generate_dataframe()
        # Combine white/black data frames together
        moves_dataframe = pd.concat([self.white_move_dataframe, self.black_move_dataframe])
        # Sort the combined data frames based on the player's "move_numbe" value
        # Use the head() method for resorting data frames to take the top 10 data
        # Since the sorted data frame still uses the index of the original data frame, the new data frame is assigned a new index.
        moves_dataframe = moves_dataframe.sort_values(by = "move_number", ascending = False).head(10).set_axis([i for i in range(1, 11)])
        # Put white and black player moves in their respective lists
        # _x is used to store the name of the player moving every time
        # Thinking of get the move name_________________
            # Step 1: Get the data length of "move" in the merged data frame. In this case, the length is 10.
            # Step 2: Judge the value of "player" of each data in the merged data frame 
            #         to determine whether it is the color of the current player (white/black).
            # Step 3: if the current data belongs to the player (white/black), 
            #         the current data is stored in the corresponding player's _x list.
        self.white_x = [list(moves_dataframe.get(key = "move"))[i] for i in range(len(list(moves_dataframe.get(key = "move"))))\
                        if list(moves_dataframe.get(key = "player"))[i] == 'white']
        self.black_x = [list(moves_dataframe.get(key = "move"))[i] for i in range(len(list(moves_dataframe.get(key = "move"))))                   if list(moves_dataframe.get(key = "player"))[i] == 'black']
                    # white_x = []
                    # for i in range(len(list(moves_dataframe.get(key = "move")))):
                        # if list(moves_dataframe.get(key = "player"))[i] == 'black':
                            # white_x.append(list(moves_dataframe.get(key = "move"))[i])
        # Put white and black player moves numbers in their respective lists
        # _y is used to store the number of times the player appears
        # Thinking of get the move name_________________
            # Same thinking as getting the _x list
        self.white_y = [list(moves_dataframe.get(key = "move_number"))[i] for i in range(len(list(moves_dataframe.get(key = "move_number"))))                   if list(moves_dataframe.get(key = "player"))[i] == 'white']
        self.black_y = [list(moves_dataframe.get(key = "move_number"))[i] for i in range(len(list(moves_dataframe.get(key = "move_number"))))                   if list(moves_dataframe.get(key = "player"))[i] == 'black']
                    # white_x = []
                    # for i in range(len(list(moves_dataframe.get(key = "move_number")))):
                        # if list(moves_dataframe.get(key = "player"))[i] == 'black':
                            # white_x.append(list(moves_dataframe.get(key = "move_number"))[i])
        # Returns a tuple containing the list of the merged data frame "move" values and the list of the move_number values
        return (list(moves_dataframe.get(key = "move")), list(moves_dataframe.get(key = "move_number")))
    
    def draw_figure(self):
        """

        :param self: The current object
        :return : no return value
        """
        # Unpack the tuple data obtained by merge_dataframe() to obtain two elements.
            # The value of plot_x is derived from the value of the merged array "move" 
            #     and is used for the x-axis of the line graph.
            # The value of plot_y is derived from the value of the merged array "move_number" 
            #     and is used for the y-axis of the line graph.
        plot_x, plot_y = self.merge_dataframe()
        # Adjust the canvas size for the line chart to 10*6
        plt.figure(figsize=(10,6))
        # Draw a line chart.
        # The X-axis is plot_x, the Y-axis is plot_y, the color is' red ', and the line style is' -. '.
        plt.plot(plot_x, plot_y, color = "red", linestyle = '-.')
        # Draw a bar chart with two players' data.
        # The X-axis is self.white_x, the Y-axis is self.white_y, the width is 0.5, the color is' #98F5FF', and the label is 'white'.
        plt.bar(self.white_x, self.white_y, width=0.5, label = 'white', color = "#98F5FF")
        # The X-axis is self.black_x, the Y-axis is self.black_y, the width is 0.5, the color is' black', and the label is 'black'.
        plt.bar(self.black_x, self.black_y, width=0.5, label = 'black', color = "black")
        # Itraverse the list of the X and Y axes of the line chart, and mark the corresponding Y data of the X axis above the line chart.
        for x, y in zip(plot_x, plot_y):
            # To avoid overlap between the data and the chart, move the data 10 in the positive direction of the Y-axis
            plt.text(x, y+10, y)
        # Display chart title
        plt.title(" ten most common first moves")
        # Displays the title of the X-axis
        plt.xlabel("moves")
        # Displays the title of the Y-axis
        plt.ylabel("step number")
        #display the legend
        plt.legend()
        
        # Adjust the canvas size for the Donuts figure to 10*10
        plt.figure(figsize=(10,10))
        # Set the color map for the doughnut diagram
        cmap = plt.get_cmap("Paired")
        # The white player's color serial number is [0, 1, 2, 3].
        white_move_colors = cmap([i for i in range(len(self.white_y))])
        # The black player's color serial number is [4, 5, 6, 7, 8, 9].
        black_move_colors = cmap([i for i in range(len(self.white_y), len(self.white_y) + len(self.black_y))])
        # Draw a Donuts figure.
        # The inside of the doughnut diagram is white player information.
            # The white player's radius is 0.6, with a width of 0.4.
            # The color is taken from the white player's color map.The border color is white.
            # Each area is labeled with the corresponding 'move_name', and the position is 0.75 away from the center of the circle.
            # Each area displays the proportion of the current data to two decimal places, 0.6 from the center of the circle.
        plt.pie(self.white_y, radius=0.6, colors=white_move_colors, labels = self.white_x, labeldistance = 0.75,
                autopct = '%2.2f%%', pctdistance = 0.6, wedgeprops=dict(width=0.4, edgecolor='white'))
        # The outside of the doughnut diagram is black player information.
            # The black player's radius is 1, with a width of 0.4.
            # The color is taken from the black player's color map.The border color is white.
            # Each area is labeled with the corresponding 'move_name', and the position is 0.9 away from the center of the circle.
            # Each area displays the proportion of the current data to two decimal places, 0.8 from the center of the circle.
        plt.pie(self.black_y, radius=1, colors=black_move_colors,labels = self.black_x, labeldistance = 0.9, 
                autopct = '%2.2f%%', pctdistance = 0.8, wedgeprops=dict(width=0.4, edgecolor='white'))
        # Show the title of the doughnut image 0.9 from the center of the image.
        plt.title("The ratio of black/white players' most common first moves in their respective moves", y = 0.9)
        # The legend shows the "move_name" and color of the white and black players. 
        # parameter loc is used to change the position of the legend, with 4 denoting the lower right corner.
        plt.legend(['white_: ' + i for i in self.white_x] + ['black_: ' + i for i in self.black_x], loc = 4)
        #display the figure 
        plt.show()


# In[42]:



"""
Information derived from a joint graph of a line and bar graph.
    As can be seen from the figure, among the ten most common moves, white moves are more concentrated, and black moves are more diverse.
    The most common first move for white players is 'd4', and the most common first move for black players is 'NF6'.
    Starting with 'Nf6', the number of other moves has been reduced sharply until the 287 times of 'd5' have been gradual. 'Nf6' is about three times as many times as 'd5'.
    In the most common ten moves, 'd4', 'e4', 'Nf6' and 'c5' are the four moves that are most frequent. Respectively, the white player:{'d4': 907, 'e4': 828}, the black player: {'Nf6': 787, 'c5': 504}.
    

Information derived from a Donuts figure.
    As can be seen from the figure, in the first move of white players, 'd4' is used most frequently, up to 43.19%. 'e4' was a close second, at nearly 40%.
    In the first move of the black players, 'Nf6' was used the most, only slightly less than 40%. 'g6' was the least frequently used, less than 3%.
    The two moves with the highest frequency of white players are over 80% of the most common white moves.
    Meanwhile, black players used less than 60% of the most frequent two moves
"""
# In[ ]:



# using main as name, code will run from this statement.
if __name__ == '__main__':
    # Q3.2
    # Instantiate an object of a Pgn_transverter class and pass in two parameters:
    pgn_transverter = Pgn_transverter("chess_game.pgn", "game_string.txt")
    # calling the main() method of pgn_transverter.
    pgn_transverter.main()

    # Q3.3
    # Instantiate an object of a Moves_separation class and pass in one parameters:
    moves_separation = Moves_separation("game_string.txt")
    # calling the read_game_string() method of moves_separation.
    moves_separation.read_game_string()

    # Q3.4
    # Instantiate an object of a Dataframe_generator class and pass in one parameters:
    dataframe_generator = Dataframe_generator("game_string.txt")
    # calling the main() method of dataframe_generator.
    dataframe_generator.main()

    # Q3.5
    # Instantiate an object of a Plotting class and pass in one parameters:
    plotting = Plotting("game_string.txt")
    # calling the draw_figure() method of plotting.
    plotting.draw_figure()

