with Ada.Text_IO; use Ada.Text_IO;

procedure Example_If is
   -- Déclaration de la variable
   X : Integer;

begin
   -- Utilisation de l'instruction if sans print
   if X > 0 then
      test; -- Aucune action pour le cas où le nombre est positif
   elsif X = 0 then
      test; -- Aucune action pour le cas où le nombre est nul
   else
      test; -- Aucune action pour le cas où le nombre est négatif
   end if;
end Example_If;
