CREATE TABLE companies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    ticker VARCHAR(20) UNIQUE -- necessary?
);

CREATE TABLE analyses (
    id SERIAL PRIMARY KEY,
    company_id INT REFERENCES companies(id) ON DELETE CASCADE,
    source_url TEXT,
    raw_content TEXT NOT NULL,
    ai_summary TEXT,
    priority_score NUMERIC(5,2),
    collection_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE evaluation_parameters (
    id SERIAL PRIMARY KEY,
    parameter_name VARCHAR(100) NOT NULL,
    description TEXT,
    weight NUMERIC(3,2)
);