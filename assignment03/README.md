# Assignment 03

[Assignment 03][2] is a two part assignment based on event analysis.

## Part One (1-5)

During part one, we were asked to come up with some visualization methods
for the EHR data set. 

### Group (1)

In part one, we were asked to get into groups. The following list
contains all the group members.

- Jeremy Grifski

### Tasks & Visualization (2, 3, 5)

In part one, we were asked to come up with some interesting tasks to support
in our visualization such as finding the time span of the most frequent encounter 
during the 2nd month. Then, we were asked to abstract that task, so it could be
reused in other scenarios.

To address subsection 2, 3, and 5, we listed some data of interest, some associated
tasks, some inspiration for visualization, and a sample visualization.

#### Data of interest

- PatientID
- Flags (PTSD, Depression, Audiology, etc.)

#### Tasks

- Count flag total per patient over time
  - Line plot (flag count over time)
- Count lifetime flags per patient against total incidents (# of occurrences of PatientID)
  - Scatterplot (lifetime flag totals vs. incident count)
- Interactive
  - Both plots show an overview of everything
  - Allow for patient selection which fades out both graphs
  
#### Inspiration

![Controlling the Blue Line][1]

#### Design

### Design Analysis (4)

- how does the design address *event-relevant* tasks?
- how many items can the design show on a 24-inch monitor?
- does it use overview+detail technique?
- does it show "temporal" changes?
- whether or not it introduces clutter by comparing with all other designs
- is the design visually pleasing?

## Part Two (6)



[1]: assets/controlling-the-blue-line.jpeg
[2]: https://sites.google.com/site/datavisualizationspring2019/exercise/assignment-3-seeing-sequences-in-trajectory-data
