from os import remove
from os.path import isfile


def data_store():
    return

# As the init grows to encompass config options per analyze choice,
# this really needs to be genericized.


def init(in_file, out_file):
    global username
    global server
    global mode
    with open(in_file, "r") as input_file:
        input_file = open(in_file)
        username = input_file.readline().split("=", 1)[1].strip()
        server = input_file.readline().split("=")[1].strip()
        mode = input_file.readline().split("=")[1].strip()
        if isfile(out_file):
            remove(out_file)


def print_block(morgue_file_lines, starting_index):
    output = ""
    while True:
        output += morgue_file_lines[starting_index].strip()
        if mode in ["original", "compact"]:
            output += "\n"
        if mode == "compact":
            break
        if (morgue_file_lines[starting_index]
                [len(morgue_file_lines[starting_index])-1] in ['.', '!']):
            output += "\n"
            break
        starting_index += 1
    return output


def write_output(output):
    with open("output.txt", "a") as o:
        o.write(output)
