import vtk
import csv


def get_csv_as_dict_list():
    dict_list = []
    with open('../../data/EHRdataSample.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for line in csv_reader:
            dict_list.append(line)
    return dict_list


def main():
    dict_list = get_csv_as_dict_list()
    colors = vtk.vtkNamedColors()


if __name__ == '__main__':
    main()
