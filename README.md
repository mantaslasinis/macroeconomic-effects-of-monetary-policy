# Replication of Research: Monetary Policy Shocks

## Overview

This project replicates the key results of the original research on monetary policy shocks and their effects on macroeconomic indicators. The analysis includes data preprocessing, regression analysis, impulse response function computation, and Granger causality testing. The goal is to employ methods used in the original research to check the robustness of the results.

---

## Project Structure

### 1. **Data**
   - `data/stage1Data.xlsx`: Contains Stage 1 data used for regression adjustments.
   - `data/allShocks.xlsx`: Includes monthly and quarterly shocks data.
   - `data/regressionData.xlsx`: Regression dataset for macroeconomic variables.
   - Additional data files supporting macroeconomic indicators and shocks.

### 2. **Scripts**
   - `lib/adjust_stage1_data.py`: Adjusts Stage 1 data for analysis.
   - `lib/run_stage1_regression.py`: Runs Stage 1 regressions to analyze shocks.
   - `lib/generate_stage1_results_table.py`: Generates regression results tables.
   - `lib/var_regression.py`: Performs Vector Autoregression (VAR) analysis.
   - `lib/impulse_response_function.py`: Computes impulse response functions.
   - `lib/bootstrap.py`: Bootstraps confidence intervals for VAR results.
   - `lib/local_projection.py`: Implements local projection methods for robustness.
   - `lib/generate_table_3.py`: Produces Granger causality test results.

### 3. **Results**
   - `results/table-2.tex`: LaTeX file summarizing Stage 1 regression results.
   - `results/Figure-1.png`: Time series plot of CH shocks.
   - `results/Figure-2.png`: Impulse response function for key macroeconomic variables.
   - `results/Figure-4.png`: Comparison of baseline and standard VAR models.
   - `results/Figure-7.png`: Impulse response with bank rate included.

---

## Analysis Steps

1. **Data Preprocessing**
   - Load datasets (`stage1Data.xlsx`, `allShocks.xlsx`, and `regressionData.xlsx`).
   - Adjust Stage 1 data using `adjust_stage1_data.py`.

2. **Stage 1 Regression**
   - Use `run_stage1_regression.py` to regress shocks on macroeconomic indicators.
   - Generate Table 2 using `generate_stage1_results_table.py`.

3. **Impulse Response Analysis**
   - Perform VAR analysis with `var_regression.py`.
   - Compute impulse responses with `impulse_response_function.py` and bootstrap confidence intervals.
   - Visualize results in Figures 1, 2, and 4.

4. **Granger Causality Tests**
   - Test for causality using `grangercausalitytests` in `lib`.
   - Summarize results in Table 3 with `generate_table_3.py`.

---

## Key Outputs

- **Table 2**: Regression results summarizing the relationship between shocks and macroeconomic variables.
- **Figures**:
  - Figure 1: Time series plot of CH shocks.
  - Figure 2: Impulse response analysis for baseline VAR.
  - Figure 4: Comparison of baseline and standard VAR models.
  - Figure 7: Impulse response analysis with bank rate.
- **Table 3**: Granger causality results for shocks and macroeconomic indicators.

---

## Initialization

To initialize the script, load kernel from .venv folder, add the directory of this folder to the .env file (that you should create from .env.example), and then run the master.ipynb (also install any needed libraries if they are not yet installed).

