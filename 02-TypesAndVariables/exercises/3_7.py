###
# A program that calculates and prints:
# - the number of people and percentage of the total
#   population living in the Northern Hemisphere
# - the number of people and percentage of the total
#   population living in the Southern Hemisphere
#
total = 8_000_000_000
north = 7_200_000_000
south = total - north
print("World population:", total)
print(f"Northern Hemisphere: {north} ({north / total:.0%})") #:.0% - mnoży *100, zaokrągla do całości bez miejsc po przecinku
print(f"Southern Hemisphere: {south} ({south / total:.0%})")