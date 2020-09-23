DROP TABLE IF EXISTS animals;
DROP TABLE IF EXISTS owners;

CREATE TABLE owners(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE animals(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    species VARCHAR(255),
    owner_id INT REFERENCES owners(id)
);