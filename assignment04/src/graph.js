d3.select("body").append("svg")
  .attr("width", 960)
  .attr("height", 800);

var svg = d3.select("svg");

svg.append("rect")
  .attr("width", "100%")
  .attr("height", "100%")
  .attr("fill", "gray");

var margin = {
  top: 30,
  right: 30,
  bottom: 30,
  left: 30
}

var width = +svg.attr("width") - margin.left - margin.right
var height = +svg.attr("height") - margin.top - margin.bottom

var g = svg.append("g")
  .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

svg.append("text")
  .attr("x", width / 2)
  .attr("y", 20)
  .attr("text-anchor", "middle")
  .style("font-size", "16px")
  .style("text-decoration", "underline")
  .text("Patient ID vs. Days from First TBI");

var parseTime = d3.timeParse("%d-%b-%y");

var x = d3.scaleLinear()
  .range([0, width]);

var y = d3.scaleBand()
  .range([0, height])
  .padding(.2);

var colors = d3.scaleSequential(d3.interpolateCool);

d3.csv("data/EHRdataSample.csv").then(function(data) {

  console.log(data);

  xMax = d3.max(data, function(d) {
    return Number(d.Days_From1stTBI);
  })
  xMin = d3.min(data, function(d) {
    return Number(d.Days_From1stTBI);
  })
  bound = d3.max([xMax, Math.abs(xMin)])

  x.domain([-bound, bound]);
  colors.domain([-bound, bound]);

  y.domain(
    data.map(function(d) {
      return d.PatientID;
    })
  );

  g.selectAll(".bar")
    .data(data)
    .enter().append("rect")
    .attr("class", "bar")
    .attr("x", function(d) {
      return x(d.Days_From1stTBI);
    })
    .attr("y", function(d) {
      return y(d.PatientID);
    })
    .attr("width", function(d) {
      return 3;
    })
    .attr("height", y.bandwidth())
    .attr("fill", function(d, i) {
      return colors(d.Days_From1stTBI);
    })
    .attr("opacity", function(d) {
      if (d.Days_From1stTBI < 0) {
        return 0.5;
      } else {
        return 1.0;
      }
    })
    .on("mouseover", handleMouseOver)
    .on("mouseout", handleMouseOut);

  g.append("g")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x))
    .append("text")
    .attr("x", 0)
    .attr("y", -5)
    .attr("fill", "#000")
    .attr("text-anchor", "start")
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

});

function handleMouseOver(d, i) { // Add interactivity
  svg.append("text")
    .attr("x", function() {
      return x(d.Days_From1stTBI);
    })
    .attr("y", function() {
      return y(d.PatientID) + 20;
    })
    .attr("fill", "#FFF")
    .attr("id", "t" + d.EncounterID)
    .text(function() {
      return d.Encounter_date; // Value of the text
    });
}

function handleMouseOut(d, i) {
  d3.select("#t" + d.EncounterID).remove(); // Remove text location
}
