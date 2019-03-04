# Assignment 04

In assignment 4, we were asked to directly visualize a 2D vector field from
a given data file. Naturally, [I used D3][1]. In the following sections, I'll
explain my findings.

## Direct visualization

To visualize the vector field, I used several data filtering methods. For the
sake of completeness, I'll share all of the figures I generated below.

### Figure 1

The following visualization demonstrates 1 x 1 sampling for a total of 16,000
vectors.

![1 x 1 Sampling Vector Field][2]

Due to the density of the vectors, it's very difficult to see any sort of
pattern here. In fact, we can't even see the axes. On top of that, it takes
some time to render and 16,000 data points.

### Figure 2

The following visualization demonstrates 2 x 2 sampling for a total of 8,000
vectors.

![2 x 2 Sampling Vector Field][3]

Reducing the vector count by half introduces what look like aliasing defects
in the visualization. That said, at the very least the axes are visible, and
rendering time is decent.

[1]: assignment03.html
[2]: assets/1-by-1-sampling.JPG
[3]: assets/2-by-2-sampling.JPG
