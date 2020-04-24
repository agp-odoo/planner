# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Custom Planning Module',
    'category': 'Planning',
    'summary': 'Custom Planning Module',
    'description': """
Custom Planning Module
==================================================
The idea of this module is to have a board where users can share ideas for projects, sourcing, or other company related topics.
This is great for new businesses that want to grow and take on other profitable opportunities. 

Example:

If a user thinks the company should open up an office in a new location, they can submit a new stage on the board
with resources that help the company make the idea become reality. The user could post possible office spaces under the stage, or
resources that help the company understand the local law system (licenses, fees, taxes, etc.).

Requirements:
- KanBan board for ideas with the ability to create new stages
- URLs are rendered as content rather than just anchor tags
- Admins can approve, decline or delay a task
- Admins can edit any stage or task
- Any user can create a stage or edit their own stages/tasks
- A way to calculate the total cost of the stage
- A way to calculate the profitablity of the stage
- Like button for other users to "vote" on a task

    """,
    'author': 'Odoo S.A.',
    'website': 'http://www.odoo.com',
    'price': '0.99',
    'currency': 'USD',
    'images': ['static/description/banner.png'],
    'depends': ['base', 'base_automation', 'base_import_module'],
    'data': [
        'data/models/models.xml',
        'data/fields/x_idea_board.xml',
        'data/fields/x_idea.xml',
        'data/actions/actions.xml',
        'views/views.xml',
        'views/assets.xml',
        'security/ir.model.access.csv',
    ],
}
