import pets_db

################################################################################
#     ____                          __     _                          __ __
#    / __ \  __  __  ___    _____  / /_   (_)  ____    ____          / // /
#   / / / / / / / / / _ \  / ___/ / __/  / /  / __ \  / __ \        / // /_
#  / /_/ / / /_/ / /  __/ (__  ) / /_   / /  / /_/ / / / / /       /__  __/
#  \___\_\ \__,_/  \___/ /____/  \__/  /_/   \____/ /_/ /_/          /_/   
#                                                                          
#  Question 4
################################################################################
#
# Instructions:
# Question 4 and Question 5 are about writing SQL. THey use the database that is 
# created in the file `pets_db.py`. 
# These questions use a database called SQLite. You do not need to install anything.
# In the file `pets_db.py` three tables are created. Data is then added to each 
# of the tables. The questions below are about how the data in each of the tables
# is related.

# Part 4.A:
# Write SQL to select the pets that are owned by nobody.
# The output should be a list of tuples in the format: (<pet name>, <species>, <age>)

sql_pets_owned_by_nobody = """

SELECT name, species, age
FROM animals
LEFT JOIN people_animals ON animal_id = pet_id
WHERE owner_id IS NULL


"""

# Part 4.B:
# Write SQL to select how the number of pets are older than their owners. 
# The output should be an integer.

sql_pets_older_than_owner = """

SELECT COUNT(*)
FROM animals AS A
JOIN people_animals ON A.animal_id = people_animals.pet_id
JOIN people AS P ON people_animals.owner_id = P.person_id
WHERE A.age > P.age

"""

# Part 4.C: BONUS CHALLENGE! 
# Write SQL to select the pets that are owned by Bessie and nobody else.
# The output should be a list of tuples in the format: (<person name>, <pet name>, <species>)
sql_only_owned_by_bessie = """ 

SELECT P.name, A.name, A.species
FROM people AS P
JOIN people_animals ON P.person_id = people_animals.owner_id
JOIN animals AS A ON people_animals.pet_id = A.animal_id
WHERE P.name = 'bessie'
AND A.animal_id NOT IN (
    SELECT pet_id
    FROM people_animals
    WHERE owner_id <> P.person_id
);

"""