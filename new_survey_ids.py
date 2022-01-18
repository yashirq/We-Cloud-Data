import json


class New_Survey_Ids:

    def survey_ids(self):

        survey_id_list = []

        with open('We-Cloud-Data/InternalProject/new_surveys.json', 'r') as f:
            data = f.readlines()
            for survey in data:
                survey = survey.strip()
                survey = json.loads(survey)
                survey_id = survey['sid']
                survey_id_list.append(survey_id)

        return survey_id_list
