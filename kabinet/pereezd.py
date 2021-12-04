import os.path, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) 

from modules import *
from papa_pg import get_data, loger_pg

class Pereezd():

    def get_pereezd_new_data(self):
            query = '''SELECT terminals.department,
        departments.post_index, departments.region,
        departments.city, departments.street, departments.hous,
        departments.koatu, departments.tax_id,
        terminals.model, terminals.serial_number, terminals.soft,
        terminals.producer, terminals.date_manufacture,
        terminals.rne_rro, terminals.fiscal_number, terminals.oro_serial, terminals.ticket_serial,
        terminals.to_rro, departments.district_city,
        otbor.term
        FROM otbor, terminals, departments
        WHERE otbor.term = terminals.termial
        AND departments.department = terminals.department
        ORDER BY terminals.termial;'''
            return get_data(query)


    def main_pereezd(self):
        data = self.get_pereezd_new_data()
        self.info = ''
        for u in data:
            koatu2 = mk_koatu2(u[3], u[17], u[6])
            u = list(u)
            if u[2] == '':
                u[2] = 'Київська'
            
            shablon =f"""<?xml version="1.0" encoding="windows-1251" standalone="no"?>
        <DECLAR xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="J1311405.xsd">
            <DECLARHEAD>
                <TIN>40243180</TIN>
                <C_DOC>J13</C_DOC>
                <C_DOC_SUB>114</C_DOC_SUB>
                <C_DOC_VER>5</C_DOC_VER>
                <C_DOC_TYPE>0</C_DOC_TYPE>
                <C_DOC_CNT>4</C_DOC_CNT>
                <C_REG>26</C_REG>
                <C_RAJ>50</C_RAJ>
                <PERIOD_MONTH>12</PERIOD_MONTH>
                <PERIOD_TYPE>1</PERIOD_TYPE>
                <PERIOD_YEAR>2021</PERIOD_YEAR>
                <C_STI_ORIG>2650</C_STI_ORIG>
                <C_DOC_STAN>1</C_DOC_STAN>
                <LINKED_DOCS>
            <DOC NUM="1" TYPE="1">
                <C_DOC>J13</C_DOC>
                <C_DOC_SUB>601</C_DOC_SUB>
                <C_DOC_VER>2</C_DOC_VER>
                <C_DOC_TYPE>0</C_DOC_TYPE>
                <C_DOC_CNT>4</C_DOC_CNT>
                <C_DOC_STAN>1</C_DOC_STAN>
                <FILENAME>26500040243180J1360102100000000411220212650.XML</FILENAME>
            </DOC>
            </LINKED_DOCS>
                <D_FILL>01122021</D_FILL>
                <SOFTWARE>CABINET 0.5.0</SOFTWARE>
            </DECLARHEAD>
        <DECLARBODY>
        <HMN>1</HMN>
        <HPR>1</HPR>
        <H01G1S>переїзд</H01G1S>
        <HKSTI>2650</HKSTI>
        <HSTI>ГОЛОВНЕ УПРАВЛІННЯ ДФС У М.КИЄВІ, ДПІ У ГОЛОСІЇВСЬКОМУ РАЙОНІ (ГОЛОСІЇВСЬКИЙ РАЙОН М.КИЄВА)</HSTI>
        <HNAME>ТОВАРИСТВО З ОБМЕЖЕНОЮ ВIДПОВIДАЛЬНIСТЮ "ЕЛЕКТРУМ ПЕЙМЕНТ СІСТЕМ"</HNAME>
        <HTIN>40243180</HTIN>
        <T3RXXXXG1S ROWNUM="1">Відділення № {u[0]}</T3RXXXXG1S>
        <T3RXXXXG2 ROWNUM="1">{u[1]}</T3RXXXXG2>
        <T3RXXXXG3S ROWNUM="1">{u[2]}</T3RXXXXG3S>
        <T3RXXXXG4S ROWNUM="1" xsi:nil="true"/>
        <T3RXXXXG5S ROWNUM="1">{u[3]}</T3RXXXXG5S>
        <T3RXXXXG6S ROWNUM="1">{u[4]}</T3RXXXXG6S>
        <T3RXXXXG7S ROWNUM="1">{u[5]}</T3RXXXXG7S>
        <T3RXXXXG8S ROWNUM="1" xsi:nil="true"/>
        <T3RXXXXG9S ROWNUM="1" xsi:nil="true"/>
        <T3RXXXXG10S ROWNUM="1" xsi:nil="true"/>
        <T3RXXXXG11 ROWNUM="1">{u[6]}</T3RXXXXG11>
        <T3RXXXXG11S ROWNUM="1">{koatu2}</T3RXXXXG11S>
        <T3RXXXXG12S ROWNUM="1">{u[7]}</T3RXXXXG12S>
        <T3RXXXXG13 ROWNUM="1">1716</T3RXXXXG13>
        <T3RXXXXG13S ROWNUM="1">ГУ ДПС У РІВНЕНСЬКІЙ ОБЛАСТІ ( М.РІВНЕ)</T3RXXXXG13S>
        <R0401G1>420</R0401G1>
        <R0401G1S>{u[8]}</R0401G1S>
        <R0402G1S>{u[9]}</R0402G1S>
        <R0403G1>1256</R0403G1>
        <R0403G1S>{u[10]}</R0403G1S>
        <R0404G1S>{u[11]}</R0404G1S>
        <R0405G1D>25042018</R0405G1D>
        <R0408G1S>{u[12]}</R0408G1S>
        <R0409G1S>{u[13]}</R0409G1S>
        <R0501G1S>Торгівля. Громадське харчування. Сфера послуг.</R0501G1S>
        <R0601G1S>{u[14]}</R0601G1S>
        <R0602G1>40</R0602G1>
        <R0603G1S>{u[15]}</R0603G1S>
        <R0604G1>100</R0604G1>
        <R0701G1S>{u[16]}</R0701G1S>
        <R0702G1S>39205324</R0702G1S>
        <R0703G1S>97</R0703G1S>
        <R0703G2D>01092016</R0703G2D>
        <R0703G3D>31122024</R0703G3D>
        <M07>1</M07>
        <M05>1</M05>
        <HKBOS>2903722436</HKBOS>
        <HBOS>ПОЖАРСЬКИЙ ВЯЧЕСЛАВ ЮХИМОВИЧ</HBOS>
        <HFILL>{now_date_kabinet()}</HFILL>
        </DECLARBODY>
        </DECLAR>"""

            ofname = KABINET_DIR + u[0] + '_pereezd_' + u[9] + '.xml'
            self.info += f'{ofname}\n'
            text_to_file_cp1251(shablon, ofname)


        loger_pg('pereezd')

