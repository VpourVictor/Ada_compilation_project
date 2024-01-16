with Ada.Text_IO; use Ada.Text_IO;

procedure ExampleCode is
   type MyAccess is access Integer;

   procedure MyProc(X: Integer; Y: in out Boolean) is
   begin
      Y := X > 0;
   end MyProc;

   A, B: Integer := 0;
   Condition: Boolean := True;

begin
   MyProc(A, Condition);  -- Utilisation de la procédure avec une condition initiale

   if Condition then
      test_if;
   else
      test_else;
   end if;

   while B < 5 loop
      Put(B);
      New_Line;

      B := B + 1;
   end loop;

   test; -- Placeholder for main logic
end ExampleCode;
