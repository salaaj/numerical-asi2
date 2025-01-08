import pandas as pd
import matplotlib.pyplot as plt

def forward_diff(x, y):
    fd = [y[i + 1] - y[i] for i in range(len(y) - 1)]
    return fd + ["Not available"]  

def backward_diff(x, y):
    bd = ["Not available"] + [y[i] - y[i - 1] for i in range(1, len(y))]
    return bd

def centered_diff(x, y):
    cd = ["Not available"] + [(y[i + 1] - y[i - 1]) / 2 for i in range(1, len(y) - 1)] + ["Not available"]
    return cd

def linear_interpolation(x, y, missing_index):
    x1, x2 = x[missing_index - 1], x[missing_index + 1]
    y1, y2 = y[missing_index - 1], y[missing_index + 1]
    return y1 + (y2 - y1) * (x[missing_index] - x1) / (x2 - x1)

def display_table(df, title, highlight_row=None, highlight_col=None):
    fig, ax = plt.subplots(figsize=(6, len(df) * 0.6))
    ax.axis('tight')
    ax.axis('off')
    table = ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center')
    
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.auto_set_column_width(col=list(range(len(df.columns))))
    
    if highlight_row is not None and highlight_col is not None:
        cell = table[(highlight_row + 1, highlight_col)] 
        cell.set_facecolor('#FFD700')  
    
    plt.title(title, fontsize=12, pad=10)
    plt.show()


def main():
    print("Numerical Methods Assignment")
    print("1. Forward diff")
    print("2. Backward diff")
    print("3. Centered diff")
    print("4. Missing Value")
    
    choice = int(input("Choose an option (1-4): "))
    
    n = int(input("Enter the number of data points: "))
    print("Enter the x-values:")
    x = [float(input()) for _ in range(n)]
    
    print("Enter the y-values (use 'None' for missing values):")
    y = []
    missing_index = None
    for i in range(n):
        value = input()
        if value.lower() == 'none':
            y.append(None)
            missing_index = i
        else:
            y.append(float(value))
    
    if choice == 1:
        result = forward_diff(x, y)
        table = pd.DataFrame({'x': x, 'y': y, 'Forward diff': result})
        display_table(table, "Forward diff Table")
    elif choice == 2:
        result = backward_diff(x, y)
        table = pd.DataFrame({'x': x, 'y': y, 'Backward diff': result})
        display_table(table, "Backward diff Table")
    elif choice == 3:
        result = centered_diff(x, y)
        table = pd.DataFrame({'x': x, 'y': y, 'Centered diff': result})
        display_table(table, "Centered diff Table")
    elif choice == 4:
        if missing_index is not None:
            interpolated_value = linear_interpolation(x, y, missing_index)
            y[missing_index] = interpolated_value
            
            
            table = pd.DataFrame({'x': x, 'y': y})
            
            display_table(table, "Missing Value Table", highlight_row=missing_index, highlight_col=1)
        else:
            print("No missing value found in the data!")

    else:
        print("Invalid choice!")

if name == "main":
    main()