#!/usr/bin/env python3
import sys

def edit(list_of_strings):
    res = []
    for strg in list_of_strings:
        if "TIME" in strg:
            res.append(strg.replace("\r\n", ",rank\r\n"))
        else:
            div = 3000
           
            if "Euro" in strg:
                div = 10000
            
            # get the number
            start = strg.index('Megawatt') + 9
            end = strg.index('\r\n') 
            num = float(strg[start:end])

            ranks = num//div
            if int(ranks) == 0:
                res.append(strg[:end] + ',' + str(0) + strg[end:])
            for i in range(int(ranks)):
                new = strg[:end] + ',' + str(i) + strg[end:]
                res.append(new)
        
    return res

def processfile(inputfile, outputfile):
    with open(inputfile, newline='') as input:
        all = input.readlines()
        filtered = edit(all)

    with open(outputfile, 'w+') as output:
        output.writelines(filtered)


files = [
    "electricity_production_capacities_for_renewables_and_wastes_processed"
]


for file in files:
    processfile("./{0}.csv".format(file), "./{0}_isotype.csv".format(file) )