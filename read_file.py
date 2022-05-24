
import io

feature_sets = {
    "feature": 1,
    "permission": 2,
    "activity": 3,
    "service_receiver": 3,
    "provider": 3,
    "service": 3,
    "intent": 4,
    "api_call": 5,
    "real_permission": 6,
    "call": 7,
    "url": 8
}
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

# feature_sets = {
#     "activity": 1,
#     "permission": 2,
#     "receiver": 3,
#     "service": 4,
#     "provider": 5,
#     "intent_filter": 6,
#     "api_connection": 7,
#     "api_content": 8,
#     "api_file": 9,
#     "api_intent": 10,
#     "api_data": 11
# }


class ReadFile:
    @classmethod
    def read_file(cls, path, file_name, feature_map):


        #feature_vector = {i: 0 for i in range(1, 12)}
        content = io.open(path, 'r').readlines()

        for _line in content:
            _line = _line.rstrip()
            _index = _line.split('::')
            #print(_index)
            #if _index[0] in feature_sets:
            if _index[1] not in feature_map[_index[0]].keys():
                feature_map[_index[0]][_index[1]] = []
            feature_map[_index[0]][_index[1]].append(file_name)


        #return feature_vector


