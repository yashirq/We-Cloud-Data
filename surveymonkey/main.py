from postgres_db import Postgres_Database
from surveys import Surveys
from surveys_data_collector import Surveys_Data_Collector
from survey_data_transmit import Survey_Data_Transmit
from retrieve_questions_info import Retrieve_Questions_Info
from retrieve_responses_info import Retrieve_Responses_Info


def main():

    # # 00
    # # ***** RUNING THIS WILL REMOVE ALL DATA IN DATABASE *****
    # # ***** DO NOT RUN THIS UNLESS NECESSARY ******
    # # Call create_tables() to generate empty tables in database
    # Postgres_Database().create_tables()
    # print('\nStep #1 all tables are created successfully\n ===========================================================================')

    # 01
    # Call surveys() to generate all_surveys.json and new_surveys.json
    Surveys().surveys()
    if not Surveys().new_survey_ids():
        print('\nStep #1 Do not find any new surveys\n ===========================================================================')
        return
    print('\nStep #1 all new surveys are founded\n ===========================================================================')

    # 02
    # Call questions_data() to generate questions_data.json
    Surveys_Data_Collector().questions_data()
    print('\nStep #2 all new surveys\' question_data are collected\n ===========================================================================')
    # Call responses_data() to generate responses_data.json
    Surveys_Data_Collector().responses_data()
    print('\nStep #2 all new surveys\' response_data are collected\n ===========================================================================')

    # 03
    # Call local_to_s3() to upload 02_questions_data.json
    # , 02_responses_data.json, 02_new_questions_data.json
    # and 02_new_responses_data  to s3 bucket
    Survey_Data_Transmit().local_to_s3('questions_data.json')
    Survey_Data_Transmit().local_to_s3('responses_data.json')
    Survey_Data_Transmit().local_to_s3('new_questions_data.json')
    Survey_Data_Transmit().local_to_s3('new_responses_data.json')
    print('\nStep #3 all surveys and new surveys\' questions_data and response_data are uploaded to s3\n ===========================================================================')

    # Call s3_to_local() to download questions_data.json,
    # responses_data.json, new_questions_data.json and
    # new_responses_data.json from s3 bucket to local
    Survey_Data_Transmit().s3_to_local('questions_data.json')
    Survey_Data_Transmit().s3_to_local('responses_data.json')
    Survey_Data_Transmit().s3_to_local('new_questions_data.json')
    Survey_Data_Transmit().s3_to_local('new_responses_data.json')
    print('\nStep #3 all surveys and new surveys\' questions_data and response_data are downloaded from s3\n ===========================================================================')

    # 04
    # Call retrieve_questions_info() to generate questions_info.json
    Retrieve_Questions_Info().retrieve_questions_info()
    print('\nStep #4 all new surveys\' questions_info are retrieved\n ===========================================================================')

    # 05
    # Call retrieve_responses_info() to generate different kinds of response.json
    Retrieve_Responses_Info().retrieve_responses_info()
    print('\nStep #5 all new surveys\' responses_info are retrieved\n ===========================================================================')

    # 06
    # Call insert_to_tables() to insert record into tables
    Postgres_Database().insert_to_tables()
    print('\nStep #6 all new surveys\' record are inserted to corresponding tables\n ===========================================================================')


if __name__ == '__main__':
    main()
