with Ada.Text_IO; use Ada.Text_IO;

procedure DivisionExample is
   A, B: Integer := 10;

begin
   -- Utilisation de /=
   if A /= B then
      test_different;
   else
      test_equal;
   end if;

   X := 10;
   Y := 20;

   Div := X / Y;

   test; -- Placeholder for main logic
end DivisionExample;
