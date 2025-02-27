# Enhanced-ETL-Workflow-with-Python-AWS-S3-RDS-and-Glue-for-Data-Engineers


![AWS Services](https://img.shields.io/badge/AWS-S3%20|%20RDS%20|%20Glue-orange?logo=amazon-aws)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Data Formats](https://img.shields.io/badge/Data-CSV%20|%20JSON%20|%20XML-green)

A cloud-native ETL pipeline leveraging **AWS S3**, **RDS**, and **Glue** to process multi-format data with unit standardization and automated logging.

---

## 📌 Project Highlights
- **Extract**: Multi-format data ingestion (CSV/JSON/XML) from S3
- **Transform**: Unit conversions (`inches → meters`, `pounds → kilograms`)
- **Load**: Persist data to **AWS RDS** and **S3**
- **Automation**: Optional schema inference/job scheduling with AWS Glue
- **Logging**: Timestamped audit trail stored locally + S3

---

## 🛠️ Tech Stack
| **Category**       | **Tools**                                                                 |
|---------------------|--------------------------------------------------------------------------|
| **Cloud Services**  | AWS S3 (Storage), AWS RDS (Database), AWS Glue (ETL Automation)         |
| **Languages**       | Python (Pandas, Boto3, SQLAlchemy), SQL                                  |
| **Data Formats**    | CSV, JSON, XML                                                           |

---
## Step 1: Gather Data Files

### Download the dataset
```bash
wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0221EN-SkillsNetwork/labs/module%206/Lab%20-%20Extract%20Transform%20Load/data/source.zip
```

## 2. RDS Database Setup

### Create PostgreSQL/MySQL Instance in AWS RDS
- Go to AWS RDS Console.
- Select PostgreSQL/MySQL engine and configure instance.
- Set DB identifier, username, and password.
- Launch the instance.

### Whitelist IP in Security Groups
- Go to VPC -> Security Groups.
- Add inbound rule for PostgreSQL (5432) or MySQL (3306) with your IP.

### Connection String Format
- PostgreSQL: `postgresql://<user>:<password>@<endpoint>:5432/<database>`
- MySQL: `mysql://<user>:<password>@<endpoint>:3306/<database>`

## 3. (Optional) AWS Glue

### Create Crawler
- Go to AWS Glue -> Crawlers -> Add crawler.
- Set data store to S3 (`s3://etl-project-raw-data/`).
- Run the crawler.

### Define Glue Job for Transformations
- Go to AWS Glue -> Jobs -> Add job.
- Set source, define transformations, and set output.
- Optionally, schedule the job.

## Step 4: Define Functions for ETL with AWS Integration

### Extract Data:
- Upload raw CSV, JSON, and XML files to the S3 bucket.
- Download the files from S3 for processing in your ETL pipeline.

### Transform Data:
- Perform unit conversions (inches to meters, pounds to kilograms).
- Clean and standardize the data.

### Load Data to AWS:

#### Load to RDS and S3:
- After the data is transformed, store the resulting CSV file in the new S3 bucket with the name `transformed_data`.

#### Load to RDS:
- Connect to your RDS instance using SQLAlchemy and Pandas and load the data into a relational database table.

## Step 5: Logging
- Use Python’s logging library to track the progress of the extraction, transformation, and loading phases.
- Save the logs in a text file and optionally upload them to S3 for centralized log storage.

## Step 6: Execution

### Follow the sequence of operations:
- **Upload Raw Data to S3**: Extract raw files from the ZIP and upload them to the S3 bucket.
- **Extract and Transform Data**: Download raw data files from S3, apply transformations, and save the results locally or directly to S3.
- **Load Data into AWS Services**: 
  - Upload the transformed CSV back to S3.
  - Load the final transformed data into AWS RDS using SQLAlchemy.
  - Ensure RDS service will be accessible from your SQL workbench.
- **Monitor Logs**: Ensure that the entire pipeline is logged, and store logs either locally or in S3.





