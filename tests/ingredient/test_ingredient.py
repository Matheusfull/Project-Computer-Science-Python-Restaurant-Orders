from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    # teste passa com a implementação correta da classe Ingredient

    # teste falha caso a classe retorne hashes diferentes
    # para dois ingredientes iguais
    ingredient1 = Ingredient("bacon")
    ingredient2 = Ingredient("bacon")
    assert hash(ingredient1) == hash(ingredient2)

    # teste falha caso a classe retorne hashes iguais
    # para dois ingredientes diferentes
    ingredient1 = Ingredient("bacon")
    ingredient2 = Ingredient("carne")
    assert hash(ingredient1) != hash(ingredient2)

    # teste falha caso a comparação de igualdade de dois
    # ingredientes iguais (ou de um ingrediente com ele mesmo) seja falsa
    ingredient1 = Ingredient("bacon")
    ingredient2 = Ingredient("bacon")
    assert ingredient1 == ingredient2

    # teste falha caso a comparação de igualdade de dois
    # ingredientes diferentes seja verdadeira
    ingredient1 = Ingredient("bacon")
    ingredient2 = Ingredient("carne")
    assert ingredient1 != ingredient2

    # seu teste falha caso a implementação do método
    # __repr__ retorne um valor inadequado
    ingredient1 = Ingredient("bacon")
    assert ingredient1.__repr__() == "Ingredient('bacon')"

    # seu teste falha caso o atributo name de um ingrediente
    # seja diferente que o passado ao construtor
    ingredient1 = Ingredient("bacon")
    assert ingredient1.name == "bacon"

    # seu teste falha caso o atributo restrictions de um
    # ingrediente não contenha os valores corretos para o alimento passado
    ingredient1 = Ingredient("farinha")
    assert ingredient1.restrictions == {Restriction.GLUTEN}
