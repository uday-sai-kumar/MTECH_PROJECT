#from androguard.misc import *
from warn.core.core import *
#from androguard_v2.core.analysis.analysis import *
from androguard_new.misc import *
#from androguard_new.misc import *
intent_methods = [
        [
            'Landroid/content/Intent', '<init>']]

# intent_methods = [
#         [
#             'Landroid/content/Intent', '<init>'],
#         [
#             'Landroid/content/Intent', 'setFlags'],
#         [
#             'Landroid/content/Intent', 'addFlags'],
#         [
#             'Landroid/content/Intent', 'putExtra'],
#         [
#             'Landroid/content/Intent', 'setDataAndType'],
#         [
#             'Landroid/content/IntentFilter', '<init>']]
apk_dir = "/Users/udaysaikumar/Documents/THESIS/CODES/DATASET/APKTOOl/0a0a78000e418ea28fa02e8c162c43396db6141ef8fe876db4027fef04bed663"
a, d, dx = AnalyzeAPK(apk_dir)
print(type(dx))
count = 0
for i in range(len(intent_methods)):
    methods = dx.find_methods()

    #methods = dx.find_methods(intent_methods[i][0], intent_methods[i][1])
    for _methods in methods:
         print(_methods.get_method().get_name())
         print(count+1)
         count= count+1
    count = 0
    #registers = data_flow_analysis(methods, dx)
    #registers = data_flow_analysis(methods, dx)
    # for _registers in registers:
    #     print(_registers)
