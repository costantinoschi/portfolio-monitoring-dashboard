# Portfolio Monitoring Dashboard
## Overview
The **Portfolio Monitoring Dashboard** is an interactive real-time monitoring tool designed to track the performance of portfolio companies. By ingesting and visualizing key financial data, this dashboard provides actionable insights for investors, analysts, and portfolio managers. The dashboard includes features such as key performance indicators (KPIs), real-time data ingestion, and alerts for underperformance or deviations from financial forecasts.

## Features
**Automated Data Ingestion**: Real-time data is pulled directly from portfolio companies' financial systems (e.g., QuickBooks, SAP) into the system, enabling up-to-date analysis and decision-making.

**Key Performance Indicators (KPIs)**: The dashboard visualizes essential financial metrics such as revenue, EBITDA, cash flow, and debt levels, offering a comprehensive snapshot of portfolio performance.

**Alerts**: The system identifies underperformance or deviations from forecasts by analyzing financial data. Alerts are triggered for companies that fall below forecasted targets.

**Dynamic Filters**: Users can filter and drill down on specific companies in the portfolio, ensuring customized views of financial performance.

**Visualizations**: Interactive charts, such as revenue trends and EBITDA vs. cash flow comparisons, enable users to quickly grasp financial trends and relationships.

## Technologies
**Python**: The backend is powered by Python, utilizing libraries such as Dash and Streamlit for building interactive and responsive user interfaces.

**Plotly**: Data visualization is handled by Plotly Express, creating dynamic and engaging charts that reflect key financial trends.

**SQLite**: SQLite is used as the lightweight relational database for storing and retrieving financial data for portfolio companies.

**Streamlit**to : Streamlit is used for building the web application interface, allowing for rapid development and deployment.

**SQL**: SQL is utilized to query and manage data stored in the database, ensuring seamless interaction with the portfolio's financial data.

## Installation
To run this project locally, ensure that you have the required dependencies installed. You can set up the environment by following these steps:

1. Clone the repository:

    `git clone https://github.com/your-username/portfolio-monitoring-dashboard.git`
    `cd portfolio-monitoring-dashboard`

2. Install the required packages:

    `pip install -r requirements.txt`

3. Set up the SQLite database:

    Make sure the database is properly populated with financial data from portfolio companies. The schema is defined in the code, and sample data can be inserted using SQL queries.

4. Run the dashboard:

    `streamlit run app.py`

5. Open the application in your web browser, typically at `http://localhost:8501`.

## Usage
Once the dashboard is running, users can interact with the following features:

**Select Companies**: Use the sidebar to select specific companies within the portfolio to display data for.

**View KPIs**: The main dashboard displays total revenue, EBITDA, cash flow, and debt levels for the selected companies.

**Visualize Trends**: Interactive charts are available to view revenue trends and the relationship between EBITDA and cash flow.

**View Alerts**: Any companies with a negative forecast variance (indicating underperformance) are displayed in the alert section.

## Contributing
Contributions are welcome! If you'd like to contribute to the development of this project, please follow these steps:

1. Fork the repository
2. Create a new branch for your feature or fix
3. Commit your changes
4. Push to your fork
5. Create a pull request with a clear description of your changes
