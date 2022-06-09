from warn.core.core import *
from androguard.misc import *

def detect_connection(x):
    """
    :param x:  a VMAnalysis instance
    :return:   a formatted strings
    """
    formatted_str = [
     'Ljava/net/InetSocketAddress.<init>[Detected remote address and IP port]']
    local_formatted_str = []
    connection_methods = [['Ljava/net/Socket', '<init>'], ['Ljava/net/InetSocketAddress', 'Ljava/net/InetSocketAddress'] ]
    for i in range(len(connection_methods)):
        structural_analysis_results = x.find_methods(connection_methods[i][0], connection_methods[i][1], '.')
        # returns methods analysis object
        # print('outside')
        # _map = map(lambda x: x.get_method(), x.find_methods(classname='Ljava/net/InetSocketAddress', methodname='Ljava/net/InetSocketAddress'))
        # print(list(_map))
        #print(type(structural_analysis_results))
        # structural_analysis_results = x.tainted_packages.search_methods(connection_methods[i][0], connection_methods[i][1], '.')
       # for result in range(len(structural_analysis_results)):
        registers = data_flow_analysis(structural_analysis_results, x)
        for _registers in registers:
            #print('hi')
            #print(type(_registers))
            if len(_registers) >= 2:
                #print(_registers)
                remote_address = get_register_value(1, _registers)
                remote_port = get_register_value(2, _registers)
                local_formatted_str.append("remote address '%s' on the '%s' port " % (remote_address, remote_port))

    if local_formatted_str != []:
        return formatted_str
    else:
        return []

def get_content_parameter(x):
    """
    @:param x : a list of registers relating file parameter value
    @:rtype : a list of file api calls including parameter value
    """
    value_option = ('content://sms-mms', 'content://sms', 'content://telephony', 'content://calendar',
                    'content://browser/bookmarks', 'content://calllog', 'content://mail',
                    'content://downloads')
    value = []
    for i in range(len(x)):
        parameter = get_register_value(i, x)
        for j in range(len(value_option)):
            if value_option[j] in parameter:
                value.append(value_option[j])

    return value

def detect_content(x):

    formatted_str = []
    content_apis = [
     [
      'Landroid/content/ContentResolver', 'query'], ['Landroid/content/ContentResolver', 'insert'], ['Landroid/content/ContentResolver', 'update']]
    for i in range(len(content_apis)):
        structural_analysis_results = x.find_methods(content_apis[i][0], content_apis[i][1], '.')
        #for results in range(len(structural_analysis_results)):
        registers = data_flow_analysis(structural_analysis_results, x)
        for _registers in registers:
            parameter_value = get_content_parameter(_registers)
            if parameter_value != []:
                [formatted_str.append(content_apis[i][0] + '.' + content_apis[i][1] + '[' + j + ']') for j in
                 parameter_value]
        return list(set(formatted_str))

def get_file_parameter(x):
    """
        @:param x : a list of registers relating file parameter value
        @:rtype : a list of file api calls including parameter value
        """
    value_option = ('su', 'ls', 'loadjar', 'grep', '/sh', '/bin', 'pm install', '/dev/net',
                    'insmodrm', 'mount', 'root', '/system', 'stdout', 'reboot', 'killall',
                    'chmod', 'stderr', 'sdcard', 'imei', 'Imei', '.exe', '.sh', 'jar',
                    'zip', '\\u', 'query', 'http', 'https')
    value = []
    for i in range(len(x)):
        parameter = get_register_value(i, x)
        for j in range(len(value_option)):
            if value_option[j] in parameter:
                value.append(value_option[j])

    return value

