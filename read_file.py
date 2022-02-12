
import os

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


class ReadFile:
    @classmethod
    def read_file(cls, path):
        #print(path)
        feature_vector = {i: 0 for i in range(1, 9)}
        content = open(path).readlines()

        for _line in content:
            _index=_line.split('::')[0]
            if _index in feature_sets:
                feature_vector[feature_sets[_line.split('::')[0]]] += 1

        return feature_vector


