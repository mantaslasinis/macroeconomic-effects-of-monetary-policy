def generate_table_3(summary_3_lags, summary_6_lags, output_file="results/table-3.tex"):
    with open(output_file, "w") as f:
        # Write the LaTeX table header
        f.write("\\begin{table}[ht]\n")
        f.write("\\centering\n")
        f.write("\\begin{tabular}{lcc|cc}\n")
        f.write("\\hline\n")
        f.write(" & \\multicolumn{2}{c|}{$I = 3$ lags} & \\multicolumn{2}{c}{$I = 6$ lags} \\\\\n")
        f.write("\\textbf{Variable} & \\textbf{F-statistics} & \\textbf{p-values} & \\textbf{F-statistics} & \\textbf{p-values} \\\\\n")
        f.write("\\hline\n")
        
        # Write each row of the table
        for i in range(len(summary_3_lags)):
            var = summary_3_lags.iloc[i]['Variable']
            f_stat_3 = summary_3_lags.iloc[i]['F-statistics']
            p_val_3 = summary_3_lags.iloc[i]['p-values']
            f_stat_6 = summary_6_lags.iloc[i]['F-statistics']
            p_val_6 = summary_6_lags.iloc[i]['p-values']
            f.write(f"{var} & {f_stat_3:.2f} & {p_val_3:.2f} & {f_stat_6:.2f} & {p_val_6:.2f} \\\\\n")
        
        # Write the table footer
        f.write("\\hline\n")
        f.write("\\end{tabular}\n")
        f.write("\\caption{Predictability of Monetary Policy Innovations}\n")
        f.write("\\label{table:predictability}\n")
        f.write("\\end{table}\n")