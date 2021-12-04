import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import get_data, loger_pg
#from papa_pg import get_kabinet_rro_data


class Rro():

    def get_kabinet_rro_data(self):
        query = '''SELECT terminals.department,
    departments.post_index, departments.region, departments.district_region,
    departments.city, departments.street, departments.hous,
    departments.koatu, departments.tax_id,
    terminals.model, terminals.serial_number, terminals.soft,
    terminals.producer, terminals.date_manufacture,
    terminals.rne_rro, terminals.oro_serial, terminals.ticket_serial,
    otbor.term
    FROM otbor, terminals, departments
    WHERE otbor.term = terminals.termial
    AND departments.department = terminals.department
    ORDER BY terminals.termial;'''
        return get_data(query)



    def main_rro(self):
        self.info = ''
        data = self.get_kabinet_rro_data()

        for insert_data in data:
            insert_data = list(insert_data)
            if insert_data[2] == '':
                insert_data[2] = 'Київська'
            
            shablon =f"""<?xml version="1.0" encoding="windows-1251" standalone="no"?>
        <DECLAR xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="J1311402.xsd">
            <DECLARHEAD>
                <TIN>40243180</TIN>
                <C_DOC>J13</C_DOC>
                <C_DOC_SUB>114</C_DOC_SUB>
                <C_DOC_VER>2</C_DOC_VER>
                <C_DOC_TYPE>0</C_DOC_TYPE>
                <C_DOC_CNT>12</C_DOC_CNT>
                <C_REG>26</C_REG>
                <C_RAJ>50</C_RAJ>
                <PERIOD_MONTH>9</PERIOD_MONTH>
                <PERIOD_TYPE>1</PERIOD_TYPE>
                <PERIOD_YEAR>2019</PERIOD_YEAR>
                <C_STI_ORIG>2650</C_STI_ORIG>
                <C_DOC_STAN>1</C_DOC_STAN>
                <LINKED_DOCS xsi:nil="true"/>
                <D_FILL>04092019</D_FILL>
                <SOFTWARE>CABINET 0.4.1</SOFTWARE>
            </DECLARHEAD>
        <DECLARBODY>
        <HMN>1</HMN>
        <HR>1</HR>
        <HKSTI>2650</HKSTI>
        <HSTI>ГОЛОВНЕ УПРАВЛІННЯ ДФС У М.КИЄВІ, ДПІ У ГОЛОСІЇВСЬКОМУ РАЙОНІ (ГОЛОСІЇВСЬКИЙ РАЙОН М.КИЄВА)</HSTI>
        <HNAME>ТОВАРИСТВО З ОБМЕЖЕНОЮ ВIДПОВIДАЛЬНIСТЮ "ЕЛЕКТРУМ ПЕЙМЕНТ СІСТЕМ"</HNAME>
        <HTIN>40243180</HTIN>
        <T3RXXXXG1S ROWNUM="1">Відділення № {insert_data[0]}</T3RXXXXG1S>
        <T3RXXXXG2 ROWNUM="1">{insert_data[1]}</T3RXXXXG2>
        <T3RXXXXG3S ROWNUM="1">{insert_data[2]}</T3RXXXXG3S>
        <T3RXXXXG4S ROWNUM="1">{insert_data[3]}</T3RXXXXG4S>
        <T3RXXXXG5S ROWNUM="1">{insert_data[4]}</T3RXXXXG5S>
        <T3RXXXXG6S ROWNUM="1">{insert_data[5]}</T3RXXXXG6S>
        <T3RXXXXG7S ROWNUM="1">{insert_data[6]}</T3RXXXXG7S>
        <T3RXXXXG8S ROWNUM="1" xsi:nil="true"/>
        <T3RXXXXG9S ROWNUM="1" xsi:nil="true"/>
        <T3RXXXXG10S ROWNUM="1" xsi:nil="true"/>
        <T3RXXXXG11 ROWNUM="1">{insert_data[7]}</T3RXXXXG11>
        <T3RXXXXG12S ROWNUM="1">{insert_data[8]}</T3RXXXXG12S>
        <T3RXXXXG13 ROWNUM="1">2657</T3RXXXXG13>
        <T3RXXXXG13S ROWNUM="1">ГУ ДФС У М.КИЄВІ (СВЯТОШИНСЬКИЙ Р-Н М.КИЄВА)</T3RXXXXG13S>
        <R0401G1>458</R0401G1>
        <R0401G1S>{insert_data[9]}</R0401G1S>
        <R0402G1S>{insert_data[10]}</R0402G1S>
        <R0403G1>1088</R0403G1>
        <R0403G1S>{insert_data[11]}</R0403G1S>
        <R0404G1S>{insert_data[12]}</R0404G1S>
        <R0405G1D>{insert_data[13].replace('.', '')[:9]}</R0405G1D>
        <R0408G1S>{insert_data[14]}</R0408G1S>
        <R0501G1S>Торгівля. Громадське харчування. Сфера послуг.</R0501G1S>
        <R0601G1S>{insert_data[15]}</R0601G1S>
        <R0602G1>40</R0602G1>
        <R0603G1S>{insert_data[16]}</R0603G1S>
        <R0604G1>100</R0604G1>
        <R0701G1S>ТОВ "ПОС"</R0701G1S>
        <R0702G1S>39205324</R0702G1S>
        <R0703G1S>97</R0703G1S>
        <R0703G2D>01092016</R0703G2D>
        <R0703G3D>31122024</R0703G3D>
        <M04>1</M04>
        <R0901G1S>a.kulchitskiy@elpaysys.com</R0901G1S>
        <M05>1</M05>
        <HKBOS>2903722436</HKBOS>
        <HBOS>ПОЖАРСЬКИЙ ВЯЧЕСЛАВ ЮХИМОВИЧ</HBOS>
        <HFILL>{now_date_kabinet()}</HFILL>
        </DECLARBODY>
        </DECLAR>
        """

            ofname = KABINET_DIR + insert_data[0] + '_rro_' + insert_data[10] + '.xml'
            #print(ofname)
            text_to_file_cp1251(shablon, ofname)
            self.info += ofname + '\n'

        loger_pg('rro')

