# Data Analysis

## Evelyn Griffith

## Program Input and Output

### What is the output from running the following commands?

`poetry run dataanalysis --data-file input/data.txt`

```📦 The data file contains 50 data values in it!

🚀 Let's do some sophisticated data analysis!

🧮 Here are the results of the data analysis:

The computed mean is 87.8!
The computed median is 88.05!
The computed variance is 3.69!
The computed standard deviation is 1.92!

💡 What does this tell you about the population of this city?
```

### What are the first five lines of the contents of the file that is input into the `dataanalysis`?

```1970-01-01,81.342
1971-01-01,83.300
1972-01-01,84.700
1973-01-01,85.500
1974-01-01,86.100
```

### What is the output from running the test suite with the command `poetry run task test`?

```============================================================== test session starts ==============================================================
platform win32 -- Python 3.8.2, pytest-7.1.1, pluggy-1.0.0
rootdir: C:\Users\gforc\computer-science-102-spring-2022-ee5-data-analysis-EvelynGriffith\dataanalysis
collected 13 items

tests\test_summarize.py ...........
tests\test_transform.py ..

============================================================== 13 passed in 0.18s ===============================================================
```

## Source Code

### Describe in detail how your provided source code works

#### What is a function that analyzes a data set by computing the standard deviation? How does it work?

```def compute_standard_deviation(numbers: List[float]) -> float:
    """Compute the standard deviation of a list of numbers."""
    # call the function to calculate the variance
    vari = compute_variance(numbers)
    # calculate the standard deviation as the square root of the variance
    stand_dev = vari**0.5
    # return the calculated standard devision of the list of numbers
    return stand_dev
```

This function starts off with the function definition line. This function called compute_standard_deviation will call on a list of floats called numbers. This will then use a variable called vari to call on the function called compute_numbers while running the variable numbers through that. It will then take the variable called vari and perform the computation **0.5 which will take the square root. This will then be returned as a variable called stand_dev.

#### What is the purpose of the following function in the context of the `display` module?

```def transform_string_to_number_list(data_text: str) -> List[float]:
    """Transform a string of (date, float) values to a list of floats."""
    data_number_list = []
    for line in data_text.splitlines():
        ordered_pair = line.split(",")
        data_number_list.append(float(ordered_pair[1]))
    return data_number_list
```

This function is called the transform_string_to_number_list function. It takes a variable called data_text which is a string and then return it as a list of float values. This starts with teh variable called data_number_list which is an empty string. This will then be passed into a for loop which takes the variable called line and then splits the lines within data_text this line will then be split again into individual entities and appended to the data_number_list. This list will then be returned.

#### What is the purpose of the following function in the context of the `summarize` module?

```def compute_difference(numbers: List[float]) -> List[float]:
    """Compute difference for each value from the calculated mean."""
    # compute the mean
    mean = compute_mean(numbers)
    # compute the differences from the mean
    differences = []
    for number in numbers:
        differences.append(number - mean)
    return differences
```

This function is called then compute_difference function which takes a variable called number which is a list of floats and then returns another list of floats called differences. This will first compute the mean of the variable called numbers by calling on the compute_mean function. It will the do a for loop that takes the number within numbers and appends it to the list called differences.

## Professional Development

### What are some examples of computer science skills that were important 30 years ago but are less important to learn now? Why are they less important now?

I think the creation of poetry shells as well as the installation of dependencies was much harder and had to be coded from scratch whereas now we just have to say poetry install and it does all of that for us. My mother told me that she took weeks to code certain structures that we now have all of the installation tools for, such as docker. Docker does amazing things that would take weeks of work in the past.

### What are some examples of computer science skills that were important 30 years ago but are just as important to learn now? Why are they as important now as in the past?

I think learning the basics of how a computer "thinks" is always going to be important and learning how to think in the way that computer logic functions is never going to go away. I think that this is important becuase it is a basis for all computer languages and even if the languages change, the way that a computer functions, in the sense of its binary code and computational makeup, might not. The idea that computers take in only binary code, as in 0 and 1, I dont think will change anytime soon, and so learning how this works and how to communicate with a computer is a very useful skill.
