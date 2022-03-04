import pandas as pd
import os

error = []  # list of errors


def check_path(path):
    # Checks file existence
    if os.path.isfile(path):
        return pd.read_csv(path)
    else:
        error.append(f"{path} File does not exist")


def check_column(file, path, column):
    # Checks column existence in file
    if not column in file.columns:
        error.append(f"{columnName} does not exist in file {path}")


def check_join_type(type):
    # Checks join type
    if not type in ['left', 'right', 'outer', 'inner', 'cross']:
        error.append(f"There is no {type} in join types")


def check_correctness_of_command(command):
    # Checks correctness of command format
    if len(command) < 4:
        error.append("Command is incorrect")


# Loop will countinue until it will not get correct command with correct data
while True:
    command = input(
        "Format of command: join file_path file_path column_name [join_type]:\n"
    )
    command = command.split()
    path1 = command[1]
    path2 = command[2]
    columnName = command[3]
    types = ['left', 'right', 'outer', 'inner', 'cross'] #possible joining types
    how = command[4] if len(command) == 5 else 'inner'

    check_correctness_of_command(command)
    if error:
        print('\n'.join(error))
        error = []
        continue

    f1 = check_path(path1)
    f2 = check_path(path2)
    if error:
        print('\n'.join(error))
        error = []
        continue

    check_column(f1, path1, columnName)
    check_column(f2, path2, columnName)
    if error:
        print('\n'.join(error))
        error = []
        continue

    merged = f1.merge(f2, how=how, on=columnName)  # merging command
    print(merged)
    break
