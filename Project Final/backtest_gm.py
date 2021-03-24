import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt

# import os
# import bot_functions as botf

#%% read dataframe

# dataframe = pd.DataFrame()
# dataframe_1 = pd.DataFrame()
data = pd.read_csv('FX_EURUSD_3.csv')

#%%
hourtime = data.iloc[:, 0]
df_o = data.iloc[:, 1]
df_h = data.iloc[:, 2]
df_l = data.iloc[:, 3]
df_c = data.iloc[:, 4]
# df_vol = data.iloc[:, 5]

#%% average true range

true_range = pd.Series(data = np.empty, index = data.index)
atr = pd.Series(data = np.empty, index = data.index) 

hc, lc = 0, 0

for i in data.index:
    if i > 0:
        if df_h.iloc[i] > df_c.iloc[i - 1]:
            hc = df_h.iloc[i]
            if df_l[i] > df_c.iloc[i - 1]:
                lc = df_c.iloc[i - 1]
            else:
                lc = df_l.iloc[i]
                
        elif df_h.iloc[i] <= df_c.iloc[i - 1]:
            hc = df_c.iloc[i - 1]
            if df_l[i] > df_c.iloc[i - 1]:
                lc = df_c.iloc[i - 1]
            else:
                lc = df_l.iloc[i]
 
        true_range[i] = hc - lc
        
    else:
        true_range[i] = df_h[i] - df_l[i]
              
atr = true_range.ewm(span = 32, min_periods = 32, adjust = False).mean()
# span 32 min_periods use 5 min resolution, cover most recent 80+80 min
# span 64 min_periods use 1 min resolution, cover most recent 32+32 min

#%% volume profile 

# def volume_profile (df_vol, df_c, timeframe = 1000):
#    tot_vol = df_vol.rolling(timeframe, min_periods = timeframe).sum()
#    value_factor = 0.8
#    value_area = tot_vol * value_factor
#    # calculate statistical distribution
#    # point of control
#    # value area
#    # treatment for valley
#    
#    return value_vol

#%% exponential moving average

ema16 = df_c.ewm(span = 16, min_periods = 16, adjust = False).mean()
ema32 = df_c.ewm(span = 32, min_periods = 32, adjust = False).mean()
ema64 = df_c.ewm(span = 64, min_periods = 64, adjust = False).mean()
   
# ema16 = pd.Series(data = np.zeros, index = data.index)
# ema32 = pd.Series(data = np.zeros, index = data.index)
# ema64 = pd.Series(data = np.zeros, index = data.index)

# def calculate_ema(index, data): # index from main timeline
#        
#    if (index >= 15) & (index < 31):
#        
#        ema16 = df_c[0:index].ewm(span = 16, min_periods = 16, adjust = False).mean()
#        
#    elif (index >= 31) & (index < 63):
#        
#        ema16 = df_c[0:index].ewm(span = 16, min_periods = 16, adjust = False).mean()
#        ema32 = df_c[0:index].ewm(span = 32, min_periods = 32, adjust = False).mean()
#        
#    elif (index >= 63):
#        
#        ema16 = df_c[0:index].ewm(span = 16, min_periods = 16, adjust = False).mean()
#        ema32 = df_c[0:index].ewm(span = 32, min_periods = 32, adjust = False).mean()
#        ema64 = df_c[0:index].ewm(span = 64, min_periods = 64, adjust = False).mean()
#        
#    return ema16, ema32, ema64
#
#for index in data.index:
#    
#    ema16, ema32, ema64 = calculate_ema(index, data)

#%% position process

account = 10000 # 1 million / active leverage

equity = pd.Series(data = np.empty, index = hourtime[:len(hourtime) - 1])
equity[:] = 0

def initiate_position(d_i, entry_price):
    risk = 2 * atr[d_i] # per risk = 2 unit atr
    frac = kelly(risk)

    pos_size = account * frac / entry_price
    # atr_leverage = int(order_size / atr[d_i])

    return pos_size
        
def close_position(d_i, entry_price, position):
    # 20x leverage trading EUR/USD
    gain = 20 * position * (df_c[d_i] - entry_price)

    return gain

def kelly(risk, ratio = 2.5): # ratio use 2.5 now, for simplicity
    reward = risk * ratio
    # set success rate as 0.5 for now
    p = 0.5
    # calculate this trade's portion in the total investment
    frac = (reward * p - risk * (1-p)) / reward

    # limit position size to 50% of the total investment to reduce risk during extreme situation/volatility
    if frac > 0.5:
        frac = 0.5

    return frac

