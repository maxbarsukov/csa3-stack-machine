from src.translator import translate


def start() -> None:
    with open("./examples/hello_world.asm", encoding="utf-8") as f:
        source = f.read()

    instr, data = translate(source)
    print(instr)
    print(data)
