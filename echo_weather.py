from weather import Weather, Unit

weather = Weather(unit=Unit.CELSIUS)
location = weather.lookup_by_location('amsterdam')
#lookup = weather.lookup(560743)
#condition = lookup.condition
condition = location.condition

#print(condition.text)