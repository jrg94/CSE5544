# CSE 5544 Assignment 02

In this assignment, we were asked to review two visualizations: one effective
and one ineffective. These visualizations must come from a written publication,
so we can follow their design process. Examples papers can be found on the
course [paper list][1].

Each visualization must be evaluated based on the following criteria:

- How effective do you judge this visualization to be? Why?
- What are the most noticeable elements of the visualization? Are they the most important?
- Is there essential information missing?
- Are there elements which carry no information?
- Are colors used effectively?
- Does this visualization encourage any misperceptions?
- How could this visualization be improved? Offer specific suggestions.

In total, each review should be between a half and a full page of prose.

## Research Discovery

As a bit of background, I chose to read up on some of the music research as
it's related to my final project and personal research interests. The following
list of papers have been aggregated for my personal use:

- [Analyzing Visual Mappings of Traditional and Alternative Music Notation][2]
- [An approach to leveraging multitrack information for artistic music visualization][3]
- [Visualizing Music in its Entirety Using Acoustic Features: Music Flowgram][4]
- [Simple: Assessing Music Similarity Using Subsequences Joins][5]
- [Improving Visualization of High-Dimensional Music Similarity Spaces][6]

For this particular assignment, I chose to evaluate visualizations from the first
and third papers.

## The Effective Visualization

After reviewing a few papers, I decided that the most effective visualization was from
the following paper:

**Dasaem Jeong and Juhan Nam, “Visualizing Music in its Entirety using Acoustic Features: 
Music Flowgram”, in Proceedings of the International Conference on Technologies for Music 
Notation and Representation, 2016, pp. 25–32.**

In particular, I took interest in the application of the music flowgram detailed
in the paper:

![Music Flowgram][7]

With all that said, let's take some time to review the literature.

### Music Flowgram Background

In order to review this visualization, I think it's important to discuss the goal of
the research which was to create a music visualization that is less dense than sheet
music for listeners. In other words, the researchers were interested in finding a way
to simplify the music following task as score following is traditionally very difficult.
In addition, the researchers noted that traditional music notation does not capture
the global structure of a piece. Instead, it focuses on transient elements through
measures.

According to the researchers, there has been plenty of research to try to address 
the shortcomings in the music following task. However, manual mapping of music
to score is an expensive process, and automated processes are still being researched.
As a result, the researchers chose to circumvent music notation by introducing a
new music visualization called the music flowgram which can be seen above.

To be clear, a music flowgram is not a new idea. Instead, it's a concept borrowed
from Freytag who visualized tension progress in storytelling. In this case, the idea 
is to demonstrate a change in music over time using a continuous two-dimensional graph.
From this graph, listeners should be able to grasp the emotional aspects of music which
are derived from loudness, tempo, and harmony.

### Music Flowgram Review

At first glance, the music flowgram above appears to do exactly what the researchers intended.
Without really knowing what the graph shows technically, we can see a bit of storytelling
or trends in the graph. In this particular example, we can see the growth and decay of
various portions of the song which likely imitate the ebb and flow of musical storytelling.

Upon further investigation, we'll discover that volume is mapped to the y-axis. 
Meanwhile, onset density--which is related to tempo--is mapped to the graph color (red), 
and auditory roughness is mapped to the background color (blue).

That said, just how effective is this visualization?

## The Ineffective Visualization

As for the ineffective visualization, I didn't have to look far:

**Miller, Matthias, et al. "Analyzing Visual Mappings of Traditional and Alternative 
Music Notation." arXiv preprint arXiv:1810.10814 (2018).**

In particular, I noticed a rather dense table of information in the paper:

![Overview Mapping][8]

[1]: https://sites.google.com/site/datavisualizationspring2019/paperreadings/critique
[2]: https://arxiv.org/pdf/1810.10814.pdf
[3]: https://qmro.qmul.ac.uk/xmlui/handle/123456789/15516
[4]: http://tenor-conference.org/proceedings/2016/04_Jeong_tenor2016.pdf
[5]: https://wp.nyu.edu/ismir2016/wp-content/uploads/sites/2294/2016/07/099_Paper.pdf
[6]: https://pdfs.semanticscholar.org/6861/648ea009eec227b2d53c0da03ad8e3e9c183.pdf
[7]: music-flowgram.JPG
[8]: overview-mapping.JPG
