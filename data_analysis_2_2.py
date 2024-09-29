from collections import Counter
import readrides_dict
rows = readrides_dict.read_rides_as_dict('Data/ctabus.csv')

"""
route,date,daytype,rides
3,01/01/2001,U,7354
"""
answer_1 = len(set([row['route'] for row in rows]))
answer_2 = sum([int(row['rides'])
               for row in rows if row['route'] == '22' and row['date'] == '02/02/2011'])
answer_3 = Counter()
answer_4_2001 = Counter()
answer_4_2011 = Counter()
for row in rows:
    answer_3[row['route']] += int(row['rides'])
    year = row['date'][-4:]
    if year == '2001':
        answer_4_2001[row['route']] += int(row['rides'])
    elif year == '2011':
        answer_4_2011[row['route']] += int(row['rides'])


print(f"Number of unique routes: {answer_1}")
print(f"Number of passengers: {answer_2}")
print(f"Number of rides per bus line: {answer_3}")
print(f"Lines with greatest increase in passengers: {
      (answer_4_2011 - answer_4_2001).most_common(5)}")
