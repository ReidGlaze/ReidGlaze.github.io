---
title: "Beyond the Buzzer: A Tableau Tale of the 2023 NBA Playoffs"
date: 2023-07-28 00:00:00 -0700
image: /assets/images/basketballcanva.png
categories: [DAA Bootcamp]
tags: [tableau, data analytics]     # TAG names should always be lowercase
---



The 2023 NBA playoffs provided an exciting display of talent, and Tableau's powerful data visualization capabilities enable us to delve into the numbers behind the star performances. In this tableau story, we'll take a closer look at player data to uncover interesting insights and standout performances from the tournament.

# Datasets used
Two datasets were used:
1. The [first data set](https://www.basketball-reference.com/playoffs/NBA_2023_per_game.html) includes the average metrics for each player per game. This dataset was used for slides 1, 4, and 5.
2. The [second data set](https://www.basketball-reference.com/playoffs/NBA_2023_totals.html) includes the total metrics for each player. This dataset was used for slides 2 and 3.

These tables were joined on the player column using Tableau.

## Slide 1: Charting the All-Around Players


Their initial point of focus is a bubble chart that depicts the average assists, rebounds, and points earned by every player. Points find their place on the x-axis, assists on the y-axis, and the magnitude of the bubbles denotes the quantity of rebounds. The different positions of the players are differentiated through color codes.

There's one player who breaks the mold - Nikola Jokic. Despite his role as a center, Jokic's assist record is remarkably higher than the average player in his position, effectively spotlighting his capacity as a playmaker. His aptitude for rebounds additionally bolsters his standing as a significant player on the field.

Included in the chart are regression lines for each position. Based on these regression lines, it was inferred that point guards generally account for the most assists in relation to points. Meanwhile, centers take the lead in gathering the most rebounds. In an unexpected revelation, shooting guards, small forwards, power forwards, and centers appear to have similar point / assist ratios to eachother.

[![bubble plot](/assets/images/bubbleplot.png)](https://public.tableau.com/views/2023NBAPlayoffsAnalysis/FullStory?:language=en-US&:display_count=n&:origin=viz_share_link)

## Slide 2: Scoring Dynamics Across Teams

A stacked bar chart was devised to depict the sum total of points each team racked up in the playoffs. As would be expected, those teams that were knocked out earlier in the series exhibit a smaller total point tally. It's logical to find Miami and Denver leading the pack in terms of total points since they were the teams that made it all the way to the finals. Despite Denver's ultimate victory, Miami recorded a higher aggregate of points. Yet, within the individual player statistics, it was Nikola Jokic who towered above all others, with an impressive score of 600 points during the playoffs.


An additional intriguing trend was discerned. It seems that the contribution of the top three players from each team is approximately equal to the total points scored by the remaining members of their respective teams. This pattern was noticeable across all sixteen teams. Interestingly, in some of these teams, the top trio of players managed to outscore the rest of their teammates.


[![stacked bar](/assets/images/stackedbar.png)](https://public.tableau.com/views/2023NBAPlayoffsAnalysis/FullStory?:language=en-US&:display_count=n&:origin=viz_share_link)

## Slide 3: Beyond the Arc - 3-Point Prowess


A heat map illustrating the 3-point percentage for each position within each team was generated. However, positions with fewer than 12 attempted 3-point shots were omitted from the heat map. This exclusion was necessary to ensure the reliability of the data, as a limited sample size could be influenced significantly by chance occurrences and might not accurately represent the true shooting abilities of those positions.

Several positions stood out:
* The small forwards for the Milwaukee Bucks made  46.99% of 83 attempted 3 pointers.
* The shooting gaurds for the Milwaukee Bucks made 48.28% of 29 attempted 3 pointers.
* The centers for the Denver Nuggets made 46.05% of 76 attempted 3 pointers.
* The shooting gaurds for the Boston Celtics made 45.45% of 110 attempted 3 pointers.
* The power forwards for the Boston Celtics made 45% of 40 attempted 3 pointers.
  

[![heat map](/assets/images/heatmap.png)](https://public.tableau.com/views/2023NBAPlayoffsAnalysis/FullStory?:language=en-US&:display_count=n&:origin=viz_share_link)

## Slide 4: Assists by Position


Assists play a pivotal role in team strategy, and this treemap breaks down assists by position. As expected, point guards dominate this category, showcasing their essential role in facilitating teamwork. One standout player, Trae Young, secures the highest average assists, reflecting his crucial role in guiding his team's offense.

An interesting observation is once again Nikola Jokic, the center who surprisingly secured the second-highest number of assists overall, an exceptional feat for a position not typically known for playmaking abilities.

[![tree map](/assets/images/treemap.png)](https://public.tableau.com/views/2023NBAPlayoffsAnalysis/FullStory?:language=en-US&:display_count=n&:origin=viz_share_link)

## Slide 5: Unraveling the NBA Finals Stars


In the NBA Finals, I focus on the top 5 players from the two competing teams. Nikola Jokic shines as the 7th player to achieve two triple-doubles in an NBA Finals, solidifying his reputation as an all-around player. His average stats reflect his awe-inspiring performances throughout the tournament.

In this Tableau-driven exploration, we've uncovered the exceptional talents and standout moments of NBA players during the 2023 playoffs. The numbers tell an intriguing story, revealing the players' prowess and the moments that captivated basketball fans worldwide.

[![tree map](/assets/images/topplayers.png)](https://public.tableau.com/views/2023NBAPlayoffsAnalysis/FullStory?:language=en-US&:display_count=n&:origin=viz_share_link)

*Join us in this exciting journey of data-driven discovery, where Tableau empowers us to appreciate the intricacies of the game and celebrate the stars who left a lasting impact on basketball's grandest stage.*
