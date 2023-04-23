# Req 3
import pandas as pd
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        # 1 - eu devo colocar os inicializadores da classe
        # 2 - faço a leitura do aquivo csv e guardo numa variável
        # 3 - por cada linha eu vou usar as classes auxiliares
        # para colocar os ingredientes e os pratos
        self.dishes = set()
        info = pd.read_csv(source_path)

        # O itertuples é para iterar nas colunas simultaneamente
        # e index=False é para não ter a coluna index
        for row in info.itertuples(index=False):
            self.dishes.add(Dish(row[0], row[1]))

        for row in info.itertuples(index=False):
            for unit_dish in self.dishes:
                if unit_dish.name == row[0]:
                    unit_dish.add_ingredient_dependency(Ingredient(row[2]),
                                                        row[3])
