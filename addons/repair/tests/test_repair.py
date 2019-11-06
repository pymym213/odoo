# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from datetime import datetime

from odoo.addons.account.tests.account_test_classes import AccountingTestCase
from odoo.tests import tagged


@tagged('post_install', '-at_install')
class TestRepair(AccountingTestCase):

    @classmethod
    def setUpClass(cls):
        super(TestRepair, cls).setUpClass()

        # Partners
        cls.res_partner_1 = cls.env['res.partner'].create({'name': 'Wood Corner'})
        cls.res_partner_address_1 = cls.env['res.partner'].create({'name': 'Willie Burke', 'parent_id': cls.res_partner_1.id})
        cls.res_partner_12 = cls.env['res.partner'].create({'name': 'Partner 12'})

        # Products
        cls.product_product_3 = cls.env['product.product'].create({'name': 'Desk Combination'})
        cls.product_product_11 = cls.env['product.product'].create({'name': 'Conference Chair'})
        cls.product_product_5 = cls.env['product.product'].create({'name': 'Product 5'})
        cls.product_product_6 = cls.env['product.product'].create({'name': 'Large Cabinet'})
        cls.product_product_12 = cls.env['product.product'].create({'name': 'Office Chair Black'})
        cls.product_product_13 = cls.env['product.product'].create({'name': 'Corner Desk Black'})
        cls.product_product_2 = cls.env['product.product'].create({'name': 'Virtual Home Staging'})
        cls.product_service_order_repair = cls.env['product.product'].create({
            'name': 'Repair Services',
            'type': 'service',
        })

        # Location
        cls.stock_location_14 = cls.env['stock.location'].create({
            'name': 'Shelf 2',
            'location_id': cls.env.ref('stock.warehouse0').lot_stock_id.id,
        })

        # Repair Orders
        cls.repair1 = cls.env['repair.order'].create({
            'address_id': cls.res_partner_address_1.id,
            'guarantee_limit': datetime.today().strftime('%Y-%m-%d'),
            'invoice_method': 'none',
            'user_id': False,
            'product_id': cls.product_product_3.id,
            'product_uom': cls.env.ref('uom.product_uom_unit').id,
            'partner_invoice_id': cls.res_partner_address_1.id,
            'location_id': cls.env.ref('stock.stock_location_stock').id,
            'operations': [
                (0, 0, {
                    'location_dest_id': cls.product_product_11.property_stock_production.id,
                    'location_id': cls.env.ref('stock.stock_location_stock').id,
                    'name': cls.product_product_11.get_product_multiline_description_sale(),
                    'product_id': cls.product_product_11.id,
                    'product_uom': cls.env.ref('uom.product_uom_unit').id,
                    'product_uom_qty': 1.0,
                    'price_unit': 50.0,
                    'state': 'draft',
                    'type': 'add',
                    'company_id': cls.env.company.id,
                })
            ],
            'fees_lines': [
                (0, 0, {
                    'name': cls.product_service_order_repair.get_product_multiline_description_sale(),
                    'product_id': cls.product_service_order_repair.id,
                    'product_uom_qty': 1.0,
                    'product_uom': cls.env.ref('uom.product_uom_unit').id,
                    'price_unit': 50.0,
                    'company_id': cls.env.company.id,
                })
            ],
            'partner_id': cls.res_partner_12.id,
        })

        cls.repair0 = cls.env['repair.order'].create({
            'product_id': cls.product_product_5.id,
            'product_uom': cls.env.ref('uom.product_uom_unit').id,
            'address_id': cls.res_partner_address_1.id,
            'guarantee_limit': datetime.today().strftime('%Y-%m-%d'),
            'invoice_method': 'after_repair',
            'user_id': False,
            'partner_invoice_id': cls.res_partner_address_1.id,
            'location_id': cls.env.ref('stock.stock_location_stock').id,
            'operations': [
                (0, 0, {
                    'location_dest_id': cls.product_product_12.property_stock_production.id,
                    'location_id': cls.env.ref('stock.stock_location_stock').id,
                    'name': cls.product_product_12.get_product_multiline_description_sale(),
                    'price_unit': 50.0,
                    'product_id': cls.product_product_12.id,
                    'product_uom': cls.env.ref('uom.product_uom_unit').id,
                    'product_uom_qty': 1.0,
                    'state': 'draft',
                    'type': 'add',
                    'company_id': cls.env.company.id,
                })
            ],
            'fees_lines': [
                (0, 0, {
                    'name': cls.product_service_order_repair.get_product_multiline_description_sale(),
                    'product_id': cls.product_service_order_repair.id,
                    'product_uom_qty': 1.0,
                    'product_uom': cls.env.ref('uom.product_uom_unit').id,
                    'price_unit': 50.0,
                    'company_id': cls.env.company.id,
                })
            ],
            'partner_id': cls.res_partner_12.id,
        })

        cls.repair2 = cls.env['repair.order'].create({
            'product_id': cls.product_product_6.id,
            'product_uom': cls.env.ref('uom.product_uom_unit').id,
            'address_id': cls.res_partner_address_1.id,
            'guarantee_limit': datetime.today().strftime('%Y-%m-%d'),
            'invoice_method': 'b4repair',
            'user_id': False,
            'partner_invoice_id': cls.res_partner_address_1.id,
            'location_id': cls.stock_location_14.id,
            'operations': [
                (0, 0, {
                    'location_dest_id': cls.product_product_13.property_stock_production.id,
                    'location_id': cls.env.ref('stock.stock_location_stock').id,
                    'name': cls.product_product_13.get_product_multiline_description_sale(),
                    'price_unit': 50.0,
                    'product_id': cls.product_product_13.id,
                    'product_uom': cls.env.ref('uom.product_uom_unit').id,
                    'product_uom_qty': 1.0,
                    'state': 'draft',
                    'type': 'add',
                    'company_id': cls.env.company.id,
                })
            ],
            'fees_lines': [
                (0, 0, {
                    'name': cls.product_service_order_repair.get_product_multiline_description_sale(),
                    'product_id': cls.product_service_order_repair.id,
                    'product_uom_qty': 1.0,
                    'product_uom': cls.env.ref('uom.product_uom_unit').id,
                    'price_unit': 50.0,
                    'company_id': cls.env.company.id,
                })
            ],
            'partner_id': cls.res_partner_12.id,
        })

        cls.res_repair_user = cls.env['res.users'].create({
            'name': 'Repair User',
            'login': 'maru',
            'email': 'repair_user@yourcompany.com',
            'groups_id': [(6, 0, [cls.env.ref('stock.group_stock_user').id])]})

        cls.res_repair_manager = cls.env['res.users'].create({
            'name': 'Repair Manager',
            'login': 'marm',
            'email': 'repair_manager@yourcompany.com',
            'groups_id': [(6, 0, [cls.env.ref('stock.group_stock_manager').id])]})

    def _create_simple_repair_order(self, invoice_method):
        product_to_repair = self.product_product_5
        partner = self.res_partner_address_1
        return self.env['repair.order'].create({
            'product_id': product_to_repair.id,
            'product_uom': product_to_repair.uom_id.id,
            'address_id': partner.id,
            'guarantee_limit': datetime.today().strftime('%Y-%m-%d'),
            'invoice_method': invoice_method,
            'partner_invoice_id': partner.id,
            'location_id': self.env.ref('stock.stock_location_stock').id,
            'partner_id': self.res_partner_12.id
        })

    def _create_simple_operation(self, repair_id=False, qty=0.0, price_unit=0.0):
        product_to_add = self.product_product_5
        return self.env['repair.line'].create({
            'name': 'Add The product',
            'type': 'add',
            'product_id': product_to_add.id,
            'product_uom_qty': qty,
            'product_uom': product_to_add.uom_id.id,
            'price_unit': price_unit,
            'repair_id': repair_id,
            'location_id': self.env.ref('stock.stock_location_stock').id,
            'location_dest_id': product_to_add.property_stock_production.id,
            'company_id': self.env.company.id,
        })

    def _create_simple_fee(self, repair_id=False, qty=0.0, price_unit=0.0):
        product_service = self.product_product_2
        return self.env['repair.fee'].create({
            'name': 'PC Assemble + Custom (PC on Demand)',
            'product_id': product_service.id,
            'product_uom_qty': qty,
            'product_uom': product_service.uom_id.id,
            'price_unit': price_unit,
            'repair_id': repair_id,
            'company_id': self.env.company.id,
        })

    def test_00_repair_afterinv(self):
        repair = self._create_simple_repair_order('after_repair')
        self._create_simple_operation(repair_id=repair.id, qty=1.0, price_unit=50.0)
        # I confirm Repair order taking Invoice Method 'After Repair'.
        repair.with_user(self.res_repair_user).action_repair_confirm()

        # I check the state is in "Confirmed".
        self.assertEqual(repair.state, "confirmed", 'Repair order should be in "Confirmed" state.')
        repair.action_repair_start()

        # I check the state is in "Under Repair".
        self.assertEqual(repair.state, "under_repair", 'Repair order should be in "Under_repair" state.')

        # Repairing process for product is in Done state and I end Repair process by clicking on "End Repair" button.
        repair.action_repair_end()

        # I define Invoice Method 'After Repair' option in this Repair order.so I create invoice by clicking on "Make Invoice" wizard.
        make_invoice = self.env['repair.order.make_invoice'].create({
            'group': True})
        # I click on "Create Invoice" button of this wizard to make invoice.
        context = {
            "active_model": 'repair_order',
            "active_ids": [repair.id],
            "active_id": repair.id
        }
        make_invoice.with_context(context).make_invoices()

        # I check that invoice is created for this Repair order.
        self.assertEqual(len(repair.invoice_id), 1, "No invoice exists for this repair order")
        self.assertEqual(len(repair.move_id.move_line_ids[0].consume_line_ids), 1, "Consume lines should be set")

    def test_01_repair_b4inv(self):
        repair = self._create_simple_repair_order('b4repair')
        # I confirm Repair order for Invoice Method 'Before Repair'.
        repair.with_user(self.res_repair_user).action_repair_confirm()

        # I click on "Create Invoice" button of this wizard to make invoice.
        repair.action_repair_invoice_create()

        # I check that invoice is created for this Repair order.
        self.assertEqual(len(repair.invoice_id), 1, "No invoice exists for this repair order")

    def test_02_repair_noneinv(self):
        repair = self._create_simple_repair_order('none')

        # Add a new fee line
        self._create_simple_fee(repair_id=repair.id, qty=1.0, price_unit=12.0)

        self.assertEqual(repair.amount_total, 12, "Amount_total should be 12")
        # Add new operation line
        self._create_simple_operation(repair_id=repair.id, qty=1.0, price_unit=14.0)

        self.assertEqual(repair.amount_total, 26, "Amount_total should be 26")

        # I confirm Repair order for Invoice Method 'No Invoice'.
        repair.with_user(self.res_repair_user).action_repair_confirm()

        # I start the repairing process by clicking on "Start Repair" button for Invoice Method 'No Invoice'.
        repair.action_repair_start()

        # I check its state which is in "Under Repair".
        self.assertEqual(repair.state, "under_repair", 'Repair order should be in "Under_repair" state.')

        # Repairing process for product is in Done state and I end this process by clicking on "End Repair" button.
        repair.action_repair_end()

        self.assertEqual(repair.move_id.location_id.id, self.env.ref('stock.stock_location_stock').id,
                         'Repaired product was taken in the wrong location')
        self.assertEqual(repair.move_id.location_dest_id.id, self.env.ref('stock.stock_location_stock').id,
                         'Repaired product went to the wrong location')
        self.assertEqual(repair.operations.move_id.location_id.id, self.env.ref('stock.stock_location_stock').id,
                         'Consumed product was taken in the wrong location')
        self.assertEqual(repair.operations.move_id.location_dest_id.id, self.product_product_5.property_stock_production.id,
                         'Consumed product went to the wrong location')

        # I define Invoice Method 'No Invoice' option in this repair order.
        # So, I check that Invoice has not been created for this repair order.
        self.assertNotEqual(len(repair.invoice_id), 1, "Invoice should not exist for this repair order")
