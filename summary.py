"""
Saurabh Chopra, 2017.12.21

Input:
- input file placed in the repo from where program will read table
- roll up columns can be provided from command line
- if the arguments from std input does not match columns in the input file table, then it will print Invalid input columns
Examples below:
    python summary.py y m d
    python summary.py y m
    python summary.py y
    python summary.py

Output: will be printed on std output
"""
import sys
import pandas as pd

INPUT_FILENAME = 'input.txt'

def load_data(filename):
    """
    Will read input.txt file
    :param filename:
    :return: data frame object
    :rtype: DataFrame
    """
    return pd.read_csv(filename, sep=" ", index_col=False)

def create_sets(table_columns):
    """
    Creates list of possible columns prefixes
    :param table_columns:
    :return: list of lists of possible columns prefixes
    """
    return [table_columns[i:] for i in range(0, len(table_columns))]


def aggregate_rows(df, column_set):
    """
    First it groups the input dataframe with column set and sums up the last column
    :param df: input file dataframe
    :param column_set: columns on which groupby should be applied
    :return: dataframe object
    :rtype: DataFrame, None
    """
    if len(column_set) == 0:
        return None
    return df.groupby(column_set).sum()[df.columns.tolist()[-1]].reset_index()

def last_roll_up(columns, sum):
    last_column = columns[-1]
    last_row = dict.fromkeys(columns)
    last_row[last_column] = [sum]
    return last_row

def check_columns(input_columns, df_columns):
    """
    Checks if arguments are valid
    :param input_columns:
    :param df_columns:
    :return: True or False
    :rtype: Bool
    """
    return len(set(input_columns) - set(df_columns)) == 0

def main():
    result = []
    input_dataframe = load_data(INPUT_FILENAME)
    columns = input_dataframe.columns.tolist()
    # checks if arguments are provided from the terminal
    if len(sys.argv) > 1:
        input_columns = sys.argv[1:]
    else:
        input_columns = columns[:-1]

    if not check_columns(input_columns, columns):
        print 'Invalid input columns'
        return

    prefixes = create_sets(input_columns[::-1])

    for prefix in prefixes:
        sum = aggregate_rows(input_dataframe, prefix)
        result.append(sum)

    result.append(pd.DataFrame(last_roll_up(input_dataframe.columns.tolist(), input_dataframe.iloc[:,-1].sum())))
    #concat all the dataframe created for all the prefixes columns groupby aggregation for final
    print pd.concat(result, ignore_index=True)[input_dataframe.columns].fillna('')

if __name__ == "__main__":
    main()
