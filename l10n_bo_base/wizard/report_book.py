import xlwt
import base64
from io import StringIO
from odoo import models, fields


class ReportBookExcel(models.TransientModel):
    _name = 'report.account.excel'
    _description = 'report journal '

    excel_data = fields.Char('Name', size=256)
    file_name = fields.Binary('Employee Check Excel Report', readonly=True)


class ReporBook(models.TransientModel):
    _name = 'report.account'
    _description = 'Report de ventas '

    initial_date = fields.Date(
         string='Initial Date',
         required=True

    )

    final_date = fields.Date(
        string='Fecha Final',
        required=True
    )

    journal_ids = fields.Many2many(
        string='Employees',
        comodel_name='account.journal'
    )
    def generate_report_xlsx(self):
        # XLS report

        cols = ["ESPECIFICACION",#0
                "Nº",#1
                "FECHA DE LA FACTURA",#2
                "Nº DE LA FACTURA",#3
                "NºDE AUTORIZACION",#4
                "ESTADO",#5
                "NIT/CI CLIENTE",#6
                "NOMBRE O RAZON SOCIAL",#7
                "IMPORTE TOTAL DE LA VENTA",#8
                "IMPORTE ICE/IEHD/IPJ/TASAS/OTROS NO SUJETOS AL IVA",#9
                "EXPORTACIONES Y OPERACIONES EXENTAS",#10
                "VENTAS GRAVADAS A TASA CERO ",#11
                "SUB TOTAL",#12
                "DESCUENTOS, BONIFICACIONES Y REBAJAS SUJETAS AL IVA",#13
                "IMPORTE BASE PARA DEBITO FISCAL",#14
                "DEBITO FISCAL",#15
                "CODIGO DE CONTROL"]#16

        workbook = xlwt.Workbook()
        sheet = workbook.add_sheet("Planilla de Colaboradores")

        style_title = xlwt.easyxf(
            'pattern: pattern solid, fore_colour white;'
            'align: vertical center, horizontal center;'
            'font: name Calibri, bold on, height 280;'
        )

        style_sub_title = xlwt.easyxf(
            'pattern: pattern solid, fore_colour white;'
            'align: vertical center, horizontal center;'
            'font: name Calibri, bold on, height 180;'
        )

        style_columns = xlwt.easyxf(
            'pattern: pattern solid, fore_colour white;'
            'borders: left thin, right thin, top thin,bottom thin;'
            'align: vertical center, horizontal center;'
            'font: name Calibri, bold on, height 180;'
        )


        style5 = xlwt.easyxf('font: name Times New Roman bold on;align: horiz left;', num_format_str='#,##0')

##contenido
        sheet.write_merge(0, 0, 0, 0, cols[0] ,style_columns )
        sheet.write_merge(0, 0, 1, 1, cols[1] ,style_columns )
        sheet.write_merge(0, 0, 2, 2, cols[2] ,style_columns )
        sheet.write_merge(0, 0, 3, 3, cols[3] ,style_columns )
        sheet.write_merge(0, 0, 4, 4, cols[4] ,style_columns )
        sheet.write_merge(0, 0, 5, 5, cols[5] ,style_columns )
        sheet.write_merge(0, 0, 6, 6, cols[6] ,style_columns )
        sheet.write_merge(0, 0, 7, 7, cols[7] ,style_columns )
        sheet.write_merge(0, 0, 8, 8, cols[8] ,style_columns )
        sheet.write_merge(0, 0, 9, 9, cols[9] ,style_columns )
        sheet.write_merge(0, 0, 10, 10, cols[10] ,style_columns )
        sheet.write_merge(0, 0, 11, 11, cols[11] ,style_columns )
        sheet.write_merge(0, 0, 12, 12, cols[12] ,style_columns )
        sheet.write_merge(0, 0, 13, 13, cols[13] ,style_columns )
        sheet.write_merge(0, 0, 14, 14, cols[14] ,style_columns )
        sheet.write_merge(0, 0, 15, 15, cols[15] ,style_columns )
        sheet.write_merge(0, 0, 16, 16, cols[16], style_columns)

        fila_init = 0
        account_move_sale_lines_obj = self.env['account.move']
        account_journal_obj = self.env['account.journal']

        list_journal_ids = []
        for p in self.journal_ids:
            list_journal_ids.append(p.id)
        if len(list_journal_ids) == 0:
            journal_all = account_journal_obj.search([])
            for p in journal_all:
                list_journal_ids.append(p.id)

        seq = 0
        account_move_sale_ids = account_move_sale_lines_obj.search([
            ('date', '>=', self.initial_date),
            ('date', '<=', self.final_date),
            ('journal_id', 'in', list_journal_ids)
        ])

        seq +=1
        for o in account_move_sale_ids:

            # sheet.write_merge(fila_init + 1, fila_init + 1, 0, 0, o.name, style_sub_title)
            sheet.write_merge(fila_init + 1, fila_init + 1, 1, 1, seq or '', style_sub_title)
            sheet.write_merge(fila_init + 1, fila_init + 1, 2, 2, o.invoice_date or '--', style_sub_title)
            sheet.write_merge(fila_init + 1, fila_init + 1, 3, 3, o.name or '', style_sub_title)
            sheet.write_merge(fila_init + 1, fila_init + 1, 4, 4, o.authorization_number or '',style_sub_title)
            sheet.write_merge(fila_init + 1, fila_init + 1, 5, 5, o.state or '', style_sub_title)
            sheet.write_merge(fila_init + 1, fila_init + 1, 6, 6, o.nit or '--', style_sub_title)
            sheet.write_merge(fila_init + 1, fila_init + 1, 7, 7, o.razonsocial or '--', style_sub_title)
            sheet.write_merge(fila_init + 1, fila_init + 1, 8, 8, o.amount_total or '--',style_sub_title)
            # sheet.write_merge(fila_init + 1, fila_init + 1, 9, 9, total_hours_worked, style_sub_title)
            # sheet.write_merge(fila_init + 1, fila_init + 1, 10, 10, total_hours, style_sub_title)
            # sheet.write_merge(fila_init + 1, fila_init + 1, 10, 10, total_hours, style_sub_title)
            sheet.write_merge(fila_init + 1, fila_init + 1, 12, 12, o.amount_residual, style_sub_title)
            sheet.write_merge(fila_init + 1, fila_init + 1, 13, 13, o.invoice_line_ids.discount, style_sub_title)
            # sheet.write_merge(fila_init + 1, fila_init + 1, 13, 13, o.invoice_line_ids.discount, style_sub_title)
            # sheet.write_merge(fila_init + 1, fila_init + 1, 13, 13, o.invoice_line_ids.discount, style_sub_title)
            sheet.write_merge(fila_init + 1, fila_init + 1, 16, 16, o.control_code, style_sub_title)

        output = StringIO()
        # output=io.BytesIO()
        output.write("\n")

        filename = ('/tmp/Reporte de libro ' + '.xls')
        workbook.save(filename)
        fp = open(filename, "rb")
        file_data = fp.read()
        out = base64.encodestring(file_data)

        # Files actions
        attach_vals = {
            'excel_data': 'Reporte_De_Libro' + '.xls',
            'file_name': out

        }

        act_id = self.env['report.account.excel'].create(attach_vals)
        fp.close()

        return {
        'type': 'ir.actions.act_window',
        'res_model': 'report.account.excel',
        'res_id': act_id.id,
        'view_type': 'form',
        'view_mode': 'form',
        'context': self.env.context,
        'target': 'new',
        }


