# Final Project: Inverted Additions
# [CS 201 Data Structures II, Spring 2021](https://hulms.instructure.com/courses/1260)
-------
## Range-Tree

A data structure used for range queries. It uses Balanced binary search tree for set of data points in n-dimensional space.

## Properties

- It stores data in leaf nodes in a sorted manner. 
- Every internal node in n-dimensional space stores an associated tree.
- Search Complexity for n-dimensional space O(log^d n + k)

## Implementation

- We have implemented 1D and 2D range tree to process a sample COVID-19 data obtained from https://ourworldindata.org/coronavirus.
- This data structure is best used for searching only and constructs a Range Tree once and stores it for search operations, hence deletion and insertion are not operated on range trees.

## Presenation

For detailed insight on our implemention, refer to our video presentation https://www.youtube.com/watch?v=CbNOre1wUho&t=2s
