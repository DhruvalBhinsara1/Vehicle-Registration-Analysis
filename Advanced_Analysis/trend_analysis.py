import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import pathlib
from statsmodels.tsa.seasonal import seasonal_decompose
import numpy as np
from sklearn.linear_model import LinearRegression

# Setup output folder
notebook_dir = pathlib.Path(__file__).parent.parent.resolve()
output_dir = os.path.join(notebook_dir, 'Advanced_Analysis', 'images')
os.makedirs(output_dir, exist_ok=True)

# Load cleaned data
file_path = os.path.join(notebook_dir, 'Dataset', 'Vehicle_Data_Cleaned.csv')
if not os.path.exists(file_path):
    file_path = os.path.join(notebook_dir, 'Dataset', 'Vehicle_Data.csv')
df = pd.read_csv(file_path, low_memory=False)

# Parse registration date
if 'regvalidfrom' in df.columns:
    df['regvalidfrom'] = pd.to_datetime(df['regvalidfrom'], errors='coerce')
    df = df.dropna(subset=['regvalidfrom'])
    df['YearMonth'] = df['regvalidfrom'].dt.to_period('M')
    monthly_trend = df.groupby('YearMonth').size()
    monthly_trend.index = monthly_trend.index.to_timestamp()
    # Filter to start from 2000
    monthly_trend = monthly_trend[monthly_trend.index >= pd.Timestamp('2000-01-01')]
    # --- Data summary and outlier detection ---
    summary_stats = monthly_trend.describe(percentiles=[.01, .05, .25, .5, .75, .95, .99])
    print('Monthly Registrations Summary:')
    print(summary_stats)
    # Detect extreme outliers (above 99th percentile)
    high_outlier_thresh = summary_stats['99%']
    low_outlier_thresh = summary_stats['1%']
    outlier_mask = (monthly_trend > high_outlier_thresh) | (monthly_trend < low_outlier_thresh)
    num_outliers = outlier_mask.sum()
    if num_outliers > 0:
        print(f'Warning: {num_outliers} outlier months detected. Outliers will be capped for clarity.')
    # Cap outliers for plotting (winsorize)
    monthly_trend_clean = monthly_trend.copy()
    monthly_trend_clean[outlier_mask & (monthly_trend > high_outlier_thresh)] = high_outlier_thresh
    monthly_trend_clean[outlier_mask & (monthly_trend < low_outlier_thresh)] = low_outlier_thresh

    # Plot actual trend with moving average and peak/trough annotations (using cleaned data)
    plt.figure(figsize=(14,6))
    sns.lineplot(x=monthly_trend_clean.index, y=monthly_trend_clean.values, marker='o', label='Registrations per Month (Capped Outliers)')
    # Moving average (12 months)
    ma = pd.Series(monthly_trend_clean.values).rolling(window=12, min_periods=1).mean()
    plt.plot(monthly_trend_clean.index, ma, color='purple', linestyle='-', linewidth=2, label='12-Month Moving Average')
    # Detect peaks and troughs
    from scipy.signal import find_peaks
    peaks, _ = find_peaks(monthly_trend_clean.values, distance=6)
    troughs, _ = find_peaks(-monthly_trend_clean.values, distance=6)
    plt.scatter(monthly_trend_clean.index[peaks], monthly_trend_clean.values[peaks], color='red', label='Peaks', zorder=5)
    plt.scatter(monthly_trend_clean.index[troughs], monthly_trend_clean.values[troughs], color='blue', label='Troughs', zorder=5)
    # Annotate highest peak
    if len(peaks) > 0:
        max_peak = peaks[np.argmax(monthly_trend_clean.values[peaks])]
        plt.annotate(f'Peak: {monthly_trend_clean.values[max_peak]:,.0f}',
                    xy=(monthly_trend_clean.index[max_peak], monthly_trend_clean.values[max_peak]),
                    xytext=(monthly_trend_clean.index[max_peak], monthly_trend_clean.values[max_peak]+5000),
                    arrowprops=dict(facecolor='red', shrink=0.05), fontsize=11, color='red', ha='center')
    # Annotate lowest trough
    if len(troughs) > 0:
        min_trough = troughs[np.argmin(monthly_trend_clean.values[troughs])]
        plt.annotate(f'Trough: {monthly_trend_clean.values[min_trough]:,.0f}',
                    xy=(monthly_trend_clean.index[min_trough], monthly_trend_clean.values[min_trough]),
                    xytext=(monthly_trend_clean.index[min_trough], monthly_trend_clean.values[min_trough]-5000),
                    arrowprops=dict(facecolor='blue', shrink=0.05), fontsize=11, color='blue', ha='center')
    # Year gridlines
    for year in range(monthly_trend_clean.index[0].year, monthly_trend_clean.index[-1].year+1):
        plt.axvline(pd.Timestamp(f'{year}-01-01'), color='gray', linestyle=':', linewidth=0.5)
    plt.title('Monthly Vehicle Registration Trend (2000 onwards)')
    plt.xlabel('Month (Year)')
    plt.ylabel('Number of Registrations')
    plt.figtext(0.5, -0.18, 'Blue line: monthly registrations (outliers capped). Purple: 12-month moving average. Red/blue dots/arrows: peaks/troughs. Vertical lines: year markers. Outlier months capped at 99th/1st percentile.', wrap=True, ha='center', fontsize=11)
    plt.legend()
    plt.tight_layout(rect=[0,0.2,1,1])
    plt.savefig(os.path.join(output_dir, 'registrations_trend_actual_2000_onwards.png'))
    plt.close()

    # Decompose trend (seasonal_decompose)
    result = seasonal_decompose(monthly_trend_clean, model='additive', period=12)
    # Trend component with year markers
    plt.figure(figsize=(14,4))
    plt.plot(result.trend.index, result.trend.values, label='Trend', color='purple')
    for year in range(result.trend.index[0].year, result.trend.index[-1].year+1):
        plt.axvline(pd.Timestamp(f'{year}-01-01'), color='gray', linestyle=':', linewidth=0.5)
    plt.title('Trend Component (2000 onwards)')
    plt.xlabel('Month (Year)')
    plt.ylabel('Smoothed Registrations')
    plt.figtext(0.5, -0.15, 'Purple line: long-term direction of registrations. Vertical lines: year markers.', wrap=True, ha='center', fontsize=11)
    plt.legend()
    plt.tight_layout(rect=[0,0.18,1,1])
    plt.savefig(os.path.join(output_dir, 'registrations_trend_component_2000_onwards.png'))
    plt.close()
    # Seasonal component with year markers
    plt.figure(figsize=(14,4))
    plt.plot(result.seasonal.index, result.seasonal.values, label='Seasonality', color='orange')
    for year in range(result.seasonal.index[0].year, result.seasonal.index[-1].year+1):
        plt.axvline(pd.Timestamp(f'{year}-01-01'), color='gray', linestyle=':', linewidth=0.5)
    plt.title('Seasonal Component (2000 onwards)')
    plt.xlabel('Month (Year)')
    plt.ylabel('Seasonal Effect')
    plt.figtext(0.5, -0.15, 'Orange line: repeating seasonal patterns. Vertical lines: year markers.', wrap=True, ha='center', fontsize=11)
    plt.legend()
    plt.tight_layout(rect=[0,0.18,1,1])
    plt.savefig(os.path.join(output_dir, 'registrations_seasonal_component_2000_onwards.png'))
    plt.close()
    # Residual component with year markers and highlight outliers
    plt.figure(figsize=(14,4))
    plt.plot(result.resid.index, result.resid.values, label='Residuals', color='green')
    # Highlight outliers (top 3 absolute residuals)
    abs_resid = np.abs(result.resid.values)
    outlier_idx = np.argsort(abs_resid)[-3:]
    plt.scatter(result.resid.index[outlier_idx], result.resid.values[outlier_idx], color='red', label='Outliers', zorder=5)
    for i in outlier_idx:
        plt.annotate(f'Outlier: {result.resid.values[i]:.0f}',
                    xy=(result.resid.index[i], result.resid.values[i]),
                    xytext=(result.resid.index[i], result.resid.values[i]+1000*np.sign(result.resid.values[i])),
                    arrowprops=dict(facecolor='red', shrink=0.05), fontsize=10, color='red', ha='center')
    for year in range(result.resid.index[0].year, result.resid.index[-1].year+1):
        plt.axvline(pd.Timestamp(f'{year}-01-01'), color='gray', linestyle=':', linewidth=0.5)
    plt.title('Residual Component (2000 onwards)')
    plt.xlabel('Month (Year)')
    plt.ylabel('Unexplained Variation')
    plt.figtext(0.5, -0.15, 'Green line: unexplained variation. Red dots/arrows: outliers. Vertical lines: year markers.', wrap=True, ha='center', fontsize=11)
    plt.legend()
    plt.tight_layout(rect=[0,0.18,1,1])
    plt.savefig(os.path.join(output_dir, 'registrations_residual_component_2000_onwards.png'))
    plt.close()

    # Simple prediction: linear extrapolation (last 24 months)
    months = np.arange(len(monthly_trend)).reshape(-1,1)
    reg = LinearRegression()
    reg.fit(months[-24:], monthly_trend.values[-24:])
    future_months = np.arange(len(months), len(months)+12).reshape(-1,1)
    future_preds = reg.predict(future_months)
    future_index = pd.date_range(monthly_trend.index[-1]+pd.offsets.MonthBegin(), periods=12, freq='MS')
    plt.figure(figsize=(14,6))
    plt.plot(monthly_trend.index, monthly_trend.values, label='Actual Registrations')
    plt.plot(future_index, future_preds, label='Predicted Next Year', linestyle='--', color='red')
    # Annotate final predicted value
    plt.annotate(f'{int(future_preds[-1]):,}', xy=(future_index[-1], future_preds[-1]), xytext=(future_index[-1], future_preds[-1]+5000),
                 arrowprops=dict(facecolor='red', shrink=0.05), fontsize=12, color='red', ha='center')
    plt.title('Monthly Registration Trend & Next Year Prediction (2000 onwards)')
    plt.xlabel('Month (Year)')
    plt.ylabel('Number of Registrations')
    plt.figtext(0.5, -0.08, 'Shows actual registrations and a simple prediction for the next 12 months (red dashed line).', wrap=True, ha='center', fontsize=11)
    plt.legend()
    # Extend x-axis to show all months including predictions
    plt.xlim([monthly_trend.index[0], future_index[-1]])
    plt.tight_layout(rect=[0,0.05,1,1])
    plt.savefig(os.path.join(output_dir, 'registrations_prediction_next_year.png'))
    plt.close()
