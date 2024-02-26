## API para converter texto para SQL

Todos créditos para: https://huggingface.co/cssupport/t5-small-awesome-text-to-sql

Para rodar o projeto: `docker-compose up`.

As requisições podem serem enviadas para `http://localhost:5000/ai/text2sql`, abaixo exemplos de requisições com os resultados:

```JAVASCRIPT
POST http://127.0.0.1:5000/ai/text2sql
Content-Type: application/json

{
    "tables": [
        "CREATE TABLE student_course_attendance (student_id VARCHAR)",
        "CREATE TABLE students (student_id VARCHAR)"
    ],
    "query": "List the id of students who never attends courses?"
}

### response: SELECT student_id FROM students WHERE NOT student_id IN (SELECT student_id FROM student_course_attendance)



#####

POST http://127.0.0.1:5000/ai/text2sql
Content-Type: application/json

{
    "tables": [
        "CREATE TABLE Catalogs (date_of_latest_revision VARCHAR)"
    ],
    "query": "Find the dates on which more than one revisions were made."
}

### response: SELECT date_of_latest_revision FROM Catalogs GROUP BY date_of_latest_revision HAVING COUNT(*) > 1



#####

POST http://127.0.0.1:5000/ai/text2sql
Content-Type: application/json

{
    "tables": [
        "CREATE TABLE table_22767 ( \"Year\" real, \"World\" real, \"Asia\" text, \"Africa\" text, \"Europe\" text, \"Latin America/Caribbean\" text, \"Northern America\" text, \"Oceania\" text )"
    ],
    "query": "what will the population of Asia be when Latin America/Caribbean is 783 (7.5%)?."
}

### response: SELECT "Asia" FROM table_22767 WHERE "Latin America/Caribbean" = '783 (7.5%)'



#####

POST http://127.0.0.1:5000/ai/text2sql
Content-Type: application/json

{
    "tables": [
        "CREATE TABLE procedures ( subject_id text, hadm_id text, icd9_code text, short_title text, long_title text )",
        "CREATE TABLE diagnoses ( subject_id text, hadm_id text, icd9_code text, short_title text, long_title text )",
        "CREATE TABLE lab ( subject_id text, hadm_id text, itemid text, charttime text, flag text, value_unit text, label text, fluid text )",
        "CREATE TABLE demographic ( subject_id text, hadm_id text, name text, marital_status text, age text, dob text, gender text, language text, religion text, admission_type text, days_stay text, insurance text, ethnicity text, expire_flag text, admission_location text, discharge_location text, diagnosis text, dod text, dob_year text, dod_year text, admittime text, dischtime text, admityear text )",
        "CREATE TABLE prescriptions ( subject_id text, hadm_id text, icustay_id text, drug_type text, drug text, formulary_drug_cd text, route text, drug_dose text )"
    ],
    "query": "what is the total number of patients who were diagnosed with icd9 code 2254?"
}

### response: SELECT COUNT(DISTINCT demographic.subject_id) FROM demographic INNER JOIN diagnoses ON demographic.hadm_id = diagnoses.hadm_id WHERE diagnoses.icd9_code = "2254"



#####

POST http://127.0.0.1:5000/ai/text2sql
Content-Type: application/json

{
  "tables": [
    "CREATE TABLE exchange_rate( id bigint, actual_at timestamp,commodity_symbol varchar not null,base_currency_iso_code varchar not null,unit_symbol varchar,normalization_unit_symbol varchar,buy_value numeric(17,8),buy_change numeric(17,8),buy_value_ratio numeric(17,6),buy_normalized_value numeric(17,8),buy_normalized_change numeric(17,8),sell_value numeric(17,8),sell_change numeric(17,8),sell_change_ratio numeric(17,6),sell_normalized_value numeric(17,8),sell_normalized_change numeric(17,8),recorded_at timestamp with time zone not null,type smallint not null,kind smallint not null,read_at timestamp with time zone default CURRENT_DATE not null,country_iso_code char(2) default 'US'::bpchar not null,country_division_iso_code char(5),city_id bigint);",
    "CREATE TABLE symbol(id bigint,commodity_symbol varchar not null,type smallint not null,kind smallint not null,exchange_listed boolean default true not null,reference_name varchar,bookmarks_count bigint default 0 not null,reject_count bigint default 0 not null,pins_count bigint default 0 not null,shared_count bigint default 0 not null,visited_count bigint default 0 not null);",
    "CREATE TABLE reaction(id bigint key,commodity_symbol varchar not null,usage_tag_id bigint not null,type smallint not null,reacted_at timestamp);"
  ],
  "query": "What are the symbols with the most positive reactions and the highest exchange rate?"
}

### response: SELECT symbol, MAX(change_rate) FROM reaction WHERE reaction_type = 'positive' GROUP BY symbol ORDER BY COUNT(*) DESC LIMIT 1



####

POST http://127.0.0.1:5000/ai/text2sql
Content-Type: application/json

{
  "tables": [
    "create table t_commodity_exchange_rate( id bigint generated always as identity primary key, actual_at timestamp with time zone not null,commodity_symbol varchar not null,base_currency_iso_code varchar not null,unit_symbol varchar,normalization_unit_symbol varchar,buy_value numeric(17,8),buy_change numeric(17,8),buy_value_ratio numeric(17,6),buy_normalized_value numeric(17,8),buy_normalized_change numeric(17,8),sell_value numeric(17,8),sell_change numeric(17,8),sell_change_ratio numeric(17,6),sell_normalized_value numeric(17,8),sell_normalized_change numeric(17,8),recorded_at timestamp with time zone not null,type smallint not null,kind smallint not null,read_at timestamp with time zone default CURRENT_DATE not null,country_iso_code char(2) default 'US'::bpchar not null,country_division_iso_code char(5),city_id bigint);",
    "create table t_commodity_symbol(id bigint generated always as identityprimary key,commodity_symbol varchar not null,type smallint not null,kind smallint not null,exchange_listed boolean default true not null,reference_name varchar,bookmarks_count bigint default 0 not null,reject_count bigint default 0 not null,pins_count bigint default 0 not null,shared_count bigint default 0 not null,visited_count bigint default 0 not null);",
    "create table t_commodity_reaction(id bigint generated always as identityprimary key,commodity_symbol varchar not null,usage_tag_id bigint not null,type smallint not null,reacted_at timestamp with time zone not null);"
  ],
  "query": "What are the symbols with the most positive reactions and the highest exchange rate?"
}

### response: SELECT DISTINCT purchase_method_code FROM table WHERE NOT id IN (SELECT id FROM t_commodity_reaction WHERE t1.time zone not null IN (SELECT country_division_iso_code FROM country WHERE country_division_iso_code = 'US') AND NOT id IN (SELECT id FROM t_commodity_reaction WHERE t1.country_division_id = 0 AND NOT country_division_code IN (SELECT t1.country_division_id FROM t_commodity_symbol WHERE time_count = 'null')
```