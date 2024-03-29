from odoo import models, fields, api


# extend product.template model with calories
class DietFacts_product_template(models.Model):
    _name = 'product.template'
    _inherit = 'product.template'
    calories = fields.Integer("Calories")
    servingsize = fields.Float('Serving Size')
    lastupdated = fields.Date('Last Updated')
    dietitem = fields.Boolean('Diet Item')
    nutrient_ids = fields.One2many('nutrientproducttemplate.nutrient','product_id','Nutrients')

    @api.one
    @api.depends('nutrient_ids', 'nutrient_ids.value')
    def _calcnutrientscore(self):
        currentscore = 0
        for nutrient in self.nutrient_ids:
            if nutrient.nutrient_id.name == 'Sodium':
              currentscore = currentscore + (nutrient.value/2)
        self.nutrientscore = currentscore

    nutrientscore = fields.Float(string="Nutrient Score", store="True", compute="_calcnutrientscore")




class DietFacts_res_users_meal(models.Model):
    _name = 'res.users.meal'
    name = fields.Char("Meal Name")
    meal_date = fields.Datetime("Meal Date")
    item_ids = fields.One2many('res.users.mealitem', 'meal_id')
    user_id = fields.Many2one('res.users')
    notes = fields.Text("Meal Description")
    largemeal=fields.Boolean('Large Meal',readonly="True")

    @api.onchange('totalcalories')
    def check_largemeal(self):
        if self.totalcalories > 500:
            self.largemeal= True
        else:
            self.largemeal= False

    @api.one
    @api.depends('item_ids', 'item_ids.servings')
    def _calccalories(self):
        currentcalories = 0
        for mealitem in self.item_ids:
            currentcalories = currentcalories + (mealitem.calories * mealitem.servings)
        self.totalcalories = currentcalories

    @api.one
    @api.depends('item_ids', 'item_ids.servings')
    def _calcservings(self):
        currentservings = 0
        for mealitem in self.item_ids:
            currentservings = currentservings + mealitem.servings
        self.totalservings = currentservings

    totalcalories = fields.Integer(string="Total meal calories", store="True", compute="_calccalories")
    totalservings = fields.Float(string="Total meal servings", store="True", compute="_calcservings")


class DietFacts_res_users_mealitem(models.Model):
    _name = 'res.users.mealitem'
    meal_id = fields.Many2one('res.users.meal', 'item_ids')
    item_id = fields.Many2one('product.template')
    servings = fields.Float("Servings")
    calories = fields.Integer(related="item_id.calories", string="calories per serving", store="True", readonly="True")
    notes = fields.Text("Meal Item Notes")


class DietFacts_product_nutrient(models.Model):
    _name = 'product.nutrient'
    name = fields.Char("Nutrient Name")
    uom_id = fields.Many2one('product.uom', 'Unit of Measure')
    description = fields.Text("Description")


class DietFacts_nutrientproducttemplate(models.Model):
    _name = 'nutrientproducttemplate.nutrient'
    nutrient_id = fields.Many2one('product.nutrient',string="Product Nutrient")
    product_id = fields.Many2one('product.template')
    value = fields.Float('Nutrient Value')
    uom=fields.Char(related="nutrient_id.uom_id.name",readonly="True",string="UOM")
    dailypercent = fields.Float("Daily Recommended Value")
