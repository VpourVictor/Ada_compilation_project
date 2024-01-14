with Ada.Text_IO; use Ada.Text_IO;

procedure Example_If is
   -- Déclaration de la variable
   X : Integer;

begin
   -- Lecture de la valeur depuis la console
   Ada.Text_IO.Put("Entrez un nombre : ");
   Ada.Text_IO.Get(X);

   -- Utilisation de l'instruction if pour faire une vérification
   if X > 0 then
      Ada.Text_IO.Put_Line("Le nombre est positif.");
   elsif X = 0 then
      Ada.Text_IO.Put_Line("Le nombre est nul.");
   else
      Ada.Text_IO.Put_Line("Le nombre est négatif.");
   end if;
end Example_If;
