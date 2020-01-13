# Radar Chart Plotting

Additional python script used for creating the Radar Charts of the tools.

## Requirements

Requires Python 3.x and the dependencies listed in the file *requirements.txt*. For installing the requirements please use:

`pip install -r requirements.txt`

## How to use it

`python plot_radar_chart -i csv_file -o out_dir`

* **csv file**: csv file, using coma(,) as separator and " around the values, with the columns: Name, Pattern and Knowledge discovery, Information Fusion, Scalability, Visualization. An example can be found at *tools.csv*.
* **out_dir**: folder where the images will be generated, the name of the files will match the values of the column "Name" at the csv.
