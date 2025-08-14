# DSA-2040_Practical_Exam_ANGELA-IRUNGU-289
# Project: End-of-Semester Exam Submission 

This project demonstrates a complete analytical pipeline, beginning with raw data and concluding with actionable insights derived from both a structured database and various machine learning models. The project is divided into two distinct parts: Data Warehousing and Data Mining.

-----

## 1\. Project Overview and Objectives 

The core objective of this project was to apply key data science methodologies to real-world data challenges. The project's structure addresses the following goals:

  * **Part I: Data Warehousing & OLAP Analysis** 
    This section focuses on the principles of data engineering. A raw, transactional dataset was subjected to an **ETL (Extract, Transform, Load)** process. The data was cleaned and transformed before being loaded into a **star schema**, a specific database design optimized for analytical queries. This new structure facilitates **OLAP (Online Analytical Processing)**, allowing for efficient business analysis.

  * **Part II: Data Mining** 
    This part of the project applies machine learning techniques to different datasets. It demonstrates proficiency in both **unsupervised learning (clustering)**, used to discover patterns, and **supervised learning (classification)**, used to build predictive models. The project also includes a practical application of **association rule mining** to uncover relationships between items.

-----

## 2\. Datasets Utilized and Generated 📂

This project used a mix of provided and generated datasets to fulfill the exam's requirements.

  * **Retail Transaction Dataset:** The primary source for the data warehousing task was an Excel file, `online_retail.csv.xlsx`. This raw dataset required extensive cleaning before it could be used for analysis.
  * **Generated Database:** A SQLite database file, `retail_dw.db`, was created by the ETL script. This file represents the final, clean, and organized data warehouse.
  * **Iris Dataset:** The project utilized the built-in Iris dataset from the `scikit-learn` library for the clustering and classification tasks.
  * **Synthetic Transactional Data:** For the association rule mining, a list of transactions was dynamically generated within the code to simulate real-world shopping basket data.

-----

## 3\. How to Run the Codebase 

To replicate the project's results, a Python environment with the following libraries is required.

### Step 1: Install Dependencies

The following command can be executed in a terminal or command prompt to install all necessary libraries:

```bash
pip install pandas openpyxl matplotlib seaborn scikit-learn mlxtend
```

### Step 2: Execute the ETL Pipeline

The ETL script must be run first to create the data warehouse file.

```bash
python etl_retail.py
```

### Step 3: Run the Analysis Notebook

All subsequent analytical and machine learning code is contained within a single Jupyter Notebook.

  * Launch a Jupyter server and open the `olap_analysis.ipynb` file.
  * The cells within the notebook are structured in a logical sequence. They should be executed in order from top to bottom to ensure all variables and dependencies are loaded correctly.

-----

## 4\. Self-Assessment of Project Completion ✅

The project successfully meets all the specified requirements of the exam. The implementation demonstrates a solid understanding of the concepts and methodologies.

  * **Data Warehousing:** A complete and functional ETL pipeline was developed, resulting in a well-structured star schema. The project successfully executed and visualized OLAP queries.
  * **Data Mining:** All tasks were completed as required. This includes successful implementation of K-Means clustering, the training and comparison of Decision Tree and KNN classifiers, and the application of the Apriori algorithm for association rule mining.

The codebase is structured to be reproducible and well-documented. Challenges encountered during the development process, such as path errors and library compatibility issues, were successfully resolved, demonstrating a robust problem-solving ability.
