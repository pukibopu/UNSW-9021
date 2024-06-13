# COMP9021 24T1 - Rachid Hamadi
# Sample Exam Question 5


'''
Write a function that accepts a year between 1913 and 2013 inclusive 
and displays the maximum inflation during that year and the month(s) in which it was achieved.

Will be tested with year between 1913 and 2013.
You might find the reader() function of the csv module useful,
but you can also use the split() method of the str class.
'''

import csv

def f(year):
    '''
    >>> f(1914)
    In 1914, maximum inflation was: 2.0
    It was achieved in the following months: Aug
    >>> f(1922)
    In 1922, maximum inflation was: 0.6
    It was achieved in the following months: Jul, Oct, Nov, Dec
    >>> f(1995)
    In 1995, maximum inflation was: 0.4
    It was achieved in the following months: Jan, Feb
    >>> f(2013)
    In 2013, maximum inflation was: 0.82
    It was achieved in the following months: Feb
    '''
    months = 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'
    #like c++ style
    # Insert your code here
    # f=open('cpiai.csv','r')
    # reader_instance=csv.reader(f,delimiter=',')
    # rows=[row for row in reader_instance if row[0].split('-')[0]==str(year)]
    # print(rows)
    # months_dict = {}
    # maxn=-999.9
    # i=0
    # for row in rows:
    #     i+=1
    #     now_num=float(row[2])
    #     if now_num>=maxn:
    #         maxn=now_num
    # i=0
    # for row in rows:
    #     i+=1
    #     if maxn==float(row[2]):
    #         months_dict[i]=months[i-1]
    # print("In {}, maximum inflation was: {}".format(year,maxn))
    # print("It was achieved in the following months: "+', '.join(months_dict.values()))

    with open('cpiai.csv',newline='') as csvfile:
        reader=csv.reader(csvfile,delimiter=',')
        
        year_rows=[row for row in reader if row[0].split('-')[0]==str(year)]

        max_inflation=max(float(row[2]) for row in year_rows)

        max_inflation_months = [months[int(row[0].split('-')[1]) - 1] for row in year_rows if float(row[2]) == max_inflation]
        print(f'In {year}, maximum inflation was: {max_inflation}')
        print('It was achieved in the following months: ' + ', '.join(max_inflation_months))


f(1995)



