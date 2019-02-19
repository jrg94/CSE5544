d3.select("body").append("svg")
  .attr("width", 960)
  .attr("height", 500);

var svg = d3.select("svg"),
  margin = {
    top: 20,
    right: 20,
    bottom: 30,
    left: 50
  },
  width = +svg.attr("width") - margin.left - margin.right,
  height = +svg.attr("height") - margin.top - margin.bottom,
  g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");


var parseTime = d3.timeParse("%d-%b-%y");

var x = d3.scaleLinear()
  .range([0, width])

var y = d3.scaleBand()
  .range([0, height])
  .padding(.2);

d3.csv("/data/EHRdataSample.csv").then(function(data) {

  x.domain(
      d3.extent(data, function(d) { return d.Days_From1stTBI; }),
  );

  y.domain(
      data.map(function(d) { return d.PatientID; })
  );


  g.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x))
    .append("text")
    .attr("x", width/2)
    .attr("y", 15)
    .attr("fill", "#000")
    .text("Days From 1st TBI");

  g.append("g")
    .attr("transform", "translate(" + (width / 2) + ",0)")
    .call(d3.axisLeft(y))
    .append("text")
    .attr("fill", "#000")
    .attr("transform", "rotate(-90)")
    .attr("y", 6)
    .attr("dy", "0.71em")
    .attr("text-anchor", "end")
    .text("PatientID");

  g.selectAll(".bar")
    .data(data)
    .enter().append("rect")
    .attr("class", "bar")
    .attr("x", function(d) {
      return x(Math.min(0, Number(d.Days_From1stTBI)));
    })
    .attr("y", function(d) {
      return y(d.PatientID);
    })
    .attr("width", function(d) {
      return 5;
    })
    .attr("height", y.bandwidth())

});
