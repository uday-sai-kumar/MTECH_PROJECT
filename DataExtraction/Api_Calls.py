from androguard.misc import *

def get_api_calls(path):
    apk, dalvik, analysis = AnalyzeAPK(path)
    # print(apk.get_receivers())
    # print(analysis.get_classes())
    external_classes = analysis.get_external_classes()
    methods = []
    for i in external_classes:
        class_name = i.get_vm_class()
        methods_list = class_name.get_methods()
        for method in methods_list:
            a = '%s' % method.get_class_name()
            b = '%s' % method.get_name()
            c = '%s' % method.get_descriptor() #(function arguments) return_type
            print(a +' ---- '+ b +' --- ' + c)

            # methods.append(a.rstrip(';') + '.' + b + c)

    return list(set(methods))




APK_PATH = '/Users/udaysaikumar/Documents/THESIS/CODES/DATASET/APKTOOl/0a0a78000e418ea28fa02e8c162c43396db6141ef8fe876db4027fef04bed663'
print(get_api_calls(APK_PATH))



