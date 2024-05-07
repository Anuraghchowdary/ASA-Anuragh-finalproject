class Recipe:
    def __init__(self, name, ingredients, instructions):
        self.name = name
        self.ingredients = ingredients
        self.instructions = instructions

class RecipeApp:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

    def search_recipe(self, keyword):
        return [recipe for recipe in self.recipes if keyword.lower() in recipe.name.lower()]

    def display_recipe(self, recipe):
        if recipe in self.recipes:
            recipe_str = f"Recipe: {recipe.name}\nIngredients:\n"
            recipe_str += '\n'.join([f"- {ingredient}" for ingredient in recipe.ingredients])
            recipe_str += "\nInstructions:\n"
            recipe_str += '\n'.join([f"{i+1}. {instruction}" for i, instruction in enumerate(recipe.instructions)])
            return recipe_str
        else:
            return "Recipe not found."

    def delete_recipe(self, recipe):
        if recipe in self.recipes:
            self.recipes.remove(recipe)
            return f"{recipe.name} deleted successfully."
        else:
            return "Recipe not found."

    def edit_recipe(self, recipe, new_name, new_ingredients, new_instructions):
        if recipe in self.recipes:
            recipe.name = new_name
            recipe.ingredients = new_ingredients
            recipe.instructions = new_instructions
            return "Recipe updated successfully."
        else:
            return "Recipe not found."

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            for recipe in self.recipes:
                f.write(f"{recipe.name}\n")
                f.write("Ingredients:\n")
                f.write('\n'.join([f"- {ingredient}" for ingredient in recipe.ingredients]) + '\n')
                f.write("Instructions:\n")
                f.write('\n'.join([instruction for instruction in recipe.instructions]) + '\n\n')

    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as f:
                lines = f.readlines()
                recipe_data = []
                for line in lines:
                    if line.strip():
                        recipe_data.append(line.strip())
                    else:
                        self.add_recipe(Recipe(recipe_data[0], recipe_data[2:recipe_data.index("Instructions:")], 
                                               recipe_data[recipe_data.index("Instructions:") + 1:]))
                        recipe_data = []
        except FileNotFoundError:
            print("File not found.")

    def generate_shopping_list(self, recipes):
        shopping_list = {}
        for recipe in recipes:
            for ingredient in recipe.ingredients:
                shopping_list[ingredient] = shopping_list.get(ingredient, 0) + 1
        return shopping_list
