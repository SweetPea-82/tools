import os
import argparse

# Okay I am defining
class timeInWeek():
    def __init__(self, args):
        self.args = args

def parse_arguments():
    parser = argparse.ArgumentParser( 
                                    description='This is the help page. The arguments are below:' 
                                    )

    args = parser.parse_args()

    return args

def main():
    args = parse_arguments()


if __name__ == "__main__":
    main()