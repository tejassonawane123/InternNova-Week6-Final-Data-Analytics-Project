# Olist E-Commerce Delivery & Order Analytics Project

## 1. Project Overview

This project is an end-to-end Data Analytics project developed as part of the InternNova Week 6 Final Data Analytics Project.

The project analyzes Olist E-Commerce order data to understand order performance, delivery duration, order status, order trends, and delivery performance. Python was used for data preparation, Exploratory Data Analysis (EDA), and visualization, while Power BI was used to create an interactive business dashboard.

The project demonstrates the complete analytics workflow:

- Data preparation
- Exploratory Data Analysis
- Statistical analysis
- Data visualization
- Power BI dashboard development
- Business insights
- Data-driven recommendations
- Git and GitHub project workflow


## 2. Problem Statement

E-commerce businesses need to monitor order volumes, delivery performance, and order status to understand operational performance and identify areas requiring improvement.

The objective of this project is to analyze Olist e-commerce order data and identify meaningful patterns related to:

- Order status
- Delivery duration
- Estimated versus actual delivery performance
- Monthly order trends
- On-time and late deliveries

The analysis aims to convert the available order data into useful business insights and recommendations.


## 3. Dataset Description

The project uses the Olist E-Commerce dataset.

The dataset contains e-commerce order information including fields related to:

- Customer ID
- Order ID
- Order purchase timestamp
- Estimated delivery date
- Actual customer delivery date
- Order status
- Customer and order-related information

A prepared dataset was used for analysis after performing the required data preparation and cleaning steps.


## 4. Tools & Technologies

The following tools and technologies were used:

- Python
- Pandas
- NumPy
- Matplotlib
- Jupyter Notebook / Python scripts
- Power BI Desktop
- Git
- GitHub


## 5. Data Cleaning & Preparation

The dataset was inspected and prepared before performing the analysis.

The data preparation process included:

- Inspecting the dataset structure
- Checking available columns and data types
- Checking missing values
- Identifying duplicate records
- Preparing date-related fields
- Creating the Delivery Days calculated field
- Preparing the cleaned dataset for EDA and visualization

The prepared dataset was saved for use in the subsequent analysis.


## 6. Exploratory Data Analysis (EDA)

Exploratory Data Analysis was performed to understand the characteristics and patterns within the order data.

The analysis included:

- Dataset inspection
- Descriptive analysis
- Delivery-day analysis
- Order-status analysis
- Monthly order trend analysis
- Estimated versus actual delivery comparison
- On-time versus late delivery analysis
- Distribution analysis
- Identification of unusual delivery durations and patterns

The EDA helped identify important operational patterns that were subsequently represented through visualizations and the Power BI dashboard.


## 7. Data Visualizations

Five major visualizations were created using Python:

1. **Actual vs Estimated Delivery Days**
   - Shows the relationship between estimated delivery duration and actual delivery duration.

2. **Delivery Days Distribution**
   - Shows the distribution of delivery durations across orders.

3. **Monthly Order Trend**
   - Shows how order volume changes over time.

4. **Order Status Distribution / Order Status Share**
   - Shows the distribution of orders across different order statuses.

5. **On-Time vs Late Delivery**
   - Compares the number of orders delivered on time with orders classified as late.

These visualizations were created to communicate trends, distributions, comparisons, and delivery performance clearly.


## 8. Power BI Dashboard

An interactive Power BI dashboard was developed to provide a consolidated view of the Olist e-commerce order and delivery performance.

### KPI Cards

The dashboard contains three KPI cards:

- Total Order Records
- Average Delivery Days
- Total Order Status Records

### Dashboard Visualizations

The dashboard includes multiple visualizations such as:

- Order Status Distribution
- Order Status Share
- Monthly Order Trend
- Delivery Days Distribution

### Filter / Slicer

An order-status slicer was added to allow users to interactively filter the dashboard based on order status.

### Dashboard Title

**Olist E-Commerce Delivery & Order Analytics Dashboard**

The dashboard combines important metrics and visualizations into a single analytical view.


## 9. Business Insights

The analysis produced the following key business insights:

1. The majority of orders were successfully delivered, indicating a high overall order completion level in the dataset.

2. The average delivery time was approximately **12.5 days**, making delivery speed an important operational performance metric.

3. Delivery durations are concentrated around lower delivery times, while a smaller number of orders required considerably longer delivery periods.

4. Monthly order activity varies over time, with periods of higher and lower order volumes indicating time-based demand patterns.

5. Delivered orders represent the dominant order status, while other statuses such as shipped, canceled, unavailable, invoiced, processing, and created represent much smaller proportions.

6. The comparison between estimated and actual delivery days shows variation in delivery performance, indicating that some orders experienced differences between estimated and actual delivery duration.


## 10. Recommendations

Based on the analysis, the following recommendations are proposed:

### 1. Improve Delivery Performance

Identify orders, periods, and operational areas associated with longer delivery durations and investigate the causes of delays. Improving logistics and delivery processes can help reduce delivery time and improve customer experience.

### 2. Improve Demand Planning

Use monthly order trends to support demand forecasting, logistics capacity planning, and resource allocation during periods of higher order volume.

### 3. Improve Delivery-Time Estimation

Monitor the difference between estimated and actual delivery times and improve delivery-time estimation where significant differences are observed.

### 4. Monitor Order Status Performance

Regularly monitor canceled, unavailable, processing, and delayed orders to identify operational issues and reduce potential customer dissatisfaction.


## 11. Git & GitHub Workflow

Git and GitHub were used to maintain and manage the project.

The project workflow included:

- Creating a GitHub repository
- Cloning the repository
- Checking repository status
- Adding project files
- Creating commits
- Pushing changes to GitHub
- Pulling the latest repository changes

Meaningful project commits were created during the development process to maintain a structured project history.
