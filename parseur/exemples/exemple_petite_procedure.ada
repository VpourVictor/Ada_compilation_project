with Ada.Text_IO; use Ada.Text_IO;
procedure SmallFunction is
   function Square(X: Integer) return Integer is
      procedure Print(X: Integer) is
        begin
             Put(X);
        end Print;

begin
   Result := A + B;
   return Result;
end SmallFunction;