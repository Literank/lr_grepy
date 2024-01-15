import argparse

from grepy.grep import grep

def main():
    parser = argparse.ArgumentParser(description='''A grep-like command-line utility from LiteRank, 
                                     see https://literank.com/tutorial/9/intro''')
    parser.add_argument('pattern', type=str, help='The pattern to search for')
    parser.add_argument('file_path', type=str, help='The path to the file to search in')
    args = parser.parse_args()

    result = grep(args.pattern, args.file_path)
    for line in result:
        print(line)

if __name__ == '__main__':
    main()
