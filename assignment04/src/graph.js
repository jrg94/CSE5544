var margin = 100;
var width = 800;
var height = 800;

d3.select("body").append("svg")
  .attr("width", width + 2 * margin)
  .attr("height", height + 2 * margin)
  .append("g")
  .attr("translate(" + margin + "," + margin + ")");

var svg = d3.select("svg");

var yScale = d3.scaleLinear().range([height, 0]).domain([-1, 1]);
var xScale = d3.scaleLinear().range([0, width]).domain([-1, 1]);

svg.append("g")
  .attr("transform", "translate(0," + height / 2 + ")")
  .call(d3.axisBottom(xScale));

svg.append("g")
  .attr("transform", "translate(" + width / 2 + ",0)")
  .call(d3.axisLeft(yScale));



d3.csv("data/testGHZ400clean.data").then(function(data) {

  console.log(data);

  data.forEach(function(p) {
    

    svg.append("g")
    .append("circle")
    .attr("r",2)
    .attr("cx", xScale(p.px))
    .attr("cy", yScale(p.py))
    .attr("transform", "translate(" + (xScale(p.x) - xScale(0)) + "," + (yScale(p.y) - yScale(0)) + ")")
    ;
  });

});
