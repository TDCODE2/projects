import webbrowser as wb

websites = ["facebook", "twitter", "spotify"]
im_dumb = ["ok", "i cant get what u say"]
while True:
    user_input = input("You: ").lower()
    for site in websites:
        if site in user_input and site:
            wb.open(f"https://www.{site}.com")
    if user_input == "open youtube":
        wb.open("https://www.youtube.com/watch?v=xvFZjo5PgG0")
    if "exit" in user_input:
        break
    if "recipe for cake" in user_input:
        print("""
            The recipe for a cake is:
            Ingredients:
            2 and 1/2 cups (325g) all-purpose flour
            2 teaspoons baking powder
            1/2 teaspoon baking soda
            1/2 teaspoon salt
            1 cup (230g) unsalted butter, at room temperature
            1 and 3/4 cups (350g) granulated sugar
            4 large eggs, at room temperature
            2 teaspoons pure vanilla extract
            1 and 1/2 cups (355ml) buttermilk, at room temperature
            Instructions:
            
            Preheat the oven to 350°F (175°C). Grease and flour two 9-inch (23cm) round cake pans.
            In a medium bowl, whisk together the flour, baking powder, baking soda, and salt.
            In a large bowl, using an electric mixer, beat the butter and sugar together until light and fluffy, about 3 minutes.
            Add the eggs one at a time, beating well after each addition.
            Beat in the vanilla extract.
            Add the dry ingredients to the butter mixture in three parts, alternating with the buttermilk, beginning and ending with the dry ingredients. Beat until just combined.
            Divide the batter evenly between the prepared pans and smooth the tops.
            Bake for 25-30 minutes, or until a toothpick inserted into the center of the cakes comes out clean.
            Let the cakes cool in the pans for 10 minutes, then remove them from the pans and place them on a wire rack to cool completely.
            Once the cakes are cool, you can frost and decorate them as desired.
        """)
