import pandas as pd
import investpy
from matplotlib import pyplot as plt
import seaborn as sns
import datetime


# Seaborn global style.
sns.set_context('poster')
sns.set(rc={'figure.figsize': (10, 5), 'xtick.labelsize': 10})
sns.set_style('whitegrid')
sns.set_palette("husl", 9)

tech_data = pd.read_csv('./data/output/tech_company_data.csv')

def get_data(*args):
    for arg in args:
        stock = investpy.get_stock_historical_data(stock=f'{arg}', country='united states', as_json=False, order='ascending', from_date='01/01/2020', to_date='01/12/2020')
        sns.lineplot(data=stock, x='Date', y='Close', label=arg)

    plt.legend(loc="upper left")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title(f"Recent stock data:")
    plt.show()


def get_all_data(): # Do not execute under any circumstances.
    for ticker in tickers:
        try:
            stock = investpy.get_stock_historical_data(stock=f'{ticker}', country='united states', as_json=False, order='ascending', from_date='01/01/2020', to_date='01/12/2020')
            sns.lineplot(data=stock, x='Date', y='Close', label=ticker)
        except Exception:
            continue

    plt.legend(loc="upper left")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.title(f"Recent stock data:")
    plt.show()


def check_ticker(name):
    # This will convert the name to the ticker in case the user does not know the exact input. Will be later used as input debugging in another function.
    for company in tech_data['name']:
        if name.lower() in company.lower():
            return tech_data.loc[tech_data['name'] == company, 'ticker'].iloc[0]
    return name


def get_rsi(ticker, mode='SMA'):
    today = datetime.datetime.now()
    today_str = datetime.date.strftime(today, "%d/%m/%Y")
    from_date = datetime.datetime.now() - datetime.timedelta(days=30)
    from_date_str = datetime.date.strftime(from_date, "%d/%m/%Y")

    data = investpy.get_stock_historical_data(stock=check_ticker(), country='united states', as_json=False, order='ascending', from_date=from_date_str, to_date=today_str)

    close = data['Close']
    delta = close.diff()

    # Get rid of the first row, which is NaN since it did not have a previous row to calculate the differences.
    delta = delta[1:]

    # Make the positive gains (up) and negative gains (down) Series.
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    window_length = 14

    if mode == 'EWMA':
        # Calculate the EWMA.
        avg_gain1 = up.ewm(span=window_length).mean()
        avg_loss1 = down.abs().ewm(span=window_length).mean()

        # Calculate the RSI based on EWMA.
        RS1 = avg_gain1 / avg_loss1
        RSI1 = 100.0 - (100.0 / (1.0 + RS1))

        # Plot graph.
        RSI1.plot()
        plt.legend(['RSI (EWMA)'])
        plt.show()

    else:
        # Calculate the SMA.
        avg_gain2 = up.rolling(window_length).mean()
        avg_loss2 = down.abs().rolling(window_length).mean()

        # Calculate the RSI based on SMA.
        RS2 = avg_gain2 / avg_loss2
        RSI2 = 100.0 - (100.0 / (1.0 + RS2))

        # Plot graph.
        RSI2.plot()
        plt.legend(['RSI (SMA)'])
        plt.show()


# TODO: scatter plot for linear regression.

print(check_ticker('apple'))
