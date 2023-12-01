let lines =
  let channel = open_in "01.in" in
  let rec read_lines acc =
    try
      let line = input_line channel in
      read_lines (line :: acc)
    with End_of_file ->
      close_in channel;
      List.rev acc
  in
  read_lines []

let problem1 calibration_document =
  let first_digit s =
    let lst = List.init (String.length s) (String.get s) in
    let rec first_digit_foo lst =
      match lst with
      | [] -> 0
      | '0' :: _ -> 0
      | '1' :: _ -> 1
      | '2' :: _ -> 2
      | '3' :: _ -> 3
      | '4' :: _ -> 4
      | '5' :: _ -> 5
      | '6' :: _ -> 6
      | '7' :: _ -> 7
      | '8' :: _ -> 8
      | '9' :: _ -> 9
      | _ :: tail -> first_digit_foo tail
    in
    first_digit_foo lst
  and last_digit s =
    let lst = List.rev(List.init (String.length s) (String.get s)) in
    let rec last_digit_foo lst =
      match lst with
      | [] -> 0
      | '0' :: _ -> 0
      | '1' :: _ -> 1
      | '2' :: _ -> 2
      | '3' :: _ -> 3
      | '4' :: _ -> 4
      | '5' :: _ -> 5
      | '6' :: _ -> 6
      | '7' :: _ -> 7
      | '8' :: _ -> 8
      | '9' :: _ -> 9
      | _ :: tail -> last_digit_foo tail
    in
    last_digit_foo lst
  in
  let extract_calibration_value line =
    let first_digit = first_digit line in
    let last_digit = last_digit line in
    first_digit * 10 + last_digit
  in
  let values = List.map extract_calibration_value calibration_document in
  List.fold_left (+) 0 values

let problem2 calibration_document =
  let first_digit s =
    let lst = List.init (String.length s) (String.get s) in
    let rec first_digit_foo lst =
      match lst with
      | [] -> 0
      | '0' :: _ -> 0
      | '1' :: _ -> 1
      | '2' :: _ -> 2
      | '3' :: _ -> 3
      | '4' :: _ -> 4
      | '5' :: _ -> 5
      | '6' :: _ -> 6
      | '7' :: _ -> 7
      | '8' :: _ -> 8
      | '9' :: _ -> 9
      | 'o' :: 'n' :: 'e' :: _ -> 1
      | 't' :: 'w' :: 'o' :: _ -> 2
      | 't' :: 'h' :: 'r' :: 'e' :: 'e' :: _ -> 3
      | 'f' :: 'o' :: 'u' :: 'r' :: _ -> 4
      | 'f' :: 'i' :: 'v' :: 'e' :: _ -> 5
      | 's' :: 'i' :: 'x' :: _ -> 6
      | 's' :: 'e' :: 'v' :: 'e' :: 'n' :: _ -> 7
      | 'e' :: 'i' :: 'g' :: 'h' :: 't' :: _ -> 8
      | 'n' :: 'i' :: 'n' :: 'e' :: _ -> 9
      | _ :: tail -> first_digit_foo tail
    in
    first_digit_foo lst
  and last_digit s =
    let lst = List.init (String.length s) (String.get s) in
    let rev_s = List.rev lst in
    let rec last_digit_foo lst =
      match lst with
      | [] -> 0
      | '0' :: _ -> 0
      | '1' :: _ -> 1
      | '2' :: _ -> 2
      | '3' :: _ -> 3
      | '4' :: _ -> 4
      | '5' :: _ -> 5
      | '6' :: _ -> 6
      | '7' :: _ -> 7
      | '8' :: _ -> 8
      | '9' :: _ -> 9
      | 'e' :: 'n' :: 'o' :: _ -> 1
      | 'o' :: 'w' :: 't' :: _ -> 2
      | 'e' :: 'e' :: 'r' :: 'h' :: 't' :: _ -> 3
      | 'r' :: 'u' :: 'o' :: 'f' :: _ -> 4
      | 'e' :: 'v' :: 'i' :: 'f' :: _ -> 5
      | 'x' :: 'i' :: 's' :: _ -> 6
      | 'n' :: 'e' :: 'v' :: 'e' :: 's' :: _ -> 7
      | 't' :: 'h' :: 'g' :: 'i' :: 'e' :: _ -> 8
      | 'e' :: 'n' :: 'i' :: 'n' :: _ -> 9
      | _ :: tail -> last_digit_foo tail
    in
    last_digit_foo rev_s
  in
  let extract_calibration_value line =
    let first_digit = first_digit line in
    let last_digit = last_digit line in
    first_digit * 10 + last_digit
  in
  let values = List.map extract_calibration_value calibration_document in
  List.fold_left (+) 0 values

let () =
  let answer1 = problem1 lines in
  let answer2 = problem2 lines in
  Printf.printf "Answer 1: %d\nAnswer 2: %d\n" answer1 answer2
