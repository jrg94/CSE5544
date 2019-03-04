var width = 800;
var height = 800;

d3.select("body").append("svg")
  .attr("width", width)
  .attr("height", height)
  .append("g");

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

  data = data.reduce((rows, key, index) => (index % 400 == 0 ? rows.push([key])
  : rows[rows.length-1].push(key)) && rows, []);

  var j = 0;
  data.forEach(function(row) {
    var i = 0;
    row.forEach(function(p) {
      p.px /= 40; // Arbitrary scale down
      p.py /= 40;
      if (i % 50 == 0 && j % 50 == 0) {

        svg.append("g")
          .append("path")
          .attr("d", "M" + xScale(0) + " " + yScale(0) + " L" + xScale(p.px) + " " + yScale(p.py))
          .attr("stroke", "green")
          .attr("stroke-width", 1)
          .attr("fill", "none")
          .attr("transform", "translate(" + (xScale(p.x) - xScale(0)) + "," + (yScale(p.y) - yScale(0)) + ")");

        svg.append("g")
          .append("circle")
          .attr("r", 1.5)
          .attr("cx", xScale(p.px))
          .attr("cy", yScale(p.py))
          .attr("transform", "translate(" + (xScale(p.x) - xScale(0)) + "," + (yScale(p.y) - yScale(0)) + ")");

      }
      i++;
    });
    j++;
  });

});
