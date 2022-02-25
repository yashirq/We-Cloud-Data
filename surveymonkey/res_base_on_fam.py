import unicodedata

from write_to_file import Write_To_File


class Response_Base_On_Family:
    def __init__(self):
        self.append_json_to_file = Write_To_File().append_json_to_file
        self.cid = ''
        self.oid = ''
        self.otext = ''
        self.roid = ''
        self.rotext = ''
        self.text = ''
        self.weight = 0

    def single_choice_response(self, answers, response_dict, response_path, new_response_path):
        for answer in answers:
            if 'other_id' in answer.keys():
                self.oid = answer['other_id']
                self.otext = unicodedata.normalize(
                    'NFKD', answer['text'])
            else:
                self.cid = answer['choice_id']
            response_dict['cid'] = self.cid
            response_dict['oid'] = self.oid
            response_dict['otext'] = self.otext
            self.append_json_to_file(response_path, response_dict)
            self.append_json_to_file(new_response_path, response_dict)

    def matrix_response(self, answers, response_dict, response_path, new_response_path):
        for answer in answers:
            if 'choice_id' in answer.keys():
                self.cid = answer['choice_id']
                self.roid = answer['row_id']
            if 'other_id' in answer.keys():
                self.oid = answer['other_id']
                self.otext = answer['text']
            if 'choice_metadata' in answer.keys():
                self.weight = answer['choice_metadata']['weight']
            response_dict['cid'] = self.cid
            response_dict['roid'] = self.roid
            response_dict['oid'] = self.oid
            response_dict['otext'] = self.otext
            response_dict['weight'] = self.weight
            self.append_json_to_file(response_path, response_dict)
            self.append_json_to_file(new_response_path, response_dict)

    def opend_ended_response(self, answers, response_dict, response_path, new_response_path):
        self.text = unicodedata.normalize('NFKD', answers[0]['text'])
        response_dict['text'] = self.text
        self.append_json_to_file(response_path, response_dict)
        self.append_json_to_file(new_response_path, response_dict)

    def demographic_response(self, answers, response_dict, response_path, new_response_path):
        for answer in answers:
            self.roid = answer['row_id']
            self.rotext = unicodedata.normalize('NFKD', answer['text'])
            response_dict['roid'] = self.roid
            response_dict['rotext'] = self.rotext
            self.append_json_to_file(response_path, response_dict)
            self.append_json_to_file(new_response_path, response_dict)

    def datetime_response(self, answers, response_dict, response_path, new_response_path):
        for answer in answers:
            self.roid = answer['row_id']
            self.rotext = answer['text']
            response_dict['roid'] = self.roid
            response_dict['rotext'] = self.rotext
            self.append_json_to_file(response_path, response_dict)
            self.append_json_to_file(new_response_path, response_dict)

    def multiple_choice_response(self, answers, response_dict, response_path, new_response_path):
        for answer in answers:
            if 'other_id' in answer.keys():
                self.oid = answer['other_id']
                self.otext = unicodedata.normalize('NFKD', answer['text'])
            else:
                self.cid = answer['choice_id']
            response_dict['cid'] = self.cid
            response_dict['oid'] = self.oid
            response_dict['otext'] = self.otext
            self.append_json_to_file(response_path, response_dict)
            self.append_json_to_file(new_response_path, response_dict)
