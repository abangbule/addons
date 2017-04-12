from openerp import models, fields, api, tools

class upload_pdf(models.Model):
	_inherit = "res.partner"

	data 	= fields.Binary('Upload CRF')
