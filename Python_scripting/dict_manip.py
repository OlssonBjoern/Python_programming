## Manipulating dictionaries in Python

comicchardict = [
    { "name" : "Tony Stark", "alias" : "Iron Man", "year_of_release" : 1963, "teams" : "Avengers" },
    { "name" : "Bruce Banner", "alias" : "Hulk", "year_of_release" : 1962, "teams" : "Avengers" },
    { "name" : "Steve Rogers", "alias" : "Captain America", "year_of_release" : 1940, "teams" : "Avengers" },
    {"name": "Clark Kent", "alias" : "Superman", "year_of_release" : 1938, "teams" : "Justice League"},
    {"name": "Bruce Wayne", "alias" : "Batman", "year_of_release" : 1939, "teams" : "Justice League"},
    {"name": "Isidoro Scarlotti", "alias" : "Vulture", "year_of_release" : 1963, "teams" : "Sinister Six"},
    {"name": "Otto Octavius", "alias" : "Doctor Octopus", "year_of_release" : 1963, "teams" : "Sinister Six"}
]

# Make a SET to sort out uniqe information from the dictionary

# 2 ways of doing the same thing

# 1: "Regular" coding style
unique_teams = set()

for item in comicchardict:
    unique_teams.add(item["teams"])


# 2: "Pythonic" with set comprehension
unique_teams2 = {entry["teams"] for entry in comicchardict}

print(unique_teams)

print(unique_teams2)

# ----------------------------------------------------------------- #

# Doing the same thing but with a LIST instead of a set

list_unique_years = []

for data in comicchardict:
    # Each "data" is every dictionary in the list of dictionaries
    yor = data["year_of_release"]
    if yor not in list_unique_years:
        list_unique_years.append(yor)

unique_teams3 = []
for data in comicchardict:
    if data["teams"] in unique_teams3:
        continue
    else:
        unique_teams3.append(data["teams"])

print(list_unique_years)
print(unique_teams3)