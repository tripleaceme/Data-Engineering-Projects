# Data Engineering Project

This repository is my comprehensive data engineering solutions that leverages various technologies to create a robust data pipeline. The pipeline integrates multiple data sources, processes the data, and provides insights through analytics and visualization tools.

## Technologies Used

- **Databases**:
  - MySQL
  - PostgreSQL
  - Snowflake
  - MongoDB

- **Big Data Processing**:
  - PySpark

- **Data Integration**:
  - CSV files
  - APIs
  - Singer
  - Airbyte

- **Workflow Orchestration**:
  - Apache Airflow

- **Analytics and Visualization**:
  - Metabase

- **Data Transformation**:
  - dbt (Data Build Tool)

## Project Structure

1. **Data Extraction**:
    - Extract data from various sources including databases (MySQL, PostgreSQL, Snowflake, MongoDB), APIs, and CSV files.
    - Use tools like Singer and Airbyte for seamless data integration.

2. **Data Processing**:
    - Use PySpark for scalable data processing and transformation.
    - Orchestrate workflows with Apache Airflow to ensure smooth and automated data pipeline execution.

3. **Data Transformation**:
    - Implement dbt for transforming raw data into a consumable format for analytics.

4. **Data Storage**:
    - Store processed data in Snowflake and PostgreSQL for efficient querying and analytics.

5. **Data Visualization**:
    - Utilize Metabase for creating dashboards and visualizing data insights.

## Getting Started

### Prerequisites

- Python
- Apache Airflow
- MySQL
- PostgreSQL
- Snowflake
- MongoDB
- PySpark
- dbt
- Metabase
- Singer
- Airbyte

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

4. **Configure Airflow**:
    - Follow the [Airflow documentation](https://airflow.apache.org/docs/apache-airflow/stable/start.html) to set up and configure Airflow.

5. **Configure Metabase**:
    - Follow the [Metabase documentation](https://www.metabase.com/docs/latest/) to set up and configure Metabase.

## Usage

1. **Run Airflow**:
    ```sh
    airflow webserver --port 8080
    airflow scheduler
    ```

2. **Access Metabase**:
    - Open your web browser and go to `http://localhost:3000` to access Metabase.

3. **Run dbt transformations**:
    ```sh
    dbt run
    ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes or additions.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspiration
- Resources

