CREATE TABLE IF NOT EXISTS search_history (
    id SERIAL PRIMARY KEY,
    query VARCHAR(255) NOT NULL,
    search_date TIMESTAMP NOT NULL
);

CREATE TABLE IF NOT EXISTS search_results (
    id SERIAL PRIMARY KEY,
    search_id INTEGER REFERENCES search_history(id),
    title TEXT,
    link TEXT,
    display_link TEXT,
    formatted_url TEXT,
    html_formatted_url TEXT,
    snippet TEXT,
    html_snippet TEXT,
    html_title TEXT,
    kind TEXT,
    pagemap JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
); 