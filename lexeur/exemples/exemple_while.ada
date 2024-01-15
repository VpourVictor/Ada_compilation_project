while Next /= Head loop
  Sum  := Sum + Next.Value;
  Next := Next.Succ;
end loop Summation;