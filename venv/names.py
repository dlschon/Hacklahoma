import re
import random

class Names:
    file_lastnames = "./Resources/names.last.txt"
    file_firstnames_male = "./Resources/names.first.male.txt"
    file_firstnames_female = "./Resources/names.first.female.txt"

    # Parses the file and returns an array of type (string, float)
    def parse_file(self, fname):
        # Parse the last names file
        with open(fname) as f:
            content = f.readlines()

            name_set = []
            tokens = []
            data = []

            # Add all of the names and their probibilities to the list
            for line in content:
                tokens = re.compile(' *').split(line)
                data.append(tokens)

            # Due to shortened files, the probabilities don't add to 100%
            # To fix this, divide each probability by the cumulative sum
            cum_sum = float(tokens[2])
            for entry in data:
                name_set.append((entry[0], float(entry[1])/cum_sum))

            return name_set

    def __init__(self):
        self.last_names = self.parse_file(Names.file_lastnames)
        self.first_names_male = self.parse_file(Names.file_firstnames_male)
        self.first_names_female = self.parse_file(Names.file_firstnames_female)

    def generate_name(self, name_set):
        # a random number from 0 to 1 used to pick a name
        rand_num = random.random()
        for name in name_set:
            # Subtract the probability from the counter
            rand_num -= name[1]

            # If the counter reaches 0, return the current name
            if (rand_num < 0):
                return name[0][0].upper() + name[0][1:].lower()

    def generate_name_first_male(self):
        return self.generate_name(self.first_names_male)

    def generate_name_first_female(self):
        return self.generate_name(self.first_names_female)

    def generate_name_last(self):
        return self.generate_name(self.last_names)

    def generate_name_full_male(self):
        return self.generate_name(self.first_names_male) + " " + self.generate_name_last()

    def generate_name_full_female(self):
        return self.generate_name(self.first_names_female) + " " + self.generate_name_last()
