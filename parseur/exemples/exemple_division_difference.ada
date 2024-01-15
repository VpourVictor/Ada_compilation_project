with Ada.Text_IO; use Ada.Text_IO;

procedure DivisionExample is
   A, B: Integer := 10;

begin
   -- Utilisation de /=
   if A /= B then
      Put_Line("A n'est pas égal à B.");
   else
      Put_Line("A est égal à B.");
   end if;

   -- Utilisation de /
   Put("La division de A par B donne : ");
   Put(Float(A) / Float(B));  -- Conversion en Float pour obtenir une division réelle
   New_Line;

   test; -- Placeholder for main logic
end DivisionExample;
