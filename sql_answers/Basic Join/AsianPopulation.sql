select sum(CITY.population) from COUNTRY join CITY on CITY.CountryCode=COUNTRY.Code 
where COUNTRY.CONTINENT='Asia';
