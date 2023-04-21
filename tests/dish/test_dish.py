from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient, Restriction
from pytest import raises


# Req 2
def test_dish():
    # seu teste passa com a implementação correta da classe Dish

    # seu teste falha caso o atributo name de um prato seja diferente
    # que o passado ao construtor.
    dish1 = Dish("strogonofe", 20.00)
    assert dish1.name == "strogonofe"

    # seu teste falha caso os hashes de dois pratos
    # iguais sejam diferentes
    dish1 = Dish("fettuccine", 20.00)
    dish2 = Dish("fettuccine", 20.00)
    assert hash(dish1) == hash(dish2)

    # seu teste falha caso os hashes de dois pratos
    # diferentes sejam iguais
    dish1 = Dish("miojo", 2.00)
    dish2 = Dish("fettuccine", 20.00)
    assert hash(dish1) != hash(dish2)

    # seu teste falha caso a comparação de igualdade
    # de dois pratos iguais (ou de um prato com ele mesmo) seja falsa
    dish1 = Dish("fettuccine", 20.00)
    dish2 = Dish("fettuccine", 20.00)
    assert dish1 == dish2

    # seu teste falha caso a comparação de igualdade
    # de dois pratos diferentes seja verdadeira
    dish1 = Dish("miojo", 2.00)
    dish2 = Dish("fettuccine", 20.00)
    assert dish1 != dish2

    # seu teste falha caso a implementação do método __repr__
    # retorne um valor inadequado
    dish1 = Dish("strogonofe", 40.00)
    assert dish1.__repr__() == "Dish('strogonofe', R$40.00)"

    # seu teste falha caso um TypeError não seja levantado
    # ao criar um prato com um valor de tipo inválido
    with raises(TypeError, match="Dish price must be float."):
        Dish("strogonofe", 'vinte')

    # seu teste falha caso um ValueError não seja
    # levantado ao criar um prato com um valor inválido
    with raises(ValueError, match="Dish price must be greater then zero."):
        Dish("strogonofe", -20.00)

    # seu teste falha caso o acesso a um valor do
    # atributo recipe, ao ser indexado com um
    # ingrediente válido retorne uma quantidade
    # inválida (dica: use o método get do dicionário,
    # por exemplo dish.recipe.get(ingredient))
    ingredient_strogo = Ingredient("carne")
    dish1 = Dish("strogonofe", 40.00)
    dish1.add_ingredient_dependency(ingredient_strogo, 2)
    # seu teste falha caso o método get_ingredients
    # retorne um set de ingredientes diferente do esperado

    assert ingredient_strogo in dish1.get_ingredients()

    # seu teste falha caso o método get_restrictions
    # retorne um set de restrições diferente do esperado
    assert Restriction.ANIMAL_MEAT in dish1.get_restrictions()
