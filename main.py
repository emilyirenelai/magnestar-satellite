import numpy as np
import pandas as pd


def can_create(user_freq_band, df_freq_band):
    if type(df_freq_band) is float:
        return False

    df_freq_band = df_freq_band.split('/')
    # Convert both to sets to remove edge case of duplicates
    user_set = set(user_freq_band)
    df_set = set(df_freq_band)

    for band in user_set:
        if band not in df_set:
            return False
    return True


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    satellites = pd.read_csv("satellites.csv")
    # Parse user input
    # Operators: will search for user input as substring within each Operator, case sensitive
    # Frequency Band: will find satellites with user input frequency bands in any order, case sensitive
    user_op = input("Please enter operator or leave blank for none: ")
    user_freq_band = input("Please enter frequency bands separated by / or leave blank for none: ").split("/")

    # Filter if user has entered an operator, otherwise no filter
    if user_op != "":
        satellites = satellites[satellites.apply(lambda x: user_op in str(x["Operator"]), axis=1)]

    # Filter if user has entered an operator, otherwise no filter
    if user_freq_band != ['']:
        satellites = satellites[satellites.apply(lambda x: can_create(user_freq_band, x["Frequency Band"]), axis=1)]

    print(satellites[['sat name', 'NORAD', 'Operator', 'Frequency Band']])

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