def detect_file(x):
    formatted_str = []
    file_apis = [
     [
      'Ljava/io/File', '<init>'],
     [
      'Ljava/util/stream/Stream', '<init>'],
     [
      'Ljava/lang/StringBuilder', '<init>'],
     [
      'Ljava/lang/String', '<init>'],
     [
      'Ljava/lang/StringBuffer', '<init>'],
     [
      'Ljava/lang/StringBuilder', 'append'],
     [
      'Ljava/lang/String', 'append'],
     [
      'Ljava/lang/StringBuffer', 'append'],
     [
      'Ljava/lang/StringBuilder', 'indexOf'],
     [
      'Ljava/lang/String', 'indexOf'],
     [
      'Ljava/lang/StringBuffer', 'indexOf'],
     [
      'Ljava/lang/StringBuilder', 'substring'],
     [
      'Ljava/lang/String', 'substring'],
     [
      'Ljava/lang/StringBuffer', 'substring']]
    for i in range(len(file_apis)):
        structural_analysis_results = x.find_methods(file_apis[i][0], file_apis[i][1], '.')
        registers = data_flow_analysis(structural_analysis_results, x)
        for _registers in registers:
            parameter_value = get_file_parameter(_registers)
            if parameter_value != []:
                [formatted_str.append(file_apis[i][0] + '.' + file_apis[i][1] + '[' + j + ']') for j in parameter_value]

    return list(set(formatted_str))


def get_intent_parameter(x):
    """
    @:param x : a list of registers relating Intent parameter value
    @:rtype : a list of intent api calls including parameter value
    """
    value_option = ('CALL', 'CONNECTIVITY', 'SEND', 'SENDTO', 'BLUETOOTH')
    value = []
    for i in range(len(x)):
        parameter = get_register_value(i, x)
        for j in range(len(value_option)):
            if value_option[j] in parameter:
                value.append(value_option[j])

    return value


def detect_intent(x):
    """
    :param x: a VMAnalysis instance
    :return:  a list of formatted strings
    """
    formatted_str = []
    intent_methods = [
     [
      'Landroid/content/Intent', '<init>'],
     [
      'Landroid/content/Intent', 'setFlags'],
     [
      'Landroid/content/Intent', 'addFlags'],
     [
      'Landroid/content/Intent', 'putExtra'],
     [
      'Landroid/content/Intent', 'setDataAndType'],
     [
      'Landroid/content/IntentFilter', '<init>']]
    for i in range(len(intent_methods)):
        #print(intent_methods[i][0], ' ---- > ', intent_methods[i][1])
        structural_analysis_results = x.find_methods(intent_methods[i][0], intent_methods[i][1])
        registers = data_flow_analysis(structural_analysis_results, x)
        for _register in registers:
            #print('intent register value is ', _register)
            parameter_value = get_intent_parameter(_register)
            if parameter_value != []:
                [formatted_str.append(intent_methods[i][0] + '.' + intent_methods[i][1] + '[' + j + ']') for j in
                 parameter_value]


    return list(set(formatted_str))

def detect_data(x):
    formatted_str = []

    data_apis = [
     [
      'Ljava/io/DataInputStream', '<init>'],
     [
      'Ljava/io/DataOutputStream', '<init>'],
     [
      'Ljava/io/BufferedReader', '<init>'],
     [
      'Ljava/io/DataInputStream', 'writeBytes'],
     [
      'Ljava/io/DataInputStream', 'writeBytes'],
     [
      'Ljava/io/BufferedReader', 'writeBytes']]
    for i in range(len(data_apis)):
        structural_analysis_results = x.find_methods(data_apis[i][0], data_apis[i][1], '.')
        registers = data_flow_analysis(structural_analysis_results, x)
        for _register in registers:
            parameter_value = get_file_parameter(_register)
            if parameter_value != []:
                [ formatted_str.append(data_apis[i][0] + '.' + data_apis[i][1] + '[' + j + ']') for j in parameter_value ]

    return list(set(formatted_str))


def data_flow_result(dx):

    #a, d, dx = AnalyzeAPK(dx)
    a1 = detect_connection(dx)
    a2 = detect_content(dx)
    a3 = detect_file(dx)
    a4 = detect_intent(dx)
    a5 = detect_data(dx)
    #
    # print(a1)
    # print('connection ')
    # print(a2)
    # print('detect content')
    # print(a3)
    # print('detected file')
    # print(a4)
    # print('detect intent')
    # print(a5)
    # print('detect data')
    # result = a1 + a2 + a3 + a4 + a5
    return a1, a2, a3, a4, a5


if __name__ == '__main__':
    apk_dir = "/Users/udaysaikumar/Documents/THESIS/CODES/DATASET/APKTOOl/0a0a78000e418ea28fa02e8c162c43396db6141ef8fe876db4027fef04bed663"

    #apk_dir = 'SampleApplication.apk'
    print(data_flow_result(apk_dir))
