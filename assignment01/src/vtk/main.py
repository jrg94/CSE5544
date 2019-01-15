import vtk
import csv
import math


def get_csv_as_dict_list():
    dict_list = []
    with open('../../data/EHRdataSample.csv') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for line in csv_reader:
            dict_list.append(line)
    return dict_list


def main():
    dict_list = get_csv_as_dict_list()

    view = vtk.vtkContextView()
    view.GetRenderer().SetBackground(1.0, 1.0, 1.0)
    view.GetRenderWindow().SetSize(400, 300)

    chart = vtk.vtkChartXY()
    view.GetScene().AddItem(chart)
    chart.SetShowLegend(True)

    table = vtk.vtkTable()

    arrX = vtk.vtkFloatArray()
    arrX.SetName('X Axis')

    arrC = vtk.vtkFloatArray()
    arrC.SetName('Cosine')

    arrS = vtk.vtkFloatArray()
    arrS.SetName('Sine')

    arrT = vtk.vtkFloatArray()
    arrT.SetName('Sine-Cosine')

    table.AddColumn(arrX)
    table.AddColumn(arrC)
    table.AddColumn(arrS)
    table.AddColumn(arrT)

    numPoints = 100

    inc = 7.5 / (numPoints - 1)
    table.SetNumberOfRows(numPoints)
    for i in range(numPoints):
        table.SetValue(i, 0, i * inc)
        table.SetValue(i, 1, math.cos(i * inc))
        table.SetValue(i, 2, math.sin(i * inc))
        table.SetValue(i, 3, math.sin(i * inc) - math.cos(i * inc))

    # Cos
    points = chart.AddPlot(vtk.vtkChart.POINTS)
    points.SetInputData(table, 0, 1)
    points.SetColor(0, 100, 0, 255)
    points.SetWidth(1.0)
    points.SetMarkerStyle(vtk.vtkPlotPoints.CROSS)

    # Sin
    points = chart.AddPlot(vtk.vtkChart.POINTS)
    points.SetInputData(table, 0, 2)
    points.SetColor(0, 0, 0, 255)
    points.SetWidth(1.0)
    points.SetMarkerStyle(vtk.vtkPlotPoints.PLUS)

    # Sin - Cos
    points = chart.AddPlot(vtk.vtkChart.POINTS)
    points.SetInputData(table, 0, 3)
    points.SetColor(0, 0, 255, 255)
    points.SetWidth(1.0)
    points.SetMarkerStyle(vtk.vtkPlotPoints.CIRCLE)

    view.GetRenderWindow().SetMultiSamples(0)
    view.GetInteractor().Initialize()
    view.GetInteractor().Start()




if __name__ == '__main__':
    main()
