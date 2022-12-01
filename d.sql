-- Active: 1669157139331@@127.0.0.1@5432@postgres@public
SELECT * FROM process ;


SELECT DISTINCT(unit)  FROM process INNER JOIN unit on process.fk_unit = unit.unit_id AND process.fk_unit = 4 ;