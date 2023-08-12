package main

func do_work() {
  for true {}
}

func main() {
  go do_work()
  do_work()
}