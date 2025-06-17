import utils
import charts
import pandas as pd

def run():
  continent = input('Type Continent => ').strip().title()
  print(continent)
  df = pd.read_csv('data.csv')
  df = df[df['Continent'] == continent]

  countries = df['Country'].values
  percentages = df['World Population Percentage'].values
  charts.generate_pie_chart(f'{continent}_population', countries, percentages)

  country = input('Type Country => ').strip().title()
  print(country)

  result = utils.population_by_country(df, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'], labels, values)

if __name__ == '__main__':
  run()