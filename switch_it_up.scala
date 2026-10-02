def switchItUp(number: Int): String = {
  var name=""
  if number==0 then
    name ="Zero"
  else if number == 1 then
    name += "One"
  else if number == 2 then
    name += "Two"
  else if number == 3 then
    name += "Three"
  else if number == 4 then
    name += "Four"
  else if number == 5 then
    name += "Five"
  else if number == 6 then
    name += "Six"
  else if number == 7 then
    name += "Seven"
  else if number == 8 then
    name += "Eight"
  else if number == 9 then
    name += "Nine"
  return name
}
