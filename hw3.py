import data

#part1
#takes the list of county demographics and returns the 2014 population
def population_total(demographics:list[data.CountyDemographics]) -> int:
    total = 0
    for county in demographics:
        total += county.population["2014 Population"]
    return total

#part2
#returns a list of county demographics that are within the specified state
def filter_by_state(demographics:list[data.CountyDemographics], abbreviation:str) -> list[data.CountyDemographics]:
    same_state_counties = []
    for county in demographics:
        if county.state == abbreviation:
            same_state_counties.append(county)
    return same_state_counties

#part3
#returns the sum of the population of people with a given education for all the given counties
#returns 0 if the provided key does not exist
def population_by_education(demographics:list[data.CountyDemographics], education:str) -> float:
    sum = 0
    for county in demographics:
        if education not in county.education:
            return 0
        sum += county.population["2014 Population"] * county.education[education] / 100
    return round(sum,3)

#returns the sum of the population of people with a given ethnicity for all the given counties
#returns 0 if the provided key does not exist
def population_by_ethnicity(demographics:list[data.CountyDemographics], ethnicity:str) -> float:
    sum = 0
    for county in demographics:
        if ethnicity not in county.ethnicities:
            return 0
        sum += county.population["2014 Population"] * county.ethnicities[ethnicity] / 100
    return round(sum,3)

#returns the sum of the population of people that are below poverty level for all the given counties
def population_below_poverty_level(demographics:list[data.CountyDemographics]) -> float:
    sum = 0
    for county in demographics:
        sum += county.population["2014 Population"] * county.income['Persons Below Poverty Level'] / 100
    return round(sum,3)

#part4
#returns the percentage of population that is the given education over the total population of all the counties given in the list
#returns 0 if the provided key does not exist
def percent_by_education(demographics:list[data.CountyDemographics], education:str) -> float:
    total_pop = 0
    education_pop = 0
    for county in demographics:
        if education not in county.education:
            return 0
        total_pop += county.population["2014 Population"]
        education_pop += (county.population["2014 Population"] * county.education[education] / 100)
    return round(education_pop/total_pop,3) * 100

#returns the percentage of population that is the given education over the total population of all the counties given in the list
#returns 0 if the provided key does not exist
def percent_by_ethnicity(demographics:list[data.CountyDemographics], ethnicity:str) -> float:
    total_pop = 0
    ethnicity_pop = 0
    for county in demographics:
        if ethnicity not in county.ethnicities:
            return 0
        total_pop += county.population["2014 Population"]
        ethnicity_pop += (county.population["2014 Population"] * county.ethnicities[ethnicity] / 100)
    return round(ethnicity_pop/total_pop,3) * 100

#returns the percentage of population that is below the poverty level over the total population of all the counties given in the list
def percent_below_poverty_level(demographics:list[data.CountyDemographics]) -> float:
    total_pop = 0
    poverty_pop = 0
    for county in demographics:
        total_pop += county.population["2014 Population"]
        poverty_pop += (county.population["2014 Population"] * county.income["Persons Below Poverty Level"] / 100)
    return round(poverty_pop/total_pop, 3) * 100

#part5
#returns a list of all the counties in the given list of counties that are greater than the given percentage of the given education
#returns an empty list if the key does not exist
def education_greater_than(demographics:list[data.CountyDemographics], education:str, percentage:float) -> list[data.CountyDemographics]:
    education_list = []
    for county in demographics:
        if education not in county.education:
            return education_list
        if county.education[education] > percentage:
            education_list.append(county)
    return education_list

#returns a list of all the counties in the given list of counties that are less than the given percentage of the given education
#returns an empty list if the key does not exist
def education_less_than(demographics:list[data.CountyDemographics], education:str, percentage:float) -> list[data.CountyDemographics]:
    education_list = []
    for county in demographics:
        if education not in county.education:
            return education_list
        if county.education[education] < percentage:
            education_list.append(county)
    return education_list

#returns a list of all the counties in the given list of counties that are greater than the given percentage of the given ethnicity
#returns an empty list if the key does not exist
def ethnicity_greater_than(demographics:list[data.CountyDemographics], ethnicity:str, percentage:float) -> list[data.CountyDemographics]:
    ethnicity_list = []
    for county in demographics:
        if ethnicity not in county.ethnicities:
            return ethnicity_list
        if county.ethnicities[ethnicity] > percentage:
            ethnicity_list.append(county)
    return ethnicity_list

#returns a list of all the counties in the given list of counties that are less than the given percentage of the given ethnicity
#returns an empty list if the key does not exist
def ethnicity_less_than(demographics:list[data.CountyDemographics], ethnicity:str, percentage:float) -> list[data.CountyDemographics]:
    ethnicity_list = []
    for county in demographics:
        if ethnicity not in county.ethnicities:
            return ethnicity_list
        if county.ethnicities[ethnicity] < percentage:
            ethnicity_list.append(county)
    return ethnicity_list

#returns a list of all the counties in the given list of counties that are less than the given percentage of below the poverty level
def below_poverty_level_greater_than(demographics:list[data.CountyDemographics], percentage:float) -> list[data.CountyDemographics]:
    poverty_list = []
    for county in demographics:
        if county.income["Persons Below Poverty Level"] > percentage:
            poverty_list.append(county)
    return poverty_list

#returns a list of all the counties in the given list of counties that are less than the given percentage of below the poverty level
def below_poverty_level_less_than(demographics:list[data.CountyDemographics], percentage:float) -> list[data.CountyDemographics]:
    poverty_list = []
    for county in demographics:
        if county.income["Persons Below Poverty Level"] < percentage:
            poverty_list.append(county)
    return poverty_list