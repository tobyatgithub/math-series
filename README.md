# math-series

**Author**: Toby  
**Version**: 1.0.0 (increment the patch/fix version number up if you make more commits past your first submission)

## Overview
<!-- Provide a high level overview of what this application is and why you are building it, beyond the fact that it's an assignment for a Code Fellows 401 class. (i.e. What's your problem domain?) -->
This is a coding challenge called the math series. In this work has three main math functions, one for calculating nth value of fibonacci series, the other calculates nth of lucas series, another one calculates a sum of series where the series satisfy formular a_{n} = a_{n-1} + a_{n-2} for n larger or equal to 3.  

The code also contain a user interface in python with welcoming info and a constent input stream to ask for user input and return associated values. e.g. after you run the series.py, typing in lucas(5) will return the 5th value of lucas series.  

## Getting Started
<!-- What are the steps that a user must take in order to build this app on their own machine and get it running? -->
To run the series.py code on your machine, you will need python 3.6.  
To run the test_series via pytest, you will need both python 3.6 and pytest.  


## Architecture
<!-- Provide a detailed description of the application design. What technologies (languages, libraries, etc) you're using, and any other relevant design information. This is also an area which you can include any visuals; flow charts, example usage gifs, screen captures, etc.-->
I applied recursive technique to solve these problems. To improve the performance, I also used dynamic programming to store values and reduce redundancy.  
The core idea of recursive algorithm here is in the format of :  
```python
def f(x):
    if basecase1:  
    ...  
    if basecase2:  
    ...  
    return f(x-1) + f(x-2)  
```

## API
<!-- Provide detailed instructions for your applications usage. This should include any methods or endpoints available to the user/client/developer. Each section should be formatted to provide clear syntax for usage, example calls including input data requirements and options, and example responses or return values. -->
No API available yet.


## Change Log
<!-- Use this are to document the iterative changes made to your application as each feature is successfully implemented. Use time stamps. Here's an example:-->

11/27/18 4:59pm - Added functionality to add and delete some things.
11/27/18 22:43pm - Updated file and readme.md.

