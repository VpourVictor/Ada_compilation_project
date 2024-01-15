with Ada.Text_IO; use Ada.Text_IO;
[284, (285, 'Ada'), 46, (285, 'Text_IO'), 59, 282, (285, 'Ada'), 46, (285, 'Text_IO'), 59,

procedure Example_If is
274, (285, 'Example_If'), 267,

   -- Déclaration de la variable
   X : Integer;
   (285, 'X'), 58, (285, 'Integer'), 59,

begin
258,
   -- Utilisation de l'instruction if sans print
   if X > 0 then
   265, (285, 'X'), 62, (286, '0'), 279,  59

      test1; -- Aucune action pour le cas où le nombre est positif
      (285, 'test1'),

   elsif X = 0 then
   260, (285, 'X'), 61, (286, '0'), 279,
      test2; -- Aucune action pour le cas où le nombre est nul
      (285, 'test2'), 59,

   else
    259,
      test3; -- Aucune action pour le cas où le nombre est négatif
      (285, 'test3'), 59,

   end if;
   261, 265, 59,
end Example_If;
261, (285, 'Example_If'), 59]