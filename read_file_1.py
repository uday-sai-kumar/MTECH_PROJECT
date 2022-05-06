
import os

# feature_sets = {
#     "feature": 1,
#     "permission": 2,
#     "activity": 3,
#     "service_receiver": 3,
#     "provider": 3,
#     "service": 3,
#     "intent": 4,
#     "api_call": 5,
#     "real_permission": 6,
#     "call": 7,
#     "url": 8
# }
#
#
# class ReadFile:
#     @classmethod
#     def read_file(cls, path):
#         #print(path)
#         feature_vector = {i: 0 for i in range(1, 9)}
#         content = open(path).readlines()
#
#         for _line in content:
#             _index=_line.split('::')[0]
#             if _index in feature_sets:
#                 feature_vector[feature_sets[_line.split('::')[0]]] += 1
#
#         return feature_vector
#
#




class ReadFile:
    @classmethod
    def read_file(cls, path):

        my_dict = {
            "activity": [],
            "permission": [],
            "receiver": [],
            "service": [],
            "provider": [],
            "intent_filter": [],
            "api_connection": [],
            "api_content": [],
            "api_file": [],
            "api_intent": [],
            "api_data": []
        }
        # activity_set1 = dict()
        # permission_set2 = dict()
        # receiver_set3 = dict()
        # service_set4 = dict()
        # provider_set5 = dict()
        # intent_filter_set6 = dict()
        # activity_set7 = dict()
        # activity_set8 = dict()
        # activity_set9 = dict()
        # activity_set10 = dict()
        # activity_set11 = dict()


        # feature_vector = {i: 0 for i in range(1, 12)}
        content = open(path).readlines()

        for _line in content:
            _index=_line.split('::')[0]
            if _index in feature_sets:
                feature_vector[feature_sets[_line.split('::')[0]]] += 1

        return feature_vector


