# CSE 5544 Assignment 1

For the first assignment, we were asked to review two visualization tools.
Having worked with WebGL in the past, that was my first choice. I also decided
to explore VTK. You can find both of those reviews in the docs folder.

As for the second portion of the assignment, we were asked to use two tools
to create a couple visualizations. The remainder of this document covers that
portion of the assignment.

## Visualizations

## Favorite Image

Of the four visualizations above, my favorite visualization is:

![Favorite Viz]()

## Features

In this section, I'll be covering the two best and one worst feature of
the two tools I used: VTK and D3.

### VTK

VTK, or the Visualization Toolkit, is a visualization platform that has API
support in a handful of popular languages like Python, Java, and C++. In the
following sections, I'll cover the two best features and the worst feature.

#### Best Two Features

#### Worst Feature

By far, the **worst** feature of VTK is installation. As a PC user, I had to go
through an incredibly lengthy installation process just to start rendering
visualizations.

According to the official documentation, installing VTK is a 7-step process:

1. Download VTK
2. Download CMake
3. Create a Build Folder
4. Run CMake
5. Open the Visual Studio Project
6. Install the Project
7. Manual Building

In total, I spent about a day and a half getting all this together. After all,
the CMake build and the Visual Studio build both take over an hour. And,
if you're like me, you don't have Visual Studio or CMake, so downloading and
installing those tools takes some time.

In addition, the directions include some implicit instructions on how to run
CMake and Visual Studio, so I had to spend some time learning the ropes there
as well.

After fighting with all that, I had to install Conda to install the Python VTK
package. I'm not sure if there's an easier way to do all this, but there are
certainly no tutorials to help.

*Fun Fact*: In the time it took me to write this section, the Visual Studio build
was only 25% complete.

### D3
