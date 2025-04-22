-- Tabla Voter
CREATE TABLE voter (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    has_voted BOOLEAN DEFAULT FALSE
);

-- Tabla Candidate
CREATE TABLE candidate (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    party VARCHAR(100),
    votes INTEGER DEFAULT 0
);

-- Tabla Vote
CREATE TABLE vote (
    id SERIAL PRIMARY KEY,
    voter_id INTEGER NOT NULL UNIQUE,
    candidate_id INTEGER NOT NULL,
    CONSTRAINT fk_voter FOREIGN KEY (voter_id) REFERENCES voter(id) ON DELETE CASCADE,
    CONSTRAINT fk_candidate FOREIGN KEY (candidate_id) REFERENCES candidate(id) ON DELETE CASCADE
);