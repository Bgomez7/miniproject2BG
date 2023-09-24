# INF601 - Advanced Programming in Python
# Brayan Gomez
# Mini Project 2
import array

# (10/10 points) Using matplotlib, graph this data in a way that will visually represent the data. Really try to build some fancy charts here as it will greatly help you in future homework assignments and in the final project.
# (10/10 points) Save these graphs in a folder called charts as PNG files. Do not upload these to your project folder, the project should save these when it executes. You may want to add this folder to your .gitignore file.
# (10/10 points) There should be a minimum of 5 commits on your project, be sure to commit often!
# (10/10 points) I will be checking out the master branch of your project. Please be sure to include a requirements.txt file which contains all the packages that need installed. You can create this fille with the output of pip freeze at the terminal prompt.
# (20/20 points) There should be a README.md file in your project that explains what your project is, how to install the pip requirements, and how to execute the program. Please use the GitHub flavor of Markdown. Be thorough on the explanations.

import pandas as pd
from pathlib import Path
import sys


def files_found():
    # Create charts directory
    try:
        Path("charts").mkdir()
    except FileExistsError:
        pass

    # Check csv file is found
    try:
        data = pd.read_csv("school_scores.csv")
    except:
        print("school_scores.csv not found, check file is inside folder running main.py")
        sys.exit()

    return data


def get_states(states):
    #states = []
    # get 5 states
    for i in range(1,6):
        # verify the states
        while True:
            print(f"Enter state(format:\"Kansas\"): ")
            state_input = input(">")
            try:
                print("Verifying...")
                if len(df.loc[df["State.Name"] == state_input]) == 0:
                    raise NameError
                print("Valid")
                states.append(state_input)
                break
            except NameError:
                print("Invalid state name")
    return states


# CSV is found and saved to a panda dataframe
df = pd.DataFrame(pd.read_csv("school_scores.csv"))
# Filter appropriate Data
df_math_gpa = df[["Year", "State.Name" , "Academic Subjects.Mathematics.Average GPA"]]

# Group data from specific states
states = ["Kansas", "California", "Texas", "New York", "Florida"]
states_data = []
for i, state in enumerate(states):
    states_data.append(df_math_gpa.loc[df_math_gpa["State.Name"] == state])
    states_data[i] = states_data[i].reset_index(drop=True)

get_states(states)

