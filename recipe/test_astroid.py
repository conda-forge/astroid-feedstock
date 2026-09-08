import astroid


module = astroid.parse("answer = 6 * 7")
assignment = module.body[0]
inferred = next(assignment.value.infer())

assert inferred.value == 42
