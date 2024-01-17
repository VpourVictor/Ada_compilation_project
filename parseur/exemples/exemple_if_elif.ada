with Ada.Text_IO; use Ada.Text_IO;

procedure Example_If is
   -- Déclaration de la variable
   X : Integer;

begin

   -- Utilisation de l'instruction if sans print
   if X > 0 then
      test1 := 10;
      test12 := 10;
      test13 := test1 + test12;
   elsif X = 0 then
      test2; -- Aucune action pour le cas où le nombre est nul
   else
      test3; -- Aucune action pour le cas où le nombre est négatif
   end if;
end Example_If;
