#!/usr/bin/env python3
import sys

def check_condition(list_of_strings):
    remove = ["Albania", "Bosnia and Herzegovina", 'Iceland', "Kosovo", "Moldova", "Montenegro", "North Macedonia", "Norway", "Serbia"]
    res = []
    for str in list_of_strings:
        keep = True
        for item in remove:
            if item in str:
                keep = False

        # remove non eu
        if keep and not ("United Kingdom" in str and ("2020" in str or "2021" in str)): 

            # rename
            if "Germany" in str:
                str = str.replace("Germany (until 1990 former territory of the FRG)", "Germany")

            res.append(str)
        
    return res

def processfile(inputfile, outputfile):
    with open(inputfile, newline='') as input:
        all = input.readlines()
        filtered = check_condition(all)

    with open(outputfile, 'w+') as output:
        output.writelines(filtered)


files = [
    "consumption_of_renewables_and_wastes",
    "electricity_production_capacities_for_renewables_and_wastes",
    "heat_pumps",
    "liquid_biofeuls_production_capacities",
    "net_greenhouse_gas_emissions",
    "nuclear_energy",
    "share_of_energy_from_renewable_sources",
    "solar_thermal_collector_surface"
]


for file in files:
    processfile("./{0}.csv".format(file), "./{0}_processed.csv".format(file) )