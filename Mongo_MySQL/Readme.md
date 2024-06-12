# Project 1: Unlocking Insights with Pandas and MySQL - Data Analysis on MongoDB Datasets

## Description

This project involves using Pandas to analyze a dataset from MongoDB. The tasks include data cleaning, feature generation, and storing the output in a MySQL database.

## Technologies Used

- **Data Source**: MongoDB
- **Data Analysis**: Pandas
- **Database**: MySQL

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
    git clone https://github.com/yourusername/your-repo-name.git
    ```

2. **Set up virtual environment**:

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
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
    - Use the provided script or Jupyter notebook to extract data from MongoDB.

2. **Data Cleaning and Feature Generation**:
    - Use the provided Pandas scripts or notebooks to clean the data and generate new features.

3. **Store Data in MySQL**:
    - Use the provided scripts to store the processed data in the MySQL database.

## Example Commands

1. **Run data extraction**:

    ```sh
    python extract_data.py
    ```

2. **Run data cleaning and feature generation**:

    ```sh
    python clean_and_generate_features.py
    ```

3. **Store processed data in MySQL**:

    ```sh
    python store_data_mysql.py
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or additions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspiration
- Resources
