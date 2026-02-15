# Harvesting the Stablecoin Spread Risk Premium

### A study of USDT vs USDC Pricing on Bitcoin

This repository contains the research notebook and supporting scripts
for analyzing and harvesting the stablecoin spread risk premium between
BTCUSDT and BTCUSDC.

The study compares naive rolling statistics with a regime-aware
state-space (Kalman Filter) framework to distinguish temporary
dislocations from structural repricing and evaluate implementability
under transaction costs.

------------------------------------------------------------------------

## Setup Instructions

### 1. Install Dependencies

It is recommended to use a virtual environment.

``` bash
pip install -r requirements.txt
```

This installs all required packages for data handling, modeling, and
backtesting.

------------------------------------------------------------------------

### 2. Download the Data

Before running the notebook, download the required market data:

``` bash
python data_download.py
```

This script retrieves and stores all datasets necessary for the
analysis.

------------------------------------------------------------------------

### 3. Run the Notebook

Launch Jupyter:

``` bash
jupyter notebook
```

Then open the main research notebook.

The notebook is **preloaded with computed outputs**, so it is not
necessary to re-run the entire workflow for review purposes.

However, if experimentation is desired (e.g., modifying thresholds,
Kalman filter parameters, transaction cost assumptions, or regime
detection settings), the notebook is fully modular and can be executed
cell-by-cell without additional configuration.

------------------------------------------------------------------------

## Project Structure

    ├── requirements.txt
    ├── data_download.py
    ├── Harvesting the Stablecoin Spread Risk Premium - A Study of USDT vs USDC Pricing on Bitcoin.ipynb
    └── README.md

-   `requirements.txt` --- Python dependencies\
-   `data_download.py` --- Data retrieval script\
-   `Harvesting the Stablecoin Spread Risk Premium - A Study of USDT vs USDC Pricing on Bitcoin.ipynb` --- Full research workflow

