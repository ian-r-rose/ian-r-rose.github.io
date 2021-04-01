Title: The Population of Vermont 
Slug: vermont-population
Summary: ![oakland](/articles/transit/images/oakland.jpg)
Date: 1 April, 2021

<script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@4"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>

There has been a lot of chatter recently about the indefensible malapportionment of the United States Senate.
A senator from small, rural states like Wyoming, Montana, or Vermont,
has exactly the same voting power as a senator from large, urban states like California or New York,
leaving the citizens of those larger states enormously disenfranchised.

Ruminating on this in Los Angeles County (larger than most states), I had a question:
do more people live along the Vermont Avenue corridor
(one of the largest, most important boulevards in the county, with a subway, good food, and cultural landmarks),
or the state of Vermont
(has a high-profile senator, but is otherwise not particularly economically important)?

So I put together this quick visualization using Census block population data and street data from Open Street Map (OSM).
The answer to the above question depends on what you mean by the "Vermont Avenue corridor":

* If the corridor is defined to be strictly within a city block of Vermont Avenue, which I have approximated by census blocks, then Vermont state wins.
* If the corridor is defined to be within a mile of Vermont Avenue, which is a reasonable walkshed for transit and commerce purposes, then Vermont Avenue wins.
* Vermont Avenue starts to win when you include people living up to three-quarters of a mile from the street.

<div id="view"></div>
<script>
  vegaEmbed(
    '#view',
    '/articles/transit/images/vermont.json'
  );
</script>


As a coda, I wonder if there are any other major boulevards in the US that are named after states
and have higher populations than their namesake. I could not come up with one myself.
