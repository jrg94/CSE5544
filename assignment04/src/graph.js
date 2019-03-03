d3.select("body").append("svg")
  .attr("width", 960)
  .attr("height", 800);

var svg = d3.select("svg");

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

var yScale = d3.scaleLinear().range([height,0]).domain([-5,5]);
var xScale = d3.scaleLinear().range([0,width]).domain([-5,5]);

svg.append("g")
   .attr("transform", "translate(0," + height/2 + ")")
   .call(d3.axisBottom(xScale));

svg.append("g")
   .attr("transform", "translate(" + width/2 + ",0)")
   .call(d3.axisLeft(yScale));

d3.csv("data/testGHZ400clean.data").then(function(data) {

  console.log(data);


});
