# 📈 Real-Time Trading Analytics Platform

A real-time data analytics platform designed to ingest, process, and visualize financial market data. This project leverages **Microsoft Fabric**, **dbt**, and **Power BI** to empower data-driven decision-making in hedge funds.

---

## **📌 Introduction & Goals**

This project simulates how hedge funds analyze real-time market data to support investment strategies. The system is designed to:

- Ingest real-time stock data.
- Process and transform data using scalable cloud infrastructure.
- Visualize actionable insights via dynamic dashboards.

### **Executive Summary**

- **Data:** Real-time stock market data from public APIs (e.g., Alpha Vantage, Yahoo Finance).  
- **Tools Used:**  
  - **Microsoft Fabric** (Dataflow, OneLake, Synapse)  
  - **dbt (Data Build Tool)**  
  - **Power BI**  
  - **Azure Event Hubs**  
- **Goal:** To create a real-time analytics pipeline that delivers up-to-date stock trends and performance insights through an interactive Power BI dashboard.

---

## **📂 Contents**

- [The Data Set](#the-data-set)  
- [Used Tools](#used-tools)  
  - [Connect](#connect)  
  - [Buffer](#buffer)  
- Pipelines
  - Stream processing
  - Processing Data Stream
  -Visualization
---

## **📊 The Data Set**

This project uses publicly available financial data for simulation purposes.  
**Source:** [Alpha Vantage](https://www.alphavantage.co/) and [Yahoo Finance](https://finance.yahoo.com/)

**Features:**  
- Stock Prices (Open, Close, High, Low, Volume)  
- Timestamps for real-time updates  
- Financial indicators (Moving Average, RSI, Bollinger Bands)  

---

## **🛠️ Used Tools**

### **Connect**  
- **Microsoft Fabric Dataflow:** Ingests real-time stock data into OneLake.  
- **Azure Event Hubs:** Streams real-time data into Fabric.  

### **Buffer**  
- **dbt (Data Build Tool):** Cleans and transforms raw data.  
- **Power BI:** Visualizes financial insights with dynamic dashboards.  

---

## **🚀 Project Workflow**

1. **Data Ingestion**  
   - Streaming data from APIs via **Azure Event Hubs**.  
   - Batch ingestion using **Fabric Dataflows**.

2. **Data Storage**  
   - Raw and processed data stored in **OneLake**.  

3. **Data Processing**  
   - Transformations managed in **dbt**.  
   - Financial metrics calculation using dbt models.

4. **Visualization**  
   - Interactive Power BI dashboards displaying stock trends and performance.

---

## **📈 Sample Dashboard**

> _[Insert a screenshot or link to your Power BI dashboard here]_  

---

## **🔍 Conclusion**

This project demonstrates how to build a scalable, cloud-based data analytics solution for financial market analysis using **Microsoft Fabric**, **dbt**, and **Power BI**. The pipeline can be extended for more complex financial modeling or real-time trading strategies.

---

