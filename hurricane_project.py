# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]


# write your update damages function here:
def update_damage(x):
    a = []
    for y in x:
        if 'M' in y:
            a.append(float(y[:-1]) * 1000000)
        elif 'B' in y:
            a.append(float(y[:-1]) * 1000000000)
        else:
            a.append(y)
    return a
damages_num = update_damage(damages)
print(damages_num)

# write your construct hurricane dictionary function here:
hurricane_dict = {x:{'Name': x, 'Month': y, 'Year': z, 'Max Sustained Wind': n, 'Areas': m, 'Damage': c, 'Deaths': k}
                  for x, y, z, n, m, c, k in
                  zip(names, months, years, max_sustained_winds, areas_affected, damages_num, deaths)}
print(hurricane_dict)

# write your construct hurricane by year dictionary function here:
def hurr_by_year(dict):
    z = {}
    for hurricane in dict.values():
        if hurricane['Year'] not in z.keys():

            a = {hurricane['Year']: [n for n in dict.values() if n['Year'] == hurricane['Year']]}
            z.update(a)
    return z
hurr_dict_by_year = hurr_by_year(hurricane_dict)
print(hurr_dict_by_year)

# write your count affected areas function here:
def count_hurr(dict):
    z = {}
    for x in dict.values():
        for y in x['Areas']:
            if y not in z.keys():
                z.update({y: len([n for x in dict.values() for n in x['Areas'] if n == y])})
    return z
num_inst = count_hurr(hurricane_dict)
print(num_inst)

# write your find most affected area function here:
def most_affected(dict):
    return {k: v for k,v in sorted(dict.items(), key = lambda item: item[1], reverse=True)}
most_aff = most_affected(num_inst)
print(most_aff)

# write your greatest number of deaths function here:
def most_affected(dict):
    a = {k: v for k,v in sorted(dict.items(), key = lambda item: item[1]['Deaths'], reverse=True)}
    return {list(a.keys())[0]: dict[list(a.keys())[0]]['Deaths']}
deadliest_hurr = most_affected(hurricane_dict)
print(deadliest_hurr)

# write your catgeorize by mortality function here:
def mortality_scale(dict):
    zero, one, two, three, four = [], [], [], [], []
    for x in dict.values():
        if x['Deaths'] >= 10000:
            four.append(x)
        elif x['Deaths'] >= 1000:
            three.append(x)
        elif x['Deaths'] >= 500:
            two.append(x)
        elif x['Deaths'] >= 100:
            one.append(x)
        else:
            zero.append(x)
    return {0:zero, 1: one, 2: two, 3: three, 4: four}
mortality = mortality_scale(hurricane_dict)
print(mortality)

# write your greatest damage function here:
def greatest_damage(dict):
    a = {x['Name']: x['Damage'] for x in dict.values() if x['Damage'] != 'Damages not recorded'}
    b = {k: v for k,v in sorted(a.items(), key = lambda item: item[1], reverse=True)}
    return {next(iter(b)): b[next(iter(b))]}
greatest_dmg = greatest_damage(hurricane_dict)
print(greatest_dmg)

# write your catgeorize by damage function here:
def damage_scale(dict):
    zero, one, two, three, four = [], [], [], [], []
    for x in dict.values():
        if x['Damage'] == 'Damages not recorded':
            zero.append(x)
        elif x['Damage'] >= 50000000000:
            four.append(x)
        elif x['Damage'] >= 10000000000:
            three.append(x)
        elif x['Damage'] >= 1000000000:
            two.append(x)
        elif x['Damage'] >= 100000000:
            one.append(x)
        else:
            zero.append(x)
    return {0:zero, 1: one, 2: two, 3: three, 4: four}
dmg_cat = damage_scale(hurricane_dict)
print(dmg_cat)