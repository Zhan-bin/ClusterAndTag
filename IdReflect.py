import csv
path = "data/ml-latest-small/movies.csv"
with open(path) as f:
    # 创建cvs文件读取器
    reader = csv.reader(f)
    # 读取第一行，这行是表头数据。
    header_row = next(reader)
    print(header_row)
    # 读取第二行，这行是真正的数据。
    first_row = next(reader)
    print(int(first_row[0]))
data = [['1','1','2']]
with open('data/test.csv', 'w', newline='') as t_file:
    csv_writer = csv.writer(t_file)
    for l in data:
        csv_writer.writerow(l)
