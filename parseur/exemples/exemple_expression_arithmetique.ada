with Ada.Text_IO; use Ada.Text_IO;
procedure ArithmeticExample is
   A, B, C, D, Result1, Result2, Result3: Integer;

begin
   A := 10;
   B := 5;
   C := 2;
   D := 3;

   Result0 := (A + B);
   Result01 := A + B;
   Result1 := ((A + B) + C);
   Result2 := (A / (B + C));
   Result3 := ((A / (B + C)) * D);
   Result4 := ((A + B) - C * D);
   Result5 := A + B - C / D;

end ArithmeticExample;
