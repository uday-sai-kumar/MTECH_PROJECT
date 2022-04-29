from androguard.core.bytecodes.apk import *
from androguard.core.bytecodes.dvm import *
from warn.analysis.analysis import *
from androguard.misc import *

# def AnalyzeAPK(filename, raw=False, decompiler=None):
#     """
#                 Analyze an android application and setup all stuff for a more quickly analysis !
#
#                 @param filename : the filename of the android application or a buffer which represents the application
#                 @param raw : True is you would like to use a buffer
#                 @param decompiler : ded, dex2jad, dad or None for smali dump only
#
#                 @rtype : return the APK, DalvikVMFormat, and VMAnalysis objects
#         """
#     a = APK(filename, raw)
#     d, dx = AnalyzeDex(a.get_dex(), raw=True)
#     return (
#         a, d, dx)
#
#
# def AnalyzeDex(filename, raw=False):
#     """
#                 Analyze an android dex file and setup all stuff for a more quickly analysis !
#
#                 @param filename : the filename of the android dex file or a buffer which represents the dex file
#                 @param raw : True is you would like to use a buffer
#
#                 @rtype : return the DalvikVMFormat, and VMAnalysis objects
#         """
#     d = None
#     if raw == False:
#         d = DalvikVMFormat(open(filename, 'r').read())
#     else:
#         d = DalvikVMFormat(filename)
#     dx = VMAnalysis(d)
#     d.set_vmanalysis(dx)
#     return (
#         d, dx)



def detect_connection(x):
    """
    :param x:  a VMAnalysis instance
    :return:   a formatted strings
    """
    print(type(x))
    formatted_str = [
     'Ljava/net/InetSocketAddress.<init>[Detected remote address and IP port]']
    local_formatted_str = []
    connection_methods = [['Ljava/net/Socket', '<init>'], ['Ljava/net/InetSocketAddress', 'Ljava/net/InetSocketAddress']]
    for i in range(len(connection_methods)):
        structural_analysis_results = x.find_methods(classname=connection_methods[i][0], methodname=connection_methods[i][1])
        print(i)
        print( structural_analysis_results)
        # structural_analysis_results = x.tainted_packages.search_methods(connection_methods[i][0], connection_methods[i][1], '.')
        # for result in range(len(structural_analysis_results)):
        #     registers = data_flow_analysis(structural_analysis_results, x)
        #     if len(registers) >= 2:
        #         remote_address = get_register_value(1, registers)
        #         remote_port = get_register_value(2, registers)
        #         local_formatted_str.append("remote address '%s' on the '%s' port " % (remote_address, remote_port))

    if local_formatted_str != []:
        return formatted_str
    else:
        return []


def data_flow_result(x):
    result = []
    a, d, dx = AnalyzeAPK(x)
    a1 = detect_connection(dx)

    print(a1)

    result = a1
    return result


if __name__ == '__main__':
    apk_dir = "/Users/udaysaikumar/Documents/THESIS/CODES/DATASET/APKTOOl/0a0a78000e418ea28fa02e8c162c43396db6141ef8fe876db4027fef04bed663"
    #apk_dir = 'SampleApplication.apk'
    print(data_flow_result(apk_dir))
