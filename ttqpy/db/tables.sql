DROP TABLE IF EXISTS answer;
DROP TABLE IF EXISTS answer_type;
DROP TABLE IF EXISTS "option";
DROP TABLE IF EXISTS question;
DROP TABLE IF EXISTS test;
DROP TABLE IF EXISTS users;

CREATE TABLE test
(
    id serial NOT NULL,
    "name" character varying COLLATE pg_catalog."default",
    subject character varying COLLATE pg_catalog."default",
    weight double precision,
    CONSTRAINT test_pkey PRIMARY KEY (id)
);

CREATE TABLE answer_type
(
    id serial  NOT NULL,
    "name" character varying COLLATE pg_catalog."default",
    CONSTRAINT answer_type_pkey PRIMARY KEY (id)
);

CREATE TABLE question
(
    id serial  NOT NULL,
    test_id integer,
    question character varying COLLATE pg_catalog."default",
    correct_answer character varying COLLATE pg_catalog."default",
    manually_graded boolean,
    "number" integer,
    CONSTRAINT question_pkey PRIMARY KEY (id),
    CONSTRAINT question_test_id_fkey FOREIGN KEY (test_id)
        REFERENCES test (id)
);

CREATE TABLE "option"
(
    id serial  NOT NULL,
    question_id integer,
    value character varying COLLATE pg_catalog."default",
    label character varying COLLATE pg_catalog."default",
    CONSTRAINT option_pkey PRIMARY KEY (id),
    CONSTRAINT option_question_id_fkey FOREIGN KEY (question_id)
        REFERENCES question (id)
);

CREATE TABLE answer
(
    id serial  NOT NULL,
    question_id integer,
    answer_type_id integer,
    answer character varying COLLATE pg_catalog."default",
    CONSTRAINT answer_pkey PRIMARY KEY (id),
    CONSTRAINT answer_answer_type_id_fkey FOREIGN KEY (answer_type_id)
        REFERENCES answer_type (id) MATCH SIMPLE,
    CONSTRAINT answer_question_id_fkey FOREIGN KEY (question_id)
        REFERENCES question (id)
);

CREATE TABLE users
(
    id serial NOT NULL,
    username character varying COLLATE pg_catalog."default",
    password_hash character varying COLLATE pg_catalog."default",
    first_name character varying COLLATE pg_catalog."default",
    last_name character varying COLLATE pg_catalog."default",
    email character varying COLLATE pg_catalog."default",
    token character varying COLLATE pg_catalog."default",
    token_expiration timestamp,
    admin boolean,
    CONSTRAINT users_pkey PRIMARY KEY (id)
);