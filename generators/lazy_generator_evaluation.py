# With a generator, we have only the current value and cannot reference any other items in the sequence.
# This can sometimes make generators more difficult to use, but many modules and functions can help.
# The main library "itertools" provides
# 1. islice: Allows slicing a potentially infinite generator
# 2. chain: Chains together multiple generators
# 3. takewhile: Adds a condition that will end a generator
# 4. cycle: Makes a finite generator infinite by constantly repeating it

# Problem statement
# ===================
# Let’s say we’ve had an analysis routine going over temporal data, one piece of data per second,
# for the last 20 years—that’s 631,152,000 data points!
# The data is stored in a file, one second per line, and we cannot load the entire dataset into memory.
# As a result, if we wanted to do some simple anomaly detection, we’d have to use generators to save memory!

# The problem will be: Given a datafile of the form “timestamp, value,” find days whose values differ from the normal distribution.

from random import normalvariate, randint
from dataclasses import dataclass
from itertools import count
from datetime import datetime
from itertools import groupby
from itertools import islice
from scipy.stats import normaltest
from itertools import filterfalse
from operator import attrgetter


@dataclass
class Datum:
    date: datetime
    value: float


def read_data(filename):
    with open(filename) as fd:
        for line in fd:
            data = line.strip().split(',')
            timestamp, value = map(int, data)
            yield Datum(datetime.fromtimestamp(timestamp), value)


def read_fake_data(filename):
    for timestamp in count():
        #  We insert an anomalous data point approximately once a week
        if randint(0, 7 * 60 * 60 * 24 - 1) == 1:
            value = 100
        else:
            value = normalvariate(0, 1)
        yield Datum(datetime.fromtimestamp(timestamp), value)


# Now we’d like to create a function that outputs groups of data that occur in the same day.
# The only limitation is that groups will be formed only for data that is sequential.
# So if we had the input A A A A B B A A and had groupby group by the letter, we would get three groups:
# (A, [A, A, A, A]), (B, [B, B]), and (A, [A, A]).
def groupby_day(iterable):
    key = lambda row: row.date.day
    for day, data_group in groupby(iterable, key):
        yield list(data_group)


# Now to do the actual anomaly detection. We do this by creating a function that, given one group of data,
# returns whether it follows the normal distribution (using scipy.stats.normaltest).
# We can use this check with itertools.filterfalse to filter down the full dataset only to inputs
# that don’t pass the test. These inputs are what we consider to be anomalous.

def is_normal(data, threshold=1e-3):
    values = map(attrgetter("value"), data)
    k2, p_value = normaltest(tuple(values))
    return p_value >= threshold


def filter_anomalous_groups(data):
    yield from filterfalse(is_normal, data)


# Finally, we can put together the chain of generators to get the days that had anomalous data
def filter_anomalous_data(data):
    data_group = groupby_day(data)
    yield from filter_anomalous_groups(data_group)


if __name__ == '__main__':
    data = read_fake_data("fake_filename")
    anomaly_generator = filter_anomalous_data(data)
    first_five_anomalies = islice(anomaly_generator, 5)

    for data_anomaly in first_five_anomalies:
        start_date = data_anomaly[0].date
        end_date = data_anomaly[-1].date
        print(f"Anomaly from {start_date} - {end_date}")


    # Understanding groupby
    def print_groupby(iterable, keyfunc=None):
        for k, g in groupby(iterable, keyfunc):
            print("key: '{}'--> group: {}".format(k, list(g)))


    print_groupby("BCAACACAADBBB")
    print("***************************")
    print_groupby(sorted("BCAACACAADBBB"))