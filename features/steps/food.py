from behave import given, when, then

@given("there were {amount:d} cucumbers")
def step_cucumber(context, amount):
    pass

@when("I eat {eaten:d} cucumbers")
def step_eating(context, eaten):
    pass

@then("I should have {left:d} cucumbers")
def step_after(context, left):
    pass
