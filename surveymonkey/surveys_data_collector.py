import json
import pathlib

import auth
from surveys import Surveys
from write_to_file import Write_To_File


class Surveys_Data_Collector:

    def __init__(self):
        self.new_surveys = Surveys().new_survey_ids()  # Find recent added surveys
        self.append_json_to_file = Write_To_File().append_json_to_file
        self.clear_file = Write_To_File().clear_file
        self.questions_data_path = '%s/output/02questions_data.json' % pathlib.Path(
            __file__).parent.resolve()
        self.responses_data_path = '%s/output/02responses_data.json' % pathlib.Path(
            __file__).parent.resolve()
        self.new_questions_data_path = '%s/output/02new_questions_data.json' % pathlib.Path(
            __file__).parent.resolve()
        self.new_responses_data_path = '%s/output/02new_responses_data.json' % pathlib.Path(
            __file__).parent.resolve()
        self.empty_surveys_path = '%s/output/02empty_surveys.json' % pathlib.Path(
            __file__).parent.resolve()
        self.new_empty_surveys_path = '%s/output/02new_empty_surveys.json' % pathlib.Path(
            __file__).parent.resolve()

    def questions_data(self):
        if not self.new_surveys:
            print('There is no new surveys. No need to write questions data.')
            return

        self.clear_file(self.new_questions_data_path)

        for survey in self.new_surveys:
            auth.sm_conn.request('GET', '/v3/surveys/%s/details' %
                                 survey, headers=auth.headers)
            res = auth.sm_conn.getresponse()
            data = json.load(res)
            if data['title'] == 'Untitled Survey' and data['question_count'] == 0:
                self.append_json_to_file(self.empty_surveys_path, data['id'])
                self.append_json_to_file(
                    self.new_empty_surveys_path, data['id'])
            else:
                self.append_json_to_file(self.questions_data_path, data)
                self.append_json_to_file(self.new_questions_data_path, data)

    def responses_data(self):
        if not self.new_surveys:
            print('There is no new surveys. No need to write responses data.')
            return

        self.clear_file(self.new_responses_data_path)

        for survey in self.new_surveys:
            auth.sm_conn.request('GET', '/v3/surveys/%s/responses/bulk' %
                                 survey, headers=auth.headers)
            res = auth.sm_conn.getresponse()
            data = json.load(res)
            self.append_json_to_file(self.responses_data_path, data)
            self.append_json_to_file(self.new_responses_data_path, data)
