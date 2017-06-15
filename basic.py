import csv

def import_csv(filename):
    file = open(filename)
    reader = list(csv.reader(file))
    return reader

def get_row_data(row, *dataset):
    data = dataset[0]
    return data[0][row][0].split(';')

def get_apple_data(*dataset):
    return get_row_data(0, dataset)

def get_income_on_row(row):
    count = float(row[3])
    price = float(row[2])
    return count*price

def build_shop_ui(*dataset):
    return "" #todo add product list
