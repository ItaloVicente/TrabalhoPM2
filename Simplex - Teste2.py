from pyomo.environ import *

def solve_linear_programming(objective_function, sense, constraints, solver_path):
    """
    Resolve um problema de programação linear.

    Args:
        objective_function (dict): Dicionário com os coeficientes das variáveis na função objetivo, exemplo: {'x1': 1, 'x2': 2}.
        sense (str): 'maximize' para maximizar ou 'minimize' para minimizar.
        constraints (list): Lista de dicionários para definir restrições.
        solver_path (str): Caminho para o executável do solver GLPK.

    Returns:
        dict: Valores das variáveis e da função objetivo.
    """
    # Criando o modelo
    model = ConcreteModel()

    # Extraindo as variáveis da função objetivo e das restrições
    variables = {var for expr in [objective_function] + [c['expression'] for c in constraints] for var in expr.keys()}

    # Criando as variáveis do modelo
    model.variables = Var(variables, domain=NonNegativeReals)

    # Definição da função objetivo
    def objective_rule(model):
        return sum(coef * model.variables[var] for var, coef in objective_function.items())

    model.obj = Objective(rule=objective_rule, sense=maximize if sense == 'maximize' else minimize)

    # Adicionando as restrições
    model.constraints = ConstraintList()
    for constraint in constraints:
        expr = sum(coef * model.variables[var] for var, coef in constraint['expression'].items())
        if constraint['operator'] == '<=':
            model.constraints.add(expr <= constraint['rhs'])
        elif constraint['operator'] == '>=':
            model.constraints.add(expr >= constraint['rhs'])
        elif constraint['operator'] == '==':
            model.constraints.add(expr == constraint['rhs'])

    # Chamando o solver GLPK
    solver = SolverFactory('glpk', executable=solver_path)
    result = solver.solve(model, tee=False)

    # Coletando os resultados
    solution = {
        'status': str(result.solver.status),
        'objective': model.obj()
    }
    for var in variables:
        solution[var] = model.variables[var]()

    return solution

solver_path = "winglpk-4.65/glpk-4.65/w64/glpsol.exe"
a = input("Pressione enter para a Questao 1")
# Questão 1:
objective = {'x1': 1, 'x2': 1, 'x3': 3, 'x4': 2}
constraints = [
    {'expression': {'x1': 1, 'x2': 2, 'x3': -1, 'x4': 5}, 'rhs': 4, 'operator': '<='},
    {'expression': {'x1': 5, 'x2': -2, 'x4': 6}, 'rhs': 8, 'operator': '<='},
    {'expression': {'x1': 2, 'x2': 3, 'x3': -2, 'x4': 3}, 'rhs': 3, 'operator': '<='},
    {'expression': {'x1': -1, 'x3': 1, 'x4': 2}, 'rhs': 0, 'operator': '<='}
]

# Chamando a função e imprimindo os resultados
result = solve_linear_programming(objective, 'maximize', constraints, solver_path)
print("Resultados Questão 1:", result)


a = input("Pressione enter para a Questao 2 (Estou levando em consideracao que trabalham 8 horas por dia durante 5 dias):")
print("Corte: 25 x 8 x 5 x 60 = 60000 minutos")
print("Costura: 35 x 8 x 5 x 60 = 84000 minutos")
print("Embalagem: 5 x 8 x 5 x 60 = 12000 minutos")
objective = {'x1': 8, 'x2': 12}
constraints = [
    {'expression': {'x1': 20, 'x2': 60}, 'rhs': 60000, 'operator': '<='},
    {'expression': {'x1': 70, 'x2': 60}, 'rhs': 84000, 'operator': '<='},
    {'expression': {'x1': 12, 'x2': 4}, 'rhs': 12000, 'operator': '<='}
]

result = solve_linear_programming(objective, 'maximize', constraints, solver_path)
print("Resultados Questão 2:", result)

a = input("Pressione enter para a Questao 3")
objective = {'x1': 24, 'x2': 22, "x3": 45}
constraints = [
    {'expression': {'x1': 2, 'x2': 1, 'x3': 3}, 'rhs': 42, 'operator': '<='},
    {'expression': {'x1': 2, 'x2': 1, 'x3': 2}, 'rhs': 40, 'operator': '<='},
    {'expression': {'x1': 1, 'x2': 0.5, 'x3': 1}, 'rhs': 45, 'operator': '<='}
]

