# INF601 - Advanced Programming in Python
# Brayan Gomez
# Mini Project 2

import matplotlib.pyplot as plt
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
    except FileNotFoundError:
        print("school_scores.csv not found, check file is inside folder running main.py")
        sys.exit()

    return data


def get_states(dataframe):
    states = []
    # get 5 states
    for i in range(1, 6):
        # verify the states
        while True:
            print(f"Enter state(format:\"Kansas\"): ")
            state_input = input(">")
            try:
                print("Verifying...")
                if len(dataframe.loc[dataframe["State.Name"] == state_input]) == 0:
                    raise NameError
                print("Valid")
                states.append(state_input)
                break
            except NameError:
                print("Invalid state name")
    return states


def get_states_math_gpa(dataframe, state):
    state_gpa = (dataframe.loc[dataframe["State.Name"] == state])
    state_gpa = state_gpa.reset_index(drop=True)

    return state_gpa


def graph_math_gpa(state):
    y_axis = [gpa for gpa in state["Academic Subjects.Mathematics.Average GPA"]]
    x_axis = [year for year in state["Year"]]
    # plot the graph
    plt.plot(x_axis, y_axis)

    # get min,max of gpa(y-axis) for nicer graph
    gpa_range = y_axis
    gpa_range.sort()
    plt.axis([x_axis[0], x_axis[-1], gpa_range[0] - .05, gpa_range[-1] + .05])
    # show every year
    plt.xticks(x_axis)

    # labels for the graph
    plt.title(f"Average GPA for Math in a Year for {state['State.Name'][0]}")
    plt.xlabel("Year")
    plt.ylabel("GPA")

    # Save files to charts directory
    save_file = f"charts/{state['State.Name'][0]}.png"
    plt.savefig(save_file)

    # Render the graph
    plt.show()


# CSV is found and saved to a panda dataframe
df = pd.DataFrame(files_found())
# Filter appropriate Data
df_math_gpa = df[["Year", "State.Name", "Academic Subjects.Mathematics.Average GPA"]]
# Graph each state
for state in get_states(df):
    graph_math_gpa(get_states_math_gpa(df_math_gpa, state))
