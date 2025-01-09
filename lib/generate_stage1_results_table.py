import pandas as pd

def generate_stage1_results_table(results):
    variables = [
        ("Constant ($\\alpha$)", None),
        ("Initial Bank Rate ($i_{t-14}$)", None),
        ("Forecasted output growth ($\\hat{y}_{m,j}^F$)", "Quarters ahead"),
        ("Forecasted inflation ($\\hat{\\pi}_{m,j}^F$)", "Quarters ahead"),
        ("Change in forecasted output growth ($\\hat{y}_{m,j}^F - \\hat{y}_{m-1,j}^F$)", "Quarters ahead"),
        ("Change in forecasted inflation ($\\hat{\\pi}_{m,j}^F - \\hat{\\pi}_{m-1,j}^F$)", "Quarters ahead"),
        ("Change in unemployment rate ($u_{t-j}$)", "Months"),
    ]
    
    subcategories = {
        "Forecasted output growth ($\\hat{y}_{m,j}^F$)": [-1, 0, 1, 2],
        "Forecasted inflation ($\\hat{\\pi}_{m,j}^F$)": [-1, 0, 1, 2],
        "Change in forecasted output growth ($\\hat{y}_{m,j}^F - \\hat{y}_{m-1,j}^F$)": [-1, 0, 1, 2],
        "Change in forecasted inflation ($\\hat{\\pi}_{m,j}^F - \\hat{\\pi}_{m-1,j}^F$)": [-1, 0, 1, 2],
        "Change in unemployment rate ($u_{t-j}$)": [-1, -2, -3],
    }
    
    coef = results.params.values
    std_err = results.bse.values

    latex_code = "\\begin{table}[h!]\n    \\centering\n"
    latex_code += "    \\renewcommand{\\arraystretch}{1.3} % Adjust row height\n"
    latex_code += "    \\begin{tabular}{p{6cm} >{\\centering\\arraybackslash}p{2cm} >{\\centering\\arraybackslash}p{2cm}}\n"
    latex_code += "    \\toprule\n"
    latex_code += "    \\textbf{Variable} & \\textbf{Coefficient} & \\textbf{Standard Error} \\\\\n"
    latex_code += "    \\midrule\n"

    coef_idx = 0
    for var, subcat in variables:
        if subcat is None:
            latex_code += f"    {var} & {coef[coef_idx]:.3f} & {std_err[coef_idx]:.3f} \\\\\n"
            coef_idx += 1
        else:
            latex_code += f"    {var} \\\\ {subcat} & & \\\\\n"
            for sub in subcategories[var]:
                latex_code += f"    \\hspace{{0.5cm}} {sub} & {coef[coef_idx]:.3f} & {std_err[coef_idx]:.3f} \\\\\n"
                coef_idx += 1
            latex_code += "    \\addlinespace\n"

    latex_code += "    \\bottomrule\n"
    latex_code += "    \\end{tabular}\n"
    latex_code += "    \\caption{Regression Results with Hierarchical Subcategories}\n"
    latex_code += "    \\label{tab:regression_results}\n"
    latex_code += "\\end{table}"

    return latex_code
