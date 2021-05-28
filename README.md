# Final Project: Inverted Additions
# [CS 201 Data Structures II, Spring 2021](https://hulms.instructure.com/courses/1260)
-------
## Range-Tree

A data structure used for range queries. It uses Balanced binary search tree for set of data points in n-dimensional space.

## Properties

- It stores data in leaf nodes in a sorted manner. 
- Every internal node in n-dimensional space stores an associated tree.
- Search Complexity for n-dimensional space O(log^d n + k)
- This data structure is best used for searching only and constructs a Range Tree once and stores it for search operations, hence deletion and insertion are not of much interest.

## Motivation

In light of COVID-19 pandemic that has taken over the world by storm, processing of COVID-19 data is extremely essential. This can speed up information retrieval and subsequently aid in bringing attention to areas affected adversely by the pandemic. Range searching is of great significance in such a scenario. For instance the researcher wants to search for countries having new cases per day between 5300 to 6000, then this can be achieved using range searching and thus range tree is one of the appropriate data structure to retrive results.

## Implementation

- We have implemented 1D and 2D range tree to process COVID-19 data of South Asian countries obtained from https://ourworldindata.org/coronavirus.
- Our interface includes a forms in which the user can perform the following steps to retrieve data:
  - Select a country name or select 'All' countries by default in the drop down list
  - Select the starting date and ending date to view data of the country/countries within the desired dates. The user can then press the search button to retrieve all the records between the given range of dates (which is our 1D search) or can enter add another field to filter the information further (this would lead to 2D search).
  - If the user presses an add button, another search box appears. From the drop down list, user can select to search on any of the relevant fields for eg. new cases.
  - The user then has to enter range for the selected field. for eg. 0 to 1000.
  - On pressing search, all the records that satisfy the desired ranges would appear in a new csv file.

## Presenation

For detailed insight on our implemention and demonstration, refer to our video presentation https://www.youtube.com/watch?v=CbNOre1wUho&t=2s

## Contributors

- Shalin Ali
- Sana Fatima
- Areesha Najam
- Mubaraka Shabbir
