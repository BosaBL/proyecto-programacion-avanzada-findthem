'''
Created on 08-06-2022

@author: matias
'''
import csv

class mod:
        with open("Player.csv", "w") as csvfile:
            fieldnames=["Name", "Score"]
            writer=csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader() 
            writer.writerow({"Name": "a", "Score": "1"})
                             
            with open("Player.csv") as File:
                reader=csv.DictReader(File)
                for row in reader:
                    fieldnames.append(row)