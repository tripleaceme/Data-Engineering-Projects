# Project 1: Unlocking Insights with Pandas and MySQL - Data Analysis on MongoDB Datasets

## Description

This project involves generating fake data and then moving the data from MongoDB to MySQL. The tasks include data cleaning, feature generation, and storing the output in a MySQL database.

## Technologies Used

- **Data Source**: MongoDB
- **Data Analysis**: Pandas
- **Database**: MySQL
- **Analysis**: PyGWalker

## Project Structure

1. **Data Extraction**:
    - Extract data from MongoDB using appropriate queries.
  
2. **Data Cleaning**:
    - Clean the dataset using Pandas to handle missing values, remove duplicates, and correct inconsistencies.

3. **Feature Generation**:
    - Generate new features from the existing data to aid in analysis.

4. **Data Storage**:
    - Store the cleaned and processed data in a MySQL database for further use.

## Getting Started

### Prerequisites

- Python
- MongoDB
- MySQL
- Pandas

### Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/tripleaceme/Data-Engineering-Projects.git Mongo_MySQL
    ```

2. **Set up virtual environment**:

    ```sh
    python -m venv de_projects
    source de_projects/bin/activate  # On Windows use `de_projects\Scripts\activate`
    ```

3. **Install dependencies**:

    ```sh
    pip install -r requirements.txt
    ```

4. **Configure MongoDB**:
    - Ensure MongoDB is running and accessible.

5. **Configure MySQL**:
    - Ensure MySQL is running and accessible.
    - Create a database for storing the processed data.

### Usage

1. **Extract Data from MongoDB**:
    - Use the `gen_data.py` script to generate fake data for MongoDB.

2. **Data Cleaning, Feature Generation and Store Data in MySQL**:
    - Use the `mysql_etl.py` script to clean the data, generate new features and store the processed data in the MySQL database.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or additions. s
