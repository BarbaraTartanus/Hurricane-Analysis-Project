# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# 1
# Update Recorded Damages
conversion = {"M": 1000000,
              "B": 1000000000}

def update_recorded_damages(damages):
  updated_damages = []
  for record in damages:
    if record == "Damages not recorded":
      updated_damages.append("Damages not recorded")
    elif "M" in record:
      float_str = record.split("M")
      value = float(float_str[0]) * conversion["M"]
      updated_damages.append(value)
    elif "B" in record:
      float_str = record.split("B")
      value = float(float_str[0]) * conversion["B"]
      updated_damages.append(value)
  return updated_damages
# test function by updating damages
converted_damages = update_recorded_damages(damages)
#print(converted_damages)

# 2 
# Create and view the hurricanes dictionary
def combining_hurricane_info(names, months, years, max_sustained_winds, areas_affected, converted_damages, deaths):
  strongest_atlantic_hurricanes = {}
  for i, value in enumerate(names):
    strongest_atlantic_hurricanes[value] = {"Name": names[i],
                                            "Month": months[i], 
                                            "Year": years[i], 
                                            "Max Sustained Wind": max_sustained_winds[i], 
                                            "Areas Affected": areas_affected[i], 
                                            "Damage": converted_damages[i],
                                            "Deaths": deaths[i]}
  return (strongest_atlantic_hurricanes)


strongest_atlantic_hurricanes = combining_hurricane_info(names, months, years, max_sustained_winds, areas_affected, converted_damages, deaths)

#print(strongest_atlantic_hurricanes)


# 3
# Organizing by Year
# create a new dictionary of hurricanes with year and key


def create_year_dictionary(strongest_atlantic_hurricanes):
  hurricanes_by_year = {}
  for hurricane in strongest_atlantic_hurricanes:
      current_year = strongest_atlantic_hurricanes[hurricane]['Year']
      current_hurricane = strongest_atlantic_hurricanes[hurricane]
      if current_year not in hurricanes_by_year:
          hurricanes_by_year[current_year] = [current_hurricane]
      else:
          hurricanes_by_year[current_year].append(current_hurricane)
  return hurricanes_by_year

hurricanes_by_year = create_year_dictionary(strongest_atlantic_hurricanes)

#print(hurricanes_by_year)

# 4
# Counting Damaged Areas
# create dictionary of areas to store the number of hurricanes involved in

def count_affected_areas(areas_affected):
  affected_area_count = {}
  for areas in areas_affected:
    for area in areas:
      affected_area_count[area] = affected_area_count.get(area, 0) +1
  return affected_area_count

affected_area_count = count_affected_areas(areas_affected)

#print(affected_area_count)
# 5 
# Calculating Maximum Hurricane Count

# find most frequently affected area and the number of hurricanes involved in

def find_area_most_affected(areas_affected):
  highest_hits_area = max(areas_affected.keys(), key=(lambda new_k: areas_affected[new_k]))
  print("The area affected by the most hurricanes is " + highest_hits_area + " with " + str(areas_affected[highest_hits_area]) + " hits.")
  
find_area_most_affected(affected_area_count)

# 6
# Calculating the Deadliest Hurricane
# find highest mortality hurricane and the number of deaths

def dict_highest_mortality(names, deaths):
  hurricanes_by_mortality = {}
  for i, value in enumerate(names):
    hurricanes_by_mortality[value] = deaths[i] 
  return hurricanes_by_mortality

hurricanes_by_mortality = dict_highest_mortality(names, deaths)
#print(hurricanes_by_mortality)

def find_highest_mortality(hurricanes_by_mortality):
  highest_mortality_val = max(hurricanes_by_mortality.keys(), key=(lambda new_k: hurricanes_by_mortality[new_k]))
  print("The hurricane " + highest_mortality_val + " is causing the greatest number of hits with " + str(hurricanes_by_mortality[highest_mortality_val]) + " casualties." )

find_highest_mortality(hurricanes_by_mortality)

# 7
# Rating Hurricanes by Mortality

# categorize hurricanes in new dictionary with mortality severity as key

mortality_scale = {0: 0,
                   1: 100,
                   2: 500,
                   3: 1000,
                   4: 10000}

def mortality_rates(strongest_atlantic_hurricanes):
  dict_mortality_rates = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
  for key, value in strongest_atlantic_hurricanes.items(): 
    death = value["Deaths"]
    if death == mortality_scale[0]:
        dict_mortality_rates[0].append(value)
    elif death > mortality_scale[0] and death <= mortality_scale[1]:
        dict_mortality_rates[1].append(value)
    elif death > mortality_scale[1] and death <= mortality_scale[2]:
        dict_mortality_rates[2].append(value)
    elif death > mortality_scale[2] and death <= mortality_scale[3]:
        dict_mortality_rates[3].append(value)
    elif death > mortality_scale[3] and death <= mortality_scale[4]:
        dict_mortality_rates[4].append(value)
    else:
       dict_mortality_rates[5].append(value)
  
  return dict_mortality_rates   
        
hurricanes_by_mortality_scale = mortality_rates(strongest_atlantic_hurricanes)
#print(hurricanes_by_mortality_scale)

# 8 Calculating Hurricane Maximum Damage
def calculating_maximum_damage(strongest_atlantic_hurricanes):
  damage = [thing for thing in converted_damages if not thing == "Damages not recorded"]
  max_damage = max(damage)
  for key, value in strongest_atlantic_hurricanes.items():
    if value["Damage"] == max_damage:
      result = [value["Name"], max_damage]
      print("The hurricane that caused the greatest damage is " + str(result[0]) + " costing " + str(result[1]) + "$." )

calculating_maximum_damage(strongest_atlantic_hurricanes)

# find highest damage inducing hurricane and its total cost


# 9
# Rating Hurricanes by Damage
damage_scale = {0: 0,
                1: 100000000,
                2: 1000000000,
                3: 10000000000,
                4: 50000000000}
  
# categorize hurricanes in new dictionary with damage severity as key

def damage_rates(strongest_atlantic_hurricanes):
  dict_damage_rates = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
  for key, value in strongest_atlantic_hurricanes.items(): 
    damage = value["Damage"]
    if damage == "Damages not recorded":
        dict_damage_rates[0].append(value)
    elif damage > damage_scale[0] and damage <= damage_scale[1]:
        dict_damage_rates[1].append(value)
    elif damage > damage_scale[1] and damage <= damage_scale[2]:
        dict_damage_rates[2].append(value)
    elif damage > damage_scale[2] and damage <= damage_scale[3]:
        dict_damage_rates[3].append(value)
    elif damage > damage_scale[3] and damage <= damage_scale[4]:
        dict_damage_rates[4].append(value)
    else:
       dict_damage_rates[5].append(value)
  
  return dict_damage_rates

hurricanes_by_damage_scale = damage_rates(strongest_atlantic_hurricanes)
