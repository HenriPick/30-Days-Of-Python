empty_list = []

big_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(len(big_list))

print(f'First item:', big_list[0], 'middle item:', big_list[(len(big_list) // 2)], 'last item:', big_list[-1])

mixed_data_types = ['Henri', 15, '6 foot', False, '123 hello lane']

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print(it_companies)

print(f'Number of companies:', len(it_companies))

print(f'First company:', it_companies[0], 'middle company:', it_companies[(len(it_companies) // 2)], 'last company:', it_companies[-1])

it_companies[0] = 'Dell'
print(it_companies)

it_companies.append('HP')
print(it_companies)

it_companies.insert(len(it_companies) // 2, 'Facebook')
print(it_companies)

it_companies[0] = it_companies[0].upper()
print(it_companies)

print(' '.join(it_companies))

print('Apple' in it_companies)

it_companies.sort()
print(it_companies)

it_companies.reverse()
print(it_companies)

print(it_companies[3:])

print(it_companies[:-3])

it_companies = it_companies[:len(it_companies) // 2] + it_companies[len(it_companies) // 2 + 1:]
print(it_companies)

it_companies.pop(0)
print(it_companies)

it_companies.pop(len(it_companies) // 2)
print(it_companies)

it_companies.pop(-1)
print(it_companies)

it_companies.clear()
print(it_companies)

del it_companies

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']

full_stack = front_end + back_end
full_stack.insert(5, 'Python')
full_stack.insert(6, 'SQL')
print(full_stack)

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)
min_age = ages[0]
print(f'max age:', min_age)
max_age = ages[-1]
print(f'min age:', max_age)
ages.insert(0, min_age)
ages.insert(-1, max_age)

median_age = ages[len(ages) // 2] 
if len(ages) % 2 == 0:
    median_age = (ages[len(ages) // 2 - 1] + ages[len(ages) // 2]) / 2
print(median_age)

total_age = 0
for i in ages:
    total_age += i

average_age = total_age // len(ages)
print(average_age)

range_of_ages = max_age - min_age
print(range_of_ages)

print(abs(min_age - average_age) >= abs(max_age - average_age))

countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

middle_country = len(countries) // 2
if len(countries) % 2 == 0:
    print(countries[middle_country - 1] + ' and ' + countries[middle_country])
else:
    print(countries[middle_country])
    
if len(countries) % 2 == 0:
    list_1 = countries[0: middle_country]
    list_2 = countries[middle_country: ]
else:
    list_1 = countries[0: middle_country + 1]
    list_2 = countries[middle_country + 1: ]
print("List 1:", list_1)
print("List 2:", list_2)

country_1, country_2, country_3, *scandic_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(country_1)
print(country_2)
print(country_3)
print(scandic_countries)