import pathlib


tables = {
    1: 'surveys',
    2: 'families',
    3: 'subtypes',
    4: 'questions',
    5: 'question_choices',
    6: 'question_rows',
    7: 'open_ended_responses',
    8: 'single_choice_responses',
    9: 'multiple_choice_responses',
    10: 'matrix_responses',
    11: 'demographic_responses',
    12: 'datetime_responses'
}

tables2 = tables.copy()
for index in tables2:
    tables2[index] = f'gz_{tables2.get(index)}_v3'

# 1 surveys
create_surveys_table = f'''CREATE TABLE "{tables2[1]}" (
    "sid" BIGINT,
    "survey_title" TEXT,
    PRIMARY KEY ("sid")
    );'''
new_surveys_path = '%s/output/01new_surveys.json' % pathlib.Path(
    __file__).parent.resolve()

# 2 families
create_families_table = f'''CREATE TABLE "{tables2[2]}" (
    "fid" INT,
    "family" VARCHAR(20) UNIQUE NOT NULL,
    PRIMARY KEY("fid")
    );'''
families_path = '%s/families.json' % pathlib.Path(
    __file__).parent.resolve()

# 3 subtypes
create_subtypes_table = f'''CREATE TABLE "{tables2[3]}" (
    "stid" INT,
    "subtype" VARCHAR(30) NOT NULL,
    PRIMARY KEY("stid")
    );'''
subtypes_path = '%s/subtypes.json' % pathlib.Path(
    __file__).parent.resolve()

# 4 questions
create_questions_table = f'''CREATE TABLE "{tables2[4]}" (
    "sid" BIGINT,
    "position" INT,
    "qid" BIGINT,
    "fid" INT,
    "stid" INT,
    "question" TEXT,
    "survey_link" VARCHAR(256),
    PRIMARY KEY ("qid"),
    CONSTRAINT "FK_{tables2[4]}.sid"
      FOREIGN KEY ("sid")
        REFERENCES "{tables2[1]}"("sid"),
    CONSTRAINT "FK_{tables2[4]}.fid"
      FOREIGN KEY ("fid")
        REFERENCES "{tables2[2]}"("fid"),
    CONSTRAINT "FK_{tables2[4]}.stid"
      FOREIGN KEY ("stid")
        REFERENCES "{tables2[3]}"("stid")  
    );'''
new_questions_path = '%s/output/04new_questions.json' % pathlib.Path(
    __file__).parent.resolve()

# 5 question_choices
create_question_choices_table = f'''CREATE TABLE "{tables2[5]}" (
    "qid" BIGINT,
    "cid" BIGINT,
    "ctext" TEXT,
    PRIMARY KEY ("cid"),
    CONSTRAINT "FK_{tables2[5]}.qid"
      FOREIGN KEY ("qid")
        REFERENCES "{tables2[4]}"("qid")
    );'''
new_question_choices_path = '%s/output/04new_question_choices.json' % pathlib.Path(
    __file__).parent.resolve()

# 6 question_rows
create_question_rows_table = f'''CREATE TABLE "{tables2[6]}" (
    "qid" BIGINT,
    "roid" BIGINT,
    "rotext" TEXT,
    PRIMARY KEY ("roid"),
    CONSTRAINT "FK_{tables2[6]}.qid"
      FOREIGN KEY ("qid")
        REFERENCES "{tables2[4]}"("qid")
    );'''
new_question_rows_path = '%s/output/04new_question_rows.json' % pathlib.Path(
    __file__).parent.resolve()

# 7 open_ended_responses
create_open_ended_responses_table = f'''CREATE TABLE "{tables2[7]}" (
    "rid" BIGINT,
    "qid" BIGINT,
    "text" TEXT,
    PRIMARY KEY ("rid", "qid"),
    CONSTRAINT "FK_{tables2[7]}.qid"
      FOREIGN KEY ("qid")
        REFERENCES "{tables2[4]}"("qid")
    );'''
new_open_ended_responses_path = '%s/output/05new_open_ended_response.json' % pathlib.Path(
    __file__).parent.resolve()

# 8 single_choice_responses
create_single_choice_responses_table = f'''CREATE TABLE "{tables2[8]}" (
    "rid" BIGINT,
    "qid" BIGINT,
    "cid" BIGINT,
    "oid" BIGINT,
    "otext" TEXT,
    PRIMARY KEY ("rid", "qid"),
    CONSTRAINT "FK_{tables2[8]}.qid"
      FOREIGN KEY ("qid")
        REFERENCES "{tables2[4]}"("qid"),
    CONSTRAINT "FK_{tables2[8]}.cid"
      FOREIGN KEY ("cid")
        REFERENCES "{tables2[5]}"("cid")
    );'''
new_single_choice_responses_path = '%s/output/05new_single_choice_response.json' % pathlib.Path(
    __file__).parent.resolve()

