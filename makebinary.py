#!/usr/bin/env python
import numpy as np
import pandas as pd
import sys
import argparse
import os.path


parser = argparse.ArgumentParser(description="Make binary matrix from transaction logs")

parser.add_argument("infiles", help="csv dumps from the db", nargs="+")

args = parser.parse_args()

for csvdump in args.infiles:
    data = pd.read_csv(csvdump)
    data = data.sort_values('ReceiptNumber')
    # print data
    # sys.exit(1)
    #get the maximum item number
    max_item_number = data.Item.max() + 1
    #get the number of unique transactions
    num_of_transactions = len(data.ReceiptNumber.unique())

    data_final = np.zeros((num_of_transactions, max_item_number), dtype =int)

    data_final = pd.DataFrame(data_final)

    # print len(data)

    y=0
    for x in range(0,len(data) - 1):
        t1=data.iloc[x]['ReceiptNumber']
        data_final.at[y, data.iloc[x]['Item']]=1
        if (t1 != data.iloc[x+1]['ReceiptNumber']) and (x != 179):
            y=y+1

    out_file_name = os.path.splitext(csvdump)[0] + "_binary.csv"
    data_final.index.name = "trID"
    data_final.to_csv(out_file_name)


sys.exit(0)
