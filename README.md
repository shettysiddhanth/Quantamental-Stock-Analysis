# Quantamental Stock Analysis

This repository contains a series of notebooks and scripts that demonstrate the application of various quantitative investment strategies on the NIFTY50 stock index. We utilize quantamental filters such as Basic EPS, Return on Networth/Equity, Current Ratio, PBIT Margin, and Return on Capital Employed to refine the stock universe significantly. Our strategies incorporate advanced financial modeling techniques, including Brownian motion and mean reversion, integrated with Markowitz analysis to construct a Global Minimum Variance (GMV) portfolio. Additionally, we implement CPPI strategies to manage risk and minimize drawdowns.

## Project Outcomes
- Refined the stock universe by up to 86% using quantamental filters.
- Developed a GMV portfolio with a 24.9% yield for 2023.
- Achieved a 24.29% return in 2023 through CPPI strategies.

## Key Concepts

### Quantamental Filters
Quantamental analysis combines quantitative and fundamental analysis to refine stock selection. In this project, we use:
- **Basic EPS (Earnings Per Share)**: Measures a company's profitability.
- **Return on Networth / Equity (ROE)**: Evaluates profitability relative to shareholders' equity.
- **Current Ratio**: Measures a company's ability to pay short-term obligations.
- **PBIT Margin**: Indicates the percentage of revenue that has turned into profit before interest and taxes.
- **Return on Capital Employed (ROCE)**: Assesses a company's efficiency at generating profits from its capital.

### Brownian Motion
Brownian motion is a stochastic process used to model random movements in financial markets. It helps simulate the unpredictable behavior of asset prices.

### Mean Reversion
Mean reversion is the financial theory suggesting that asset prices and historical returns eventually revert to their long-term mean or average level. This concept is used to identify potential investment opportunities.

### Markowitz Analysis
Markowitz analysis, also known as Modern Portfolio Theory (MPT), is used to construct portfolios that optimize or maximize expected return based on a given level of market risk. It emphasizes the benefits of diversification.

### Global Minimum Variance (GMV) Portfolio
The GMV portfolio is designed to have the lowest possible risk (variance) for a given return. It is constructed using Markowitz analysis to balance risk and return.

### Constant Proportion Portfolio Insurance (CPPI)
CPPI is a risk management strategy that dynamically adjusts the asset allocation between risky assets and a risk-free asset to protect the portfolio from significant losses while allowing for potential growth.

## Repository Structure
- `importNSE.py`: Script to import NSE stock data.
- `import_ratios.py`: Script to import financial ratios like Basic EPS, ROE, Current Ratio, PBIT Margin, and ROCE.
- `filter.ipynb`: Notebook for applying quantamental filters to stock data.
- `consolidaton.ipynb`: Notebook for data consolidation and preprocessing.
- `brownian_motion.ipynb`: Notebook demonstrating Brownian motion and mean reversion models.
- `GMV.ipynb`: Notebook for constructing the GMV portfolio using Markowitz analysis.
- `return_calc.ipynb`: Notebook for calculating returns and evaluating portfolio performance.
- `backtesting_data.ipynb`: Notebook for backtesting the portfolio strategies.
- Data Files:
  - `backtesting_data.csv`: Data used for backtesting the strategies.
  - `filtered_data.csv`: Data after applying quantamental filters.
  - `predicted_stock_prices.csv`: Predicted stock prices used for simulations.
  - `training_data.csv`: Training data for the models.

## Technologies Used
- **InfluxDB**: For managing and querying financial time series data.
- **Python**: Primary programming language used for data analysis and modeling.
- **Jupyter Notebooks**: For interactive data analysis and visualization.