#%% pre-settings

# spread = 1 # bid/ask spread
pos_check = 0
position = 0
entry_price = 0
stop_risk = 0
exit_limit = 0
pos_open_1, pos_open_2 = 0, 0

trades = 0

risk_ratio = 1
reward_ratio = 2.5

realized = pd.Series(data = np.nan, index = data.index)

#%% trading operations

for d_i in data.index[63: len(df_c)]:

    cur_time = hourtime[d_i]
    pre_time = hourtime[d_i - 1]

    if pos_check == 0:

        if (ema16[d_i] > ema64[d_i]) and (ema16[d_i - 1] <= ema64[d_i - 1]):
        # if (ema8[d_i] > ema32[d_i]) & (ema8[d_i - 1] <= ema32[d_i - 1]):

            if ema64[d_i] > ema64[d_i - 16] :
                entry_price = df_c[d_i]
                stop_risk = risk_ratio * atr[d_i]
                # stop_risk = risk_factor * entry_price
                exit_limit = reward_ratio * atr[d_i]
                # exit_limit = profit_factor * entry_price
                position = initiate_position(d_i, entry_price)
                pos_check = 1
                pos_open_1 += 1
                
                equity[cur_time] = equity[pre_time]
                
            else:
                equity[cur_time] = equity[pre_time]
            
        elif (ema16[d_i] < ema64[d_i]) and (ema16[d_i - 1] >= ema64[d_i - 1]):
        # elif (ema8[d_i] < ema32[d_i]) & (ema8[d_i - 1] >= ema32[d_i - 1]):

            if ema64[d_i] < ema64[d_i - 16]:
                entry_price = df_c[d_i]
                stop_risk = risk_ratio * atr[d_i]
                # stop_risk = risk_factor * entry_price
                exit_limit = reward_ratio * atr[d_i]
                # exit_limit = profit_factor * entry_price
                position = initiate_position(d_i, entry_price)
                pos_check = 1
                pos_open_2 += 1
                
                equity[cur_time] = equity[pre_time]
            else:
                equity[cur_time] = equity[pre_time]
        else:
            equity[cur_time] = equity[pre_time]

    elif pos_check == 1:

        # condition 1 for closing long position / profit target reached
        if df_c[d_i] - entry_price >= exit_limit:
            realized[d_i] = close_position(d_i, entry_price, position)
            pos_check = 0
            trades += 1
            
            equity[cur_time] = equity[pre_time] + realized[d_i]
            
        # condition 2 for closing long position / profit target reached
        elif entry_price - df_c[d_i] >= stop_risk:
            realized[d_i] = close_position(d_i, entry_price, position)
            pos_check = 0
            trades += 1
            
            equity[cur_time] = equity[pre_time] + realized[d_i]
            
        # condition 3 for closing long position / ema crossover
        elif (ema16[d_i] < ema32[d_i]) and (ema16[d_i - 1] >= ema32[d_i - 1]):
            realized[d_i] = close_position(d_i, entry_price, position)
            pos_check = 0
            trades += 1

            equity[cur_time] = equity[pre_time] + realized[d_i]
        else:
            equity[cur_time] = equity[pre_time]
    else:
        print('no operation')

        
#%% performance 

realized.dropna(inplace=True)
equity.drop(equity.tail(1).index, inplace=True)

win, lose = 0, 0

win_tot, win_avg, lose_tot, lose_avg = 0, 0, 0, 0

for i in realized.index:
    if realized[i] > 0:
        win += 1
        win_tot = win_tot + realized[i]
    elif realized[i] < 0:
        lose += 1
        lose_tot = lose_tot + realized[i]

win_rate = round(win/trades, 4)
lose_rate = round(lose/trades, 4)

win_avg = round(win_tot/win, 2)
lose_avg = round(lose_tot/lose, 2)

sum_realized = win_tot + lose_tot

#%% local output

print('long win rate :', win_rate)
print('long win average (percentage):', round(win_avg/account * 100, 4))
print('long lose rate :', lose_rate)
print('long lose average (percentage):', round(lose_avg/account * 100, 4))

print('long trade(s) :', trades)
print('total long realized gain (percentage):', round(sum_realized/account * 100, 4))



