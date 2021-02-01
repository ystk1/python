import csv  # CSVモジュールの読み込み

# with open('data/sample.csv') as f:
#     reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
#     l_f = [row for row in reader]


with open('data/sample.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    # Passing the cav_reader object to list() to get a list of lists
    list_of_rows = list(csv_reader)
    print(list_of_rows)


print(list_of_rows)
# [[11.0, 12.0, 13.0, 14.0], [21.0, 22.0, 23.0, 24.0], [31.0, 32.0, 33.0, 34.0]]

print(list_of_rows[0][0])
# 11.0

print(type(list_of_rows[0][0]))
# <class 'float'>

text_a = "チューリップには{}と{}があります。"

with open('test2.txt', 'w') as f2:
	with open('test.txt', 'w') as f:
		for d in list_of_rows:
			# f.write("test %s , %s\n" % d[0],d[1])
			# f.write(text_a.format(d[0], d[1]))

			f.write("%s選手は、%sでした。\n" %(d[0], d[1]))
			f2.write("%s選手は、%sでした。\n" %(d[1], d[0]))

