"""переделачть чтобы читал из базы"""

import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 


from modules import *


vsyo_zapros = file_to_arr(IN_DATA_PATH + 'vsyo_zapros_vnesh_otbor.csv')
head = vsyo_zapros[0]
data = vsyo_zapros[1:]

for data_line in data:
    insert_data = vec_to_hash(head, data_line)
    
    shablon =f"""<?xml version="1.0" encoding="windows-1251" standalone="no"?>
<DECLAR xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="J1314804.xsd">
    <DECLARHEAD>
        <TIN>40243180</TIN>
        <C_DOC>J13</C_DOC>
        <C_DOC_SUB>148</C_DOC_SUB>
        <C_DOC_VER>4</C_DOC_VER>
        <C_DOC_TYPE>0</C_DOC_TYPE>
        <C_DOC_CNT>1498</C_DOC_CNT>
        <C_REG>26</C_REG>
        <C_RAJ>50</C_RAJ>
        <PERIOD_MONTH>2</PERIOD_MONTH>
        <PERIOD_TYPE>1</PERIOD_TYPE>
        <PERIOD_YEAR>2020</PERIOD_YEAR>
        <C_STI_ORIG>2650</C_STI_ORIG>
        <C_DOC_STAN>1</C_DOC_STAN>
        <LINKED_DOCS xsi:nil="true"/>
        <D_FILL>19112020</D_FILL>
        <SOFTWARE>CABINET 0.4.1</SOFTWARE>
    </DECLARHEAD>
  <DECLARBODY>
<HKSTI>2650</HKSTI>
<HSTI>ГОЛОВНЕ УПРАВЛІННЯ ДПС У М.КИЄВІ, ДПІ У ГОЛОСІЇВСЬКОМУ РАЙОНІ (ГОЛОСІЇВСЬКИЙ РАЙОН М.КИЄВА)</HSTI>
<HNAME>ТОВАРИСТВО З ОБМЕЖЕНОЮ ВIДПОВIДАЛЬНIСТЮ "ЕЛЕКТРУМ ПЕЙМЕНТ СІСТЕМ"</HNAME>
<HTIN>40243180</HTIN>
<R001G1S>{insert_data['fiscal_number']}</R001G1S>
<R002G1>458</R002G1>
<R002G1S>{insert_data['model']}</R002G1S>
<R003G1S>{insert_data['serial_number']}</R003G1S>
<R004G1>1088</R004G1>
<R004G1S>{insert_data['soft']}</R004G1S>
<T1RXXXXG11S ROWNUM="1">{insert_data['fiscal_number']}</T1RXXXXG11S>
<T1RXXXXG12S ROWNUM="1">{insert_data['oro_number']}</T1RXXXXG12S>
<T1RXXXXG2S ROWNUM="1">{insert_data['oro_serial']}</T1RXXXXG2S>
<T1RXXXXG31S ROWNUM="1">{insert_data['fiscal_number']}</T1RXXXXG31S>
<T1RXXXXG32S ROWNUM="1">{insert_data['ticket_number']}</T1RXXXXG32S>
<T1RXXXXG4S ROWNUM="1">{insert_data['ticket_serial']}</T1RXXXXG4S>
<R012G1S>відмова від КОРО</R012G1S>
<R013G1S>КОРО</R013G1S>
<M01>1</M01>
<HKBOS>2903722436</HKBOS>
<HBOS>ПОЖАРСЬКИЙ ВЯЧЕСЛАВ ЮХИМОВИЧ</HBOS>
<HFILL>{now_date_kabinet()}</HFILL>
</DECLARBODY>
</DECLAR>
"""

    ofname = KABINET_DIR + 'otmena_knigi_' + insert_data['fiscal_number'] + '_' + insert_data['serial_number'] + '.xml'
    #print(ofname)
    text_to_file_cp1251(shablon, ofname)

loger('otmena_knigi')
