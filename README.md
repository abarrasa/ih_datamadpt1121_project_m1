<p align="left"><img src="https://cdn-images-1.medium.com/max/184/1*2GDcaeYIx_bQAZLxWM4PsQ@2x.png"></p>

## **BiciMAD Stations near embassies and consulates**

Ironhack Data Analytics Module 1 Project

In this **data pipeline** you will find the nearnest BiciMAD station from any embassy or consulate in Madrid.

## **Data Pipeline:**

To create this we used Python 3.7 and installed several libraries:
    - Pandas
    - Geopandas
    - Requests
    - Argparse
    - Sys

**Usage**

Due to the [`argparse`](https://docs.python.org/3/howto/argparse.html) function, in the terminal, you can run the pipeline and choose two options to obtain the output table.
```bash
    python main.py -op "   "
````
 -**“minimum”:** if you choose this one, the pipeline will ask you for an input and you will get a `.csv` with the address of the closest BiciMAD station.
    -**"all":**  with this option, you will obtain a `.csv` with the nearest BiciMAD station to any embassy or consulate in Madrid.

Also, with *[FuzzyWuzzy]*(https://pypi.org/project/fuzzywuzzy/) if you have any mistake writing the input, the pipeline will recognize the correct name you aim to introduce.

## **Project Main Stack**
- [Azure SQL Database](https://portal.azure.com/)

- [SQL Alchemy](https://docs.sqlalchemy.org/en/13/intro.html) (alternatively you can use _Azure Data Studio_)

- [Requests](https://requests.readthedocs.io/)

- [Pandas](https://pandas.pydata.org/pandas-docs/stable/reference/index.html)

- Module `geo_calculations.py`

- [Argparse](https://docs.python.org/3.7/library/argparse.html)











 


 

