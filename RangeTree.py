import csv
from datetime import datetime
from typing import List
import tkinter as tk
import os

class Node(object):
    """A node in a Range Tree."""

    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.isLeaf = False
        self.assoc = None


def LoadData(param1 = None):
    with open("CovidData.csv") as csvfile:
        readCSV = csv.reader(csvfile, delimiter=",")
        readCSV = list(readCSV)[1:]
        data = {}
        all_data = {}
        for row in readCSV:
            #Store the data of selected countries from the csv file in a dictionary with country as a key
            date = datetime.strptime(row[1], '%d/%m/%Y')

             # Create the country as a key in dict
            if row[0] not in data.keys():
                data[row[0]] = []
            if param1 == None:
                data[row[0]] += [date.date()]
            else:
                if row[param1] == '':
                    row[param1] = 0
                data[row[0]] += [(date.date(), float(row[param1]))]
            
            #Simultaneously, store the data of all rows in a dict. The key is a tuple (country, date)
            if (row[0], row[1]) not in all_data.keys():
                all_data[(row[0], row[1])] = []
            all_data[(row[0], row[1])] = row[2:]
    
    csvfile.close()
    return (data, all_data)


def ConstructRangeTree1d(data, parent):
    if not data:
        return None
    if len(data) == 1:
        node = Node(data[0])
        node.parent = parent
        node.isLeaf = True
    else:
        mid_val = len(data)//2
        node = Node(data[mid_val])
        node.parent = parent
        node.left = ConstructRangeTree1d(data[:mid_val], node)
        node.right = ConstructRangeTree1d(data[mid_val+1:], node)
    return node


def printTree(node, level=0):
    if node != None:
        printTree(node.right, level + 1)
        print(' ' * 4 * level + '->', node.value)
        printTree(node.left, level + 1)

def ConstructRangeTree2d(data, parent, enable=True):
    if not data:
        return None
    if len(data) == 1:
        node = Node(data[0])
        node.parent = parent
        node.isLeaf = True
    else:
        mid_val = len(data)//2
        node = Node(data[mid_val])  # node.value = (x,y)
        node.parent = parent
        node.left = ConstructRangeTree2d(data[:mid_val], node, enable)
        node.right = ConstructRangeTree2d(data[mid_val+1:], node, enable)
    if enable:
        node.assoc = ConstructRangeTree2d(
            sorted(data, key=lambda x: x[1]), None, enable=False)
    return node


def withinRange(point, range, check):
     '''
    Checks if the value of node is within the required range

    Arguments:
        point       : A point in tree
        range       : A list containing range to be checked with
        check       : specifies which option should be performed
    Returns :
        True if in range else False
    '''
    if check == 1:
        x = point
        if (x >= range[0][0] and x <= range[0][1]):
            return True
        else:
            return False
    elif check == 2:
        x = point[0]
        y = point[1]
        if (x >= range[0][0] and x <= range[0][1] and y >= range[1][0] and y <= range[1][1]):
            return True
        else:
            return False


def getValue(point, enable, dim):
    '''
    Reads the desired value from node

    Arguments:
        point       : A point in tree
        enable      : True when we need to read first coord of point when used as a helper function by 2D range search
        dimension   : specifies the dimension of range tree.
    Returns : value of node
    '''
    if dim == 1:
        value = point.value
    elif dim == 2:
        if enable:
            value = point.value[0]
        else:
            value = point.value[1]
    return value


def FindSplitNode(root, p_min, p_max, dim, enable):
    '''
    Searches for a common node that splits the range

    Arguments:
        tree        : A Node in tree
        p_min       : Starting range 
        p_max       : Ending range 
        dimension   : specifies the dimension of range tree.
        enable      : True when we need to read first coord of point when used as a helper function by 2D range search

    Returns : A Node
    '''
    splitnode = root
    while splitnode != None:
        node = getValue(splitnode, enable, dim)
        if p_min < node and p_max < node:
            splitnode = splitnode.left
        elif p_min > node and p_min > node:
            splitnode = splitnode.right
        else:
            break
    return splitnode


def SearchRangeTree1d(tree, p1, p2, dim = 1, enable = True):
    '''
    Performs 1D range search

    Arguments:
        tree        : A Node in tree
        p1          : Starting range 
        p2          : Ending range 
        dimension   : specifies the dimension of range tree. By default 1
        enable      : True when we need to read first coord of point when used as a helper function by 2D range search

    Returns : list of result of range query
    '''
    nodes = []
    splitnode = FindSplitNode(tree, p1, p2, dim, enable)
    if splitnode == None:
        return nodes
    elif withinRange(getValue(splitnode, enable, dim), [(p1, p2)], 1):
        nodes.append(splitnode.value)
    nodes += SearchRangeTree1d(splitnode.left, p1, p2, dim, enable)
    nodes += SearchRangeTree1d(splitnode.right, p1, p2, dim, enable)
    return nodes

