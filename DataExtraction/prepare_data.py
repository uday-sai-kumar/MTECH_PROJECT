from DataExtraction.manifest_parse import parse_manifest
from DataExtraction.dataflow_analysis import data_flow_result
from androguard.misc import AnalyzeAPK

apk_dir = "/Users/udaysaikumar/Documents/THESIS/CODES/DATASET/APKTOOl/0a0a78000e418ea28fa02e8c162c43396db6141ef8fe876db4027fef04bed663"
a, d, dx = AnalyzeAPK(apk_dir)

activities, permissions, receivers, services, providers, intent_filters = parse_manifest(a)

a1, a2, a3, a4, a5 = data_flow_result(dx)


f = open("/Users/udaysaikumar/Documents/THESIS/CODES/DATASET/APKTOOl/my_file.txt", "a")
for _x in activities:
    f.write("activity::"+_x+"\n")
for _x in permissions:
    f.write("permission::"+_x+"\n")
for _x in receivers:
    f.write("receiver::"+_x+"\n")
for _x in services:
    f.write("service::"+_x+"\n")
for _x in providers:
    f.write("provider::"+_x+"\n")
for _x in intent_filters:
    f.write("intent_filter::"+_x+"\n")
for _x in a1:
    f.write("api_connection::"+_x+"\n")
for _x in a2:
    f.write("api_content::"+_x+"\n")
for _x in a3:
    f.write("api_file::"+_x+"\n")
for _x in a4:
    f.write("api_intent::"+_x+"\n")
for _x in a5:
    f.write("api_data::"+_x+"\n")
f.close()
