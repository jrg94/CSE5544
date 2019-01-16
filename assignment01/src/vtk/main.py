from vtk import *
import csv


def get_csv_as_dict_list():
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


def dict_list_to_bins(dict_list, bin_key):
    dict_bins = {}
    for item in dict_list:
        bin_val = item[bin_key]
        if dict_bins.get(bin_val, None):
            dict_bins[bin_val] += 1
        else:
            dict_bins[bin_val] = 1
    return dict_bins


def label_axes(chart, x_label, y_label):
    chart.GetAxis(vtk.vtkAxis.BOTTOM).SetTitle(x_label)
    chart.GetAxis(vtk.vtkAxis.LEFT).SetTitle(y_label)


def add_data_column(name):
    col = vtk.vtkFloatArray()
    col.SetName(name)
    return col


def scatter_plot(view, dict_list, key_y):
    chart = vtk.vtkChartXY()
    view.GetScene().AddItem(chart)
    chart.SetShowLegend(True)
    label_axes(chart, "Age", "Count")

    # Create data columns
    table = vtk.vtkTable()
    arr_age = add_data_column("Age")
    arr_patient_count = add_data_column("Patient Count")

    # Add columns to table
    table.AddColumn(arr_age)
    table.AddColumn(arr_patient_count)

    # Sort dict_list
    dict_list = sorted(dict_list, key=lambda data: float(data[key_y]))
    data_bins = dict_list_to_bins(dict_list, key_y)
    print(data_bins)

    # Populate columns
    numPoints = len(dict_list)
    table.SetNumberOfRows(numPoints)
    for i in range(numPoints):
        key_y_val = dict_list[i][key_y]
        table.SetValue(i, 0, key_y_val)
        table.SetValue(i, 1, data_bins[key_y_val])

    # Key
    points = chart.AddPlot(vtk.vtkChart.POINTS)
    points.SetInputData(table, 0, 1)
    points.SetColor(0, 100, 0, 255)
    points.SetWidth(1.0)
    points.SetMarkerStyle(vtk.vtkPlotPoints.CIRCLE)

    view.GetRenderWindow().SetMultiSamples(0)


def main():
    dict_list = get_csv_as_dict_list()

    view = vtk.vtkContextView()
    view.GetRenderer().SetBackground(1.0, 1.0, 1.0)
    view.GetRenderWindow().SetSize(800, 800)

    scatter_plot(view, dict_list, "Age")

    # Screen shot
    screen_shot(view.GetRenderWindow(), "count-by-age-plot")

    view.GetInteractor().Initialize()
    view.GetInteractor().Start()


if __name__ == '__main__':
    main()
