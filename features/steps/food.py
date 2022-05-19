from behave import given, when, then

@given("there were 5 cucumbers")
def step_cucumber(context):
    pass

@when("I eat 3 cucumbers")
def step_eating(context):
    pass

@then("I should have 2 cucumbers")
def step_after(context):
    pass
