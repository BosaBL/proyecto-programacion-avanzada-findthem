'''
Created on 08-06-2022

@author: matias
'''
import csv

class mod:
    myData=[["Player_name", "Player_score"],
          ["sarta", "123",]]
    
    myFile=open("Player.csv", "w")
    with myFile:
        writer=csv.writer(myFile)
        writer.writerows(myData)
    print("ola")