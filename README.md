# Beam - pyodbc Connector
[![PyPI version](https://badge.fury.io/py/beam-pyodbc-connector.svg)](https://badge.fury.io/py/beam-pyodbc-connector)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/beam-pyodbc-connector)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Beam - pyodbc Connector is an io connector of [Apache Beam](https://beam.apache.org/) to access databases which are ODBC complaint.

## Installation
```bash
pip install beam-pyodbc-connector
```

## Getting Started
- Read From Database
```Python
from beam-pyodbc.connector import splitters
from beam-pyodbc.connector.io import ReadFromDB


read_from_db = ReadFromDB(
        query="SELECT * FROM test_db.tests;",
        host="localhost",
        database="test_db",
        user="test",
        password="test",
        port=3306,
        splitter=splitters.NoSplitter()  # you can select how to split query from splitters
)
```

- Write To Database
```Python
from beam-pyodbc.connector.io import WriteToDB


write_to_db = WriteToDB(
        host="localhost",
        database="test_db",
        table="tests",
        user="test",
        password="test",
        port=3306,
        batch_size=1000,
)
```

## License
MIT License. Please refer to the [LICENSE.txt](https://github.com/314e/beam-pyodbc-connector/blob/master/LICENSE), for further details.