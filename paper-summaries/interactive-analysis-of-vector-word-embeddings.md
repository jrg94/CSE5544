# Interactive Analysis of Word Vector Embeddings: Paper Summary

At a high level, this paper discusses various tasks related to word vector 
embeddings, defines a set of key tasks, demonstrates a set of of visualizations 
to address those tasks, and, finally, shares user feedback. 

In terms of background, the authors do a great job of explaining what word 
vector embeddings are and how they're modeled. In particular, they explain 
how word vector embeddings represent the semantic relationship between 
words. Those relationships can then be demonstrated using a variety of 
visualization techniques.

Fortunately, the authors don't stop there. They actually continue their 
analysis by building their own visualizations using common data analysis 
and visualization tools: Python and D3. In addition, they made use of some 
other common libraries like the natural language processing library GloVe. 
In terms of actual data, the authors used two data sources: several English 
writings pre-1700 and English Wikipedia. While representing the same 
language, the data sets served as a nice contrast in semantic relationships 
between terms. 

Since I had no prior background in the subject, I found the content to be 
rather technical. However, I find the reading beneficial for two reasons. 
For one, it gives a nice overview of several visualization techniques which 
can be used in other application areas. In addition, it demonstrates the power 
of tools like Python and D3 for data analysis and visualization. In terms of 
visualization, the authors focused a lot on ordered hues to demonstrate 
semantic relationships. In general, I think it does a nice job as it allows 
you to see two features clearly: the relationship between adjacent elements 
and any overall trends (if applicable). For example, figure 8 uses hue to 
show co-occurrence for the terms aunt and uncle. For aunt, there's a clear 
overall lack of co-occurrence for almost all of the terms which can be clearly 
seen due to the lack of hue change over the set. Beyond that, I was a fan of 
any visualization that tried to clearly show connections. Overall, the paper 
was a pleasure to read.
