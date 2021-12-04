from modules import file_to_arr



def mk_vsyo_zapros():
    
    otbor = file_to_arr(IN_DATA_PATH + 'otbor.csv')[1:]
    otbor_objects = []
    for line in otbor:
        otbor_objects.append(line[0])
    
    otbor = otbor_objects
    print(otbor)
    
    vsyo = file_to_arr(IN_DATA_PATH + 'vsyo_zapros.csv')
    head = ';'.join(vsyo[0]) + '\n'
    text = head
    for vsyo_line in vsyo:
        if vsyo_line[1] in otbor:
            text += ';'.join(vsyo_line) + '\n'
            print(vsyo_line)
        
    text_to_file(text, IN_DATA_PATH + 'vsyo_zapros_vnesh_otbor.csv')


def vec_to_hash(head, vec):
    d = dict()
    try:
        for i in range(len(head)):
            d[head[i]] = vec[i]
    except:
        #print('>> err ', vec)
        pass
    return d

def arr_to_hash(arr, key_col_num):
    #arr = clear_arr(arr)
    head = arr[0]
    
    h_arr = dict()
    for vec in arr[1:]:
        try:
            h_arr[vec[key_col_num]] = vec_to_hash(head, vec)
        except:
            #print('>> err ', vec)
            pass
    return h_arr
    
def file_to_hash(fname, key):
    a = file_to_arr(fname)
    return arr_to_hash(a, key)

def col_key(hh, mykey):
    os.system('cls')
    print('\n\n')
    s = set()
    for key in hh:
        try:
            line = hh[key]
            s.add(line[mykey])
        except:
            #('>> no key', key)
            pass
    
    listkey = list(s)
    for i in range(len(listkey)):
        if not listkey[i]:
            continue
        p_cyan(f'\t{i} {listkey[i]}')
    
    #print('')
    print('\n\n\n -> ', end = '')
    choise = int(input())
    os.system('cls')
    
    return listkey[choise]
        
        
        


