import csv
import argparse


def main():
    parser = argparse.ArgumentParser(description='Fix csv file.')
    parser.add_argument('sourcecsv', nargs=1, help='source csv to fix')
    parser.add_argument('targetcsv', nargs=1, help='target fixed csv to create')
    parser.add_argument('--in-delimiter', nargs='?', help='delim')
    parser.add_argument('--in-quote', nargs='?', help='quote')
    args = parser.parse_args()

    if not args.in_delimiter or not args.in_quote:
        with open(args.sourcecsv[0], 'r') as sfile:
            dialect = csv.Sniffer().sniff(sfile.read(1024))
            sfile.seek(0)
            source_reader = csv.reader(sfile, dialect)
            with open(args.targetcsv[0], 'w') as tfile:
                target_writer = csv.writer(tfile, delimiter=',')
                for row in source_reader:
                    target_writer.writerow(row)
    else:
        dlim = args.in_delimiter
        quote = args.in_quote
        with open(args.sourcecsv[0], 'r') as sfile:
            source_reader = csv.reader(sfile, delimiter=dlim, quotechar=quote)
            with open(args.targetcsv[0], 'w') as tfile:
                target_writer = csv.writer(tfile, delimiter=',')
                for row in source_reader:
                    target_writer.writerow(row)


if __name__ == '__main__':
    main()
