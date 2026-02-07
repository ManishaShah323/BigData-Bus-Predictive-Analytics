# BigData-Bus-Predictive-Analytics

## Project Overview

This project describes a predictive analytics system for analysing public bus transport data in the United Kingdom using big data programming techniques. The primary aim of the project is to process open public transport datasets and predict the likelihood of service disruption or service removal based on historical timetable and service exception data.

The system utilises structured timetable and route datasets provided by the UK Bus Open Data Service (BODS) in General Transit Feed Specification (GTFS) format. The data is cleaned, preprocessed, and stored using Python, Pandas, and SQLite, and subsequently analysed using machine learning models to generate actionable insights.

This project was completed as part of the **Big Data Programming Project (ST5011CEM)** module at **Softwarica College of IT & E-Commerce**, in collaboration with **Coventry University**.


## Project Objectives

The main objectives of this project are:

- To collect and integrate large-scale public transport datasets from open data sources  
- To clean and preprocess GTFS-based transport data to make it suitable for analysis  
- To store and manage datasets using Pandas DataFrames and an SQLite relational database  
- To apply machine learning models to predict public transport service disruption and removal risk  
- To evaluate model performance using standard classification metrics  
- To reflect on technical challenges, data limitations, and ethical considerations  


## Datasets Used

The project uses open-access GTFS datasets obtained from the UK Bus Open Data Service (BODS), including:

- **Agency Data** – transport operator information  
- **Route Data** – route identifiers and route-level metadata  
- **Trip Data** – scheduled public transport services  
- **Stop Times Data** – arrival and departure schedules  
- **Calendar and Calendar Dates** – service availability and service exception records  
- **Route Shapes** – geographic route representations  

Data Source:
UK Bus Open Data Service (BODS / GTFS)  
https://www.bus-data.dft.gov.uk/


## System Workflow

- GTFS datasets are loaded using Python and Pandas  
- Data cleaning and preprocessing are performed, including date conversion, handling missing values, and dataset integration  
- Processed datasets are stored and queried using SQLite for relational processing  
- Feature engineering is applied to generate temporal and operational indicators  
- Machine learning models are trained and evaluated to classify service disruption risk  
- Results are analysed and interpreted using evaluation metrics  


## Tools and Technologies

- **Python**  
- **Pandas** and **NumPy** for data processing  
- **SQLite** for relational data storage  
- **Scikit-learn** for machine learning and evaluation  
- **GitHub** for version control and project management  


## Machine Learning Models

The following machine learning models were implemented and evaluated:

- **Logistic Regression** – used as the primary predictive model due to its interpretability, low computational complexity, and suitability for binary classification  
- **Decision Tree Classifier** – used as a comparative model to explore non-linear relationships and validate feature engineering decisions  

Model performance was evaluated using accuracy, precision, recall, F1-score, ROC-AUC, and confusion matrices.


## Ethical and Legal Considerations

This project exclusively uses open-access public datasets and does not collect or process any personal or sensitive information. As a result, it complies with GDPR principles and open data licensing requirements. Potential bias and limitations associated with historical public transport datasets are acknowledged and discussed in the project report.


## Author

**Manisha Kumari Shah**  
BSc Computer Science with Artificial Intelligence – Second Year  
Softwarica College of IT & E-Commerce