def SearchRangeTree2d(tree, x1, x2, y1, y2, dim = 2):
    '''
    Performs 2D range search

    Arguments:
        tree        : A Node in tree
        x1          : Starting range for x-coord
        x2          : Ending range for x-coord
        y1          : Starting range for y-coord
        y2          : Ending range for y-coord
        dimension   : specifies the dimension of range tree. By default 2

    Returns : Results from 2D search
    '''
    results = []
    splitnode = FindSplitNode(tree, x1, x2, 2, True)
    if (splitnode != None):
        if (splitnode.isLeaf):
            if (withinRange(splitnode.value, [(x1, x2), (y1, y2)], 2)):
                # print(results)
                results.append(splitnode.value)
        vl = splitnode.left
        value = getValue(vl, True, dim)
        results = []
        while (vl.isLeaf != True):
            if (x1 <= value):
                results += SearchRangeTree1d(vl.right.assoc, y1, y2, dim, False, results)
                vl = vl.left
            else:
                vl = vl.right
            # print(vl.value)
            if (withinRange(vl.value, [(x1, x2), (y1, y2)], 2)):
                results.append(vl.value)
        # print(results)
        vr = splitnode.right
        value = getValue(vr, True, dim)
        while (vr.isLeaf != True):
            if (x2 >= vr.value[0]):
                results += SearchRangeTree1d(vr.left.assoc, y1, y2, dim, False, results)
                vr = vr.right
            else:
                vr = vr.left
            # print(vr.value)
            if (withinRange(vr.value, [(x1, x2), (y1, y2)], 2)):
                results.append(vr.value)
        # print(results)
    return results


def displayData(all: dict, final: list, dimension):
    '''
    Displays results in a csv file

    Arguments:
        all         : All Data initially read from csv
        final       : Results from range query
        dimension   : specifies the dimension of range tree.
    Returns : None
    '''
    # open the file in the write mode
    if dimension == 1:
        f = open('RangeQuery1D.csv', 'w')
    else:
        f = open('RangeQuery2D.csv', 'w')
    f.truncate(0)
    # create the csv writer
    writer = csv.writer(f)

    headings = ["Country", "Date", "Total Cases", "New Cases", "Total Deaths", "New Deaths", 
    "Total Cases/Million", "Total Deaths/Million", "ICU Patients/Million", "Hospital Patients/Million", 
    "Total Tests/Million", "New tests/Million", "Positive Rate", "Total Vaccinations", "People Vaccinated", 
    "People Fully Vaccinated", "New Vaccinations", "Population", "GDP / capita" ]

    writer.writerow(headings)
    for key in final:
        display = [key[0], key[1]]
        for val in all[(key[0], key[1])]:
            if val == '':
                val = 0
            display.append(val)
        writer.writerow(display)
    f.close()
    if dimension == 2:
        file = "RangeQuery1D.csv"
        os.startfile(file)
    else:
        file = "RangeQuery2D.csv"
        os.startfile(file)


def main(Countries,  date1, date2,  param1=None, x1=None, x2=None, dimension=1):
    '''
    Handles all function calls

    Arguments:
        Countries   : A country name from the drop down list. String data type.
        date1       : Starting date for range query
        date2       : Ending date for range query
        param1      : The first column number to be read from the excel file . By default is None else should be a valid integer value
        x1          : Starting value for range query related to param1. By default is None
        x2          : Ending value for range query related to param1. By default is None
        dimension   : specifies the dimension of range tree. By default 1

    Returns : None
    '''
    if dimension == 1: 
        data, all_data = LoadData()
    else:
        data, all_data = LoadData(param1)
    final = []
    date1 = datetime.strptime(date1, '%d/%m/%Y')
    date2 = datetime.strptime(date2, '%d/%m/%Y')
    for country in Countries:
        values = data[country]
        values.sort()
        # print(values)
        if dimension == 1:
            root = ConstructRangeTree1d(values, None)
            search = SearchRangeTree1d(root, date1.date(), date2.date(), 1)
            for tup in search:
                d = tup.strftime("%d/%m/%Y")
                tup_new = (country, d)
                final.append(tup_new)
        elif dimension == 2:
            tree = ConstructRangeTree2d(values, None)
            search = SearchRangeTree2d( tree, date1.date(), date2.date(), x1, x2, 2)
            for tup in search:
                d = tup[0].strftime("%d/%m/%Y")
                tup_new = (country, d, tup[1])
                final.append(tup_new)
    displayData(all_data, sorted(final), dimension)
# main(['Afghanistan'] , '03/03/2020', '06/03/2020', 3, 2, 6, dimension=2)
