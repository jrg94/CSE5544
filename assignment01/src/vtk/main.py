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


def dict_list_to_bins(dict_list, bin_key, comparison_key=None):
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


def create_data_column(name: str):
    """
    Creates a data column by name

    :param name: the name of the data column
    :return: the data column
    """
    col = vtk.vtkFloatArray()
    col.SetName(name)
    return col


def add_column_to_chart(chart, table, index: int, color: tuple, mark):
    points = chart.AddPlot(vtk.vtkChart.POINTS)
    points.SetInputData(table, 0, index)
    points.SetColor(color[0], color[1], color[2], color[3])
    points.SetWidth(1.0)
    points.SetMarkerStyle(mark)


def scatter_plot(view, dict_list, key_y):
    chart = vtk.vtkChartXY()
    view.GetScene().AddItem(chart)
    chart.SetShowLegend(True)
    label_axes(chart, "Age", "Count")

    # Create data columns
    table = vtk.vtkTable()
    arr_age = create_data_column("Age")
    arr_patient_count = create_data_column("Patient Count")
    arr_stress_count = create_data_column("Stress Count")
    arr_anxiety_count = create_data_column("Anxiety Count")

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

    scatter_plot(view, dict_list, "Age")

    # Screen shot
    # screen_shot(view.GetRenderWindow(), "count-by-age-with-stress-and-anxiety-plot")

    view.GetInteractor().Initialize()
    view.GetInteractor().Start()


if __name__ == '__main__':
    main()
