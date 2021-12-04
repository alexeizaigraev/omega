import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
#from modules_base import *
from papa_pg import get_data, loger_pg


class Knigi():

    def get_kabinet_knigi_data(self):
        query = '''SELECT terminals.fiscal_number, terminals.model, terminals.serial_number,
    terminals.soft, terminals.rne_rro, terminals.department,
    departments.address, departments.koatu, departments.tax_id,
    terminals.oro_number, terminals.oro_serial,
    otbor.term
    FROM otbor, terminals, departments
    WHERE otbor.term = terminals.termial
    AND departments.department = terminals.department
    ORDER BY terminals.termial;'''
        return get_data(query)

    def knigi_main(self):
        info = ''
        data = self.get_kabinet_knigi_data()

        for insert_data in data:
            shablon =f"""<?xml version="1.0" encoding="windows-1251" standalone="no"?>
        <DECLAR xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="J1311302.xsd">
            <DECLARHEAD>
                <TIN>40243180</TIN>
                <C_DOC>J13</C_DOC>
                <C_DOC_SUB>113</C_DOC_SUB>
                <C_DOC_VER>2</C_DOC_VER>
                <C_DOC_TYPE>0</C_DOC_TYPE>
                <C_DOC_CNT>242</C_DOC_CNT>
                <C_REG>26</C_REG>
                <C_RAJ>50</C_RAJ>
                <PERIOD_MONTH>8</PERIOD_MONTH>
                <PERIOD_TYPE>1</PERIOD_TYPE>
                <PERIOD_YEAR>2019</PERIOD_YEAR>
                <C_STI_ORIG>2650</C_STI_ORIG>
                <C_DOC_STAN>1</C_DOC_STAN>
                <LINKED_DOCS xsi:nil="true"/>
                <D_FILL>29082019</D_FILL>
                <SOFTWARE>CABINET</SOFTWARE>
            </DECLARHEAD>
        <DECLARBODY>
        <HKORO>1</HKORO>
        <HR>1</HR>
        <HKSTI>2650</HKSTI>
        <HSTI>ГОЛОВНЕ УПРАВЛІННЯ ДФС У М.КИЄВІ, ДПІ У ГОЛОСІЇВСЬКОМУ РАЙОНІ (ГОЛОСІЇВСЬКИЙ РАЙОН М.КИЄВА)</HSTI>
        <HNAME>ТОВАРИСТВО З ОБМЕЖЕНОЮ ВIДПОВIДАЛЬНIСТЮ "ЕЛЕКТРУМ ПЕЙМЕНТ СІСТЕМ"</HNAME>
        <HTIN>40243180</HTIN>
        <R0301G1S>{insert_data[0]}</R0301G1S>
        <R0302G1>420</R0302G1>
        <R0302G1S>{insert_data[1]}</R0302G1S>
        <R0303G1S>{insert_data[2]}</R0303G1S>
        <R0304G1>1014</R0304G1>
        <R0304G1S>{insert_data[3]}</R0304G1S>
        <R0307G1S>{insert_data[4]}</R0307G1S>
        <R0401G1S>Відділення №{insert_data[5]}</R0401G1S>
        <R0402G1S>{insert_data[6]}</R0402G1S>
        <R0403G1>{insert_data[7]}</R0403G1>
        <R0404G1S>{insert_data[8]}</R0404G1S>
        <R0501G1>832</R0501G1>
        <R0501G1S>ГУ ДПС У ЧЕРНІГІВСЬКІЙ ОБЛАСТІ</R0501G1S>
        <R0601G1S>{insert_data[0]}</R0601G1S>
        <R0601G2S>{insert_data[9]}</R0601G2S>
        <R0602G1S>{insert_data[10]}</R0602G1S>
        <R0603G1>40</R0603G1>
        <M01>1</M01>
        <HKBOS>2903722436</HKBOS>
        <HBOS>ПОЖАРСЬКИЙ ВЯЧЕСЛАВ ЮХИМОВИЧ</HBOS>
        <HFILL>{now_date_kabinet()}</HFILL>
        <HZ>1</HZ>
            <HZM>7</HZM>
            <HMONTH>7</HMONTH>
            <HZY>2019</HZY>
        </DECLARBODY>
        </DECLAR>"""

            ofname = KABINET_DIR + insert_data[-1] + '_knigi_' + insert_data[2] + '.xml'
            #print(ofname)
            info += text_to_file_cp1251(shablon, ofname) + '\n'
            self.info = info

        #loger_pg('knigi')