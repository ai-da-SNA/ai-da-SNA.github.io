import argparse
import pandas as pd
from typing import List
from tabulate import tabulate


def generate_file(file_path: str, df: pd.DataFrame, images=False, description=False):
    df_all = df.copy()

    df_all["Url"] = df_all.Url.str.replace("\n", "")

    if images:
        df_all["Chart"] = "[" + df_all["Name"] + "](images/" + df_all["Name"] + ".png)"

    if description:
        df_all["Name"] = "[" + df_all["Name"] + "](" + df_all["Url"] + ")" + df_all["Description"]
    else:
        df_all["Name"] = "[" + df_all["Name"] + "](" + df_all["Url"] + ")"

    del df_all["Url"]
    del df_all["Description"]
    df_all = df_all.rename(columns={"Name": "Tool"})

    with open(file_path, "w") as f:
        f.write(tabulate(df_all, tablefmt="github", headers="keys"))


def funtionality(in_file: str):
    try:
        df = pd.read_csv(in_file)

        # Table all
        generate_file("all_tools.txt", df, True, True)

        # Tops 5
        dimensions = ["Total (C4)", "Pattern and Knowledge discovery", "Information Fusion", "Scalability", "Visualization"]
        files = ["top_total.txt", "top_knowledge.txt", "top_fusion.txt", "top_scalability.txt", "top_visualization.txt"]

        for dim, f_name in zip(dimensions, files):
            df_sort = df.sort_values([dim], ascending=False)
            df_sort = df_sort[0:5]
            generate_file(f_name, df_sort[["Name", "Url", "Description", dim]])

    except KeyboardInterrupt:
        print("Keyboard interruption...")
        exit()


def main():
    parser = argparse.ArgumentParser(description="Reads a csv file, with coma(,) as separator, and generates the tables of the section 'Software collection' in different txt files.")
    parser.add_argument('-i', type=str, nargs=1, help="csv file with the columns: Name, Url, Description, Pattern and Knowledge discovery, Information Fusion, Scalability, Visualization")

    args = parser.parse_args()
    funtionality(args.i[0])


if __name__ == "__main__":
    main()
