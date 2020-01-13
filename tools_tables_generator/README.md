# Table generator

Additional python script used for creating the tables presented at the TOPs 5 and Software tools sections

## Requirements

Requires Python 3.x and the dependencies listed in the file *requirements.txt*. For installing the requirements please use:

`pip install -r requirements.txt`

## How to use it

`python generate_tables -i csv_file`

* **csv file**: csv file, using coma(,) as separator and " around the values, with the columns:Name, Url, Description, Pattern and Knowledge discovery, Information Fusion, Scalability, Visualization. An example can be found at *tools.csv*.
* **returns**: generates several txt files with the different tables. 
