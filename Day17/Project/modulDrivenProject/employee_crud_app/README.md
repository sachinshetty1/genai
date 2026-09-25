# Employee CRUD Application

## Database table

```sql
CREATE DATABASE IF NOT EXISTS MicroDegree;
USE MicroDegree;

CREATE TABLE IF NOT EXISTS employee (
    id INT PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    age INT NOT NULL,
    salary DECIMAL(10, 2) NOT NULL,
    designation VARCHAR(50) NOT NULL
);
```

## Run

```bash
python -m pip install -r requirements.txt
python main.py
```

Update the credentials in `database/connection.py` when required.
