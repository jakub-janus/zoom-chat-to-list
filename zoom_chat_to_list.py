#This short program creates an xlsx table - an automated attendance list - based on messages sent via the public chat in Zoom, using Numpy and Pandas libraries.
#The automation may be used to check attendance during Zoom meetings (e.g., online classrooms), with specific cut-off times for a beginning and an end of a given meeting.
#It lists the unique names of participants (in alphabetical order) and the exact time of their messages.
#It skips the messages sent outside of a given timeframe or via the private chat in Zoom.
#chat.txt file provided here contains artificial data to illustrate the outcomes of the program.

#To do

# 0. Ask all the participants of your Zoom meeting to confirm their presence by writing in the public chat at the beginning and - if you prefer to do so - at the end of your Zoom meeting (e.g., ask them to write "present!"). The recommended Zoom login format is "Name Surname".

# 1. Export chat.txt file from a Zoom meeting.

# 2. If in Google Colab, drop chat.txt file from Zoom to Files in the left-hand side panel. (Copy it to the folder containing the main.py file when using your own machine. You may also source it in any other way.)

# 3. Run the program.

# 4. If needed, specify cut-off times for attendance (maximum and minimum time of a message sent in the public chat).

# 5. Done - your list is printed and list.xlsx is ready for download. (Or written in your folder.)

#Comments welcome

import os # Uncomment when working on your own machine
import sys 
import pandas as pd #Libraries
import numpy as np
from openpyxl import Workbook

os.chdir(sys.path[0]) # Uncomment when working on your own machine

q = input("Would you like to specify time conditions - min and max time of response of meeting participants? (y/n)")
if q == 'y':
    t1 = input("Maximum time - beggining of meeting (hh:mm:ss):")
    t2 = input("Minimum time - end of meeting (hh:mm:ss):")
else: 
    pass

with open("chat.txt", "r", encoding = "utf-8") as f:
    lines = [i for line in f for i in line.split('],')]

print('Zoom chat file loaded.')

cleaned_from_private = [x for x in lines if 'Privately' not in x] # Clean private chat entries

matrix = [line.split() for line in cleaned_from_private]

n = len(matrix) # no. of entries in chat

list_time_name = []
for i in range(n):
    list_time_name.append([matrix[i][0], matrix[i][2], matrix[i][3]]) # nested list

name = []
time = []
for i in range(n):
    name.append([list_time_name[i][2] + str(' ') + list_time_name[i][1]])
    time.append(list_time_name[i][0])

name_2 = sum(name, []) # flat lists
time_2 = time

df = pd.DataFrame()
df['Name'] = name_2
df['Time'] = time_2

df = df.sort_values(by = ['Name'], ascending = True)
df_first = df.drop_duplicates('Name', keep = 'first')
df_last = df.drop_duplicates('Name', keep = 'last')

df_final = pd.DataFrame()
df_final['Name'] = df_first['Name'].reset_index(drop = True)
df_final['Beginning of meeting'] = df_first['Time'].reset_index(drop = True)
df_final['End of meeting'] = df_last['Time'].reset_index(drop = True)
df_final['End of meeting'] = np.where(df_final['End of meeting'] != df_final['Beginning of meeting'], df_final['End of meeting'], '-')

if q == 'y':
    df_final['Beginning of meeting'] = np.where(df_final['Beginning of meeting'] <= t1, df_final['Beginning of meeting'], '-') # Check time conditions
    df_final['End of meeting'] = np.where(df_final['End of meeting'] >= t2, df_final['End of meeting'], '-')
else:
    pass

df_final.to_excel("list.xlsx", sheet_name = 'list')

print('Done! The list is ready.')
print('')
print(df_final)