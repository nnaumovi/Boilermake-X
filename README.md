# Boilermake-X
Making a game for Boilermake X!


## Inspiration
We were originally inspired to make an rpg game because we are a close friend group and have on many occasions spent time playing games together to destress from school and work; we often found ourselves spitballing ideas that we thought would be enjoyable to experience from a player's perspective, and started to note these down. We had the idea to make a video game together as a fun personal project, and wanted to fill it with easter eggs from our inside jokes, as well as use it as a form of expression to explore concepts and topics that we are personally interested and passionate about.

## What it does
Our video game idea centers around a farming-themed lifestyle simulator, where the player is able to raise and collect crops and materials to cook and sell food products, build supplies, and develop their home and surrounding land. Our final vision for the project would allow players to choose different "paths", with the different choices they make affecting metrics such as their earned money and the sustainability of their lifestyle. Our goal is for the game to be a low-stress rpg experience, as well as incorporate real-world data to influence gameplay; by rewarding players for making certain choices in the game, such as upgrading their home to use solar panels for energy or planting sustainable crops, we would help educate players and raise awareness about important issues such as food insecurity, climate change, and sustainable practices.

## How we built it
We used Unity to develop the visual aspects of the game, and designed custom character sprites for all of the components of the game, including the playable character, crops, and environment. We used C# scripts to implement some game mechanics, such as an in-game timer to enable events based on passing time, such as food spoiling in the kitchen or the player cooking a meal. We also used CockroachDB, Python, and Flask to create a database and REST API which includes various tables that organize and store the data required for the internal game mechanics, such as food recipes and materials for building different tools. Our goal is to connect the REST API into the Unity project for our game, and use HTTP requests to retrieve this information via SQL queries to unique item IDs.

## Challenges we ran into
We originally had plans to be one a four-person team, but one teammate was unfortunately unable to participate. Out of the three of us who did attend Boilermake, one started to feel ill 12 hours into the challenge; since we had divided labor based of each teammate's prior knowledge of technologies, our teammate being ill significantly compromised our productivity with Unity, and ultimately our ability to produce the final frontend product. Along with many technical issues and time spent learning to use new tools during the event itself, we were unable to reach our original goal of a smaller, beta-stlye demo of our game during the official hackathon period.

## Accomplishments that we're proud of
Despite limited knowledge with most of the technology we used, we were able to successfully implement many of the basic features required for our game; specifically, we have a fully functional database that we can easily continue to fill with information as we continue to develop and expand the game. We also have the basis of a UI with some basic game mechanics, which we can continue to expand upon over time as we learn more about the software tools.

## What we learned
We learned about serverless databases, scripting custom functions for specific game mechanics using C#, and gained a lot of experience using new tools such an Unity, Cockroach DB, and Flask.

## What's next for The Journey to Paradise
We are excited to continue working on our game on our own time to make progress towards our original vision for the game. We look forward to eventually reaching our bigger goals that we envisioned but thought to be too unrealistic to tackle for a 36-hour hackathon; further, we hope to be able to improve upon the game mechanics we have already implemented as we become more proficient with the software tools and have more time to flesh out ideas for more advanced gameplay.
