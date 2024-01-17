with Ada.Text_IO; use Ada.Text_IO;

procedure SmallFunction is
   A, B, Result: Integer;

   procedure Print(X: Integer) is
   begin
      test1;
   end Print;

begin
   A := 5;
   B := 10;

   Result := A + B;

   Print(Result);
end SmallFunction;