Title: The Population of Vermont 
Slug: vermont-population
Summary: ![oakland](/articles/transit/images/oakland.jpg)
Date: 1 April, 2021

<script src="https://cdn.jsdelivr.net/npm/vega@5"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@4"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6"></script>

<style>
form.vega-bindings {
  position: absolute;
  right: 0px;
  bottom: 0px;
}

#view {
  float: right;
  margin-left: 1em;
  margin-bottom: 3em;
}

</style>
<div id="view"></div>
<script>
  vegaEmbed(
    '#view',
    '/articles/transit/images/vermont.json'
  );
</script>

There has been a lot of chatter recently about the indefensible malapportionment of the United States Senate.
A senator from small, rural states like Wyoming, Montana, or Vermont,
has exactly the same voting power as a senator from large, urban states like California or New York,
leaving the citizens of those larger states enormously disenfranchised.

Ruminating on this in Los Angeles County (larger than most states), I had a question:
do more people live along the Vermont Avenue corridor
(one of the largest, most important boulevards in the county, with a subway, good food, and cultural landmarks),
or the state of Vermont, [population 623,989](https://www.census.gov/quickfacts/fact/table/VT/PST045219)
(has a high-profile senator, but is otherwise not particularly economically important)?

So I put together this quick visualization using
[Census block population data](https://geohub.lacity.org/datasets/lacounty::2010-census-data-by-block)
and [street data](https://download.geofabrik.de/north-america/us/california/) from Open Street Map (OSM).
The answer to the above question depends on what you mean by the "Vermont Avenue corridor":

* If the corridor is defined to be strictly within a city block of Vermont Avenue, which I have approximated by census blocks, then Vermont state has a higher population.
* If the corridor is defined to be within a mile of Vermont Avenue, which is a reasonable walkshed for transit and commerce purposes, then Vermont Avenue has a higher population.
* Vermont Avenue starts to win when you include people living up to three-quarters of a mile from the street.

As a coda, I wonder if there are any other major boulevards in the US that are named after states
and have higher populations than their namesake. I could not come up with one myself.
