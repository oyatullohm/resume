from django import template
register = template.Library()
@register.simple_tag
def bg_color (value):
    if value >= 14 :
        value = 1
    color =  {
            1:'background-color:#000;',
            2:'background-color:rgb(108, 77, 55);',
            3:'background-color:rgb(3, 75, 3);',
            4:'background-color:rgb(75, 2, 24);',
            5:'background-color:#010c57;',
            6:'background-color:rgb(255, 3, 3);',
            7:'background-color:rgb(9, 11, 30);',
            8:'background-color:rgba(122, 125, 107);',
            9:'background-color:rgba(3, 59, 60);',
            10:'background-color:chocolate;',
            11:'background-color:rgb(255, 106, 0);;',
            12:'background-color:#fef208;',
            13:'background-color:rgba(204, 242, 15);',
        }

    return color[value]