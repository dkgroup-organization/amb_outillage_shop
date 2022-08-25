# -*- coding: utf-8 -*-
# from odoo import http


# class DkgAmbCustom(http.Controller):
#     @http.route('/dkg_amb_custom/dkg_amb_custom/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dkg_amb_custom/dkg_amb_custom/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dkg_amb_custom.listing', {
#             'root': '/dkg_amb_custom/dkg_amb_custom',
#             'objects': http.request.env['dkg_amb_custom.dkg_amb_custom'].search([]),
#         })

#     @http.route('/dkg_amb_custom/dkg_amb_custom/objects/<model("dkg_amb_custom.dkg_amb_custom"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dkg_amb_custom.object', {
#             'object': obj
#         })
