# Assignment 03

[Assignment 03][2] is a two part assignment based on event analysis.

## Part One

During part one, we were asked to come up with some visualization methods
for the EHR data set. 

### Group

In part one, we were asked to get into groups according to subsection 1. The 
following list contains all the group members.

- Jeremy Grifski

### Tasks & Visualization

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

The following hockey scatterplot does a great job of illustrating what I would like to
do for the lifetime flag totals vs. incident count graph. Each patient would have their
own label on that graph which could be selected so all other patients would fade.

![Controlling the Blue Line][1]

In this example, they do a bit of filtering by team, so it may be nice to filter
by flag or something else.

As for the line plot, I drew some inspiration from the graphics from Google Search
Console which allows you to select which lines to show:

![Clicks and Impressions Over Time][3]

![Clicks, Impressions, and Position Over Time][4]

It's not always clear how these graphs relate to each other, but you can clearly
see how their trends are correlated.

#### Design

Based on the images above, I'd be interested in creating a dual interactive plot
where the top plot is a scatter plot and the bottom plot is a line plot. Selecting
a patient would allow you to bring that patient to the foreground in both plots.
You could also potential filter patients by a specific attribute, so only those
patients would be in the foreground of both graphs.

Specifically, the top plot would map every patient against their lifetime flag 
count (y-axis) and their incidents (samples). In this plot, I would expect
to see some sort of linear trend where more samples means more lifetime
incidents. Patients who don't follow the trend may indicate outliers who
need additional treatment.

Meanwhile, the bottom plot would be a line graph of every patient's
flag count over time (unsure about the units). In this plot, I would expect
to see some sort of separation between mTBI patients and other patients.

Obviously, the challenge in the second graph is labeling. We wouldn't want
to use color to separate the lines as there could be thousands of patients.
In addition, the x-axis isn't exactly simple. Not all patients share the 
same time line or have the same number of samples, so mapping could be
an issue. For those reasons, it may make sense to leave out the line plot
and focus on the patient mapping. 

At any rate, here's a sample look at the double plot solution:

![Individual Patient Overview][5]

Look to the explanation above for details.

### Design Analysis

As a part of subsection 4, we were asked to participate in the voting
of other designs. In addition, we were asked to critically analyze our
own design using the following criteria:

- how does the design address *event-relevant* tasks?
- how many items can the design show on a 24-inch monitor?
- does it use overview+detail technique?
- does it show "temporal" changes?
- whether or not it introduces clutter by comparing with all other designs
- is the design visually pleasing?

## Part Two (6)

To be completed next week.

[1]: assets/controlling-the-blue-line.jpeg
[2]: https://sites.google.com/site/datavisualizationspring2019/exercise/assignment-3-seeing-sequences-in-trajectory-data
[3]: assets/clicks-impressions-over-time.JPG
[4]: assets/clicks-impressions-position-over-time.JPG
