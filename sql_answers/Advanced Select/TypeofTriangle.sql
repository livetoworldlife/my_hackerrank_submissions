SELECT
CASE
    WHEN A+B>C and A+C>B and B+C>A THEN 
                                        CASE
                                            WHEN A=B and B=C THEN "Equilateral"
                                            WHEN A=B or A=C or B=C THEN "Isosceles"
                                            WHEN A!=B or A!=C or B!=C THEN "Scalene"
                                        END
    ELSE "Not A Triangle"
END
FROM TRIANGLES;
