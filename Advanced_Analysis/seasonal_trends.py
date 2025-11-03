import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import pathlib

# Setup output folder
notebook_dir = pathlib.Path().resolve().parent
output_dir = os.path.join(notebook_dir, 'Advanced_Analysis', 'images')
os.makedirs(output_dir, exist_ok=True)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import pathlib

# Setup output folder
notebook_dir = pathlib.Path(__file__).parent.parent.resolve()
output_dir = os.path.join(notebook_dir, 'Advanced_Analysis', 'images')
os.makedirs(output_dir, exist_ok=True)

# Load cleaned data
file_path = os.path.join(notebook_dir, 'Dataset', 'Vehicle_Data_Cleaned.csv')
if not os.path.exists(file_path):
    # Try alternative path
    file_path = os.path.join(notebook_dir, 'Dataset', 'Vehicle_Data.csv')
    print(f"Vehicle_Data_Cleaned.csv not found, using {file_path}")
df = pd.read_csv(file_path, low_memory=False)

# Parse registration date
if 'regvalidfrom' in df.columns:
    df['regvalidfrom'] = pd.to_datetime(df['regvalidfrom'], errors='coerce')
    df = df.dropna(subset=['regvalidfrom'])
    df['Year'] = df['regvalidfrom'].dt.year
    df['Month'] = df['regvalidfrom'].dt.month
    df['MonthName'] = df['regvalidfrom'].dt.strftime('%b')

    # Filter to years >= 2000
    df_recent = df[df['Year'] >= 2000]
    # Monthly registration trend (2000 onwards)
    monthly = df_recent.groupby(['Year', 'MonthName']).size().reset_index(name='Registrations')
    # Ensure months are ordered
    month_order = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    monthly['MonthName'] = pd.Categorical(monthly['MonthName'], categories=month_order, ordered=True)
    pivot = monthly.pivot(index='MonthName', columns='Year', values='Registrations').fillna(0)
    import numpy as np
    plt.figure(figsize=(14,7))
    # Use log normalization for better contrast
    from matplotlib.colors import LogNorm
    sns.heatmap(pivot, cmap='magma', norm=LogNorm(vmin=max(pivot.min().min(), 1), vmax=pivot.max().max()))
    plt.title('Monthly Registration Heatmap by Year (2000 onwards)')
    plt.xlabel('Year')
    plt.ylabel('Month')
    plt.figtext(0.5, -0.08, 'Light color = High registrations, Dark color = Low registrations (log scale)', ha='center', fontsize=12)
    plt.tight_layout(rect=[0,0.05,1,1])
    plt.savefig(os.path.join(output_dir, 'monthly_registration_heatmap.png'), bbox_inches='tight')
    plt.close()

    # Average registrations by month (seasonality)
    avg_month = df_recent.groupby('MonthName').size().reindex(month_order)
    plt.figure(figsize=(10,5))
    sns.barplot(x=avg_month.index, y=avg_month.values, palette='coolwarm')
    plt.title('Average Registrations by Month (Seasonality, 2000+)')
    plt.xlabel('Month')
    plt.ylabel('Average Registrations')
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, 'average_registrations_by_month.png'))
    plt.close()

    # Save summary CSVs
    monthly.to_csv(os.path.join(output_dir, 'monthly_registration_trend.csv'), index=False)
    avg_month.to_csv(os.path.join(output_dir, 'average_registrations_by_month.csv'))
