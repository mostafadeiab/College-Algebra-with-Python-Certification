import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilename

def load_csv():
    file_path = askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path: return pd.read_csv(file_path)

def plot(x, y, plot_type='scatter'):
    plt.figure()
    if plot_type == 'scatter': plt.scatter(x, y)
    elif plot_type == 'line': plt.plot(x, y)
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()

df = load_csv()
print("Column Headings:", df.columns.tolist())
print("\nFirst two rows of the DataFrame:")
print(df.head(2))

cols = df.columns.tolist()
print("Columns available:", cols)

if len(cols) >= 2:
    col1 = input(f"Select the first column from {cols}: ")
    col2 = input(f"Select the second column from {cols}: ")
    
    x = df[col1].to_numpy()
    y = df[col2].to_numpy()

    print("\nStep 4: Plotting data")
    type = input("Enter the type of plot ('scatter' or 'line'): ").strip().lower()
    plot(x, y, type)
else:
    print("Not enough columns for plotting.")