result = solve_linear_programming(objective, 'maximize', constraints, solver_path)
print("Resultados Simplex (Original):", result)
z_original = result['objective']

print("Item a)")

constraints = [
    {'expression': {'x1': 2, 'x2': 1, 'x3': 3}, 'rhs': 45, 'operator': '<='},
    {'expression': {'x1': 2, 'x2': 1, 'x3': 2}, 'rhs': 40, 'operator': '<='},
    {'expression': {'x1': 1, 'x2': 0.5, 'x3': 1}, 'rhs': 45, 'operator': '<='}
]

result = solve_linear_programming(objective, 'maximize', constraints, solver_path)
print("Resultados Simplex:", result)

print("Item b)")

constraints = [
    {'expression': {'x1': 2, 'x2': 1, 'x3': 3}, 'rhs': 41, 'operator': '<='},
    {'expression': {'x1': 2, 'x2': 1, 'x3': 2}, 'rhs': 40, 'operator': '<='},
    {'expression': {'x1': 1, 'x2': 0.5, 'x3': 1}, 'rhs': 45, 'operator': '<='}
]

result = solve_linear_programming(objective, 'maximize', constraints, solver_path)
print("Resultados Simplex:", result)

print("Item c)")

constraints = [
    {'expression': {'x1': 2, 'x2': 1, 'x3': 3}, 'rhs': 42, 'operator': '<='},
    {'expression': {'x1': 2, 'x2': 1, 'x3': 2}, 'rhs': 38, 'operator': '<='},
    {'expression': {'x1': 1, 'x2': 0.5, 'x3': 1}, 'rhs': 45, 'operator': '<='}
]

result = solve_linear_programming(objective, 'maximize', constraints, solver_path)
print("Resultados Simplex:", result)

print("Item d)")

constraints = [
    {'expression': {'x1': 2, 'x2': 1, 'x3': 3}, 'rhs': 42, 'operator': '<='},
    {'expression': {'x1': 2, 'x2': 1, 'x3': 2}, 'rhs': 46, 'operator': '<='},
    {'expression': {'x1': 1, 'x2': 0.5, 'x3': 1}, 'rhs': 45, 'operator': '<='}
]

result = solve_linear_programming(objective, 'maximize', constraints, solver_path)
print("Resultados Simplex:", result)

print("Item e)")

constraints = [
    {'expression': {'x1': 2, 'x2': 1, 'x3': 3}, 'rhs': 42, 'operator': '<='},
    {'expression': {'x1': 2, 'x2': 1, 'x3': 2}, 'rhs': 40, 'operator': '<='},
    {'expression': {'x1': 1, 'x2': 0.5, 'x3': 1}, 'rhs': 15, 'operator': '<='}
]

result = solve_linear_programming(objective, 'maximize', constraints, solver_path)
print("Resultados Simplex:", result)

print("Item f)")

constraints = [
    {'expression': {'x1': 2, 'x2': 1, 'x3': 3}, 'rhs': 42, 'operator': '<='},
    {'expression': {'x1': 2, 'x2': 1, 'x3': 2}, 'rhs': 40, 'operator': '<='},
    {'expression': {'x1': 1, 'x2': 0.5, 'x3': 1}, 'rhs': 50, 'operator': '<='}
]

result = solve_linear_programming(objective, 'maximize', constraints, solver_path)
print("Resultados Simplex:", result)

print("Item g)")
print("A contratacao de um trabalhador a mais resulta em mais 8 horas disponiveis, logo o setor de costura tera mais 8 horas de limite diario")

constraints = [
    {'expression': {'x1': 2, 'x2': 1, 'x3': 3}, 'rhs': 42, 'operator': '<='},
    {'expression': {'x1': 2, 'x2': 1, 'x3': 2}, 'rhs': 48, 'operator': '<='},
    {'expression': {'x1': 1, 'x2': 0.5, 'x3': 1}, 'rhs': 45, 'operator': '<='}
]

result = solve_linear_programming(objective, 'maximize', constraints, solver_path)
print("Resultados Simplex:", result)

if result['objective'] > (z_original + 15):
    print(f"vale a pena, pois o novo valor de z supre mais de 15 reais z_original = {z_original}, novo z = {result['objective']}")