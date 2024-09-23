greeting = input(": ").strip().lower()
match greeting:
    case "hello" | "hello there" | "hello, newman":
        print("$0")
    case "how you doing?" | "how's it going?" | "how are you?" | "how are you doing?":
        print("$20")
    case _:
        print("$100")