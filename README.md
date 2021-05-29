# Final Project : Inverted Additions
# Topic : Range Trees
# [CS 201 Data Structures II, Spring 2021, Habib University]
-------

## Background and Motivation

For our final project for the course, we had to pick any problem relevant for the application of range trees. In this regard our team decided to pick an information retrieval problem pertinent to current global sitution. In light of COVID-19 pandemic that has taken over the world by storm, processing of COVID-19 data is extremely essential. This can speed up information retrieval and subsequently aid in bringing attention to areas affected adversely by the pandemic. Range searching is of great significance in such a scenario. For instance the researcher wants to search for countries having new cases per day between 5300 to 6000, then this can be achieved using range searching and thus range tree is one of the appropriate data structure to retrive results.

## Range Trees

A data structure used for range queries. It uses Balanced binary search tree for set of data points in n-dimensional space.

## Properties

- It stores data in leaf nodes in a sorted manner. 
- Every internal node in n-dimensional space stores an associated tree.
- Search Complexity for n-dimensional space O(log^d n + k)
- This data structure is best used for searching only and constructs a Range Tree once and stores it for search operations, hence deletion and insertion are not of much interest.

## Testing/How to Run Our Application
- We have implemented 1D and 2D range tree to process COVID-19 data of South Asian countries obtained from https://ourworldindata.org/coronavirus.

- Pre-Requirements:
   - In order to run our application for the testing (searching) purposes you need to install tkinter. Tkinter is the standard GUI library for Python which provides a fast and       easy way to create GUI applications. It provides a powerful object-oriented interface to the Tk GUI toolkit. You may write pip install tkinter in your terminal for the said     installation. This will get tkinter installed in your local PC. 
   - As we have added calendar in our application, we have used  tkcalendar for this purpose. Tkcalendar is a python module that provides the Calendar and DateEntry widgets for Tkinter. Fpr installation of tkcalendar you may use command i.e.  pip install tkcalendar.
   -  In our code, we have written some import statements which has been associated with the libraries mentioned above which allow us to use specific functionalities of these libraries.
   
- Our interface includes a forms in which the user can perform the following steps to retrieve data:
  - Select a country name or select 'All' countries by default in the drop down list
  - Select the starting date and ending date to view data of the country/countries within the desired dates. The user can then press the search button to retrieve all the records between the given range of dates (which is our 1D search) or can enter add another field to filter the information further (this would lead to 2D search).
  - If the user presses an add button, another search box appears. From the drop down list, user can select to search on any of the relevant fields for eg. new cases.
  - The user then has to enter range for the selected field. for eg. 0 to 1000.
  - On pressing search, all the records that satisfy the desired ranges would appear in a new csv file.

 

## Demonstration
For detailed insight on our implemention and demonstration, refer to our video presentation https://www.youtube.com/watch?v=CbNOre1wUho&t=2s

 

## Team Members
- Shalin Ali : Implemented construction of 1D and 2D range trees.
- Mubaraka Shabbir : Implemented 1D and 2D range searching
- Sana Fatima : Linking code (range tree) with GUI forms and preparation of narration (story and slides) for demo.
- Areesha Najam : Linking code (range tree) with GUI forms and preparation of narration (story and slides) for demo.

## References

- Data Set: https://ourworldindata.org/coronavirus.

- Understanding/Research of Range Trees:
  - https://www.cise.ufl.edu/class/cot5520sp18/CG_RangeTrees.pdf
  - http://www.cs.umd.edu/class/fall2020/cmsc420-0201/Lects/lect17-range-tree.pdf
  - https://www.cse.wustl.edu/~taoju/cse546/lectures/Lecture21_rangequery_2d.pdf 

- Animated pictures for story telling: https://www.dreamstime.com
 
