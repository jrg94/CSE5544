from vtk import *
import csv


def get_csv_as_dict_list():
    """
    Converts a csv file to a dictionary using DictReader

    :return: a list of dictionaries
    """
    dict_list = []
    with open('../../data/EHRdataSample.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for line in csv_reader:
            dict_list.append(line)
    return dict_list


def screen_shot(window, file_name):
    """
    Given a window and a name, it creates a screenshot alongside this source code.

    :param window: a vtkRenderer object
    :param file_name: a file name without the extension
    :return: None
    """
    window.Render()
    w2if = vtk.vtkWindowToImageFilter()
    w2if.SetInput(window)
    w2if.Update()

    writer = vtk.vtkPNGWriter()
    writer.SetFileName(file_name + ".png")
    writer.SetInputData(w2if.GetOutput())
    writer.Write()


def dict_list_to_bins(dict_list: list, bin_key: str, comparison_key=None) -> dict:
    """
    A dictionary binning function which reduces a set of data
    to a set of bins.

    :param dict_list: a list of dictionaries
    :param bin_key: a key for binning
    :param comparison_key: a key for counting
    :return: a dictionary
    """
    dict_bins = {}
    for item in dict_list:
        bin_val = item[bin_key]
        if dict_bins.get(bin_val, None):
            if comparison_key:
                dict_bins[bin_val] += float(item[comparison_key])
            else:
                dict_bins[bin_val] += 1
        else:
            if comparison_key:
                dict_bins[bin_val] = float(item[comparison_key])
            else:
                dict_bins[bin_val] = 1
    return dict_bins


def label_axes(chart, x_label: str, y_label: str):
    """
    Labels the chart axes

    :param chart: a chart instance
    :param x_label: the x-axis label
    :param y_label: the y-axis label
    :return: None
    """
    chart.GetAxis(vtk.vtkAxis.BOTTOM).SetTitle(x_label)
    chart.GetAxis(vtk.vtkAxis.LEFT).SetTitle(y_label)


def create_data_column(name: str, array):
    """
    Creates a data column by name

    :param name: the name of the data column
    :return: the data column
    """
    col = array
    col.SetName(name)
    return col


def add_column_to_chart(chart: vtkChartXY, table: vtkTable, index: int, color: tuple, mark, type=vtkChart.LINE):
    """
    Adds a column to a chart given some information

    :param chart: a VTK XY Chart
    :param table: a VTK table
    :param index: some column index
    :param color: a color tuple
    :param mark: a VTK marking
    :return: None
    """
    points = chart.AddPlot(type)
    points.SetInputData(table, 0, index)
    points.SetColor(color[0], color[1], color[2], color[3])
    points.SetWidth(1.0)

    if mark:
        points.SetMarkerStyle(mark)


def count_instances_of(dict_list, key_x, key_y):
    count = {}
    for item in dict_list:
        x = item.get(key_x)
        y = item.get(key_y)

        if not count.get(x, None):
            count[x] = {}

        if count.get(x).get(y, None):
            count[x][y] += 1
        else:
            count[x][y] = 1

    return count


def get_gender_id(gender: str) -> int:
    """
    A helper method for generating gender IDs.

    :param gender: a gender string
    :return: a gender id
    """
    if gender == "FEMALE":
        gender_id = 0
    elif gender == "MALE":
        gender_id = 1
    else:
        gender_id = 2
    return gender_id


def bar_chart(view, dict_list: list):
    chart = vtkChartXY()
    view.GetScene().AddItem(chart)
    chart.SetShowLegend(True)
    label_axes(chart, "Gender", "Count")
    table = vtk.vtkTable()

    # Create table data columns
    arr_gender = create_data_column("Gender", vtkIntArray())
    arr_patient_count = create_data_column("Count", vtkIntArray())
    arr_nsfinj_count = create_data_column("Injury Count", vtkIntArray())

    # Add table data columns to table
    table.AddColumn(arr_gender)
    table.AddColumn(arr_patient_count)
    table.AddColumn(arr_nsfinj_count)

    # Sort dict_list
    dict_list = sorted(dict_list, key=lambda data: data["Gender"])
    gender_to_count_map = dict_list_to_bins(dict_list, "Gender")
    gender_to_injury_type_map = count_instances_of(dict_list, "Gender", "Type of Injury Code")

    # Populate data table
    num_points = len(gender_to_count_map)
    table.SetNumberOfRows(num_points)
    for i in range(num_points):
        key_y_val = list(gender_to_count_map.keys())[i]
        gender_id = get_gender_id(key_y_val)
        table.SetValue(i, 0, gender_id)
        table.SetValue(i, 1, gender_to_count_map[key_y_val])
        table.SetValue(i, 2, gender_to_injury_type_map[key_y_val]["NSFINJ"])

    # Add table to chart
    add_column_to_chart(chart, table, 1, (0, 200, 0, 200), None, vtkChart.BAR)
    add_column_to_chart(chart, table, 2, (200, 0, 0, 200), None, vtkChart.BAR)

    # Labels the x-axis ticks
    labels = vtkStringArray()
    labels.SetNumberOfValues(3)
    labels.SetValue(0, "FEMALE")
    labels.SetValue(1, "MALE")
    labels.SetValue(2, "No valid match found.  Defaulted")

    # Populate the x-axis gender values
    genders = vtkDoubleArray()
    genders.SetNumberOfValues(3)
    genders.SetValue(0, 0)
    genders.SetValue(1, 1)
    genders.SetValue(2, 2)

    # Set chart axes properties
    chart.GetAxis(vtk.vtkAxis.BOTTOM).SetCustomTickPositions(genders, labels)
    chart.GetAxis(vtk.vtkAxis.BOTTOM).SetBehavior(1)
    chart.GetAxis(vtk.vtkAxis.BOTTOM).SetMinimum(-1)
    chart.GetAxis(vtk.vtkAxis.BOTTOM).SetMaximum(3)

    view.GetRenderWindow().SetMultiSamples(0)


def scatter_plot(view, dict_list: list, key_y: str):
    """
    Generates a scatter plot from a list of dictionaries,
    a view, and a data key.

    :param view: a VTK view
    :param dict_list: a list of dictionaries
    :param key_y: a data key
    :return: None
    """
    chart = vtk.vtkChartXY()
    view.GetScene().AddItem(chart)
    chart.SetShowLegend(True)
    label_axes(chart, "Age", "Count")

    # Create data columns
    table = vtk.vtkTable()
    arr_age = create_data_column("Age", vtkFloatArray())
    arr_patient_count = create_data_column("Patient Count", vtkFloatArray())
    arr_stress_count = create_data_column("Stress Count", vtkFloatArray())
    arr_anxiety_count = create_data_column("Anxiety Count", vtkFloatArray())

    # Add columns to table
    table.AddColumn(arr_age)
    table.AddColumn(arr_patient_count)
    table.AddColumn(arr_stress_count)
    table.AddColumn(arr_anxiety_count)

    # Sort dict_list
    dict_list = sorted(dict_list, key=lambda data: float(data[key_y]))
    age_to_count_map = dict_list_to_bins(dict_list, key_y)
    age_to_stress_count_map = dict_list_to_bins(dict_list, key_y, "Stress")
    age_to_anxiety_count_map = dict_list_to_bins(dict_list, key_y, "Anxiety")

    # Populate columns
    num_points = len(dict_list)
    table.SetNumberOfRows(num_points)
    for i in range(num_points):
        key_y_val = dict_list[i][key_y]
        table.SetValue(i, 0, key_y_val)
        table.SetValue(i, 1, age_to_count_map[key_y_val])
        table.SetValue(i, 2, age_to_stress_count_map[key_y_val])
        table.SetValue(i, 3, age_to_anxiety_count_map[key_y_val])

    # Key
    add_column_to_chart(chart, table, 1, (0, 200, 0, 200), vtk.vtkPlotPoints.CIRCLE)
    add_column_to_chart(chart, table, 2, (200, 0, 0, 200), vtk.vtkPlotPoints.CROSS)
    add_column_to_chart(chart, table, 3, (0, 0, 200, 200), vtk.vtkPlotPoints.PLUS)

    view.GetRenderWindow().SetMultiSamples(0)


def main():
    dict_list = get_csv_as_dict_list()

    view = vtk.vtkContextView()
    view.GetRenderer().SetBackground(1.0, 1.0, 1.0)
    view.GetRenderWindow().SetSize(800, 800)

    # scatter_plot(view, dict_list, "Age")
    bar_chart(view, dict_list)

    # Screen shot
    screen_shot(view.GetRenderWindow(), "count-by-gender-bar-graph-formatted")

    view.GetInteractor().Initialize()
    view.GetInteractor().Start()


if __name__ == '__main__':
    main()
