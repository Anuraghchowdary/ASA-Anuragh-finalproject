import unittest
from recipe import Recipe, RecipeApp

class TestRecipeApp(unittest.TestCase):
    def setUp(self):
        self.recipe1 = Recipe("Pasta Carbonara", ["Spaghetti", "Eggs"], ["Cook spaghetti", "Beat eggs"])
        self.recipe2 = Recipe("Chocolate Cake", ["Flour", "Sugar"], ["Mix flour", "Add sugar"])
        self.recipe_app = RecipeApp()
        self.recipe_app.add_recipe(self.recipe1)
        self.recipe_app.add_recipe(self.recipe2)

    def search_recipe(self, keyword):
        matching_recipes = []
        for recipe in self.recipes:
            if keyword.lower() in recipe.name.lower() or any(keyword.lower() in ingredient.lower() for ingredient in recipe.ingredients):
                matching_recipes.append(recipe)
        return matching_recipes

    def test_display_recipe(self):
        expected_output = "Recipe: Pasta Carbonara\nIngredients:\n- Spaghetti\n- Eggs\nInstructions:\n1. Cook spaghetti\n2. Beat eggs"
        self.assertEqual(self.recipe_app.display_recipe(self.recipe1), expected_output)

    def test_delete_recipe(self):
        self.recipe_app.delete_recipe(self.recipe1)
        self.assertNotIn(self.recipe1, self.recipe_app.recipes)

    def test_edit_recipe(self):
        new_name = "Updated Pasta"
        new_ingredients = ["New Spaghetti", "New Eggs"]
        new_instructions = ["New Cook spaghetti", "New Beat eggs"]
        self.assertEqual(self.recipe_app.edit_recipe(self.recipe1, new_name, new_ingredients, new_instructions), "Recipe updated successfully.")
        self.assertEqual(self.recipe1.name, new_name)
        self.assertEqual(self.recipe1.ingredients, new_ingredients)
        self.assertEqual(self.recipe1.instructions, new_instructions)

if __name__ == "__main__":
    unittest.main()
