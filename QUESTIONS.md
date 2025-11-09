# ❓ Answer to questions

## Discuss your strategy and decisions implementing the application. Please, consider time complexity, effort cost, technologies used and any other variable that you understand important on your development process. 
- I chose `Python` instead of `.NET`, which I know better, because implementing the structure in .NET would have taken more time. In Python, I basically built the home page with HTML, views, models, and load_data. I know it wasn’t necessary to use a database, but in Python it was fast and easy with just a few commands.

## How would you change your solution to account for future columns that might be requested, such as “Bill Voted On Date” or “Co-Sponsors”?
- Well, I built it using an MTV architecture, so it will be easy to just add the columns in the `Model` and refactor or build new methods in the `views`, and, if needed, include them in `home.html` to display on the frontend.

## How would you change your solution if instead of receiving CSVs of data,you were given a list of legislators or bills that you should generate a CSV for?
- Since I knew the solution would break if I tried to upload the data separately (because of foreign keys, for example), I thought about creating a script to combine the data into a single CSV file.

## How long did you spend working on the assignment?
- Probably about two and a half hours. I had to stop several times to take care of my son or have dinner, so I think that’s about the total time, including the README and the questions.