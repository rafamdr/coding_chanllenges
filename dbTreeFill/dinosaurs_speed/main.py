# You will be supplied with two data files in CSV format. The first file contains
# statistics about various dinosaurs. The second file contains additional data.
#
# Given the following formula,
#
# speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
# Where g = 9.8 m/s^2 (gravitational constant)
#
# Write a program to read in the data files from disk, it must then print the names
# of only the bipedal dinosaurs from fastest to slowest. Do not print any other information.

# $ cat dataset1.csv
# NAME,LEG_LENGTH,DIET
# Hadrosaurus,1.4,herbivore
# Struthiomimus,0.72,omnivore
# Velociraptor,1.8,carnivore
# Triceratops,0.47,herbivore
# Euoplocephalus,2.6,herbivore
# Stegosaurus,1.50,herbivore
# Tyrannosaurus Rex,6.5,carnivore

# $ cat dataset2.csv
# NAME,STRIDE_LENGTH,STANCE
# Euoplocephalus,1.97,quadrupedal
# Stegosaurus,1.70,quadrupedal
# Tyrannosaurus Rex,4.76,bipedal
# Hadrosaurus,1.3,bipedal
# Deinonychus,1.11,bipedal
# Struthiomimus,1.24,bipedal
# Velociraptorr,2.62,bipedal

# ---------------------------------------------------------------------------------------------------------------------
import math

def calculate_speed(leg_length, stride_length):
    return ((stride_length / leg_length) - 1) * math.sqrt(leg_length * 9.8)

def main():
    dict = {}

    with open('dataset2.csv', 'r') as dataset2:
        dataset2.readline() # skipping column titles
        while line := dataset2.readline():
            arr_line = line.split(',')
            if arr_line[2].startswith('bipedal'):
                dict[arr_line[0]] = [float(arr_line[1]), 0]

    with open('dataset1.csv', 'r') as dataset1:
        dataset1.readline() # skipping column titles
        while line := dataset1.readline():
            arr_line = line.split(',')
            if arr_line[0] in dict:
                dict[arr_line[0]] = calculate_speed(float(arr_line[1]), dict[arr_line[0]][0])

    remove = [k for k in dict if type(dict[k]) == type([])]
    for k in remove: del dict[k]

    dict_tuples = list(dict.items())
    dict_tuples = sorted(dict_tuples, key=lambda x: x[1], reverse=True)

    for item in dict_tuples:
        print(item)
# ---------------------------------------------------------------------------------------------------------------------


if __name__ == "__main__":
    main()
# ---------------------------------------------------------------------------------------------------------------------
