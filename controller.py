#import model_mult as model #для *
#import model_sum as model #для +
#import model_min as model #для -
import model_div as model #для :
import view
def button_click():
    #model.init(get_value())
    value_a=view.get_value()
    value_b=view.get_value()
    model.init(value_a, value_b)
    #result=model.sum()
    #result=model.mult()
    #view.view_data(result, "mult")
    #view.view_data(result, "sum")
    """универсальный метод"""
    result=model.do_it()
    view.view_data(result, "result")