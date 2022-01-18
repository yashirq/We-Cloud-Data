import http.client
import json


access_token = """OwNpo00TnGOaT4VceqO4DRHynPGnXypQWLbSjtwI8E8aC.99qUzcjMum\
iOTiZUYCWIms8msjfJVvN5uNcfAzLlxkAe25emA4GUcWROXgCqJf8o1VNEm6hxkX3hJ260qR"""
conn = http.client.HTTPSConnection("api.surveymonkey.com")
headers = {
    'Accept': "application/json",
    'Authorization': "Bearer %s" % access_token
}

# Collect all the survey ids
def survey_ids():

    ids = []
    conn.request("GET", "/v3/surveys", headers=headers)
    res = conn.getresponse()
    data = json.load(res)['data']

    for survey in data:
        id = survey['id']
        ids.append(id)

    return ids


# Collect all questions' details
def questions_details(survey_id):

    conn.request("GET", "/v3/surveys/%s/details" % survey_id, headers=headers)
    res = conn.getresponse()
    data = json.load(res)

    questions = data['pages'][0]['questions']
    qns_details = []

    for question in questions:
        qn_details = {
            "position_id": question["position"],
            "question_id": question["id"],
            "heading": question["headings"][0]["heading"],
            "family": question["family"],
            "subtype": question["subtype"]
        }

        family = qn_details["family"]
        subtype = qn_details["subtype"]

        # Find other families and subtypes
        # Remove this block if all families and subtypes are implemented
        family_set = {'open_ended', 'multiple_choice',
                      'matrix', 'single_choice'}
        subtype_set = {'vertical', 'vertical_two_col',
                       'single', 'rating', 'essay'}
        if family not in family_set:
            print(
                "########################################################################")
            print(survey_id)
            print("new family found: %s" % family)
        if subtype not in subtype_set:
            print(
                "########################################################################")
            print(survey_id)
            print("new subtype found: %s" % subtype)

        # There are 7 families in total

        # Case 1: open_ended
        # Need to do nothing

        # Case 2 & 3: single_choice | multiple_choice
        if family in ["single_choice", "multiple_choice"]:

            qn_details["choices"] = []
            choice_details = {}

            for choice in question["answers"]["choices"]:
                choice_details["choice_position"] = choice["position"]
                choice_details["choice_text"] = choice["text"]
                choice_details["choice_id"] = choice["id"]
                temp_choice = choice_details.copy()
                qn_details["choices"].append(temp_choice)

            if "other" in question["answers"].keys():
                qn_details["other_id"] = question["answers"]["other"]["id"]
                qn_details["other_text"] = question["answers"]["other"]["text"]

        # Case 4: matrix
        elif family == "matrix":

            qn_details["rows"] = []
            qn_details["choices"] = []
            row_details = {}
            choice_details = {}

            for row in question["answers"]["rows"]:
                row_details["row_position"] = row["position"]
                row_details["row_text"] = row["text"]
                row_details["row_id"] = row["id"]
                temp_row = row_details.copy()
                qn_details["rows"].append(temp_row)

            for choice in question["answers"]["choices"]:
                choice_details["choice_position"] = choice["position"]
                choice_details["choice_text"] = choice["text"]
                choice_details["choice_id"] = choice["id"]
                if subtype == "rating":
                    choice_details["weight"] = choice["weight"]
                temp_choice = choice_details.copy()
                qn_details["choices"].append(temp_choice)

        qns_details.append(qn_details)

    return qns_details


# Collect all response ids in a survey
def response_ids(survey_id):

    conn.request("GET", "/v3/surveys/%s/responses" %
                 survey_id, headers=headers)
    res = conn.getresponse()
    data = json.load(res)["data"]
    id_list = []

    for response in data:
        id = response["id"]
        id_list.append(id)

    return id_list


# Check question family
def question_family(question_id):
    for question_details in questions_details:
        if question_details["question_id"] == str(question_id):
            return question_details["family"]


# Collect a response details
def response_details(survey_id, response_id):

    conn.request("GET", "/v3/surveys/%s/responses/%s/details" %
                 (survey_id, response_id), headers=headers)
    res = conn.getresponse()
    data = json.load(res)

    res_details = [{
        "survey_id": survey_id,
        "collector_id": data["collector_id"],
        "response_id": data["id"],
    }]

    pages = data["pages"]

    for page in pages:
        res_details.append({"page_id": page["id"]})
        questions = page["questions"]

        for question in questions:
            question_details = {
                "question_id": question["id"]
            }

            family = question_family(question["id"])
            answers = question["answers"]

            if family == "open_ended":
                for answer in answers:
                    question_details["text"] = answer["text"]            

            elif family == "single_choice":
                for answer in answers:
                    question_details["choice_id"] = answer["choice_id"]

            elif family == "multiple_choice":
                for answer in answers:
                    keys = answer.keys()
                    if "choice_id" in keys:
                        question_details["choice_id"] = answer["choice_id"]
                    elif "other_id" in keys:
                        question_details["other_id"] = answer["other_id"]
                        question_details["text"] = answer["text"]

            elif family == "matrix":
                question_details["answers"] = []
                for answer in answers:
                    keys = answer.keys()
                    answer_details = {
                        "row_id": answer["row_id"],
                        "choice_id": answer["choice_id"]
                    }
                    if "choice_metadata" in keys:
                        answer_details["weight"] = answer["choice_metadata"]["weight"]

                    question_details["answers"].append(answer_details)

            res_details.append(question_details)

    return res_details


# Collect all reponses details
def responses_details():
    resps_details = []
    surv_ids = survey_ids()
    for survey_id in surv_ids:
        resp_ids = response_ids(survey_id)
        for response_id in resp_ids:
            resp_details = response_details(survey_id, response_id)
            resps_details.append(resp_details)
    return resps_details


responses = responses_details()
print(responses)