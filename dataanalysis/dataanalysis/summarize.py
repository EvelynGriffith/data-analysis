"""Summarize data values to support data analysis."""

# incorrect all of the needed type annotations

from typing import List


def compute_mean(numbers: List[float]) -> float:
    """Compute the mean for a list called numbers which contains floats."""
    # sum the list of the numbers
    Sum = sum(numbers)
    # determine the length of the list of numbers
    Size = len(numbers)
    # as long as the computation will not be an
    # undefined division by zero, compute the mean
    for i in numbers:
        if i in numbers != 0:
            mean = Sum / Size
            return mean
    # https://stackoverflow.com/questions/58400652/average-returning-a-value-even-when-list-is-empty
    # if the list was empty, then return a mean that is "not a number"
    return float("NaN")


def compute_median(numbers: List[float]) -> float:
    """Compute the median of a list of numbers."""
    # sort the numbers in an "in place" fashion
    n = len(numbers)
    numbers.sort()
    # as long as the computation will not be an
    # undefined division by zero, compute the median
    # case: the count of the values is even
    if n in numbers != 0:
        if n % 2 == 0:
            # get the two indices that are before and after the middle
            # convert to an integer to prepare for indexing
            # adjust for the fact that lists index starting at 0
            m1 = n/2
            m2 = (n/2) + 1
            m1 = int(m1) - 1
            m2 = int(m2) - 1
            # compute the median value
            median = (numbers[m1] + numbers[m2])/2
        else:
            # case: the count of the values is odd
            m = (n+1)/2
            # convert to an integer to prepare for indexing
            # adjust for the fact that lists index starting at 0
            m = int(m) - 1
            median = numbers[m]
            # if the list was empty, then return a median that is "not a number"
        # return the computed median value
        return median
    return float("Nan")

def compute_difference(numbers: List[float]) -> List[float]:
    """Compute difference for each value from the calculated mean."""
    # Refer to the book called "Doing Math with Python"
    # for details about how to implement this function
    # compute the mean
    mean = compute_mean(numbers)
    diff = []
    for num in numbers:
        diff.append(num-mean)
    return diff
    # compute the differences from the mean
    # return the computed differences from the mean


def compute_variance(numbers: List[float]) -> float:
    """Compute the variance of a list of numbers."""
    # compute the difference from the mean
    diff = compute_difference(numbers)
    squared_diff = []
    for d in diff:
        squared_diff.append(d**2)
    sum_squared_diff = sum(squared_diff)
    variance = sum_squared_diff/len(numbers))
    return variance
    # compute the squared differences
    # calculate the variance
    # return the calculated variance of the list of numbers


def compute_standard_deviation(numbers: List[float]) -> float:
    """Compute the standard deviation of a list of numbers."""
    # call the function to calculate the variance
    vari = compute_variance(numbers)
    # calculate the standard deviation as the square root of the variance
    stand_dev = vari**0.5
    # return the calculated standard devision of the list of numbers
    return stand_dev
