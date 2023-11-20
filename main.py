import re


class VowelCounter:

    def __init__(self):
        # vowels according to task specification
        self.vowels = 'a|e|i|o|u'

    def get_vowel_count(self, input: str) -> int:
        # convert input to lower case letters
        input = input.lower()
        # obtain vowels and vowel count
        vowels = re.findall(self.vowels, input)
        num_vowels = len(vowels)
        return num_vowels


if __name__ == '__main__':

    # instantiate the vowel counter
    vowel_counter = VowelCounter()

    # start infinite loop of queries and answers
    while True:
        valid = False
        while not valid:
            # obtain user input
            print("Please enter something, or enter 'q' to quit: ")
            user_input = input("Your input: ")

            # process input
            if user_input == 'q':
                quit()
            elif len(user_input) > 0:
                valid = True
            else:
                print("Input invalid.")
        
        # obtain and print vowel count
        num_vowels = vowel_counter.get_vowel_count(user_input)
        print(f"The input string contains {num_vowels} vowels.\n")