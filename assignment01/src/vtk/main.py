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


def scatter_plot(view, dict_list, key_y):
    chart = vtk.vtkChartXY()
    view.GetScene().AddItem(chart)
    chart.SetShowLegend(True)

    table = vtk.vtkTable()

    # Create x-axis collection
    arrX = vtk.vtkIntArray()
    arrX.SetName("X-axis")
    chart.GetAxis(vtk.vtkAxis.BOTTOM).SetTitle("Index")

    # Create cosine collection
    arrC = vtk.vtkFloatArray()
    arrC.SetName(key_y)
    chart.GetAxis(vtk.vtkAxis.LEFT).SetTitle(key_y)

    # Add columns to table
    table.AddColumn(arrX)
    table.AddColumn(arrC)

    # Sort dict_list
    dict_list = sorted(dict_list, key=lambda data: float(data[key_y]))

    # Populate columns
    numPoints = len(dict_list)
    table.SetNumberOfRows(numPoints)
    for i in range(numPoints):
        table.SetValue(i, 0, i)
        table.SetValue(i, 1, dict_list[i][key_y])

    print(dict_list)

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
    screen_shot(view.GetRenderWindow(), "age-by-index-scatter-plot-sorted")

    view.GetInteractor().Initialize()
    view.GetInteractor().Start()


if __name__ == '__main__':
    main()
