import argparse

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str)
    parser.add_argument('--change', type=str)
    return parser.parse_args()

def modify_yaml_line(file_path, new_content):
    # Ensure the file exists
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
    except FileNotFoundError:
        print("File not found.")
        return

    # Check if the file has at least 10 lines
    if len(lines) < 10:
        print("The file does not have enough lines.")
        return

    # Modify the 10th line
    lines[9] = new_content + '\n'  # Add newline character if needed

    # Write the changes back to the file
    with open(file_path, 'w') as file:
        file.writelines(lines)


if __name__ == '__main__':
    opt = parse_opt()
    modify_yaml_line(opt.path, opt.change)
