INSERT INTO flavour_ings (flavour_ing_id, flavour_id, ingredient_id)
SELECT fl_ig_pk.NEXTVAL, flavour_id, ingredient_id
FROM ingredients, flavours
where flavours.flavour_name = 'Vanilla' AND ingredients.ingredient_name = 'Vanilla';
INSERT INTO flavour_ings (flavour_ing_id, flavour_id, ingredient_id)
SELECT fl_ig_pk.NEXTVAL, flavour_id, ingredient_id
FROM ingredients, flavours
where flavours.flavour_name = 'Rainbow' AND ingredients.ingredient_name = 'Cream';
INSERT INTO flavour_ings (flavour_ing_id, flavour_id, ingredient_id)
SELECT fl_ig_pk.NEXTVAL, flavour_id, ingredient_id
FROM ingredients, flavours
where flavours.flavour_name = 'Mango' AND ingredients.ingredient_name = 'Milk';
INSERT INTO flavour_ings (flavour_ing_id, flavour_id, ingredient_id)
SELECT fl_ig_pk.NEXTVAL, flavour_id, ingredient_id
FROM ingredients, flavours
where flavours.flavour_name = 'Chocolate' AND ingredients.ingredient_name = 'Sugar';
INSERT INTO flavour_ings (flavour_ing_id, flavour_id, ingredient_id)
SELECT fl_ig_pk.NEXTVAL, flavour_id, ingredient_id
FROM ingredients, flavours
where flavours.flavour_name = 'Banana' AND ingredients.ingredient_name = 'Condensed Milk';