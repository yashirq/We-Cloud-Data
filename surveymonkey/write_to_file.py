import json
import os.path


class Write_To_File:

    def append_json_to_file(self, file_path, json_obj):

        with open(file_path, 'a+') as f:
            f.seek(0)
            duplicated = 0
            for line in f:
                if json.loads(line) == json_obj:
                    duplicated = 1
                    break
            if duplicated == 0:
                json.dump(json_obj, f)
                f.write('\n')

    def write_json_to_file(self, file_path, json_obj):

        with open(file_path, 'w') as f:
            json.dump(json_obj, f)
            f.write('\n')

    def clear_file(self, file_path):
        if os.path.isfile(file_path):
            file = open(file_path, 'r+')
            file.truncate(0)
            file.close()
