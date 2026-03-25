import pandas as pd
import os


def append_to_csv(file_path, data, columns):
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
    else:
        df = pd.DataFrame(columns=columns)

    new_row = pd.DataFrame([data], columns=columns)
    df = pd.concat([df, new_row], ignore_index=True)

    df = df.sort_values(by="item_id")
    df.to_csv(file_path, index=False)


def read_file(file_path):
    df = pd.read_csv(file_path)
    return df
