SELECT TOP 1
  CITY, LEN(CITY)
FROM STATION
order by len(city), city;

SELECT TOP 1
  CITY, LEN(CITY)
FROM STATION
order by len(city) desc, city;