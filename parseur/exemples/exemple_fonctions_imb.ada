with Ada.Text_IO; use Ada.Text_IO;

procedure Programme_Imbrique is

   -- Fonction imbriquée
   function Addition_Multiplication(a, b, c : Integer) return Integer is
      function Addition(x, y : Integer) return Integer is
      begin
         return x + y;
      end Addition;

      function Multiplication(x, y : Integer) return Integer is
      begin
         return x * y;
      end Multiplication;

   begin
      return a + b / c;
   end Addition_Multiplication;

   -- Déclaration de variables
   A, B, C, Resultat : Integer;

begin
   -- Initialisation des valeurs (ou tout autre moyen d'obtenir les valeurs)
   A := 5;
   B := 3;
   C := 2;

   -- Appel de la fonction imbriquée
   Resultat := Addition_Multiplication(A, B, C);

   -- Affichage du résultat
   New_Line;
end Programme_Imbrique;
