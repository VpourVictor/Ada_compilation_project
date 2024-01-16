with Ada.Text_IO; use Ada.Text_IO;
procedure ShortFunction is

   type MyAccess is access Integer;

   -- function Add(A, B: Integer) return Integer is
   procedure MyProc(X: Integer; Y: out Boolean) is begin Y := X > 0; end MyProc;
   -- function MyFunc(P: Integer) return MyAccess is (new Integer'(P));

begin
   test; -- Placeholder for main logic
end ShortFunction;