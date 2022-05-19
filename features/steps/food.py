from behave import given, when, then

@given("there were {amount:d} cucumbers")
def step_cucumber(context, amount):
    context.amount_of_cucumbers = amount

@when("I eat {eaten:d} cucumbers")
def step_eating(context, eaten):
    context.amount_of_cucumbers = context.amount_of_cucumbers - eaten

@then("I should have {left:d} cucumbers")
def step_after(context, left):
    assert context.amount_of_cucumbers == left
