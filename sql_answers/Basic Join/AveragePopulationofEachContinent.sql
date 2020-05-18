SELECT COUNTRY.continent,floor(AVG(CITY.Population))
FROM CITY
INNER JOIN COUNTRY ON CITY.CountryCode=COUNTRY.Code
GROUP BY country.continent;


