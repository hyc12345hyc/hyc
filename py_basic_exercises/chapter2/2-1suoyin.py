#-*-coding:utf-*-
#根据给定的数字形式的年月日打印出日期。
months = ['January','February','March','April','May','June','July','August','September','October','November','December']

#以1~31的数字作为结尾的列表。
endings = ['st','nd','rd'] + 17 * ['th']\
+ ['st','nd','rd'] + 7 * ['th']\
+ ['st']

year = raw_input('Year: ')
month = raw_input('Month(1~12): ')
day = raw_input('Day(1~31):')

month_number = int(month)
day_number = int(day)

#月份和天数要减一，以获得正确的索引。
month_name = months[month_number - 1]
ordinal = day + endings[day_number - 1]

print month_name + ' ' + ordinal + '. ' + year
