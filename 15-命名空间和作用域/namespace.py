# var1为全局名称
var1 = 5
def test_function():
    # var2为局部名称
    var2 = 10
    def inner_test_function():
        # var3为内嵌的局部名称
        var3 = 15