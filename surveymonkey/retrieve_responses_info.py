import json
import pathlib

from surveys import Surveys
import res_base_on_fam
from retrieve_questions_info import Retrieve_Questions_Info
from write_to_file import Write_To_File


class Retrieve_Responses_Info:

    def __init__(self):
        self.res_fam = res_base_on_fam.Response_Base_On_Family()
        self.clear_file = Write_To_File().clear_file

        self.new_responses_data = '%s/output/03s3_new_responses_data.json' % pathlib.Path(
            __file__).parent.resolve()

        self.single_choice_response_path = '%s/output/05single_choice_response.json' % pathlib.Path(
            __file__).parent.resolve()
        self.matrix_response_path = '%s/output/05matrix_response.json' % pathlib.Path(
            __file__).parent.resolve()
        self.open_ended_response_path = '%s/output/05open_ended_response.json' % pathlib.Path(
            __file__).parent.resolve()
        self.multiple_choice_response_path = '%s/output/05multiple_choice_response.json' % pathlib.Path(
            __file__).parent.resolve()
        self.demographic_response_path = '%s/output/05demographic_response.json' % pathlib.Path(
            __file__).parent.resolve()
        self.datetime_response_path = '%s/output/05datetime_response.json' % pathlib.Path(
            __file__).parent.resolve()

        self.new_single_choice_response_path = '%s/output/05new_single_choice_response.json' % pathlib.Path(
            __file__).parent.resolve()
        self.new_matrix_response_path = '%s/output/05new_matrix_response.json' % pathlib.Path(
            __file__).parent.resolve()
        self.new_open_ended_response_path = '%s/output/05new_open_ended_response.json' % pathlib.Path(
            __file__).parent.resolve()
        self.new_multiple_choice_response_path = '%s/output/05new_multiple_choice_response.json' % pathlib.Path(
            __file__).parent.resolve()
        self.new_demographic_response_path = '%s/output/05new_demographic_response.json' % pathlib.Path(
            __file__).parent.resolve()
        self.new_datetime_response_path = '%s/output/05new_datetime_response.json' % pathlib.Path(
            __file__).parent.resolve()

    def retrieve_response_info(self, survey_id: int) -> dict:

        with open(self.new_responses_data, 'r') as f:
            for line in f:  # each line is a response data set
                response_data = json.loads(line)['data']
                for res in response_data:  # there are multiple responses in each response data set
                    if int(res['survey_id']) == survey_id:
                        pages = res['pages']
                        response_id = res['id']
                        for page in pages:
                            res_qtns = page['questions']
                            for res_qtn in res_qtns:
                                question_id = res_qtn['id']
                                answers = res_qtn['answers']
                                # Check question's family id
                                fam_id = Retrieve_Questions_Info().family_id(
                                    survey_id, int(question_id))

                                # Initialize common required response info dictionary
                                res_info = {'rid': response_id,
                                            'qid': question_id}

                                if fam_id == 3:
                                    self.res_fam.opend_ended_response(
                                        answers, res_info, self.open_ended_response_path, self.new_open_ended_response_path)
                                if fam_id == 1:
                                    self.res_fam.single_choice_response(
                                        answers, res_info, self.single_choice_response_path, self.new_single_choice_response_path)
                                if fam_id == 6:
                                    self.res_fam.multiple_choice_response(
                                        answers, res_info, self.multiple_choice_response_path, self.new_multiple_choice_response_path)
                                if fam_id == 2:
                                    self.res_fam.matrix_response(
                                        answers, res_info, self.matrix_response_path, self.new_matrix_response_path)
                                if fam_id == 4:
                                    self.res_fam.demographic_response(
                                        answers, res_info, self.demographic_response_path, self.new_demographic_response_path)
                                if fam_id == 5:
                                    self.res_fam.datetime_response(
                                        answers, res_info, self.datetime_response_path, self.new_datetime_response_path)
                                if fam_id == 7:
                                    print(
                                        'New family [presentation] found. Please implement a parse function in res_base_on_fam.py')

    def retrieve_responses_info(self):
        # Find recent added surveys
        survey_ids = Surveys().new_survey_ids()

        self.clear_file(self.new_single_choice_response_path)
        self.clear_file(self.new_matrix_response_path)
        self.clear_file(self.new_open_ended_response_path)
        self.clear_file(self.new_multiple_choice_response_path)
        self.clear_file(self.new_demographic_response_path)
        self.clear_file(self.new_datetime_response_path)

        for survey_id in survey_ids:
            # Add question_info to the questions list
            self.retrieve_response_info(int(survey_id))
