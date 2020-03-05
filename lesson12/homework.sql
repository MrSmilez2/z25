CREATE TABLE our_users(
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(30) NOT NULL,
    last_name VARCHAR(30) NOT NULL,
    email VARCHAR(30) NOT NULL UNIQUE
);

CREATE TABLE test_questions(
    id SERIAL PRIMARY KEY,
    questions TEXT NOT NULL,
    test_id VARCHAR(30) NOT NULL
);

CREATE TABLE answers(
    id SERIAL PRIMARY KEY,
    question_id,
    test_id,
    FOREIGN KEY (test_id) REFERENCES test_questions (test_id),
    FOREIGN KEY (question_id) REFERENCES test_questions (id),
    answer VARCHAR(30) NOT NULL,
    result BOOLEAN
);

CREATE TABLE user_answers(
    answer SMALLINT NOT NULL,
    user_id INTEGER REFERENCES our_users(id),
    question_id INTEGER REFERENCES test_questions(id),
    answer_date DATE NOT NULL,
    PRIMARY KEY (user_id, question_id)
);