import pathlib
import json
import unicodedata
import auth


class Survey_Ids():

    def survey_ids(self):

        auth.conn.request("GET", "/v3/surveys", headers=auth.headers)
        res = auth.conn.getresponse()
        data = json.load(res)['data']

        old_surveys = '%s/old_surveys.json' % pathlib.Path(
            __file__).parent.resolve()
        new_surveys = '%s/new_surveys.json' % pathlib.Path(
            __file__).parent.resolve()
        with open(old_surveys, 'a+') as f1, open(new_surveys, 'w') as f2:
            for survey in data:
                surv = {"sid": survey["id"],
                    "svy_ttl": unicodedata.normalize("NFKD", survey["title"]),
                    "svy_link": survey["href"]
                    }
                f1.seek(0)
                
                if str(surv["sid"]) not in f1.read():
                    json.dump(surv, f1)
                    f1.write('\n')
                    json.dump(surv, f2)
                    f2.write('\n')
            f1.close()
            f2.close()
        return


survey_ids = Survey_Ids().survey_ids()


