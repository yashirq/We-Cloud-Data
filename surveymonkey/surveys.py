import pathlib
import json
import unicodedata

import auth
import sql_string


class Surveys:

    def surveys(self):

        # Get surveys
        auth.sm_conn.request('GET', '/v3/surveys', headers=auth.headers)
        res = auth.sm_conn.getresponse()
        data = json.load(res)['data']

        # Pathes for all_surveys and new_surveys
        # all_surveys include old surveys and new surveys
        all_surveys = '%s/output/01all_surveys.json' % pathlib.Path(
            __file__).parent.resolve()
        new_surveys = '%s/output/01new_surveys.json' % pathlib.Path(
            __file__).parent.resolve()

        with open(all_surveys, 'a+') as f1, open(new_surveys, 'w') as f2:
            # Retrieve required info for survey table
            for survey in data:
                # Clean the data with unicodedata.normalize
                surv = {'sid': survey['id'],
                        'survey_title': unicodedata.normalize('NFKD', survey['title'])
                        }

                # Current file position moves to the end in append mode
                # Need to move the file position to the start
                f1.seek(0)

                # Avoid duplicated writing
                auth.cursor.execute(
                    f'''SELECT sid FROM {sql_string.tables2[1]}''')
                result = auth.cursor.fetchall()
                # Flag exists check if sid is already in gz_surveys_v3 table
                exists = 0
                for sid in result:
                    if sid[0] == int(surv['sid']):
                        exists = 1
                        break

                if exists == 0:
                    json.dump(surv, f1)
                    # Add a new line for human readability
                    f1.write('\n')
                    json.dump(surv, f2)
                    f2.write('\n')

    def new_survey_ids(self):

        survey_id_list = []
        file_path = '%s/output/01new_surveys.json' % pathlib.Path(
            __file__).parent.resolve()

        with open(file_path, 'r') as f:
            data = f.readlines()
            for survey in data:
                survey = survey.strip()
                survey = json.loads(survey)
                survey_id = survey['sid']
                survey_id_list.append(survey_id)

        return survey_id_list
