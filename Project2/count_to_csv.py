
import sys
from count import count_letter

def main():
    selected_count_word = None
    args = sys.argv
    remove_case = True

    # process command line arguments
    if "-c" in args:
        remove_case = False
    if "-l" in args:
        index = args.index("-l")
        selected_count_word = args[index + 1]
    fill_zero = False

    if "-z" in args:
        fill_zero = True
    i = 1
    file_list = []
    output_file = None

    # handle all requested arguments
    while i < len(args):
        arg = args[i]
        if arg in ['-c', '-z']:
            i += 1
            continue
        if arg == "-l":
            i += 2
            continue
        if i == len(args)-1:
            output_file = arg
            i += 1
        else:
            file_list.append(arg)
            i += 1

    # call count_letter after processing arguments
    d = count_letter(remove_case, selected_count_word, fill_zero, file_list)

    with open(output_file, "w") as f:
        for k, v in d.items():
            line = "{},{}".format(k, v)
            f.write(line+"\n")

if __name__ == '__main__':
    main()
