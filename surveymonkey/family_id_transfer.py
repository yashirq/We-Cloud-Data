family_table = {'single_choice': 1,
                'matrix': 2,
                'open_ended': 3,
                'demographic': 4,
                'datetime': 5,
                'multiple_choice': 6,
                'presentation': 7
                }

# First digit in the subtype_id in the subtype_table
# refers to the family_id in the family_table
single_choice_subtype_table = {'vertical': 11,
                               'horiz': 12,
                               'menu': 13,
                               'vertical_two_col': 14}
matrix_subtype_table = {'single': 21,
                        'rating': 22,
                        'ranking': 23,
                        'menu': 24,
                        'multi': 25}
open_ended_subtype_table = {'single': 31,
                            'multi': 32,
                            'numerical': 33,
                            'essay': 34}
demographic_subtype_table = {'international': 41,
                             'us': 42}
datetime_subtype_table = {'both': 51,
                          'date_only': 52,
                          'time_only': 53}
multiple_choice_subtype_table = {'vertical': 61,
                                 'vertical_two_col': 62}
presentation_subtype_table = {'descriptive_text': 71,
                              'image': 72}