# 9 multiple_choice_responses
create_multiple_choice_responses_table = f'''CREATE TABLE "{tables2[9]}" (
    "rid" BIGINT,
    "qid" BIGINT,
    "cid" BIGINT,
    "oid" BIGINT,
    "otext" TEXT,
    PRIMARY KEY ("rid", "qid", "cid"),
    CONSTRAINT "FK_{tables2[9]}.qid"
      FOREIGN KEY ("qid")
        REFERENCES "{tables2[4]}"("qid"),
    CONSTRAINT "FK_{tables2[9]}.cid"
      FOREIGN KEY ("cid")
        REFERENCES "{tables2[5]}"("cid")
    );'''
new_multiple_choice_responses_path = '%s/output/05new_multiple_choice_response.json' % pathlib.Path(
    __file__).parent.resolve()

# 10 matrix_responses
create_matrix_responses_table = f'''CREATE TABLE "{tables2[10]}" (
    "rid" BIGINT,
    "qid" BIGINT,
    "cid" BIGINT,
    "roid" BIGINT,
    "weight" INT,
    "oid" BIGINT,
    "otext" TEXT,
    PRIMARY KEY ("rid", "qid", "cid", "roid"),
    CONSTRAINT "FK_{tables2[10]}.qid"
      FOREIGN KEY ("qid")
        REFERENCES "{tables2[4]}"("qid"),
    CONSTRAINT "FK_{tables2[10]}.cid"
      FOREIGN KEY ("cid")
        REFERENCES "{tables2[5]}"("cid"),
    CONSTRAINT "FK_{tables2[10]}.roid"
      FOREIGN KEY ("roid")
        REFERENCES "{tables2[6]}"("roid")
    );'''
new_matrix_responses_path = '%s/output/05new_matrix_response.json' % pathlib.Path(
    __file__).parent.resolve()

# 11 demographic_responses
create_demographic_responses_table = f'''CREATE TABLE "{tables2[11]}" (
    "rid" BIGINT,
    "qid" BIGINT,
    "roid" BIGINT,
    "rotext" TEXT,
    PRIMARY KEY ("rid", "qid", "roid"),
    CONSTRAINT "FK_{tables2[11]}.qid"
      FOREIGN KEY ("qid")
        REFERENCES "{tables2[4]}"("qid"),
    CONSTRAINT "FK_{tables2[11]}.roid"
      FOREIGN KEY ("roid")
        REFERENCES "{tables2[6]}"("roid")
    );'''
new_demographic_responses_path = '%s/output/05new_demographic_response.json' % pathlib.Path(
    __file__).parent.resolve()

# 12 datetime_responses
create_datetime_responses_table = f'''CREATE TABLE "{tables2[12]}" (
    "rid" BIGINT,
    "qid" BIGINT,
    "roid" BIGINT,
    "rotext" TEXT,
    PRIMARY KEY ("rid", "qid", "roid"),
    CONSTRAINT "FK_{tables2[12]}.qid"
      FOREIGN KEY ("qid")
        REFERENCES "{tables2[4]}"("qid"),
    CONSTRAINT "FK_{tables2[12]}.roid"
      FOREIGN KEY ("roid")
        REFERENCES "{tables2[6]}"("roid")
    );'''
new_datetime_responses_path = '%s/output/05new_datetime_response.json' % pathlib.Path(
    __file__).parent.resolve()

primary_keys = {
    tables2[1]: 'sid',
    tables2[2]: 'fid',
    tables2[3]: 'stid',
    tables2[4]: 'qid',
    tables2[5]: 'cid',
    tables2[6]: 'roid',
    tables2[7]: 'rid, qid',
    tables2[8]: 'rid, qid',
    tables2[9]: 'rid, qid, cid',
    tables2[10]: 'rid, qid, cid, roid',
    tables2[11]: 'rid, qid, roid',
    tables2[12]: 'rid, qid, roid'
}

create_table_syntax = {
    tables2[1]: create_surveys_table,
    tables2[2]: create_families_table,
    tables2[3]: create_subtypes_table,
    tables2[4]: create_questions_table,
    tables2[5]: create_question_choices_table,
    tables2[6]: create_question_rows_table,
    tables2[7]: create_open_ended_responses_table,
    tables2[8]: create_single_choice_responses_table,
    tables2[9]: create_multiple_choice_responses_table,
    tables2[10]: create_matrix_responses_table,
    tables2[11]: create_demographic_responses_table,
    tables2[12]: create_datetime_responses_table,
}

insert_syntax = [
    (new_surveys_path, tables2[1]),
    # (families_path, tables2[2]),
    # (subtypes_path, tables2[3]),
    (new_questions_path, tables2[4]),
    (new_question_choices_path, tables2[5]),
    (new_question_rows_path, tables2[6]),
    (new_open_ended_responses_path, tables2[7]),
    (new_single_choice_responses_path, tables2[8]),
    (new_multiple_choice_responses_path, tables2[9]),
    (new_matrix_responses_path, tables2[10]),
    (new_demographic_responses_path, tables2[11]),
    (new_datetime_responses_path, tables2[12])
]
