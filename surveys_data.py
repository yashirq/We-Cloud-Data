import json
import pathlib
import auth
from new_survey_ids import New_Survey_Ids


class Surveys_data():

    def surveys_data(self):
        new_surveys = New_Survey_Ids().survey_ids()
        surveys_data = '%s/surveys_data.json' % pathlib.Path(
            __file__).parent.resolve()

        with open(surveys_data, 'a+') as f:
            for survey in new_surveys[:2]:
                auth.conn.request("GET", "/v3/surveys/%s/details" %
                                  survey, headers=auth.headers)
                res = auth.conn.getresponse()
                data = json.load(res)
                print(data)
                json.dump(data, f)
                f.write('\n')
            f.close()


surveys_data = Surveys_data().surveys_data()
