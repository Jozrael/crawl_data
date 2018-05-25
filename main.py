from common import init
from pull_data import pull_data
import analyze


def main():
    # Sets global variables 'username', 'server', and 'mode'
    init("input.txt", "output.txt")

    # Ensures we pull all newest morgue files, but only pull each file once.
    pull_data()

    # Run any analyzer functions you want here!

    # Should be optimized to identify exact killer and collate, like the next one.
    analyze.killers()

    # Could be extended to care about any subset of these three in the input file. Also the input file could flag which of these to do.
    # Maybe even an option to not care about NONEs?
    analyze.class_race_deity_frequency()


if __name__ == "__main__":
    main()
