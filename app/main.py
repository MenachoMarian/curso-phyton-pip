import utils
import read_csv
import charts

def run():
  data = read_csv.read_csv('data.csv')
  data = list(filter(lambda item: item['Continent'] == 'South America', data))

  countries = list(map(lambda x: x['Country/Territory'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  charts.generate_pie_chart(countries, percentages)

  
  country = input('Type Country => ')
  print(country)


  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country/Territory'], labels, values)
  

if __name__ == '__main__':   #solo si se llama desde laterminal
  run()


'''
data =  [
  {
    'Country': 'Colombia',
    'Population': 500
  },
  {
    'Country': 'Bolivia',
    'Population': 300
  }
]

def run():

  keys, values = utils.get_population()
  print(keys, values)


  country = input('Type Country => ')

  result= utils.population_by_country(data, country)
  print(result)
'''