import csv

def import_csv(filename):
    file = open(filename)
    reader = list(csv.reader(file))
    return reader

def get_row_data(row, dataset):
    return dataset[row][0].split(';')

def get_apple_data(dataset):
    return get_row_data(1, dataset)

def get_income_on_row(row):
    count = int(row[2])
    price = float(row[3])
    return count*price

def build_shop_ui(dataset):
    productcount=[]
    for row in range(1,len(dataset)):
        data=get_row_data(row,dataset)
        productcount.append('%s:%s' %(data[1],data[2]))
    return ','.join(productcount) #todo add product list
