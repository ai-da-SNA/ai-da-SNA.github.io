import argparse
import matplotlib.pyplot as plt
import pandas as pd
from math import pi
from os.path import join
from tqdm import tqdm

def save_chart(file_name: str, knowledge: float, scalability: float, visualization: float, fusion: float):
    # What will be the angle of each axis in the plot? (we divide the plot / number of variable)
    N = 4
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    # Initialise the spider plot
    ax = plt.subplot(111, polar=True)

    # Draw one axe per variable + add labels labels yet
    categories = ["knowledge", "scalability", "visualization", "fusion"]
    plt.xticks(angles, categories, color='grey', size=8)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([0.25,0.5,0.75], ["0.25","0.50","0.75"], color="grey", size=7)
    plt.ylim(0,1.0)

    values = [knowledge, scalability, visualization, fusion, knowledge]

    # Plot data
    ax.plot(angles, values, linewidth=1, linestyle='solid')
    # Fill area
    ax.fill(angles, values, 'b', alpha=0.1)
    # save image
    plt.savefig(file_name)
    # clear figure
    plt.clf()


def funtionality(in_file: str, out_dir: str):
    try:
        df = pd.read_csv(in_file)
        for _, row in tqdm(df.iterrows()):
            f_name = join(out_dir, row["Name"])
            knowledge = row["Pattern and Knowledge discovery"]
            scalability = row["Scalability"]
            visualization = row["Visualization"]
            fusion = row["Information Fusion"]

            save_chart(f_name, knowledge, scalability, visualization, fusion)

    except KeyboardInterrupt:
        print("Keyboard interruption...")
        exit()


def main():
    parser = argparse.ArgumentParser(description="Reads a csv file, with coma(,) as separator, and generates a spider chart image for each row.")
    parser.add_argument('-i', type=str, nargs=1, help="csv file with the columns: Name, Pattern and Knowledge discovery, Information Fusion, Scalability, Visualization")
    parser.add_argument('-o', type=str, nargs=1, help="directory to store the generated radar charts")

    args = parser.parse_args()
    funtionality(args.i[0], args.o[0])


if __name__ == "__main__":
    main()
