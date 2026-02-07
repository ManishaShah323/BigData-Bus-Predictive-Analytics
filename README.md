# BigData-Bus-Predictive-Analytics

## Project Overview

This project describes a predictive analytics system for analysing public bus transport data in the UK using big data programming techniques. The main aim of the project is to process open transport datasets and identify bus services that may be at a higher risk of disruption based on their operational and route-related characteristics.

The system uses structured timetable and route data provided by the UK Bus Open Data Service (BODS) in General Transit Feed Specification (GTFS) format. The data is cleaned, processed, and stored using Python, Pandas, and SQLite, and then analysed using machine learning models to generate insights.

This project was completed as part of the **Big Data Programming Project (ST5011CEM)** module at **Softwarica College of IT & E-Commerce**, in collaboration with **Coventry University**.


## Project Objectives

The main objectives of this project are:

- To collect and integrate large-scale public transport datasets from open data sources  
- To clean and preprocess transport data to make it suitable for analysis  
- To store and manage datasets using Pandas DataFrames and an SQLite relational database  
- To apply machine learning models to identify high-risk bus services  
- To evaluate model performance using standard classification metrics  
- To reflect on technical challenges, data limitations, and ethical considerations  


## Datasets Used

The project uses open-access GTFS datasets obtained from the UK Bus Open Data Service (BODS), including:

- **Agency Data** – transport operator information  
- **Route Data** – bus route identifiers and route types  
- **Trip Data** – scheduled service trips  
- **Stop Times Data** – arrival and departure schedules  
- **Calendar and Calendar Dates** – service availability and exception days  
- **Route Shapes** – geographic route paths  

**Data Source:**  
UK Bus Open Data Service (BODS/GTFS)  
https://www.bus-data.dft.gov.uk/


## System Workflow

- GTFS datasets are loaded using Python and Pandas  
- Data is cleaned and preprocessed (time conversion, handling missing values, and merging datasets)  
- Datasets are stored and queried using SQLite for relational processing  
- Feature engineering is applied to generate temporal, spatial, and operational indicators  
- Machine learning models are trained and evaluated to classify disruption risk  
- Results are analysed and interpreted using evaluation metrics  


## Tools and Technologies

- **Python**  
- **Pandas** and **NumPy** for data processing  
- **SQLite** for relational data storage  
- **Scikit-learn** for machine learning and evaluation  
- **GitHub** for version control and project management  


## Machine Learning Models

The following machine learning models were implemented and evaluated:

- **Logistic Regression** – used as the primary predictive model due to its interpretability and stable performance  
- **Decision Tree Classifier** – used to explore non-linear relationships and validate feature engineering logic  

Model performance was evaluated using accuracy, precision, recall, F1-score, and confusion matrices.


## Ethical and Legal Considerations

This project uses only open-access public datasets and does not process any personal or sensitive information. As a result, it complies with GDPR principles and open data licensing requirements. Potential data bias and limitations associated with open transport datasets are discussed in the project report.


## Author

**Manisha Kumari Shah**  
BSc Computer Science with Artificial Intelligence – Second Year  
Softwarica College of IT & E-Commerce
