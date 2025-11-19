import matplotlib.pyplot as plt
import pandas as pd

# ----- Sample Dataset -----
data = {
    'Age Group': ['0–20 Years', '21–64 Years', '65+ Years'],
    'Population (Millions)': [512, 807, 98],
    'Percentage': [36.1, 57.0, 6.9]
}

df = pd.DataFrame(data)

# ----- Plotting -----
plt.figure(figsize=(10, 6))
bars = plt.bar(df['Age Group'], df['Population (Millions)'], color=['gold', 'dodgerblue', 'deeppink'])

# Add labels on top of bars
for bar, pct in zip(bars, df['Percentage']):
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 10,
             f'{yval}M\n({pct}%)', ha='center', fontsize=10)

plt.title("India's Population Distribution by Age (Sample Visualization)", fontsize=14)
plt.xlabel("Age Groups")
plt.ylabel("Population (Millions)")
plt.grid(axis='y', linestyle='--', alpha=0.5)

try:
    plt.show()
except Exception:
    # If running in a headless environment, save the figure instead
    plt.savefig('age_group_bar_plot.png', bbox_inches='tight')


# import matplotlib.pyplot as plt
import numpy as np

# Generating artificial continuous age data
ages = np.random.normal(loc=30, scale=15, size=5000)   # mean=30, std=15
ages = ages[(ages >= 0) & (ages <= 100)]

plt.figure(figsize=(10, 6))
plt.hist(ages, bins=20, color='skyblue', edgecolor='black')
plt.title("Age Distribution Histogram")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.grid(axis='y', linestyle='--', alpha=0.5)
try:
    plt.show()
except Exception:
    plt.savefig('age_histogram.png', bbox_inches='tight')
