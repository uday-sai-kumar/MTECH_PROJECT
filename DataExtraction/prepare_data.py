from DataExtraction.manifest_parse import parse_manifest
from DataExtraction.dataflow_analysis import data_flow_result
from androguard_new.misc import AnalyzeAPK
import os


#directory ="/Users/udaysaikumar/Documents/THESIS/CODES/DATASET/"
directory = ["/Users/udaysaikumar/Desktop/AZOO/APPS/", "/Users/udaysaikumar/Desktop/AZOO/APPS1/", "/Users/udaysaikumar/Desktop/AZOO/APPS2/"]
#directory =["/Users/udaysaikumar/Documents/THESIS/CODES/DATASET/MalwareSet/drebin-0/","/Users/udaysaikumar/Documents/THESIS/CODES/DATASET/MalwareSet/drebin-1/","/Users/udaysaikumar/Documents/THESIS/CODES/DATASET/MalwareSet/drebin-2½","/Users/udaysaikumar/Documents/THESIS/CODES/DATASET/MalwareSet/drebin-4","/Users/udaysaikumar/Documents/THESIS/CODES/DATASET/MalwareSet/drebin-5","/Users/udaysaikumar/Documents/THESIS/CODES/DATASET/MalwareSet/drebin-33⅓"]
#feature_directory = "/Users/udaysaikumar/Documents/THESIS/CODES/DATASET/My_Features/"
feature_directory = ["/Users/udaysaikumar/Desktop/benignmalwarefiles/a_1/", "/Users/udaysaikumar/Desktop/benignmalwarefiles/a_2/", "/Users/udaysaikumar/Desktop/benignmalwarefiles/a_3/"]
f = None
#lst = ['0a0a78000e418ea28fa02e8c162c43396db6141ef8fe876db4027fef04bed663']
for i in range(3):
    lst = os.listdir(directory[i])
    lst.sort()
    for file_name in lst:
        #print(file_name)
        apk_dir = directory[i]+file_name
        try:
            f = open(feature_directory[i] + file_name, "w")
            a, d, dx = AnalyzeAPK(apk_dir)
            activities, permissions, receivers, services, providers, intent_filters = parse_manifest(a)
            a1, a2, a3, a4, a5 = data_flow_result(dx)
            for _x in activities:
                f.write("activity::" + _x + "\n")
            for _x in permissions:
                f.write("permission::" + _x + "\n")
            for _x in receivers:
                f.write("receiver::" + _x + "\n")
            for _x in services:
                f.write("service::" + _x + "\n")
            for _x in providers:
                f.write("provider::" + _x + "\n")
            for _x in intent_filters:
                f.write("intent_filter::" + _x + "\n")
            for _x in a1:
                f.write("api_connection::" + _x + "\n")
            for _x in a2:
                f.write("api_content::" + _x + "\n")
            for _x in a3:
                f.write("api_file::" + _x + "\n")
            for _x in a4:
                f.write("api_intent::" + _x + "\n")
            for _x in a5:
                f.write("api_data::" + _x + "\n")
            f.close()
        except Exception as e:
            print('####', file_name,'####')
            try:
                f.close()
                os.remove(feature_directory[i] + file_name)
            except Exception as ee:
                print(ee)







