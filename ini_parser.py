__author__ = 'aberes'
# need  configobj installed
# shows how to parse ini file

from configobj import ConfigObj

config = ConfigObj('file.ini')
#
FeatureA = bool(int(config['FeatureA']))
print(FeatureA)

print("with section:")
section1 = config['features']
FeatureB = section1['FeatureB']
print(bool(int(FeatureB)))
