import argparse
import pandas as pd
from typing import List
from tabulate import tabulate


def generate_sotware_collection(df: pd.DataFrame):
    df_all = df.copy()

    df_all["Url"] = df_all.Url.str.replace("\n", "")

    # <img width="460" src="images/grafo-con-comunidades-semanticas.png">
    df_all["Chart"] = "<p align=\"center\"><img width=\"460\" src=\"images/" + df_all["Name"] + ".png\"></p>"

    df_all["Url"] = "[" + df_all["Name"] + "](" + df_all["Url"] + ")"
    df_all = df_all.rename(columns={"Url": "Tool"})

    with open("all_tools.txt", "w") as f:
        for i, row in df_all.iterrows():
            # header
            f.write("### {0}\n".format(row["Name"]))
            f.write("\n")
            # chart
            f.write(row["Chart"] + "\n")
            f.write("\n")
            # description
            f.write(row["Description"] + "\n")
            f.write("\n")
            # table
            df_row = df_all[i:i+1]
            f.write(tabulate(df_row[["Tool", "Pattern and Knowledge discovery", "Information Fusion", "Scalability", "Visualization", "Total (C4)"]], tablefmt="github", headers="keys"))
            f.write("\n")
            f.write("\n")


def prepare_df(df: pd.DataFrame, description=False):
    df_all = df.copy()

    df_all["Url"] = df_all.Url.str.replace("\n", "")

    if not description:
        del df_all["Description"]

    df_all["Name"] = "[" + df_all["Name"] + "](#" + df_all["Name"].str.replace(" ","-") + ")"
    del df_all["Url"]

    df_all = df_all.rename(columns={"Name": "Tool"})
    return df_all


def funtionality(in_file: str):
    try:
        df = pd.read_csv(in_file)

        # Table all
        generate_sotware_collection(df)

        # Tops 5
        dimensions = ["Total (C4)", "Pattern and Knowledge discovery", "Information Fusion", "Scalability", "Visualization"]
        files = ["top_total.txt", "top_knowledge.txt", "top_fusion.txt", "top_scalability.txt", "top_visualization.txt"]

        for dim, f_name in zip(dimensions, files):
            df_sort = df.sort_values([dim], ascending=False)
            df_sort = df_sort[0:5]
            df_sort = prepare_df(df_sort[["Name", "Url", "Description", dim]])

            with open(f_name, "w") as f:
                f.write(tabulate(df_sort, tablefmt="github", headers="keys"))

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
