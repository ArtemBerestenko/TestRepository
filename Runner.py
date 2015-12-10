__author__ = 'aberes'
# this script must be run by pure python
# it sets to text file 'results.txt' all failured tests


import unittest

import Groups

loader = unittest.TestLoader()

suite = loader.loadTestsFromModule(Groups)

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)

file = open("results.txt", "w")
for line in result.failures:
    file.write(str(line[0]))
file.close()
