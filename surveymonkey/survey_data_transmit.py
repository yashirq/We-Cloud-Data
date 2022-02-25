import pathlib
import boto3

import auth
from write_to_file import Write_To_File


class Survey_Data_Transmit:

    def __init__(self):
        # Clear 02new_empty_surveys.json
        self.new_empty_surveys_path = '%s/output/02new_empty_surveys.json' % pathlib.Path(
            __file__).parent.resolve()
        Write_To_File().clear_file(self.new_empty_surveys_path)
        self.s3 = boto3.resource('s3',
                                 region_name='ca-central-1',
                                 aws_access_key_id=auth.aws_access_key_id,
                                 aws_secret_access_key=auth.aws_secret_access_key)
        self.bucket = self.s3.Bucket('beamdata-internal-surveytools')
        self.local_questions_data = '%s/output/02questions_data.json' % pathlib.Path(
            __file__).parent.resolve()
        self.local_responses_data = '%s/output/02responses_data.json' % pathlib.Path(
            __file__).parent.resolve()
        self.local_new_questions_data = '%s/output/02new_questions_data.json' % pathlib.Path(
            __file__).parent.resolve()
        self.local_new_responses_data = '%s/output/02new_responses_data.json' % pathlib.Path(
            __file__).parent.resolve()
        self.s3_questions_data = '%s/output/03s3_questions_data.json' % pathlib.Path(
            __file__).parent.resolve()
        self.s3_responses_data = '%s/output/03s3_responses_data.json' % pathlib.Path(
            __file__).parent.resolve()
        self.s3_new_questions_data = '%s/output/03s3_new_questions_data.json' % pathlib.Path(
            __file__).parent.resolve()
        self.s3_new_responses_data = '%s/output/03s3_new_responses_data.json' % pathlib.Path(
            __file__).parent.resolve()

    def local_to_s3(self, file_name: str) -> None:
        if file_name == 'questions_data.json':
            self.bucket.upload_file(
                self.local_questions_data, 'questions_data.json')
        elif file_name == 'responses_data.json':
            self.bucket.upload_file(
                self.local_responses_data, 'responses_data.json')
        elif file_name == 'new_questions_data.json':
            self.bucket.upload_file(
                self.local_new_questions_data, 'new_questions_data.json')
        elif file_name == 'new_responses_data.json':
            self.bucket.upload_file(
                self.local_new_responses_data, 'new_responses_data.json')

    def s3_to_local(self, file_name: str) -> None:
        if file_name == 'questions_data.json':
            self.bucket.download_file(
                'questions_data.json', self.s3_questions_data)
        elif file_name == 'responses_data.json':
            self.bucket.download_file(
                'responses_data.json', self.s3_responses_data)
        elif file_name == 'new_questions_data.json':
            self.bucket.download_file(
                'new_questions_data.json', self.s3_new_questions_data)
        elif file_name == 'new_responses_data.json':
            self.bucket.download_file(
                'new_responses_data.json', self.s3_new_responses_data)
