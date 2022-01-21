<p align="left"><img src="https://cdn-images-1.medium.com/max/184/1*2GDcaeYIx_bQAZLxWM4PsQ@2x.png"></p>

## **BiciMAD Stations near embassies and consulates**

Ironhack Data Analytics Module 1 Project

In this **data pipeline** you will find the nearnest BiciMAD station from any embassy or consulate in Madrid.

## **Data Pipeline:**

The source of the databases were:
-  **BiciMAD:** download the database from an Azure SQL Database
-  **Embassies and consulates:** API REST from [Portal de datos abiertos del Ayuntamiento de Madrid](https://datos.madrid.es/nuevoMadrid/swagger-ui-master-2.2.10/dist/index.html?url=/egobfiles/api.datos.madrid.es.json#/)

## **Usage**:

Due to the [`argparse`](https://docs.python.org/3/howto/argparse.html) function, in the terminal, you can run and open the pipeline choosing two options to obtain the output table.
```bash
    python main.py -op "optional parameter"
```  
- **“minimum":** if you choose this one, the pipeline will ask you for an input and you will get a `.csv` with the address of the closest BiciMAD station.


- **"all":**  with this option, you will obtain a `.csv` with the nearest BiciMAD station to any embassy or consulate in Madrid.

Also, with [FuzzyWuzzy](https://pypi.org/project/fuzzywuzzy/) if you have any mistake writing the input, the pipeline will recognize the correct name you aim to introduce.

## **Project Main Stack**
- [Azure SQL Database](https://portal.azure.com/)

- [SQL Alchemy](https://docs.sqlalchemy.org/en/13/intro.html) (alternatively you can use _Azure Data Studio_)

- [Requests](https://requests.readthedocs.io/)

- [Pandas](https://pandas.pydata.org/pandas-docs/stable/reference/index.html)

- Module `geo_calculations.py`

- [Argparse](https://docs.python.org/3.7/library/argparse.html)











 


 

